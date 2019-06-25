from source import templates
from generators.group_generators import generate_product_group_category_mapping
from generators.product_generators import generate_product_attribute
from source import templates
from generators.global_generators import generate_colours
from utilsx import util
import glob
import os

# templates.sample_product_search_category_mapping()
# generate_product_group_category_mapping.generate()
# templates.sample_product_attribute_brand()
# templates.sample_product_attribute_stars()
# templates.sample_colour_range()

# generate_product_attribute.generate()
# generate_colours.generate()
# templates.sample_size()
# templates.sample_size_range()

# strval = "Dyed Canvas Overshirt Jacket"
# i = util.find_reverse_safe_split_index(strval, 20)
# print(strval[i:])

# strval = "Dyed Canvas Overshirt Jacket"
# i = util.find_safe_split_index(strval, 20)
# print(strval[:i])

strval = "Update your weekend wardrobe with this silk printed short sleeve shirt from Dolce and Gabbana. Get excited. Constructed with a button down closure, this piece features short sleeves and a pointed collar."
i = util.find_safe_split_index(strval, 120)
print(strval[:i])
