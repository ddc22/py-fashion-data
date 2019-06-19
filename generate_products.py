import pprint
import products_templates
import util
import generate_product_media
import file_writer
import templates
import config_data_map

pp = pprint.PrettyPrinter(indent=4)


def generate_scs_product(product, category):
    product_id = product["product_id"]
    xml_doc = templates.product.format(
        product_id=product["product_id"],
        category=category,
        name=product["name"],
        long_description=product["long_description"],
        info=product["info"],
        image_id=product["image_id"],
        brand=product["brand"])
    return xml_doc


def generate_sku_product(product):
    count = 0
    color_map = product["color_image_map"]
    colors = list(color_map.keys())
    for color, images in color_map.items():
        for size in sizes:
            if color in color_map:
                image_id = images[0]
                count += 1
                product_id = product["product_id"]
                sku_product_id = product_id + "-"
                sku_product_id += str(sizes.index(size) + 1)
                sku_product_id += str(colors.index(color) + 1)

                product_image_map[sku_product_id] = color_map[color]
                print(category, sku_product_id, color, size, image_id)

                xml_doc = templates.sku_product.format(
                    sku_product_id=sku_product_id,
                    product_id=product_id,
                    category=category,
                    color=color,
                    name=product["name"],
                    long_description=product["long_description"],
                    info=product["info"],
                    image_id=image_id,
                    brand=product["brand"],
                    size=size)
                return xml_doc


product_image_map = {}
xml_collection = []
for category, products in config_data_map.product_data.items():
    sizes = config_data_map.cat_sizes[category]
    for product in products:
        xml_collection.append(generate_scs_product(product, category))
        xml_collection.append(generate_sku_product(product))


file_writer.write_config("Product.xml", xml_collection)
# generate_product_media.generate(product_image_map)
# pp.pprint(product_image_map)
# print(products_templates.sku_product_templates)
# pp.pprint(productImageMap)
