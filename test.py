from source import templates
from generators.group_generators import generate_product_group_category_mapping
from generators.product_generators import generate_product_attribute
from source import templates
from generators.global_generators import generate_colours

import glob
import os

# templates.sample_product_search_category_mapping()
# generate_product_group_category_mapping.generate()
# templates.sample_product_attribute_brand()
# templates.sample_product_attribute_stars()
# templates.sample_colour_range()

# generate_product_attribute.generate()
generate_colours.generate()
