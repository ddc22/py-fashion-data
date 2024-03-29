
import json
from utilsx import file_writer
from source import templates
from source import config_data_map


def generate():

    product_supplier = {}
    xml_collection = []
    sequence = 0

    for category, products in config_data_map.product_data.items():
        for product in products:
            sequence += 1
            print(product["product_id"], product["price"])

            xml_doc = templates.product_price.format(
                product_id=product["product_id"],
                price=str(int(round(float(product["price"]), 2)*100)),
                currency_id=config_data_map.currency_id,
                price_type=config_data_map.price_type)
            xml_collection.append(xml_doc)

    print(""" 

    **********************************  

        Generated product price : {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ProductPrice.xml", xml_collection)
