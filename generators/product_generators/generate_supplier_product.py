from source import templates
from utils import file_writer
from source import config_data_map

# SAMPLE
# {
#     "LARGE": {
#         "DF517XM": [
#             "DF517XM"
#         ],
#         "DF517XM-11": [
#             "DF517XM",
#             "DF517XM-1",
#             "DF517XM-2",
#             "DF517XM-3",
#             "DF517XM-4"
#         ]
#     },
#     "THUMB": {
#         "DF517XM": [
#             "DF517XM-T"
#         ],
#         "ID816BN": [
#             "DF517XM-T"
#         ],
#     }
# }


def generate_supplier_product_code(product_id, sequence):
    return config_data_map.supplier_id + product_id + sequence


def generate_supplier_product_cost(product_supplier):
    xml_collection = []
    for product_id, supplier_product_id in product_supplier.items():
        print(product_id, supplier_product_id)
        xml_doc = templates.supplier_product_cost.format(
            supplier_product_id=supplier_product_id,
            cost="50.00",
            supplier_id=config_data_map.supplier_id,
            currency_id=config_data_map.currency_id,
            product_id=product_id)
        xml_collection.append(xml_doc)
    print(""" 

    ************************************************** 

        Generated supplier product cost : {count}

    **************************************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("SupplierProductCost.xml", xml_collection)


def generate(data_collection):

    product_supplier = {}
    xml_collection = []
    sequence = 0
    for product_id in data_collection:
        sequence += 1
        supplier_product_id = generate_supplier_product_code(
            product_id, str(sequence))
        product_supplier[product_id] = supplier_product_id
        print(product_id, supplier_product_id)
        xml_doc = templates.supplier_product.format(
            supplier_product_id=supplier_product_id,
            supplier_id=config_data_map.supplier_id,
            product_id=product_id)
        xml_collection.append(xml_doc)

    print(""" 

    **********************************  

        Generated supplier product {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("SupplierProduct.xml", xml_collection)

    generate_supplier_product_cost(product_supplier)
