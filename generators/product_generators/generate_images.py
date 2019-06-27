from source import config_data_map, templates
import base64
import os
from utilsx import file_writer, util
from os import path
import logging


image_category = 'PRODUCT'

workdir = os.getcwd()

missing_images = []


def get_base_64_image(image_id, extension):
    img_path = workdir+"/resources/images/PRODUCTS/"+image_id+"."+extension
    if path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = str(base64.b64encode(image_file.read()))
        return encoded_string[2:-1]
    else:
        missing_images.append(image_id)
        logging.exception(' The Image '+img_path+" Does not exist")
        return ''


def generate():
    xml_collection = []

    for category, products in config_data_map.product_data.items():
        for product in products:
            for colour, images in product["colour_image_map"].items():
                product_name = product["name"]
                image_description = product_name+" " + colour + " " + category
                image_description = util.force_length(image_description, 20)

                xml_doc = templates.image.format(
                    image_category=image_category,
                    image_id=product["image_thumbnail_id"],
                    description=image_description,
                    file_name=product["image_thumbnail_id"] + 'jpg',
                    extension='jpg',
                    image_data=get_base_64_image(product["image_thumbnail_id"], "jpg"))
                xml_collection.append(xml_doc)
                print(category, colour, product["image_thumbnail_id"])

                for image in images:
                    xml_doc = templates.image.format(
                        image_category=image_category,
                        image_id=image,
                        description=image_description,
                        file_name=image + 'jpg',
                        extension='jpg',
                        image_data=get_base_64_image(image, "jpg"))
                    xml_collection.append(xml_doc)
                    print(category, colour, image)

    print("""

    **********************************

        Generated images {count}

    **********************************


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("Image.xml", xml_collection)
    logging.warning("Missing images: ", missing_images)
