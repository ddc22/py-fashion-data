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

# strval = "Update your weekend wardrobe with this silk printed short sleeve shirt from Dolce and Gabbana. Get excited. Constructed with a button down closure, this piece features short sleeves and a pointed collar."
# i = util.find_safe_split_index(strval, 120)
# print(strval[:i])


facets = {
    "Brand_DSQUARED2": 1,
    "Brand_NIKE": 1,
    "Brand_BARBOUR": 1,
    "Brand_JUST_CAVALLI": 0,
    "Brand_VALENTINO": 4,
    "Brand_DVF": 0,
    "Brand_GUCCI": 5,
    "Brand_PRADA": 2,
    "Brand_TUMI": 1,
    "Brand_AGENT_PROVOCATEUR": 0,
    "Brand_HELMUT_LANG": 1,
    "Brand_BY_MALENE_BIRGER": 0,
    "Brand_VANS": 1,
    "Brand_DSQUARED2_UNDERWEAR": 1,
    "Brand_BOSS_SMART_CASUAL": 0,
    "Brand_VIVIENNE_WESTWOOD": 3,
    "Brand_BURBERRY": 3,
    "Brand_PAUL_AND_SHARK": 1,
    "Brand_LOVESHACKFANCY": 0,
    "Brand_HUGO_BOSS": 1,
    "Brand_BALMAIN": 0,
    "Brand_MONCLER": 3,
    "Brand_DOLCE_AND_GABBANA": 2,
    "Brand_KENZO": 1,
    "Brand_STONE_ISLAND": 7,
    "Brand_JW_ANDERSON": 1,
    "Brand_DOLCE_N_GABBANA": 0,
    "Brand_FENDI": 2,
    "Brand_2_MONCLER_1952": 1,
    "Brand_MAGDA_BUTRYM": 0,
    "Brand_BOSS_BODYWEAR": 1,
    "Brand_INTERNAL": 1,
    "Brand_BOSS_ATHLEISURE": 1,
    "Brand_BOSS_BUSINESS": 1,
    "Brand_OFF_WHITE": 2,
    "Brand_JEFFERY_WEST": 2,
    "Brand_GRENSON": 2,
    "Brand_PALM_ANGELS": 1,
    "Brand_BEN_SHERMAN": 1,
    "Brand_POLO_RALPH_LAUREN": 7,
    "Brand_PS_BY_PAUL_SMITH": 1,
    "Brand_BBCLUB": 1,
    "Brand_CALVIN_KLEIN": 0,
    "Brand_CHLOE": 0,
    "Brand_EMPORIO_ARMANI": 0,
    "Brand_BOUTIQUE_MOSCHINO": 0,
    "Brand_MALLET": 1,
    "Brand_BALR": 1,
    "Brand_GIUSEPPE_ZANOTTI": 2,
    "Brand_NAPAPIJRI": 1
}


options = []
for brand_facet, count in facets.items():
    options.append({
        "optionId": brand_facet,
        "optionName": brand_facet.replace("Brand_", "").replace("_", " ").title()
    })
print(options)
