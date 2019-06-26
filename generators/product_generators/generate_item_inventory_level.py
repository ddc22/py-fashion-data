from source import templates
from utilsx import file_writer
from source import config_data_map

locations = ["0001", "0003", "0100"]


def generate(data_collection):

    product_supplier = {}
    xml_collection = []
    sequence = 0
    for product_id in data_collection:
        for location in locations:
            xml_doc = templates.item_inventory_level.format(
                product_id=product_id,
                location_id=location,
                value="20000")
            xml_collection.append(xml_doc)

    print(""" 

    **********************************  

        Generated item inventory level {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ItemInventoryLevel.xml", xml_collection)
