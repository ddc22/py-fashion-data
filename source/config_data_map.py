import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

price_type = "R"
currency_id = "GBP"
supplier_id = "0001"


cat_sizes = {
    "MENS_SHIRTS": ["XL", "M", "L", "S"],
    "MENS_SHOES": ["8", "9", "10", "11", "12"],
    "WOMENS_BAGS": ["S"],
    "WOMENS_DRESSES": ["8", "10", "12", "14", "16", "18"]
}

# Replace
# / with underscore 
# . with "POINT"
cat_sizes = {
    "MC_JACKETS_COATS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
    "MC_SHIRTS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
    "MC_SHORTS_SWIMWEAR": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "MC_TROUSERS": ['S', 'S/M', 'M', 'M/L', 'L', 'XL', '2XL', '3XL'],
    "MC_TSHIRTS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
    "MS_DRESS_SHOES": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "MS_TRAINERS": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "MA_BAGS": ['ONE_SIZE'],
    "MA_HATS_CAPS": ['XS', 'S', 'S/M', 'M', 'M/L', 'L', 'XL', '2XL'],
    "WC_DRESSES": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "WC_JACKETS_COATS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "WC_NIGHTWEAR": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "WC_TOPS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "WC_TROUSERS": ['2XS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL'],
    "WS_BOOTS": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "WS_FLATS": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "WS_HEELS": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "WS_TRAINERS": ['5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12'],
    "WA_BAGS": ['ONE_SIZE'],
    "WA_BELTS": ['ONE_SIZE'],
    "WA_FRAGRANCE": ['ONE_SIZE'],
}


product_data = {
  "MC_JACKETS_COATS": [
    {
      "product_id": "FPCS7PX",
      "name": "Canada Denim Jacket",
      "long_description": "Update your denim collection with the DSquared2 Canada Denim Jacket. Crafted with a pointed collar and central button down closure, this jacket features exposed stitching and long button cuffed sleeves. Finished with four pockets to the front and a large contrasting branded tab to the centre. This is not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "1_FPCS7PX",
      "image_thumbnail_id": "1_FPCS7PX_T",
      "brand": "DSQUARED2",
      "price":"495.00",
      "colour_image_map": {
        "BLUE": [
          "1_FPCS7PX",
          "2_FPCS7PX",
          "3_FPCS7PX",
          "4_FPCS7PX",
          "5_FPCS7PX"
        ]
      }
    },
    {
      "product_id": "3V3A8EJ",
      "name": "Dyed Canvas Overshirt Jacket",
      "long_description": "Fuse style with practicality with the dyed canvas overshirt jacket from Stone Island. Constructed with long sleeves, a pointed collar and central zip closure, this piece features two front pockets and is finished with the brands iconic removable badge to the sleeve.",
      "info": "Machine washable. Cotton.",
      "image_id": "6_3V3A8EJ",
      "image_thumbnail_id": "6_3V3A8EJ_T",
      "brand": "STONE ISLAND",
      "price":"295.00",
      "colour_image_map": {
        "AVIO": [
          "6_3V3A8EJ",
          "7_3V3A8EJ"
        ],
        "NAVY": [
          "8_3V3A8EJ"
        ],
        "LEMONE": [
          "9_3V3A8EJ"
        ],
        "MOSTO": [
          "10_3V3A8EJ"
        ]
      }
    },
    {
      "product_id": "ZIFTSBH",
      "name": "Bandana Tracksuit Jacket",
      "long_description": "Refresh your casual collection with this Bandana Tracksuit Jacket from Palm Angels. Crafted with long sleeves, this piece features a high neckline, two side zip pockets and a central zip closure. Finished with an all over bandana print, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "11_ZIFTSBH",
      "image_thumbnail_id": "11_ZIFTSBH_T",
      "brand": "PALM ANGELS",
      "price":"339.00",
      "colour_image_map": {
        "MULTI": [
          "11_ZIFTSBH",
          "12_ZIFTSBH"
        ]
      }
    },
    {
      "product_id": "ATNYUDT",
      "name": "Over The Head Panel Jacket",
      "long_description": "Refine your casual collection with this over the head panel jacket from JW Anderson. Crafted with long sleeves and elasticated cuffs, this style features a hooded neckline with a high fleece lining and two buttoned pockets to the front. Finished with a quarter zip closure and contrasting patches to the sleeves and hood, this piece is a must have.",
      "info": "Machine washable. Cotton.",
      "image_id": "13_ATNYUDT",
      "image_thumbnail_id": "13_ATNYUDT_T",
      "brand": "JW ANDERSON",
      "price":"659.00",
      "colour_image_map": {
        "KHAKI": [
          "13_ATNYUDT",
          "14_ATNYUDT"
        ]
      }
    },
    {
      "product_id": "PK8EI8E",
      "name": "Giroux Jacket",
      "long_description": "Invest in your winter jacket collection, with Moncler's Giroux jacket. Crafted with long sleeves, this piece features a central zip down closure, two front pockets and a drawstring hooded neckline. Finished with the brands signature logo to the sleeve and boasting branded stripes to the hood and cuffs, this padded piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "15_PK8EI8E",
      "image_thumbnail_id": "15_PK8EI8E_T",
      "brand": "MONCLER",
      "price":"875.00",
      "colour_image_map": {
        "NAVY": [
          "15_PK8EI8E",
          "16_PK8EI8E"
        ],
        "BROWN": [
          "17_PK8EI8E",
          "18_PK8EI8E"
        ]
      }
    },
    {
      "product_id": "HIIX22T",
      "name": "Dyed Canvas Overshirt Jacket",
      "long_description": "Fuse style with practicality with the dyed canvas overshirt jacket from Stone Island. Constructed with long sleeves, a pointed collar and central zip closure, this piece features two front pockets and is finished with the brands iconic removable badge to the sleeve.",
      "info": "Machine washable. Cotton.",
      "image_id": "19_HIIX22T",
      "image_thumbnail_id": "19_HIIX22T_T",
      "brand": "STONE ISLAND",
      "price":"295.00",
      "colour_image_map": {
        "STUCCO": [
          "19_HIIX22T",
          "20_HIIX22T"
        ],
        "SALVIA": [
          "21_HIIX22T",
          "22_HIIX22T"
        ]
      }
    },
    {
      "product_id": "PFBGCGM",
      "name": "Jacquard Track Jacket",
      "long_description": "Make a statement in this jacquard track jacket from Gucci. Crafted with a high neckline and long sleeves, this piece features two front zipped pockets, a central zip down closure and is finished with striped ribbed trims and an all over GG print. ",
      "info": "Machine washable. Cotton.",
      "image_id": "23_PFBGCGM",
      "image_thumbnail_id": "23_PFBGCGM_T",
      "brand": "GUCCI",
      "price":"1160.00",
      "colour_image_map": {
        "CASP/BEIGE": [
          "23_PFBGCGM",
          "24_PFBGCGM"
        ]
      }
    },
    {
      "product_id": "5RG0MF2",
      "name": "Pocket Nylon Jacket",
      "long_description": "Fuse style with practicality with the pocket nylon jacket from Stone Island. Constructed with long sleeves, this piece features a pointed collar, a central zip closure and two button patch pockets. Finished with the brands signature logo to the sleeve, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "25_5RG0MF2",
      "image_thumbnail_id": "25_5RG0MF2_T",
      "brand": "STONE ISLAND",
      "price":"350.00",
      "colour_image_map": {
        "SAGE": [
          "25_5RG0MF2",
          "26_5RG0MF2"
        ]
      }
    },
    {
      "product_id": "BR2OSZX",
      "name": "Logo Hooded Jacket",
      "long_description": "Refresh your casual outerwear options with the Logo Hooded Jacket from Moncler. Crafted in a light weight design, this piece features a zip down closure, two front zip pockets and elasticated cuffs. Finished with A striped trim to the hood and the brands signature logo to the sleeve, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "27_BR2OSZX",
      "image_thumbnail_id": "27_BR2OSZX_T",
      "brand": "MONCLER",
      "price":"419.00",
      "colour_image_map": {
        "BLACK": [
          "27_BR2OSZX",
          "28_BR2OSZX"
        ]
      }
    },
    {
      "product_id": "HB05Z4U",
      "name": "Wimbledon Tracksuit Top",
      "long_description": "Show your support for the sport in this Men's Polo Ralph Lauren Wimbledon Tracksuit Top. It is perfect for everyday wear thanks to a soft polyester construction, whilst elasticated trims provide a superior fit. The look is completed in a colour block design with Polo Ralph Lauren branding and a Wimbledon logo.",
      "info": "Machine washable. Cotton.",
      "image_id": "29_HB05Z4U",
      "image_thumbnail_id": "29_HB05Z4U_T",
      "brand": "Polo Ralph Lauren",
      "price":"155.00",
      "colour_image_map": {
        "FRENCH NAVY": [
          "29_HB05Z4U",
          "30_HB05Z4U",
          "31_HB05Z4U",
          "32_HB05Z4U",
          "33_HB05Z4U"
        ]
      }
    }
  ],
  
  "MC_SHIRTS": [
    {
      "product_id": "ECY3U8K",
      "name": "Stripe Long Sleeve Shirt",
      "long_description": "This GUCCI Stripe Long Sleeve Shirt would be a welcome addition to any capsule wardrobe. This oversized piece features a pointed collar and long button cuffed sleeves. Boasting a central button down closure and chest pocket. Finished with a stripe pattern all over and the brands logo printed to the hemline.",
      "info": "Machine washable. Cotton.",
      "image_id": "1_ECY3U8K",
      "image_thumbnail_id": "1_ECY3U8K_T",
      "brand": "GUCCI",
      "price":"490.00",
      "colour_image_map": {
        "BLUE/WHITE": [
          "1_ECY3U8K",
          "2_ECY3U8K"
        ]
      }
    }, 
    {
      "product_id": "AGBI627",
      "name": "Camouflage Long Sleeve Shirt",
      "long_description": "Update your casual wardrobe with this Valentino Camouflage Long Sleeve shirt.  This classic shirt will be sure to make a statement day or evening time with the pointed collar and long sleeves. Boasting a central button closure and all over camouflage print. Finished with the the brands VLTN logo emblazoned and is not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "3_AGBI627",
      "image_thumbnail_id": "3_AGBI627_T",
      "brand": "VALENTINO",
      "price":"625.00",
      "colour_image_map": {
        "NAVY": [
          "3_AGBI627",
          "4_AGBI627"
        ]
      }
    }, 
    {
      "product_id": "DX8ASD3",
      "name": "Long Sleeved Orb Shirt",
      "long_description": "Upgrade your smart, casual look with this long sleeved Orb shirt from Vivienne Westwood. This classic long sleeved style features a pointed collar and central button down closure. Finished with the brands signature Orb logo to the chest, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "5_DX8ASD3",
      "image_thumbnail_id": "5_DX8ASD3_T",
      "brand": "VIVIENNE WESTWOOD",
      "price":"200.00",
      "colour_image_map": {
        "BURGUNDY": [
          "5_DX8ASD3",
          "6_DX8ASD3",
          "7_DX8ASD3",
          "8_DX8ASD3",
          "9_DX8ASD3"
        ],
        "WHITE": [
          "10_DX8ASD3",
          "11_DX8ASD3"
        ]
      }
    }, 
    {
      "product_id": "8PY35AD",
      "name": "Paint Camouflage Shirt",
      "long_description": "Elevate your off duty attire with the from Off White. Crafted in a paint camouflage print, this shirt features a pointed collar and central button closure. Boasting short sleeves and a chest pocket. Finished with the brands arrow print to the back and logo to the chest. This is not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "12_8PY35AD",
      "image_thumbnail_id": "12_8PY35AD_T",
      "brand": "OFF WHITE",
      "price":"460.00",
      "colour_image_map": {
        "CAMO": [
          "12_8PY35AD",
          "13_8PY35AD",
          "14_8PY35AD",
          "15_8PY35AD",
          "16_8PY35AD"
        ]
      }
    }, 
    {
      "product_id": "0J70Q0P",
      "name": "George Shirt",
      "long_description": "Refresh your wardrobe with this George shirt from Burberry. Crafted with long sleeves and a pointed collar, this piece features a central button closure and buttoned cuffs. Finished with a pocket to the chest and the brands tartan print all over.",
      "info": "Machine washable. Cotton.",
      "image_id": "17_0J70Q0P",
      "image_thumbnail_id": "17_0J70Q0P_T",
      "brand": "BURBERRY",
      "price":"250.00",
      "colour_image_map": {
        "BEIGE": [
          "17_0J70Q0P",
          "18_0J70Q0P",
          "19_0J70Q0P"
        ],
        "NAVY": [
          "20_0J70Q0P",
          "21_0J70Q0P",
          "22_0J70Q0P"
        ],
        "MARRON": [
          "23_0J70Q0P",
          "24_0J70Q0P",
          "25_0J70Q0P"
        ]
      }
    }, 
    {
      "product_id": "X7E4OMV",
      "name": "Ff Short Sleeve Shirt",
      "long_description": "Lift your collection with this FF short sleeve shirt from Fendi. Featuring a central button down closure and pointed collar, this piece features short sleeves and is emblazoned all over in the brands iconic FF logo.",
      "info": "Machine washable. Cotton.",
      "image_id": "26_X7E4OMV",
      "image_thumbnail_id": "26_X7E4OMV_T",
      "brand": "FENDI",
      "price":"489.00",
      "colour_image_map": {
        "BEIGE": [
          "26_X7E4OMV",
          "27_X7E4OMV"
        ]
      }
    }, 
    {
      "product_id": "7D7MLHR",
      "name": "Windsor Long Sleeve Shirt",
      "long_description": "Refresh your wardrobe with this Windsor long sleeve shirt from Burberry. Perfect for everyday, this piece features a pointed collar, long sleeves and buttoned cuffs. Finished with the brands vintage check all over and pocket to the chest, this would make for a welcome investment.",
      "info": "Machine washable. Cotton.",
      "image_id": "28_7D7MLHR",
      "image_thumbnail_id": "28_7D7MLHR_T",
      "brand": "BURBERRY",
      "price":"239.00",
      "colour_image_map": {
        "BEIGE": [
          "28_7D7MLHR",
          "29_7D7MLHR"
        ],
        "RED": [
          "30_7D7MLHR",
          "31_7D7MLHR"
        ]
      }
    }, 
    {
      "product_id": "NQYATWA",
      "name": "Silk Printed Short Sleeve Shirt",
      "long_description": "Update your weekend wardrobe with this silk printed short sleeve shirt from Dolce and Gabbana. Constructed with a button down closure, this piece features short sleeves and a pointed collar. Finished with an all over multi print, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "32_NQYATWA",
      "image_thumbnail_id": "32_NQYATWA_T",
      "brand": "DOLCE AND GABBANA",
      "price":"725.00 ",
      "colour_image_map": {
        "MULTI": [
          "32_NQYATWA",
          "33_NQYATWA",
          "34_NQYATWA"
        ]
      }
    }, 
    {
      "product_id": "1RZV8UL",
      "name": "Abstract Short Sleeve Shirt",
      "long_description": "Upgrade your weekend wardrobe with this Abstract Short Sleeve shirt from Prada. Designed with a pointed notched lapel collar and short sleeves, this light weight style is crafted with a pocket to the chest and central button down closure. Boasting spliced hems and branded tab to the pocket, this unique piece is finished with a multi-tonal floral abstract pattern all over.",
      "info": "Machine washable. Cotton.",
      "image_id": "35_1RZV8UL",
      "image_thumbnail_id": "35_1RZV8UL_T",
      "brand": "PRADA",
      "price":"669.00 ",
      "colour_image_map": {
        "MULTI": [
          "35_1RZV8UL",
          "36_1RZV8UL",
          "37_1RZV8UL"
        ]
      }
    }, 
    {
      "product_id": "3EN2OV5",
      "name": "Long Sleeved Orb Shirt",
      "long_description": "Upgrade your smart, casual look with this long sleeved Orb shirt from Vivienne Westwood. This classic long sleeved style features a pointed collar and central button down closure. Finished with the brands signature Orb logo to the chest, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "38_3EN2OV5",
      "image_thumbnail_id": "38_3EN2OV5_T",
      "brand": "VIVIENNE WESTWOOD",
      "price":"189.00 ",
      "colour_image_map": {
        "SKY": [
          "38_3EN2OV5",
          "39_3EN2OV5",
          "40_3EN2OV5"
        ],
        "NAVY": [
          "41_3EN2OV5",
          "42_3EN2OV5",
          "43_3EN2OV5"
        ],
        "BLACK": [
          "44_3EN2OV5",
          "45_3EN2OV5",
          "46_3EN2OV5"
        ],
        "MARINE": [
          "47_3EN2OV5",
          "48_3EN2OV5",
          "49_3EN2OV5"
        ]
      }
    }, 
    {
      "product_id": "D250OGV",
      "name": "Three Button Shirt",
      "long_description": "Update your smart wardrobe with this Vivienne Westwood three button shirt.  This classic shirt will be sure to make a statement day or evening time with the regal three tier collar.  Featuring a central button closure, logo branded buttons and the brands iconic Orb logo to the chest, this long sleeved design is a must have.",
      "info": "Machine washable. Cotton.",
      "image_id": "50_D250OGV",
      "image_thumbnail_id": "50_D250OGV_T",
      "brand": "VIVIENNE WESTWOOD",
      "price":"208.00",
      "colour_image_map": {
        "BLACK": [
          "50_D250OGV",
          "51_D250OGV",
          "52_D250OGV"
        ]
      }
    }, 
    {
      "product_id": "XH8VSRV",
      "name": "All Over Print Short Sleeve Shirt",
      "long_description": "This all over print short sleeved shirt from Polo Ralph Lauren would make a welcome addition to your collection. Crafted with short sleeves and a pointed collar with button down accents, this piece features a central button down closure and is finished in an all over print of the brands iconic logo.",
      "info": "Machine washable. Cotton.",
      "image_id": "53_XH8VSRV",
      "image_thumbnail_id": "53_XH8VSRV_T",
      "brand": "POLO RALPH LAUREN",
      "price":"70.00",
      "colour_image_map": {
        "PINK": [
          "53_XH8VSRV",
          "54_XH8VSRV"
        ]
      }
    }, 
    {
      "product_id": "TIK9458",
      "name": "Busterino Short Sleeve Shirt",
      "long_description": "Invest in your smart casual collection with this Busterino short sleeve shirt from BOSS. Crafted with short sleeves, this piece features a central button closure and a pointed collar. Finished with the brands signature logo embroidered to the chest and stripe across the front, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "55_TIK9458",
      "image_thumbnail_id": "55_TIK9458_T",
      "brand": "BOSS ATHLEISURE",
      "price":"63.00 ",
      "colour_image_map": {
        "NAVY": [
          "55_TIK9458",
          "56_TIK9458"
        ]
      }
    }, 
    {
      "product_id": "HJSK1V4",
      "name": "Tape Shirt",
      "long_description": "This Degree shirt from Helmut Lang would make a welcome addition to your collection. Crafted with a pointed collar and long buttoned sleeves, this shirt features a central button closure. Finished with contrast tape detailing, this is a must have.",
      "info": "Machine washable. Cotton.",
      "image_id": "57_HJSK1V4",
      "image_thumbnail_id": "57_HJSK1V4_T",
      "brand": "HELMUT LANG",
      "price":"409.00",
      "colour_image_map": {
        "WHITE": [
          "57_HJSK1V4",
          "58_HJSK1V4"
        ]
      }
    }, 
    {
      "product_id": "6AG38G1",
      "name": "Floral Print Shirt",
      "long_description": "Uplift your weekend wardrobe with the floral print shirt from Kenzo. Crafted with a central button closure, this piece features a pointed collar, a pointed collar and short sleeves. Finished with an all over floral print, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "59_6AG38G1",
      "image_thumbnail_id": "59_6AG38G1_T",
      "brand": "KENZO",
      "price":"112.00",
      "colour_image_map": {
        "MID BLUE": [
          "59_6AG38G1",
          "60_6AG38G1"
        ]
      }
    }, 
    {
      "product_id": "B4UN1IG",
      "name": "Polo Short Sleeved Chino Shirt",
      "long_description": "This short sleeved Chino shirt from Polo Ralph Lauren would make a welcome addition to your collection. Crafted with short sleeves, this piece features a pointed button down collar, a central button down closure and a curved hemline. Finished with the brands signature embroidered logo to the chest, this piece would make a welcome addition to your wardrobe.",
      "info": "Machine washable. Cotton.",
      "image_id": "61_B4UN1IG",
      "image_thumbnail_id": "61_B4UN1IG_T",
      "brand": "POLO RALPH LAUREN",
      "price":"85.00",
      "colour_image_map": {
        "YELLOW": [
          "61_B4UN1IG",
          "62_B4UN1IG"
        ]
      }
    }, 
    {
      "product_id": "UZ2EAHL",
      "name": "Cheetah Shirt",
      "long_description": "Elevate your smart wear look with this Cheetah shirt from PS by Paul Smith. Crafted with a pointed collar and central button down closure, this shirt is finished with a multi-tonal Cheetah print all over.",
      "info": "Machine washable. Cotton.",
      "image_id": "63_UZ2EAHL",
      "image_thumbnail_id": "63_UZ2EAHL_T",
      "brand": "PS BY PAUL SMITH",
      "price":"125.00",
      "colour_image_map": {
        "NAVY": [
          "63_UZ2EAHL",
          "64_UZ2EAHL",
          "65_UZ2EAHL"
        ]
      }
    }, 
    {
      "product_id": "JALIFR0",
      "name": "Colour Block Print Shirt",
      "long_description": "Refresh your casual collection with this Colour Block Print shirt by Polo Ralph Lauren. Designed with a button down pointed collar and central button down closure, this shirt features long button cuffed sleeves. Finished with a colour block pattern and sailor prints, this is not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "66_JALIFR0",
      "image_thumbnail_id": "66_JALIFR0_T",
      "brand": "POLO RALPH LAUREN",
      "price":"129.00",
      "colour_image_map": {
        "MULTI": [
          "66_JALIFR0",
          "67_JALIFR0"
        ]
      }
    }, 
    {
      "product_id": "UWX9KXG",
      "name": "Polo Short Sleeved Chino Shirt",
      "long_description": "This short sleeved Chino shirt from Polo Ralph Lauren would make a welcome addition to your collection. Crafted with short sleeves, this piece features a pointed button down collar, a central button down closure and a curved hemline. Finished with the brands signature embroidered logo to the chest, this piece would make a welcome addition to your wardrobe.",
      "info": "Machine washable. Cotton.",
      "image_id": "68_UWX9KXG",
      "image_thumbnail_id": "68_UWX9KXG_T",
      "brand": "POLO RALPH LAUREN",
      "price":"85.00",
      "colour_image_map": {
        "SUNSET GREEN": [
          "68_UWX9KXG",
          "69_UWX9KXG",
          "70_UWX9KXG",
          "71_UWX9KXG",
          "72_UWX9KXG"
        ]
      }
    }, 
    {
      "product_id": "O5K6LEB",
      "name": "Checked Tailored Fit Shirt",
      "long_description": "Refresh your wardrobe with this checked tailored fit shirt from Barbour International. Perfect for everyday or evening, this classic tailored fitting shirt features a button down closure, a pointed collar and long button cuffed sleeves. Finished in an all over checked print with a patch pocket to the chest, this style is a must have. ",
      "info": "Machine washable. Cotton.",
      "image_id": "73_O5K6LEB",
      "image_thumbnail_id": "73_O5K6LEB_T",
      "brand": "Barbour",
      "price":"49.00",
      "colour_image_map": {
        "DRESS TARTAN": [
          "73_O5K6LEB",
          "74_O5K6LEB"
        ]
      }
    }
  ],
  
  "MC_SHORTS_SWIMWEAR": [
    {
      "product_id": "3G3CGRK",
      "name": "Gg Logo Swim Shorts",
      "long_description": "Refresh your swimwear collection with these GG logo swim shorts from Gucci. Constructed with an elasticated waist with inner drawstrings, this pair are finished with the brands signature interlocking GG print all over, as well as contrasting piped detailing. ",
      "info": "Machine washable. Cotton.",
      "image_id": "1_3G3CGRK",
      "image_thumbnail_id": "1_3G3CGRK_T",
      "brand": "GUCCI",
      "price":"350.00",
      "colour_image_map": {
        "IVORY": [
          "1_3G3CGRK",
          "2_3G3CGRK"
        ]
      }
    }, 
    {
      "product_id": "LNQW8YH",
      "name": "Vlogo Camouflage Swim Shorts",
      "long_description": "Update your swim collection with these VLOGO Camouflage swim shorts from Valentino. Constructed with an elasticated waistband with drawstring ties, this piece features two side pockets and an all over camouflage print. Finished with the brands signature vlogo to the side, this piece would make a welcome addition to your collection.",
      "info": "Machine washable. Cotton.",
      "image_id": "3_LNQW8YH",
      "image_thumbnail_id": "3_LNQW8YH_T",
      "brand": "VALENTINO",
      "price":"389.00",
      "colour_image_map": {
        "ARMY": [
          "3_LNQW8YH",
          "4_LNQW8YH"
        ]
      }
    }, 
    {
      "product_id": "CRD05IZ",
      "name": "Camouflage Drawstring Swimshorts",
      "long_description": "Update your swim collection with these Camouflage Drawstring swim shorts from Valentino. Constructed with a stretch, drawstring waistband and three pockets, this style features an all over camouflage print and are finished with the signature Rockstud detailing to the leg.",
      "info": "Machine washable. Cotton.",
      "image_id": "5_CRD05IZ",
      "image_thumbnail_id": "5_CRD05IZ_T",
      "brand": "VALENTINO",
      "price":"325.00",
      "colour_image_map": {
        "NVY/RED": [
          "5_CRD05IZ",
          "6_CRD05IZ"
        ]
      }
    }, 
    {
      "product_id": "I39LSWL",
      "name": "Logo Swim Shorts",
      "long_description": "DSquared2 logo swim shorts are a must have this season. Cut with a drawstring waist and two slip pockets, this pair boasts spliced hems and are finished with the brands logo emblazoned down the side of the left leg.",
      "info": "Machine washable. Cotton.",
      "image_id": "7_I39LSWl",
      "image_thumbnail_id": "7_I39LSWL_T",
      "brand": "DSQUARED2 UNDERWEAR",
      "price":"179.00",
      "colour_image_map": {
        "BLACK/WHITE": [
          "7_I39LSWl",
          "8_I39LSWl"
        ],
        "YELLOW/PINK": [
          "9_I39LSWl",
          "10_I39LSWl"
        ]
      }
    }, 
    {
      "product_id": "64O23Y4",
      "name": "Starfish Swim Shorts",
      "long_description": "These BOSS starfish swim shorts are a welcome addition to this seasons leisure wardrobe. Featuring an elasticated drawstring waist, two front pockets, a rear pocket, a net underlay and the brands logo to the left leg, this pair are not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "11_64O23Y4",
      "image_thumbnail_id": "11_64O23Y4_T",
      "brand": "Boss Bodywear",
      "price":"45.00",
      "colour_image_map": {
        "ORANGE": [
          "11_64O23Y4",
          "12_64O23Y4"
        ]
      }
    }
  ],
  
  "MC_TROUSERS": [
    {
      "product_id": "8VOLTY5",
      "name": "Nylon Trousers",
      "long_description": "Update your trouser collection with the nylon trousers from Stone Island. Crafted with a an elasticated waistband with drawstring ties, this piece features cuffed hems and a multitude of pockets. Finished with the brands signature logo to the side, this piece is not one to be missed.",
      "info": "Machine washable. Nylon.",
      "image_id": "1_7SLUY2D",
      "image_thumbnail_id": "1_7SLUY2D_T",
      "brand": "STONE ISLAND",
      "price":"295.00",
      "colour_image_map": {
        "BLACK": [
          "1_8VOLTY5",
          "2_8VOLTY5"
        ]
      }
    },
    {
      "product_id": "7SLUY2D",
      "name": "Poplin Cargo Trousers",
      "long_description": "Update your essential wear with these poplin cargo trousers from Stone Island. Crafted with an elasticated waistband with inner drawstrings and five pockets, this pair boasts elasticated cuffed hems and are finished with the brands iconic removable badge to one of the leg pockets.",
      "info": "Machine washable. Cotton.",
      "image_id": "3_7SLUY2D",
      "image_thumbnail_id": "3_7SLUY2D_T",
      "brand": "STONE ISLAND",
      "price":"260.00",
      "colour_image_map": {
        "SAGE": [
          "3_7SLUY2D",
          "4_7SLUY2D"
        ]
      }
    },
    {
      "product_id": "JYRVTF8",
      "name": "Arch Cuffed Jogging Bottoms",
      "long_description": "Relax in style with the Arch cuffed jogging bottoms from Billionaire Boys Club. Constructed with cuffed hems and a drawstring waistband, this casual style is finished with the brands iconic logo and pockets on either side. ",
      "info": "Machine washable. Cotton.",
      "image_id": "5_JYRVTF8",
      "image_thumbnail_id": "5_JYRVTF8_T",
      "brand": "BBCLUB",
      "price":"90.00",
      "colour_image_map": {
        "HEATHER GREY": [
          "5_JYRVTF8",
          "6_JYRVTF8"
        ],
        "NAVY": [
          "7_JYRVTF8",
          "8_JYRVTF8"
        ]
      }
    },
    {
      "product_id": "8RAOPKD",
      "name": "Ghost Taper Trousers",
      "long_description": "Update your trouser collection with the Ghost Taper trousers from Stone Island. This pair is crafted with a fly zip closure, belt loops and a multitude of pockets. Finished with the brands signature detachable logo to the leg, these are not to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "9_8RAOPKD",
      "image_thumbnail_id": "9_8RAOPKD_T",
      "brand": "STONE ISLAND",
      "price":"207.00",
      "colour_image_map": {
        "BEIGE": [
          "9_8RAOPKD",
          "10_8RAOPKD"
        ]
      }
    },
    {
      "product_id": "YGVBYFN",
      "name": "Tapered Trousers",
      "long_description": "Update your collection with these Polo Ralph Lauren Tapered Trousers. Crafted with a button fastening waist, they feature a zip fly for a classic look. These trousers are designed with 3 pockets and are a tapered style, complete with Polo Ralph Lauren branding.",
      "info": "Machine washable. Cotton.",
      "image_id": "11_YGVBYFN",
      "image_thumbnail_id": "11_YGVBYFN_T",
      "brand": "Polo Ralph Lauren",
      "price":"119.00",
      "colour_image_map": {
        "LUXURY TAN": [
          "11_YGVBYFN",
          "12_YGVBYFN",
          "13_YGVBYFN",
          "14_YGVBYFN",
          "15_YGVBYFN"
        ]
      }
    },
    {
      "product_id": "0XYYY19",
      "name": "Slim Fit Virgin Wool Trousers",
      "long_description": "Refine your smart attire with these BOSS slim fit virgin wool trousers. These trousers feature a zip fly and hook closure, belt loops and a multitude of pockets. Cut from a virgin wool with unfinished hems for personalised alterations, this pair are a must have.",
      "info": "Machine washable. Cotton.",
      "image_id": "16_0XYYY19",
      "image_thumbnail_id": "16_0XYYY19_T",
      "brand": "BOSS BUSINESS",
      "price":"169.00",
      "colour_image_map": {
        "COLBALT": [
          "16_0XYYY19",
          "17_0XYYY19",
          "18_0XYYY19"
        ]
      }
    },
    {
      "product_id": "7905732",
      "name": "Heat Reactive Thermosensitive Trousers",
      "long_description": "Casual Stone Island Heat Reactive Thermosensitive Trousers will be a welcome addition to your off-duty wardrobe. Crafted with a fly zip closure, belt loops and three pockets. Boasting elasticated panels and cuffed bottoms, these trousers have the brands removable badge to the leg. Finished with a cotton ripstop that colours react with temperature and morphes when exposed to heat.",
      "info": "Machine washable. Cotton.",
      "image_id": "19_7905732",
      "image_thumbnail_id": "19_7905732_T",
      "brand": "STONE ISLAND",
      "price":"277.00",
      "colour_image_map": {
        "NAVY": [
          "19_7905732",
          "20_7905732"
        ]
      }
    },
    {
      "product_id": "KMKT1IP",
      "name": "All Over Printed Jogging Bottoms",
      "long_description": "Enhance your off duty look with the all over printed jogging bottoms from Moncler Genius. Constructed with an elasticated waistband, this piece features a multitude of zipped pockets and cuffed elasticated hems. Finished with an all over print, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "21_KMKT1IP",
      "image_thumbnail_id": "21_KMKT1IP_T",
      "brand": "2 MONCLER 1952",
      "price":"385.00",
      "colour_image_map": {
        "RED/BLUE": [
          "21_KMKT1IP",
          "22_KMKT1IP"
        ]
      }
    },
    {
      "product_id": "J6RU5Y6",
      "name": "Stretch Chinos",
      "long_description": "Update your trouser collection with these stretch chinos from Prada. This contemporary style features a zip fly and button closure and are designed with a multitude of pockets and belt loops. Finished with turn up hems, this pair are a must have.",
      "info": "Machine washable. Cotton.",
      "image_id": "23_J6RU5Y6",
      "image_thumbnail_id": "23_J6RU5Y6_T",
      "brand": "PRADA",
      "price":"455.00",
      "colour_image_map": {
        "AVIO": [
          "23_J6RU5Y6",
          "24_J6RU5Y6"
        ]
      }
    },
    {
      "product_id": "Z2RW7P1",
      "name": "Ralph Cargo Trousers",
      "long_description": "The Cargo Trousers from Ralph Lauren feature a button fly, 4 pockets and belt loops. The look is completed with the Ralph Lauren branding.",
      "info": "Machine washable. Cotton.",
      "image_id": "25_Z2RW7P1",
      "image_thumbnail_id": "25_Z2RW7P1_T",
      "brand": "Polo Ralph Lauren",
      "price":"145.00",
      "colour_image_map": {
        "SURPLUS CA": [
          "25_Z2RW7P1",
          "26_Z2RW7P1",
          "27_Z2RW7P1",
          "28_Z2RW7P1",
          "29_Z2RW7P1"
        ]
      }
    }
  ],
  
  "MC_TSHIRTS": [
    {
      "product_id": "QXAR93Z",
      "name": "Stripe T Shirt",
      "long_description": "Update your off duty wardrobe with this GUCCI stripe t shirt. Crafted with a crew neckline, this piece features short sleeves and ribbed trims. Finished with an all over stripe design, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "1_QXAR93Z",
      "image_thumbnail_id": "1_QXAR93Z_T",
      "brand": "GUCCI",
      "price":"315.00",
      "colour_image_map": {
        "BLACK/WHITE": [
          "1_QXAR93Z",
          "2_QXAR93Z"
        ]
      }
    },
    {
      "product_id": "1IYO8G3",
      "name": "Vlogo T Shirt",
      "long_description": "Invest in your casual wardrobe with this VLOGO t shirt from VALENTINO. Crafted to a short sleeve style, this piece features a classic crew neckline and ribbed trims. Finished with the brands signature logo to the front, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "3_1IYO8G3",
      "image_thumbnail_id": "3_1IYO8G3_T",
      "brand": "VALENTINO",
      "price":"325.00",
      "colour_image_map": {
        "WHITE/BLACK": [
          "3_1IYO8G3",
          "4_1IYO8G3"
        ],
        "WHITE/RED": [
          "5_1IYO8G3",
          "6_1IYO8G3"
        ],
        "OLIVE/PINK": [
          "7_1IYO8G3",
          "8_1IYO8G3"
        ]
      }
    },
    {
      "product_id": "WW89RF9",
      "name": "Badge Logo T Shirt",
      "long_description": "Update your casual collection with this badge logo t shirt from Stone Island. Designed with short sleeves, this piece features a crew neckline and ribbed trims. Finished with the brands signature logo badge to the front, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "9_WW89RF9",
      "image_thumbnail_id": "9_WW89RF9_T",
      "brand": "STONE ISLAND",
      "price":"110.00",
      "colour_image_map": {
        "OLIVIA": [
          "9_WW89RF9",
          "10_WW89RF9"
        ]
      }
    },
    {
      "product_id": "Q30HROD",
      "name": "Chalk Short Sleeve T Shirt",
      "long_description": "Update your casual collection with this chalk short sleeve t shirt from Stone Island. Designed with short sleeves, this piece features a crew neckline and ribbed trims. Finished with the brands signature logo to the front in a chalk like print and chalk washed effect to the rear and sleeves, this piece is not one to be missed.",
      "info": "Machine washable. Cotton.",
      "image_id": "11_Q30HROD",
      "image_thumbnail_id": "11_Q30HROD_T",
      "brand": "STONE ISLAND",
      "price":"160.00",
      "colour_image_map": {
        "BLUE": [
          "11_Q30HROD",
          "12_Q30HROD"
        ]
      }
    },
    {
      "product_id": "GX8FYCZ",
      "name": "Tiger Logo T Shirt",
      "long_description": "Inject Kenzo into your casual wardrobe with this Tiger logo t shirt. Crafted with short sleeves and a crew neckline, this piece features ribbed trims and is finished with the brands signature tonal Tiger logo emblazoned to the chest.",
      "info": "Machine washable. Cotton.",
      "image_id": "13_GX8FYCZ",
      "image_thumbnail_id": "13_GX8FYCZ_T",
      "brand": "KENZO",
      "price":"85.00",
      "colour_image_map": {
        "ORANGE": [
          "13_GX8FYCZ",
          "14_GX8FYCZ"
        ]
      }
    }
  ],
  
  "MS_DRESS_SHOES": [
    {
      "product_id": "UMBR43L",
      "name": "Dylan Oxford Brogues",
      "long_description": "Refine your look with the Dylan shoes from Grenson. Crafted in a stunning smooth leather with signature broguing detail. This oxford style lace-up is highly versatile and can be worn for all occasions.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_UMBR43L",
      "image_thumbnail_id": "1_UMBR43L_T",
      "brand": "GRENSON",
      "price":"235.00",
      "colour_image_map": {
        "TAN": [
          "1_UMBR43L",
          "2_UMBR43L",
          "3_UMBR43L",
          "4_UMBR43L",
          "5_UMBR43L"
        ]
      }
    },
    {
      "product_id": "LE7OTN5",
      "name": "Wing Tip Yardbird",
      "long_description": "Re-invent a capsule footwear essential with the wing tip Yardbird shoes by Jeffery West. This sartorial, yet casual style is crafted in a smooth patent leather, featuring a pointed toe and a lace up closure this brogue detailed pair are finished with multi tonal leather panels.",
      "info": "Upper, lining and sole: leather",
      "image_id": "6_LE7OTN5",
      "image_thumbnail_id": "6_LE7OTN5_T",
      "brand": "JEFFERY WEST",
      "price":"205.00",
      "colour_image_map": {
        "DARK BROWN": [
          "6_LE7OTN5",
          "7_LE7OTN5",
          "8_LE7OTN5",
          "9_LE7OTN5",
          "10_LE7OTN5"
        ]
      }
    },
    {
      "product_id": "NJQRYT3",
      "name": "Suede Tassel Loafers",
      "long_description": "Add to a modern sartorial wardrobe with these suede tassel loafers by Jeffery West.  This classic style features traditional loafer detailing, crafted in a soft suede this pair boast plaited rope detailing, a block heel and are finished with a leather tassel to the upper.",
      "info": "Upper, lining and sole: leather",
      "image_id": "11_NJQRYT3",
      "image_thumbnail_id": "11_NJQRYT3_T",
      "brand": "JEFFERY WEST",
      "price":"190.00",
      "colour_image_map": {
        "ZAFIRO": [
          "11_NJQRYT3",
          "12_NJQRYT3",
          "13_NJQRYT3",
          "14_NJQRYT3",
          "15_NJQRYT3"
        ]
      }
    },
    {
      "product_id": "96IUPIM",
      "name": "Maxwell Loafers",
      "long_description": "Refine your footwear collection with these Maxwell loafers from Grenson. Crafted with a smooth leather, this style features a slip on style, exposed stitching, wooden sole and would make the perfect investment.",
      "info": "Upper, lining and sole: leather",
      "image_id": "16_96IUPIM",
      "image_thumbnail_id": "16_96IUPIM_T",
      "brand": "GRENSON",
      "price":"108.00",
      "colour_image_map": {
        "BLACK": [
          "16_96IUPIM",
          "17_96IUPIM",
          "18_96IUPIM",
          "19_96IUPIM",
          "20_96IUPIM"
        ],
        "BROWN": [
          "21_96IUPIM",
          "22_96IUPIM",
          "23_96IUPIM",
          "24_96IUPIM",
          "25_96IUPIM"
        ]
      }
    },
    {
      "product_id": "ZF5LZUR",
      "name": "Dock Loafers",
      "long_description": "Add some style to your wardrobe with the dock loafers from Giuseppe Zanotti. Crafted to a slip on style, this pair feature a rounded toe, contrasting soles, an all over textured upper and is finished with the brands signature logo detailing to the front.",
      "info": "Upper, lining and sole: leather",
      "image_id": "26_ZF5LZUR",
      "image_thumbnail_id": "26_ZF5LZUR_T",
      "brand": "GIUSEPPE ZANOTTI",
      "price":"243.00",
      "colour_image_map": {
        "BLACK/WHITE": [
          "26_ZF5LZUR",
          "27_ZF5LZUR",
          "28_ZF5LZUR",
          "29_ZF5LZUR",
          "30_ZF5LZUR"
        ]
      }
    }
  ],
  
  "MS_TRAINERS": [
    {
      "product_id": "E8JC2JH",
      "name": "Diver Trainers",
      "long_description": "Finish your off duty look with these diver trainers from Mallet. Constructed with a low top and a lace up closure, this style is crafted with a neoprene, leather and mesh upper and boast metal hardware to the sole and eyelets. ",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_E8JC2JH",
      "image_thumbnail_id": "1_E8JC2JH_T",
      "brand": "MALLET",
      "price":"132.00",
      "colour_image_map": {
        "BLACK": [
          "1_E8JC2JH",
          "2_E8JC2JH",
          "3_E8JC2JH",
          "4_E8JC2JH",
          "5_E8JC2JH"
        ]
      }
    },
    {
      "product_id": "Z67OK8Z",
      "name": "Rockstud Camouflage Trainers",
      "long_description": "Add to your luxury footwear collection with these rockstud camouflage trainers from Valentino GARAVANI. This contemporary style is crafted with a lace up closure, a branded tab to the tongue and the iconic studded detailing to the sole. Finished with camouflage panel accents, these trainers are a must have.",
      "info": "Upper, lining and sole: leather",
      "image_id": "6_Z67OK8Z",
      "image_thumbnail_id": "6_Z67OK8Z_T",
      "brand": "VALENTINO",
      "price":"555.00",
      "colour_image_map": {
        "GREY/SILVER": [
          "6_Z67OK8Z",
          "7_Z67OK8Z",
          "8_Z67OK8Z",
          "9_Z67OK8Z",
          "10_Z67OK8Z"
        ],
        "BLUE": [
          "11_Z67OK8Z",
          "12_Z67OK8Z",
          "13_Z67OK8Z",
          "14_Z67OK8Z",
          "15_Z67OK8Z"
        ]
      }
    },
    {
      "product_id": "OGF7Z8S",
      "name": "Sorrento Rhinestone Trainers",
      "long_description": "Give your footwear collection a contemporary edge with these Sorrento rhinestone trainers from Dolce and Gabbana. Boasting an elastic mesh upper, emblazoned with heat-pressed crystal appliqués, this slip on pair feature taped logo detailing to the upper, rear heel and pull tab. Finished on a quirky cubed and spiked sole, this pair would make the ultimate investment.",
      "info": "Upper, lining and sole: leather",
      "image_id": "16_OGF7Z8S",
      "image_thumbnail_id": "16_OGF7Z8S_T",
      "brand": "DOLCE AND GABBANA",
      "price":"683.00",
      "colour_image_map": {
        "ROSSO": [
          "16_OGF7Z8S",
          "17_OGF7Z8S",
          "18_OGF7Z8S",
          "19_OGF7Z8S",
          "20_OGF7Z8S"
        ]
      }
    },
    {
      "product_id": "1X7O50V",
      "name": "Yellow Monster Runners",
      "long_description": "Refine a contemporary casual's collection with the yellow monster runners by Fendi. This low top trainer is crafted with a smooth leather and suede upper. Boasting unique branding to the sole, a lace up fastening with spikes to the heel and branding to the tongue, this style is finished with the brands iconic monster eyes detailing.",
      "info": "Upper, lining and sole: leather",
      "image_id": "21_1X7O50V",
      "image_thumbnail_id": "21_1X7O50V_T",
      "brand": "FENDI",
      "price":"580.00",
      "colour_image_map": {
        "BLACK": [
          "21_1X7O50V",
          "22_1X7O50V",
          "23_1X7O50V",
          "24_1X7O50V",
          "25_1X7O50V"
        ]
      }
    },
    {
      "product_id": "RGJFXE0",
      "name": "Bubble Trainers",
      "long_description": "Finish your off duty look with the Bubble trainers from Moncler. Crafted with a lightweight sole articulated in the form of bubbles which support the sole of the foot with individual islands of ultra-soft rubber arranged to follow the shape of the foot. Boasting an upper formed by a knitted sock in multi-tonal panels. This trainer is not to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "26_RGJFXE0",
      "image_thumbnail_id": "26_RGJFXE0_T",
      "brand": "MONCLER",
      "price":"420.00",
      "colour_image_map": {
        "WHITE": [
          "26_RGJFXE0",
          "27_RGJFXE0",
          "28_RGJFXE0",
          "29_RGJFXE0"
        ]
      }
    }    
  ],
  
  "MA_BAGS": [
    {
      "product_id": "RAP2OKQ",
      "name": "Ophidia Gg Backpack",
      "long_description": "Combine both style and practicality with this ophidia GG backpack from Gucci. Constructed with the brands signature GG Supreme canvas, this bag features a zip closure to the main compartment and front section. With leather trims, a carry handle and adjustable rear shoulder straps this piece is finished with the familiar Web taping and metal hardware to the front.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_RAP2OKQ",
      "image_thumbnail_id": "1_RAP2OKQ_T",
      "brand": "GUCCI",
      "price":"1200.00",
      "colour_image_map": {
        "BEIGE": [
          "1_RAP2OKQ",
          "2_RAP2OKQ",
          "3_RAP2OKQ",
          "4_RAP2OKQ"
        ]
      }
    },
    {
      "product_id": "J2PXNXG",
      "name": "Arrows Backpack",
      "long_description": "Carry your essentials in this Arrows backpack from Off White. This canvas style is constructed with a zip around fastening to the main spacious compartment, two additional front pockets and branded adjustable shoulder straps. Finished with the iconic Arrows logo print to the front, this style would make a welcome addition.",
      "info": "Upper, lining and sole: leather",
      "image_id": "5_J2PXNXG",
      "image_thumbnail_id": "5_J2PXNXG_T",
      "brand": "OFF WHITE",
      "price":"277.00",
      "colour_image_map": {
        "BLACK": [
          "5_J2PXNXG",
          "6_J2PXNXG",
          "7_J2PXNXG",
          "8_J2PXNXG",
          "9_J2PXNXG"
        ]
      }
    },
    {
      "product_id": "QW8OSUG",
      "name": "Voyage Backpack",
      "long_description": "> Backpack, > Large main compartment, > Zipped inner pocket, > Front zip fastening pocket, > Padded and adjustable shoulder straps, > Grab handle, > H37cm x W30cm x D12cm",
      "info": "Upper, lining and sole: leather",
      "image_id": "10_QW8OSUG",
      "image_thumbnail_id": "10_QW8OSUG_T",
      "brand": "Napapijri",
      "price":"45.00",
      "colour_image_map": {
        "ORANGE": [
          "10_QW8OSUG",
          "11_QW8OSUG",
          "12_QW8OSUG",
          "13_QW8OSUG",
          "14_QW8OSUG"
        ],
        "BLUE": [
          "15_QW8OSUG",
          "16_QW8OSUG",
          "17_QW8OSUG",
          "18_QW8OSUG",
          "19_QW8OSUG"
        ]
      }
    },
    {
      "product_id": "20_F0R76SA",
      "name": "Logan Backpack",
      "long_description": "Tumi bring us the Logan backpack, the perfect addition to your acessories collection. Meticulously appointed with the finest aesthetic and engineering features, Arrivé features high-polish chrome retractable handles, a lightly-padded pocket lined with a non-abrasive microfiber suede that provides additional protection, and sleek magnetic zippers. With dedicated compartments for both a laptop and tablet, this hypermodern leather backpack is soon to be a favorite among the style-savvy business set.",
      "info": "Upper, lining and sole: leather",
      "image_id": "20_F0R76SA",
      "image_thumbnail_id": "20_F0R76SA_T",
      "brand": "TUMI",
      "price":"650.00",
      "colour_image_map": {
        "BLACK": [
          "20_F0R76SA",
          "21_F0R76SA",
          "22_F0R76SA",
          "23_F0R76SA"
        ]
      }
    },
    {
      "product_id": "B06D9CZ",
      "name": "Burberry Rocco Bpk Sn93",
      "long_description": "Always look stylish with this Burberry Modern Beast Backpack. Crafted with adjustable straps for a comfortable fit, this back features a main zip compartment with internal pockets as well as a front zip pocket for additional space. This camo print design has a signature logo to the front, completing the look with Burberry branding.",
      "info": "Upper, lining and sole: leather",
      "image_id": "24_B06D9CZ",
      "image_thumbnail_id": "24_B06D9CZ_T",
      "brand": "Burberry",
      "price":"650.00",
      "colour_image_map": {
        "BLACK": [
          "24_B06D9CZ",
          "25_B06D9CZ",
          "26_B06D9CZ",
          "27_B06D9CZ"
        ]
      }
    }
  ],
    
  "MA_HATS_CAPS": [
    {
      "product_id": "5T5QQE1",
      "name": "Classic logo cap",
      "long_description": "Seal off sports-casual looks in an instant with this classically designed cap from Hugo Boss. Crafted from pure cotton, it features the brand logo in stitched and contrasting highlights for a dose of designer appeal. With an adjustable metal closure at the back to secure, this baseball cap makes a complementing addition to any relaxed off-duty ensemble.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_5T5QQE1",
      "image_thumbnail_id": "1_5T5QQE1_T",
      "brand": "Hugo Boss",
      "price":"39.00",
      "colour_image_map": {
        "WHITE": [
          "1_5T5QQE1",
          "2_5T5QQE1",
          "2_5T5QQE1"
        ]
      }
    },
    {
      "product_id": "FBCG41H",
      "name": "Basic Logo Cap",
      "long_description": "Refine your look with this basic logo cap from Paul And Shark. Comprising of six panels, this cap features an adjustable strap to the rear with a branded metal hardware accent and a logo badge stamped to the front, a piece not to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "4_FBCG41H",
      "image_thumbnail_id": "4_FBCG41H_T",
      "brand": "Paul And Shark",
      "price":"55.00",
      "colour_image_map": {
        "NAVY": [
          "4_FBCG41H",
          "5_FBCG41H",
          "6_FBCG41H",
          "7_FBCG41H"
        ]
      }
    },
    {
      "product_id": "RMM8ZJ0",
      "name": "Gucci Guccy Cap",
      "long_description": " Invest in some luxury with the Guccy cap from Gucci. Boasting a mesh rear with a contrasting leather front and peak, this piece boasts the brands iconic Guccy branding featuring a rear adjustable velcro strap finished with the familiar Sega star print.",
      "info": "Upper, lining and sole: leather",
      "image_id": "8_RMM8ZJ0",
      "image_thumbnail_id": "8_RMM8ZJ0_T",
      "brand": "GUCCI",
      "price":"360.00",
      "colour_image_map": {
        "WHITE": [
          "8_RMM8ZJ0",
          "9_RMM8ZJ0",
          "10_RMM8ZJ0",
          "11_RMM8ZJ0"
        ]
      }
    },
    {
      "product_id": "EHAXFFG",
      "name": "Logo Cap",
      "long_description": " Invest in some casual attire with the logo cap from Giuseppe Zanotti. This canvas hat features an adjustable rear sizing to fit with metal studs and a six panel design. Finished with a branded metal logo to the front, this would be a welcome addition to your accessory collection.",
      "info": "Upper, lining and sole: leather",
      "image_id": "12_EHAXFFG",
      "image_thumbnail_id": "12_EHAXFFG_T",
      "brand": "GIUSEPPE ZANOTTI",
      "price":"250.00",
      "colour_image_map": {
        "RED/GOLD": [
          "12_EHAXFFG",
          "13_EHAXFFG",
          "14_EHAXFFG",
          "15_EHAXFFG"
        ],
        "BLACK/GOLD": [
          "16_EHAXFFG",
          "17_EHAXFFG",
          "18_EHAXFFG",
          "19_EHAXFFG"
        ]
      }
    },
    {
      "product_id": "2HWV2OM",
      "name": "Logo Cap",
      "long_description": "Finish your look with this cotton logo cap from BALR. This canvas six panel style features a shiny tonal logo to the front, eyelet detailing and an adjustable strap to the rear. Finished with a subtle branded tag to the rear, this casual style would be a welcome addition to your wardrobe.",
      "info": "Upper, lining and sole: leather",
      "image_id": "20_2HWV2OM",
      "image_thumbnail_id": "20_2HWV2OM_T",
      "brand": "BALR",
      "price":"60.00",
      "colour_image_map": {
        "BLACK": [
          "20_2HWV2OM",
          "21_2HWV2OM",
          "22_2HWV2OM",
          "23_2HWV2OM"
        ]
      }
    }     
  ],
    
  "WC_DRESSES": [
    {
      "product_id": "YU3YASN",
      "name": "Michael Garden Dress Womens",
      "long_description": "Slick and stylish, the Garden Dress from Michael Kors is perfect for summer days. Design is complete with a v neck, frilled sleeves, and peplum hemline.",
      "info": "98% polyester, 2% elastane",
      "image_id": "1_YU3YASN",
      "image_thumbnail_id": "1_YU3YASN_T",
      "brand": "Michael Kors",
      "price":"150.00",
      "colour_image_map": {
        "BLACK/PINK": [
          "1_YU3YASN",
          "2_YU3YASN",
          "3_YU3YASN",
          "4_YU3YASN",
          "5_YU3YASN"
        ]
      }
    },
    {
      "product_id": "9HU95PA",
      "name": "Bowie Floral Playsuit",
      "long_description": "Update your summer collection with this Bowie floral playsuit from Zimmermann. Constructed with long sleeves, this piece features a V neckline, an elasticated waistband with a removable tie belt. Finished with an all over floral print with contrasting spot ruffels and a tie and button closure to the neckline, this piece would make a welcome addition to your wardrobe.",
      "info": "98% polyester, 2% elastane",
      "image_id": "6_9HU95PA",
      "image_thumbnail_id": "6_9HU95PA_T",
      "brand": "ZIMMERMANN",
      "price":"406.00",
      "colour_image_map": {
        "LILAC": [
          "6_9HU95PA",
          "7_9HU95PA",
          "8_9HU95PA",
          "9_9HU95PA"
        ]
      }
    },
    {
      "product_id": "ENB6YL6",
      "name": "Emelia Floral Wrap Dress",
      "long_description": "Invest in this stunning Emelia Floral Wrap Dress from Diane Von Furstenberg. Designed in the brands signature wrap dress style, this piece features short sleeves with elasticated trims, a v neckline and a cross over tie waist. Finished with an all over floral design, this piece is not one to be missed.",
      "info": "98% polyester, 2% elastane",
      "image_id": "10_ENB6YL6",
      "image_thumbnail_id": "10_ENB6YL6_T",
      "brand": "DVF",
      "price":"159.00",
      "colour_image_map": {
        "FLEUR DOT": [
          "10_ENB6YL6",
          "11_ENB6YL6",
          "12_ENB6YL6",
          "13_ENB6YL6"
        ],
        "ROSE SHOWERS": [
          "14_ENB6YL6",
          "15_ENB6YL6",
          "16_ENB6YL6",
          "17_ENB6YL6"
        ]
      }
    },
    {
      "product_id": "IX9ETYU",
      "name": "Floral Heather Dress",
      "long_description": "Opt for playful, feminine occasion wear with the floral heather dress by Zimmermann. Designed with long blouson sleeves, this piece is crafted with a deep V neckline, a zip closure to the rear and a flared skirt. Finished with an all over floral print and dot scalloped trim, this piece would make a welcome addition to your wardrobe. ",
      "info": "98% polyester, 2% elastane",
      "image_id": "18_IX9ETYU",
      "image_thumbnail_id": "18_IX9ETYU_T",
      "brand": "ZIMMERMANN",
      "price":"469.00",
      "colour_image_map": {
        "FLORAL": [
          "18_IX9ETYU",
          "19_IX9ETYU",
          "20_IX9ETYU",
          "21_IX9ETYU"
        ]
      }
    },
    {
      "product_id": "D3KEYN7",
      "name": "Corsage Plisse Mini Dress",
      "long_description": "Opt for playful, feminine occasion wear with the Corsage Plisse mini dress by Zimmermann. Designed with an Orchid print, this empire waist dress features a deep V-neckline, blouson sleeves and A-line mini skirt. Boasting fine pleating for volume and button closure, this is not to be missed.",
      "info": "98% polyester, 2% elastane",
      "image_id": "22_D3KEYN7",
      "image_thumbnail_id": "22_D3KEYN7_T",
      "brand": "ZIMMERMANN",
      "price":"441.00",
      "colour_image_map": {
        "IVORY": [
          "22_D3KEYN7",
          "23_D3KEYN7",
          "24_D3KEYN7",
          "25_D3KEYN7"  
        ]
      }
    },
    {
      "product_id": "1ITVHC7",
      "name": "3d Floral Crochet Lace Mini Dress",
      "long_description": "Refresh your dress collection with this 3D floral crochet lace mini dress from Self Portrait. Constructed with a slim fitting bodice through to a tiered mini skirt, this sleeveless piece is cut from 3D floral and fishnet crochet lace panels. With a zip closure to the rear, this piece is a must have design.",
      "info": "98% polyester, 2% elastane",
      "image_id": "26_1ITVHC7",
      "image_thumbnail_id": "26_1ITVHC7_T",
      "brand": "SELF PORTRAIT",
      "price":"300.00",
      "colour_image_map": {
        "PINK": [
          "26_1ITVHC7",
          "27_1ITVHC7",
          "28_1ITVHC7",
          "29_1ITVHC7"
        ]
      }
    },
    {
      "product_id": "2DG1Q8X",
      "name": "Web Ruffle Dress",
      "long_description": "Add some sophistication into your collection with this Web ruffle dress from Gucci. Made in Italy, this chic style is crafted with three quarter length sleeves, a full length central zip closure to the front and ruffling to the trims. This dress boasts the brands iconic Webbing in a band to the waist and in a pussy bow style, completing the dress.",
      "info": "98% polyester, 2% elastane",
      "image_id": "30_2DG1Q8X",
      "image_thumbnail_id": "30_2DG1Q8X_T",
      "brand": "GUCCI",
      "price":"1200.00",
      "colour_image_map": {
        "BLACK": [
          "30_2DG1Q8X",
          "31_2DG1Q8X",
          "32_2DG1Q8X",
          "33_2DG1Q8X"
        ]
      }
    },
    {
      "product_id": "G1T2NIQ",
      "name": "MMK Wrap Drs Ld92",
      "long_description": "Add some sophistication into your collection with this Web ruffle dress from Michael Kors. Made in Italy, this chic style is crafted with three quarter length sleeves, a full length central zip closure to the front and ruffling to the trims. This dress boasts the brands iconic Webbing in a band to the waist and in a pussy bow style, completing the dress.",
      "info": "98% polyester, 2% elastane",
      "info": "98% polyester, 2% elastane",
      "image_id": "34_G1T2NIQ",
      "image_thumbnail_id": "34_G1T2NIQ_T",
      "brand": "Michael Kors",
      "price":"195.00",
      "colour_image_map": {
        "BLACK/YELLOW": [
          "34_G1T2NIQ",
          "35_G1T2NIQ",
          "36_G1T2NIQ",
          "37_G1T2NIQ"
        ]
      }
    },
    {
      "product_id": "WUGO2O5",
      "name": "V Neck Bodycon Dress",
      "long_description": "Uplift your dress collection with this v neck bodycon dress from Just Cavalli. Boasting a vibrant print all over, this bodycon style features capped sleeves and a plunged v neckline. This design would be a welcome addition to a summer evening wardrobe.",
      "info": "98% polyester, 2% elastane",
      "image_id": "38_WUGO2O5",
      "image_thumbnail_id": "38_WUGO2O5_T",
      "brand": "JUST CAVALLI",
      "price":"204.00",
      "colour_image_map": {
        "YELLOW": [
          "38_WUGO2O5",
          "39_WUGO2O5",
          "40_WUGO2O5",
          "41_WUGO2O5"
        ]
      }
    },
    {
      "product_id": "6I33EBA",
      "name": "Striped Short Dress",
      "long_description": "Revamp your evening collection with Patrizia Pepe's Striped Short Dress. This slim fitting style is constructed with a high neck line, capped sleeves and contrasting panels for the top and skirt. Featuring bow detailing to the back and a concealed zip closure, this piece is finished with a multi tonal striped pattern to the top. ",
      "info": "98% polyester, 2% elastane",
      "image_id": "42_6I33EBA",
      "image_thumbnail_id": "42_6I33EBA_T",
      "brand": "PATRIZIA PEPE",
      "price":"195.00",
      "colour_image_map": {
        "NAVY": [
          "42_6I33EBA",
          "43_6I33EBA",
          "44_6I33EBA",
          "45_6I33EBA"
        ]
      }
    },
    {
      "product_id": "QBTCOCK",
      "name": "Lace Panel Maxi Dress",
      "long_description": "Give your dress collection an elegant finish with this lace panel maxi dress from Perseverance London. Crafted with a v neckline with a concealed zip closure to the rear, this style is finished with feminine scalloped lace panels and a contrasting satin hem.",
      "info": "98% polyester, 2% elastane",
      "image_id": "46_QBTCOCK",
      "image_thumbnail_id": "46_QBTCOCK_T",
      "brand": "PERSEVERANCE LONDON",
      "price":"430.00",
      "colour_image_map": {
        "COPPER": [
          "46_QBTCOCK",
          "47_QBTCOCK",
          "48_QBTCOCK",
          "49_QBTCOCK",
          "50_QBTCOCK"
        ]
      }
    },
    {
      "product_id": "KTN1J8J",
      "name": "Mini Shift Dress",
      "long_description": "Refine your dress collection with Gucci's Mini Shift dress. Crafted with a rounded neckline and sleeveless style, this dress features contrasting trims. Boasting a concealed zip closure. Finished with two button pockets that feature GG engraved to the buttons.",
      "info": "98% polyester, 2% elastane",
      "image_id": "51_KTN1J8J",
      "image_thumbnail_id": "51_KTN1J8J_T",
      "brand": "GUCCI",
      "price":"1340.00",
      "colour_image_map": {
        "PINK": [
          "51_KTN1J8J",
          "52_KTN1J8J",
          "53_KTN1J8J"
        ]
      }
    },
    {
      "product_id": "LOS2UO8",
      "name": "Ruffled Silk Flying Phoenix Dress",
      "long_description": "Refine your dress collection with this Kenzo ruffled silk flying phoenix dress. Constructed with shoe string straps, this midi dress features a v neckline, ruffled pleats and a slit to the front hem. Finished in an all over flying phoenix print, this silk piece is a must have for the summer seasons.",
      "info": "98% polyester, 2% elastane",
      "image_id": "54_LOS2UO8",
      "image_thumbnail_id": "54_LOS2UO8_T",
      "brand": "KENZO",
      "price":"357.00",
      "colour_image_map": {
        "PINK": [
          "54_LOS2UO8",
          "55_LOS2UO8",
          "56_LOS2UO8",
          "57_LOS2UO8"
        ]
      }
    },
    {
      "product_id": "Q1J0J0B",
      "name": "Short Sleeve Dress",
      "long_description": "Redefine smart casual in this Calvin Klein Performance Short Sleeve Dress. Crafted in a comfortable and warm cotton-based blend this dress features short sleeves, a striking block design and Calvin Klein Performance branding.",
      "info": "98% polyester, 2% elastane",
      "image_id": "58_Q1J0J0B",
      "image_thumbnail_id": "58_Q1J0J0B_T",
      "brand": "Calvin Klein",
      "price":"75.00",
      "colour_image_map": {
        "BLACK": [
          "58_Q1J0J0B",
          "59_Q1J0J0B",
          "60_Q1J0J0B",
          "61_Q1J0J0B",
          "62_Q1J0J0B"
        ]
      }
    },
    {
      "product_id": "O70OI13",
      "name": "Polo Terry Haltr Drs Ld92",
      "long_description": " Invest in luxury with the Polo Ralph Lauren Bells Shirt Dress. This vibrant cover-up dress features a keyhole effect neckline and a rounded hemline, cut to sit high on the thigh. Boasting dramatic slide slits and a matching waist tie belt, this dress is finished with pinned-up sleeves.",
      "info": "98% polyester, 2% elastane",
      "image_id": "63_O70OI13",
      "image_thumbnail_id": "63_O70OI13_T",
      "brand": "Polo Ralph Lauren",
      "price":"90.00",
      "colour_image_map": {
        "BLACK": [
          "63_O70OI13",
          "64_O70OI13",
          "65_O70OI13",
          "66_O70OI13"
        ]
      }
    },
    {
      "product_id": "OKG74AR",
      "name": "Vian Dress",
      "long_description": "Vivienne Westwood Anglomania's Vian dress sticks true to the brands signature flair for draping. Made in Italy from a lightweight jersey, this style is crafted in a one shoulder design and boasts a midi-cut. Finished with gathered and draped elements to the body, this dress will flatter your figure.",
      "info": "Upper, lining and sole: leather",
      "image_id": "67_OKG74AR",
      "image_thumbnail_id": "67_OKG74AR_T",
      "brand": "VWA",
      "price":"275.00",
      "colour_image_map": {
        "RED": [
          "67_OKG74AR",
          "68_OKG74AR",
          "69_OKG74AR",
          "70_OKG74AR",
          "71_OKG74AR"
        ]
      }
    },
    {
      "product_id": "L1LH6S7",
      "name": "Polo Alyah Pleat Mxi Ld93",
      "long_description": "Polo Ralph Lauren's Vian dress sticks true to the brands signature flair for draping. Made in Italy from a lightweight jersey, this style is crafted in a one shoulder design and boasts a midi-cut. Finished with gathered and draped elements to the body, this dress will flatter your figure.",
      "info": "Upper, lining and sole: leather",
      "image_id": "72_L1LH6S7",
      "image_thumbnail_id": "72_L1LH6S7_T",
      "brand": "Polo Ralph Lauren",
      "price":"349.00",
      "colour_image_map": {
        "MULTI": [
          "72_L1LH6S7",
          "73_L1LH6S7"
        ]
      }
    },
    {
      "product_id": "Q8NFDIT",
      "name": "Dantia Dress",
      "long_description": "Refresh your collection with this Dantia dress from BOSS. Constructed in a midi length, this piece features a rounded neckline and sleeveless design. Boasting a concealed zip to the back, this dress features a slit to the front. This dress is not to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "74_Q8NFDIT",
      "image_thumbnail_id": "74_Q8NFDIT_T",
      "brand": "BOSS SMART CASUAL",
      "price":"299.00",
      "colour_image_map": {
        "BLUE": [
          "74_Q8NFDIT",
          "75_Q8NFDIT",
          "76_Q8NFDIT",
          "77_Q8NFDIT"
        ]
      }
    },
    {
      "product_id": "2V2H79O",
      "name": "Desplisa Dress",
      "long_description": "Update your casual dress collection with the Desplisa dress from BOSS. Designed in a sleeveless style with a scoop neckline and asymmetric layering, this dress features a pleated pattern. Finished with brush-stroke artwork and hand painted edges, this is not to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "78_2V2H79O",
      "image_thumbnail_id": "78_2V2H79O_T",
      "brand": "BOSS SMART CASUAL",
      "price":"525.00",
      "colour_image_map": {
        "WHITE": [
          "78_2V2H79O",
          "79_2V2H79O",
          "80_2V2H79O"
        ]
      }
    },
    {
      "product_id": "14R6OR8",
      "name": "Zofia Short Dress",
      "long_description": "Invest in this Agent Provocateur Zofia short dress. Crafted with an alluring twist and elegant long sleeves, this little dress features open cut-out panels to the shoulder and waist. Finished with two side slits and an asymmetric silhouette.",
      "info": "Upper, lining and sole: leather",
      "image_id": "81_14R6OR8",
      "image_thumbnail_id": "81_14R6OR8_T",
      "brand": "AGENT PROVOCATEUR",
      "price":"200.00",
      "colour_image_map": {
        "BLACK": [
          "81_14R6OR8",
          "82_14R6OR8",
          "83_14R6OR8",
          "84_14R6OR8",
          "85_14R6OR8"
        ]
      }
    } 
  ],    
    
  "WC_TOPS": [
    {
      "product_id": "FDJD03B",
      "name": "Logo Vest T Shirt",
      "long_description": "Refresh your staple wardrobe with the logo vest t shirt from Balmain. This classic sleeveless style is designed with a crew neckline, branded buttons to one shoulder and is finished with the brands signature logo in tonal wording to the chest.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_FDJD03B",
      "image_thumbnail_id": "1_FDJD03B_T",
      "brand": "BALMAIN",
      "price":"195.00",
      "colour_image_map": {
        "BLACK": [
          "1_FDJD03B",
          "2_FDJD03B",
          "3_FDJD03B",
          "4_FDJD03B"
        ],
        "PEACH": [
          "5_FDJD03B",
          "6_FDJD03B",
          "7_FDJD03B"
        ]
      }
    },
    {
      "product_id": "RTUS3HV",
      "name": "Chaos T Shirt",
      "long_description": "Upgrade your staple wardrobe with the chaos t shirt from Vivienne Westwood Anglomania. Cut in a classic crew neckline, this piece features with short sleeves and ribbed trims. Finished with the brands signature logo with tonal text to the front, this piece is not one to be missed. ",
      "info": "Upper, lining and sole: leather",
      "image_id": "8_RTUS3HV",
      "image_thumbnail_id": "8_RTUS3HV_T",
      "brand": "VIVIENNE WESTWOOD",
      "price":"95.00",
      "colour_image_map": {
        "WHITE": [
          "8_RTUS3HV",
          "9_RTUS3HV",
          "10_RTUS3HV"
        ]
      }
    },
    {
      "product_id": "9CN4SVB",
      "name": "Logo Crop T Shirt",
      "long_description": "Update your casual attire with this logo crop t shirt from DSquared2. This cropped style features short sleeves and a crew neckline, finished with the brands signature logo emblazoned across the chest. This t shirt is not to be missed and would make a welcome addition to your wardrobe.",
      "info": "Upper, lining and sole: leather",
      "image_id": "11_9CN4SVB",
      "image_thumbnail_id": "11_9CN4SVB_T",
      "brand": "DSQUARED2",
      "price":"180.00",
      "colour_image_map": {
        "BLACK": [
          "11_9CN4SVB",
          "12_9CN4SVB",
          "13_9CN4SVB"
        ],
        "WHITE": [
          "14_9CN4SVB",
          "15_9CN4SVB",
          "16_9CN4SVB"
        ]
      }
    },
    {
      "product_id": "A1N1OBZ",
      "name": "Medallion Print Vest",
      "long_description": "Refresh your off duty collection with the medallion print vest from Balmain. Constructed to a sleeveless style, this piece features a crew neckline and the brands iconic branded buttons to the shoulders. Finished a branded coin emblazoned to the chest, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "17_A1N1OBZ",
      "image_thumbnail_id": "17_A1N1OBZ_T",
      "brand": "BALMAIN",
      "price":"225.00",
      "colour_image_map": {
        "BLACK": [
          "17_A1N1OBZ",
          "18_A1N1OBZ",
          "19_A1N1OBZ"
        ]
      }
    },
    {
      "product_id": "6U4IJY8",
      "name": "Boyfriend Logo T Shirt",
      "long_description": "Revitalise your casual attire with this boyfriend logo t shirt from McQ Alexander McQueen. Crafted with short sleeves, this piece features a crew neckline and ribbed trims. Finished with the brands signature logo to the front, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "20_6U4IJY8",
      "image_thumbnail_id": "20_6U4IJY8_T",
      "brand": "MCQ",
      "price":"130.00",
      "colour_image_map": {
        "ACID PINK": [
          "20_6U4IJY8",
          "21_6U4IJY8",
          "22_6U4IJY8"
        ]
      }
    },
    {
      "product_id": "BH1SP2Z",
      "name": "Logo Tape Tank Top",
      "long_description": "Refresh your collection with this logo tape tank top from Emporio Armani. Crafted to a sleeveless style, this piece features a rounded neckline and racer back. Finished with the brands signature logo to the straps, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "23_BH1SP2Z",
      "image_thumbnail_id": "23_BH1SP2Z_T",
      "brand": "EMPORIO ARMANI",
      "price":"36.00",
      "colour_image_map": {
        "MARINE": [
          "23_BH1SP2Z",
          "24_BH1SP2Z",
          "25_BH1SP2Z",
          "26_BH1SP2Z"
        ]
      }
    },
    {
      "product_id": "KP34LCW",
      "name": "MMK Ruffle Ls Blouse Ld92",
      "long_description": "Refresh your collection with this logo tape tank top from Emporio Armani. Crafted to a sleeveless style, this piece features a rounded neckline and racer back. Finished with the brands signature logo to the straps, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "info": "Upper, lining and sole: leather",
      "image_id": "27_KP34LCW",
      "image_thumbnail_id": "27_KP34LCW_T",
      "brand": "Michael Kors",
      "price":"135.00",
      "colour_image_map": {
        "PINK": [
          "27_KP34LCW",
          "28_KP34LCW",
          "29_KP34LCW",
          "30_KP34LCW"
        ]
      }
    },
    {
      "product_id": "HH8V4OS",
      "name": "Bow Logo T Shirt",
      "long_description": "Refresh your daily essentials with the Boutique Moschino Bow Logo t shirt. Crafted with short sleeves, this piece features a crew neckline and oversized short sleeves. Finished with a chain ribbon design to the neck and the brands logo to the centre.",
      "info": "Upper, lining and sole: leather",
      "image_id": "31_HH8V4OS",
      "image_thumbnail_id": "31_HH8V4OS_T",
      "brand": "BOUTIQUE MOSCHINO",
      "price":"135.00",
      "colour_image_map": {
        "BLACK": [
          "31_HH8V4OS",
          "32_HH8V4OS",
          "33_HH8V4OS",
          "34_HH8V4OS",
          "35_HH8V4OS"
        ]
      }
    },
    {
      "product_id": "NZJJMRY",
      "name": "Laurel Floral Top",
      "long_description": "Update your collection with the LoveshackFancy Laurel floral top. Constructed with a rounded neckline and central button closure, this top boasts layered details and short sleeves. Featuring a floral print all over, this bohemian style top is a must have.",
      "info": "Upper, lining and sole: leather",
      "image_id": "36_NZJJMRY",
      "image_thumbnail_id": "36_NZJJMRY_T",
      "brand": "LOVESHACKFANCY",
      "price":"220.00",
      "colour_image_map": {
        "BLUE": [
          "36_NZJJMRY",
          "37_NZJJMRY",
          "38_NZJJMRY"
        ]
      }
    },
    {
      "product_id": "WGCIKII",
      "name": "Domino Floral Wrap Top",
      "long_description": "Refresh your collection with this domino floral wrap top from LoveShackFancy. Crafted with a deep v neckline, this piece features blouson sleeves and a tie to the waistband. Finished with an all over floral print, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "39_WGCIKII",
      "image_thumbnail_id": "39_WGCIKII_T",
      "brand": "LOVESHACKFANCY",
      "price":"290.00",
      "colour_image_map": {
        "PINK": [
          "39_WGCIKII",
          "40_WGCIKII",
          "41_WGCIKII"
        ]
      }
    }
  ],    
    
  "WC_TROUSERS": [
    {
      "product_id": "ZNNFWDD",
      "name": "Sports Leggings",
      "long_description": "Add to your weekend wardrobe with these Calvin Klein Performance Crafted from a moisture wicking fabric, these leggings feature a high-rise waistband for extra support and coverage. Boasting an optimised stretch and finished with the brands signature logo to the waistband and leg.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_ZNNFWDD",
      "image_thumbnail_id": "1_ZNNFWDD_T",
      "brand": "CALVIN KLEIN",
      "price":"33.00",
      "colour_image_map": {
        "BLACK": [
          "1_ZNNFWDD",
          "2_ZNNFWDD",
          "3_ZNNFWDD",
          "4_ZNNFWDD",
          "5_ZNNFWDD"
        ]
      }
    },
    {
      "product_id": "EUJGYRY",
      "name": "Logo Waistband Leggings",
      "long_description": "Add to your weekend wardrobe with these Emporio Armani logo waistband leggings. Crafted with the brands signature logo to the waistband and Eagle to the leg, this pair are a must have.",
      "info": "Upper, lining and sole: leather",
      "image_id": "6_EUJGYRY",
      "image_thumbnail_id": "6_EUJGYRY_T",
      "brand": "EMPORIO ARMANI",
      "price":"50.00",
      "colour_image_map": {
        "MARINE": [
          "6_EUJGYRY",
          "7_EUJGYRY",
          "8_EUJGYRY",
          "9_EUJGYRY",
          "10_EUJGYRY"
        ]
      }
    },
    {
      "product_id": "FJCGS4R",
      "name": "Floral Semi Sheer Leggings",
      "long_description": "These floral semi sheer leggings from Off White are the perfect contemporary addition to your wardrobe. Constructed with a branded elasticated waistband, these leggings are cut from a semi sheer fabric and boasts an all over floral print, making them a welcome addition to your wardrobe.",
      "info": "Upper, lining and sole: leather",
      "image_id": "11_FJCGS4R",
      "image_thumbnail_id": "11_FJCGS4R_T",
      "brand": "OFF WHITE",
      "price":"310.00",
      "colour_image_map": {
        "BLACK": [
          "11_FJCGS4R",
          "12_FJCGS4R",
          "13_FJCGS4R",
          "14_FJCGS4R"
        ]
      }
    },
    {
      "product_id": "MMJYL7T",
      "name": "Norali Stripe Trousers",
      "long_description": "Bring your wardrobe up-to-date with the By Malene Birger Norali Stripe trousers. Crafted with an elasticated waistband, this piece features an all over striped print.",
      "info": "Upper, lining and sole: leather",
      "image_id": "15_MMJYL7T",
      "image_thumbnail_id": "15_MMJYL7T_T",
      "brand": "BY MALENE BIRGER",
      "price":"145.00",
      "colour_image_map": {
        "BLACK STRIPE": [
          "15_MMJYL7T",
          "16_MMJYL7T",
          "17_MMJYL7T",
          "18_MMJYL7T"
        ]
      }
    },
    {
      "product_id": "G6GBE13",
      "name": "Ck Perf Side Lgo Lg Ld92",
      "long_description": "Bring your wardrobe up-to-date with the Calvin Klein Norali Stripe trousers. Crafted with an elasticated waistband, this piece features an all over striped print.",
      "info": "Upper, lining and sole: leather",
      "image_id": "19_G6GBE13",
      "image_thumbnail_id": "19_G6GBE13_T",
      "brand": "CALVIN KLEIN",
      "price":"50.00",
      "colour_image_map": {
        "BLUE": [
          "19_G6GBE13",
          "20_G6GBE13",
          "21_G6GBE13",
          "22_G6GBE13"
        ]
      }
    },
    {
      "product_id": "O14M0TL",
      "name": "Gg Wide Leg Trousers",
      "long_description": "Refine your look with Gucci's GG wide leg trousers. Crafted with four pockets, this piece features a concealed zip and button closure, wide leg fit and a tonal trim to the sides. Finished with the brands signature GG print, this piece would make a welcome addition to your wardrobe.",
      "info": "Upper, lining and sole: leather",
      "image_id": "23_O14M0TL",
      "image_thumbnail_id": "23_O14M0TL_T",
      "brand": "GUCCI",
      "price":"799.00",
      "colour_image_map": {
        "CASPIAN": [
          "23_O14M0TL",
          "24_O14M0TL",
          "25_O14M0TL",
          "26_O14M0TL"
        ]
      }
    },
    {
      "product_id": "49MR07F",
      "name": "Gg Trousers",
      "long_description": "Refine your look with Gucci's GG trousers. Inspired by the brand's Italian elegance, these classic trousers are designed in a straight fit with the famous GG logo waistband and partially concealed button fastenings. These sophisticated trousers would be a welcome addition to your wardrobe.",
      "info": "Upper, lining and sole: leather",
      "image_id": "27_49MR07F",
      "image_thumbnail_id": "27_49MR07F_T",
      "brand": "GUCCI",
      "price":"750.00",
      "colour_image_map": {
        "BLACK": [
          "27_49MR07F",
          "28_49MR07F",
          "29_49MR07F",
          "30_49MR07F"
        ]
      }
    },
    {
      "product_id": "9X8452W",
      "name": "Portofino Caddy Jogging Bottoms",
      "long_description": "Update your casual collection with these portofino caddy jogging bottoms from Dolce And Gabbana. Crafted with a stretch waistband and adjustable toggles, this pair features cuffed ankles, two zip pockets and striped branded taping to both legs. Finished with a floral print all over, this piece is not one to be missed.",
      "info": "Upper, lining and sole: leather",
      "image_id": "31_9X8452W",
      "image_thumbnail_id": "31_9X8452W_T",
      "brand": "DOLCE N GABBANA",
      "price":"775.00",
      "colour_image_map": {
        "MULTI": [
          "31_9X8452W",
          "32_9X8452W",
          "33_9X8452W",
          "34_9X8452W"
        ]
      }
    },
    {
      "product_id": "UF1RJT2",
      "name": "Legging Jeans",
      "long_description": "Invest in the True Religion Runway legging jeans. This skinny fit style is designed in a a super stretch denim for ultimate comfort and features tonal stitching, branded metal hardware and four pockets.",
      "info": "Upper, lining and sole: leather",
      "image_id": "35_UF1RJT2",
      "image_thumbnail_id": "35_UF1RJT2_T",
      "brand": "True Religion",
      "price":"104.00",
      "colour_image_map": {
        "BLUE": [
          "35_UF1RJT2",
          "36_UF1RJT2",
          "37_UF1RJT2",
          "38_UF1RJT2"
        ],
        "BLACK": [
          "39_UF1RJT2",
          "40_UF1RJT2",
          "41_UF1RJT2",
          "42_UF1RJT2"
        ]
      }
    },
    {
      "product_id": "123AS3Y",
      "name": "Cropped Slim Trousers",
      "long_description": "Refine your look with these cropped slim trousers from Victoria by Victoria Beckham. Crafted to a cropped style, this piece features a zip and button closure, belt loops and four pockets. Finished with a contrasting satin waist, this piece is not one to be missed. ",
      "info": "Upper, lining and sole: leather",
      "image_id": "43_123AS3Y",
      "image_thumbnail_id": "43_123AS3Y_T",
      "brand": "VICTORIA BECKHAM",
      "price":"277.00",
      "colour_image_map": {
        "GREEN": [
          "43_123AS3Y",
          "44_123AS3Y",
          "45_123AS3Y",
          "46_123AS3Y",
          "47_123AS3Y"
        ]
      }
    } 
  ],    
    
  "WS_BOOTS": [
    {
      "product_id": "2JU0UX4",
      "name": "Marmont Leather Ankle Boots",
      "long_description": "Upgrade your everyday footwear collection with the Marmont leather ankle boots from Gucci. Featuring fold over fringe detailing to the toe, this smooth leather style is cut to an ankle length with a low heel and a zip fastening to the side. Designed with a squared toe, this sophisticated style is finished with the brands signature interlocking G to the front.",
      "info": "Upper, lining and sole: leather",
      "image_id": "1_2JU0UX4",
      "image_thumbnail_id": "1_2JU0UX4_T",
      "brand": "GUCCI",
      "price":"799.00",
      "colour_image_map": {
        "BLACK": [
          "1_2JU0UX4",
          "2_2JU0UX4",
          "3_2JU0UX4",
          "4_2JU0UX4",
          "5_2JU0UX4"
        ]
      }
    },
    {
      "product_id": "2E1DQ3Y",
      "name": "Rockstud Heeled Ankle Boots",
      "long_description": "Step in style with the Rockstud Heeled Ankle boots from Valentino GARAVANI. Crafted in a smooth leather with a pointed toe, this pair feature rockstud detail to the sides and front. Finished with a stiletto heel and inside zip, this pair would make a welcome addition.",
      "info": "Upper, lining and sole: leather",
      "image_id": "6_2JU0UX4",
      "image_thumbnail_id": "6_2JU0UX4_T",
      "brand": "VALENTINO",
      "price":"780.00",
      "colour_image_map": {
        "BLACK": [
          "6_2JU0UX4",
          "7_2JU0UX4",
          "8_2JU0UX4",
          "9_2JU0UX4",
          "10_2JU0UX4"
        ]
      }
    },
    {
      "product_id": "3WND6I4",
      "name": "Czech Boots",
      "long_description": "Upgrade your everyday footwear collection with the Czech boots from Magda Butrym. Crafted in a smooth leather, these boots feature a unique cut to the knee, pointed toe and kitten heel. Finished with a detachable draped jewel design to the front, these are a must have.",
      "info": "Upper, lining and sole: leather",
      "image_id": "11_3WND6I4",
      "image_thumbnail_id": "11_3WND6I4_T",
      "brand": "MAGDA BUTRYM",
      "price":"1081.00",
      "colour_image_map": {
        "CREAM": [
          "11_3WND6I4",
          "12_3WND6I4",
          "13_3WND6I4",
          "14_3WND6I4",
          "15_3WND6I4"
        ]
      }
    },
    {
      "product_id": "7O13DZV",
      "name": "Susanna Short Boots",
      "long_description": "Upgrade your footwear collection with the Susanna Short Boots  from Chloe. Crafted with a trio of buckle straps across the front, this piece features an elongated pointed toe, a zip closure to the side and a low cuban heel. Finished with the brands iconic embellished floral pattern in metal studs, this statement piece would make a welcome addition to your collection.",
      "info": "Upper, lining and sole: leather",
      "image_id": "16_7O13DZV",
      "image_thumbnail_id": "16_7O13DZV_T",
      "brand": "CHLOE",
      "price":"680.00",
      "colour_image_map": {
        "BLACK/GOLD": [
          "16_7O13DZV",
          "17_7O13DZV",
          "18_7O13DZV",
          "19_7O13DZV",
          "20_7O13DZV"
        ]
      }
    },
    {
      "product_id": "Y929WCY",
      "name": "Chloe Rylee Croc Medium Boots",
      "long_description": "The Rylee medium croc boots from Chloe are the perfect piece to complete your footwear collection. Crafted using a crocodile print leather, this style features two straps adorned with metal buckles to the top, whilst the main shoe boasts cut out detailing. Sitting on a Western heel constructed from stacked leather and matte rubber, this lace up pair would make a welcome addition.",
      "info": "Upper, lining and sole: leather",
      "image_id": "21_Y929WCY",
      "image_thumbnail_id": "21_Y929WCY_T",
      "brand": "CHLOE",
      "price":"1095.00",
      "colour_image_map": {
        "SEPTSUN": [
          "21_Y929WCY",
          "22_Y929WCY",
          "23_Y929WCY",
          "24_Y929WCY",
          "25_Y929WCY"
        ]
      }
    }     
  ],
}
# print(json.dumps(product_data, indent=4))
