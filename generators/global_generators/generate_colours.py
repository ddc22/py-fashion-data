from source import templates, config_data_map
from source import cat_hierarchy

import logging
from utilsx import file_writer


def generate():
    colour_range_xml_collection = []
    colour_xml_collection = []

    for category, products in config_data_map.product_data.items():
        category_description = category[3:].replace("_", " and ").title()
        colour_range_xml = templates.colour_range_start.format(
            range_id=category,
            description=category_description
        )
        colour_set = set()
        for product in products:
            sizes = config_data_map.cat_sizes[category]
            colour_map = product["colour_image_map"]
            for colour, images in colour_map.items():
                colour_set.add(colour)

        for colour in colour_set:
            colour_id = colour.replace("/", "_").replace(" ", "_")

            colour_xml = templates.colour.format(
                colour_id=colour_id,
                category_id=category,
                colour_description=colour.title(),
            )
            colour_xml_collection.append(colour_xml)
            print(colour_id, category, colour)

            colour_range_xml = colour_range_xml + templates.colour_range_colours.format(
                range_id=category,
                colour=colour_id
            )

        print("==============")

        print(category)
        colour_range_xml = colour_range_xml + templates.colour_range_end
        colour_range_xml_collection.append(colour_range_xml)

    print(""" 
    ****************************************  

        Generated colour range count:  {count}

    ****************************************""".format(count=str(len(colour_range_xml_collection))))
    file_writer.write_config("ColourRange.xml", colour_range_xml_collection)

    print("""    ****************************************  

        Generated colour count {count}

    ****************************************  
    """.format(count=str(len(colour_xml_collection))))
    file_writer.write_config("Colour.xml", colour_xml_collection)
