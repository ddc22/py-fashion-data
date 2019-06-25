from source import templates, config_data_map
from source import cat_hierarchy

import logging
from utilsx import file_writer


def generate():
    size_range_xml_collection = []
    size_xml_collection = []

    for category, sizes in config_data_map.cat_sizes.items():
        size_range_xml = templates.size_range_start.format(
            size_range_id=category,
            description=category.replace("_", " ").title()
        )
        for size in sizes:
            size_id = size.replace("/", "_").replace(".", "POINT")

            size_xml = templates.size.format(
                size_id=size_id,
                size_range_id=category,
                size_description=size,
            )
            size_xml_collection.append(size_xml)

            size_range_xml = size_range_xml + templates.size_range_sizes.format(
                size_range_id=category,
                size=size.replace("/", "_").replace(".", "POINT")
            )

        size_range_xml = size_range_xml + templates.size_range_end
        size_range_xml_collection.append(size_range_xml)

    print(""" 
    ****************************************  

        Generated size count:  {count}

    ****************************************""".format(count=str(len(size_xml_collection))))
    file_writer.write_config("Size.xml", size_xml_collection)

    print("""    ****************************************  

        Generated size range count {count}

    ****************************************  
    """.format(count=str(len(size_range_xml_collection))))
    file_writer.write_config("SizeRange.xml", size_range_xml_collection)
