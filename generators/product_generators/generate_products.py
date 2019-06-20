
from source import cat_hierarchy
from source import config_data_map
from source import templates

import logging
from utils import file_writer
generated_data = {
    "products_array": [],
    "product_image_map": {
        "LARGE": {},
        "THUMB": {}
    }
}


def generate_sku_product_id(product_id, sizes, colors, size, color):
    sku_product_id = product_id + "-"
    sku_product_id += str(sizes.index(size) + 1)
    sku_product_id += str(colors.index(color) + 1)
    return sku_product_id


def generate_scs_product(product, category):
    product_id = product["product_id"]
    generated_data["products_array"].append(product_id)
    product_image_map = generated_data["product_image_map"]
    product_image_map["LARGE"][product_id] = [product["image_id"]]
    product_image_map["THUMB"][product_id] = [product["image_thumbnail_id"]]

    long_description = product["long_description"][:199]
    name = product["name"][:19]
    xml_doc = templates.product.format(
        product_id=product["product_id"],
        category=category,
        name=name,
        long_description=long_description,
        info=product["info"],
        image_id=product["image_id"],
        brand=product["brand"])
    return xml_doc


def generate_sku_product(product, category):
    count = 0
    color_map = product["color_image_map"]
    colors = list(color_map.keys())
    xml_collection = []
    if category not in config_data_map.cat_sizes:
        logging.warning('Category sizes not defined')
    sizes = config_data_map.cat_sizes[category]
    for color, images in color_map.items():
        for size in sizes:
            image_id = images[0]
            count += 1
            product_id = product["product_id"]

            sku_product_id = generate_sku_product_id(
                product_id, sizes, colors, size, color)

            generated_data["products_array"].append(sku_product_id)
            product_image_map = generated_data["product_image_map"]
            product_image_map["LARGE"][sku_product_id] = color_map[color]
            print(category, product_id, sku_product_id, color, size, image_id)

            # Max length fixes
            long_description = product["long_description"][:199]
            name = product["name"][:19]
            xml_doc = templates.sku_product.format(
                sku_product_id=sku_product_id,
                product_id=product_id,
                category=category,
                color=color,
                name=name,
                long_description=long_description,
                info=product["info"],
                image_id=image_id,
                brand=product["brand"],
                size=size)
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
