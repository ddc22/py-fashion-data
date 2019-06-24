from source import templates
from source import cat_hierarchy

from utilsx import file_writer

level_1 = "FASHION"


def generate_product_group(category, parent_hierarchy=[]):
    current_parent_hierarchy = parent_hierarchy.copy()
    current_level = len(current_parent_hierarchy) + 2
    level = {}
    for i in range(1, 11):
        level["level_"+str(i)] = ''

    level["level_1"] = level_1
    l = 1
    for group in current_parent_hierarchy:
        l += 1
        level["level_"+str(l)] = group

    l += 1
    level["level_"+str(l)] = category["group_id"]
    xml_doc = templates.group.format(
        group_id=category["group_id"],
        level_1=level["level_1"],
        level_2=level["level_2"],
        level_3=level["level_3"],
        level_4=level["level_4"],
        level_5=level["level_5"],
        level_6=level["level_6"],
        level_7=level["level_7"],
        level_8=level["level_8"],
        level_9=level["level_9"],
        level_10=level["level_10"],
        name=category["name"],
        group_type_id='productGroup',
        group_hierarchy_id=level_1,
        level=str(current_level)
    )
    print(category["group_id"], current_level)

    current_parent_hierarchy.append(category["group_id"])
    child_xmls = []
    for child_category in category["children"]:
        child_xmls = child_xmls + \
            generate_product_group(child_category, current_parent_hierarchy)

    return [xml_doc] + child_xmls


def generate():

    xml_collection = []
    for category in cat_hierarchy.data:
        xml_collection.extend(generate_product_group(category))
    print("""

    ********************************************

        Generated product group count {count}

    ********************************************


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ProductGroup.xml", xml_collection)


# generate()
