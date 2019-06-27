
from source import cat_hierarchy
from source import config_data_map
from source import templates

import logging
from utilsx import file_writer
from utilsx import util

generated_data = {
    "products_array": [],
    "grouped_skus": {},
    "product_image_map": {
        "LARGE": {},
        "THUMB": {}
    }
}


def generate_sku_product_id(product_id, sizes, colours, size, colour):
    sku_product_id = product_id + "-"
    sku_product_id += str(sizes.index(size) + 1)
    sku_product_id += str(colours.index(colour) + 1)
    return sku_product_id


def generate_scs_product(product, category):
    product_id = product["product_id"]
    generated_data["products_array"].append(product_id)
    product_image_map = generated_data["product_image_map"]
    product_image_map["LARGE"][product_id] = [product["image_id"]]
    product_image_map["THUMB"][product_id] = [product["image_thumbnail_id"]]

    long_description = util.force_length(product["long_description"], 199)
    name = util.safe_force_reverse_length(product["name"], 19)
    # Brand greater than 19 not allowed
    util.assert_max_length(product["brand"], 19)
    xml_doc = templates.product.format(
        product_id=product["product_id"],
        category=category,
        name=name,
        long_description=long_description,
        info=util.safe_force_length(product["info"], 299),
        image_id=product["image_id"],
        brand=util.force_length(product["brand"], 20))
    return xml_doc


def generate_sku_product(product, category):
    count = 0
    colour_map = product["colour_image_map"]
    colours = list(colour_map.keys())
    xml_collection = []
    if category not in config_data_map.cat_sizes:
        logging.exception('Category sizes not defined')
        pass
    sizes = config_data_map.cat_sizes[category]
    for colour, images in colour_map.items():
        for size in sizes:
            image_id = images[0]
            count += 1
            product_id = product["product_id"]

            sku_product_id = generate_sku_product_id(
                product_id, sizes, colours, size, colour)

            generated_data["products_array"].append(sku_product_id)
            if product_id not in generated_data["grouped_skus"]:
                generated_data["grouped_skus"][product_id] = []
            generated_data["grouped_skus"][product_id].append(sku_product_id)

            product_image_map = generated_data["product_image_map"]
            product_image_map["LARGE"][sku_product_id] = colour_map[colour]
            print(category, product_id, sku_product_id, colour, size, image_id)

            # Max length fixes
            long_description = util.force_length(
                product["long_description"], 200)
            name = util.safe_force_reverse_length(product["name"], 19)

            colour_id = colour.replace("/", "_").replace(" ", "_")
            size_id = size.replace("/", "_").replace(".", "POINT")
            xml_doc = templates.sku_product.format(
                sku_product_id=sku_product_id,
                product_id=product_id,
                category=category,
                colour=colour_id,
                name=name,
                long_description=long_description,
                info=util.force_length(product["info"], 300),
                image_id=image_id,
                brand=util.force_length(product["brand"], 20),
                size=size_id)
            xml_collection.append(xml_doc)
    return xml_collection


def generate():
    xml_collection = []

    for category, products in config_data_map.product_data.items():
        for product in products:
            xml_collection.append(generate_scs_product(product, category))
            xml_collection.extend(generate_sku_product(product, category))

    print("""

    **********************************

        Generated products count {count}

    **********************************


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("Product.xml", xml_collection)

    return generated_data
