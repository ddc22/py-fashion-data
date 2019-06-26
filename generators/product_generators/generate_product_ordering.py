from source import templates
from utilsx import file_writer
from source import config_data_map


def generate(data_collection):

    product_supplier = {}
    xml_collection = []
    sequence = 0
    for product_id in data_collection:
        xml_doc = templates.product_ordering.format(
            product_id=product_id,
            delivery_type_id="Express")
        xml_collection.append(xml_doc)

    print(""" 

    **********************************  

        Generated product ordering {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ProductOrdering.xml", xml_collection)
