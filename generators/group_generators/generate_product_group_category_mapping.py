from source import templates
from source import cat_hierarchy

from utilsx import file_writer

level_1 = "FASHION"


def generate_product_group(category):
    category["group_id"]

    xml_doc = templates.product_search_category_mapping.format(
        catrgory_id=category["group_id"].lower(),
        product_group_id=category["group_id"]
    )
    print(category["group_id"])

    child_xmls = []
    for child_category in category["children"]:
        child_xmls = child_xmls + generate_product_group(child_category)

    return [xml_doc] + child_xmls


def generate():

    xml_collection = []
    for category in cat_hierarchy.data:
        xml_collection.extend(generate_product_group(category))
    print("""

    ********************************************

        Generated ProductSearchCategoryMapping count {count}

    ********************************************


    """.format(count=str(len(xml_collection))))
    file_writer.write_config(
        "ProductSearchCategoryMapping.xml", xml_collection)
