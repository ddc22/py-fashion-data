from source import templates
from source import config_data_map

from utilsx import file_writer


def generate():

    xml_collection = []
    for category_id, products in config_data_map.product_data.items():
        for product in products:
            product_id = product["product_id"]

            xml_doc = templates.product_product_group.format(
                product_id=product_id,
                group_id=category_id)
            xml_collection.append(xml_doc)
            print(category_id, product_id)

    print(""" 

    **********************************  

        Generated product product group count {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ProductProductGroup.xml", xml_collection)
