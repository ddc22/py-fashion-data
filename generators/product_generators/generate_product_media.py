from source import templates
from utils import file_writer
media = ["LARGE", "THUMB"]

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


def generate(media_map):

    xml_collection = []
    for sub_type, product_image in media_map.items():
        for product_id, images in product_image.items():
            sequence = 0
            for image_id in images:
                sequence += 1
                media_id = product_id+"-M" + str(sequence)
                print(product_id, media_id, image_id)
                xml_doc = templates.product_media.format(
                    media_id=media_id,
                    sub_type=sub_type,
                    product_id=product_id,
                    image_id=image_id)
                xml_collection.append(xml_doc)

    print(""" 

    **********************************  

        Generated media count {count}

    **********************************    


    """.format(count=str(len(xml_collection))))
    file_writer.write_config("ProductMedia.xml", xml_collection)
