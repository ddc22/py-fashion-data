import shutil
import os
import sys
import json
import util
import file_writer
import logging

import templates
import config_data_map
import generate_products
import generate_supplier_product
import generate_product_media
import generate_product_price
import generate_product_group
import generate_brand_group


shutil.rmtree('configs')
os.mkdir('configs')

generated_data = generate_products.generate()
products_array = generated_data["products_array"]
product_image_map = generated_data["product_image_map"]

generate_product_media.generate(product_image_map)
generate_supplier_product.generate(products_array)
generate_product_price.generate()
generate_product_group.generate()
generate_brand_group.generate()
# print(json.dumps(product_image_map, indent=4))
# json.dumps(products_array)
