from source import templates, config_data_map
from utilsx import file_writer
import random

prod_attribue_types = [
    {
        "path_name": "stars_option_path",
        "data_type": "FLOAT",
        "prefix": ""
    },
    {
        "path_name": "brand_option_path",
        "data_type": "STRING",
        "prefix": "Brand_"
    }
]


def generate(products_array):
    xml_collection = []
    for category, products in config_data_map.product_data.items():
        for product in products:
            brand = product["brand"].upper().replace(" ", "_")
            xml_doc = templates.product_attribute_brand.format(
                value=brand,
                product_id=product["product_id"])
            xml_collection.append(xml_doc)
            print(product["product_id"], brand)

            random_rating = round(random.uniform(1, 5), 2)
            xml_doc = templates.product_attribute_stars.format(
                value=random_rating,
                product_id=product["product_id"])
            xml_collection.append(xml_doc)
            print(product["product_id"], random_rating)

    print("""

    **********************************

        Generated product attributes {count}

    **********************************


    """.format(count=str(len(xml_collection)*2)))
    file_writer.write_config("ProductAttribute.xml", xml_collection)
