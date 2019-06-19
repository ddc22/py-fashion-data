media_template = """ 
<retail:productMedia xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns3="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:ns6="http://www.enactor.com/crm" xmlns:ns8="http://www.enactor.com/addressLookup/service" xmlns:ns9="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <retail:productMediaId>{media_id}</retail:productMediaId>
    <retail:productId>{product_id}</retail:productId>
    <retail:mediaType>IMAGE</retail:mediaType>
    <retail:mediaSubtype>LARGE</retail:mediaSubtype>
    <retail:name>LARGE</retail:name>
    <retail:imageKey type="jpg" category="PRODUCT">{image_id}</retail:imageKey>
</retail:productMedia>
"""


def generate(media_map):

    pmf = open("configs/ProductMedia.xml", "w")
    pmf.truncate()
    pmf.close()

    product_media_file = open("configs/ProductMedia.xml", "a")
    xml_header = """
    <Batch>
    """
    xml_footer = """
    </Batch>
    """

    product_media_file.write(xml_header)

    for product_id, images in media_map.items():
        sequence = 0
        for image_id in images:
            sequence += 1
            media_id = product_id+"-M" + str(sequence)
            print(product_id, media_id, image_id)
            xml_doc = media_template.format(
                media_id=media_id,
                product_id=product_id,
                image_id=image_id)
            product_media_file.write(xml_doc)

    product_media_file.write(xml_footer)
    product_media_file.close()
