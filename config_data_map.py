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
    "WOMENS_DRESSES": ["8", "10", "12", "14", "16", "18"],
    "MC_JACKETS_COATS": ["XL", "M", "L", "S"],
    "MC_SHIRTS": ["XL", "M", "L", "S"]
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
            "price": "495.00",
            "color_image_map": {
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
            "price": "295.00",
            "color_image_map": {
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
            "price": "339.00",
            "color_image_map": {
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
            "price": "659.00",
            "color_image_map": {
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
            "price": "875.00",
            "color_image_map": {
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
            "price": "295.00",
            "color_image_map": {
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
            "price": "1160.00",
            "color_image_map": {
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
            "price": "350.00",
            "color_image_map": {
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
            "price": "419.00",
            "color_image_map": {
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
            "price": "155.00",
            "color_image_map": {
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
            "product_id": "0J70Q0P",
            "name": "George Shirt",
            "long_description": "This GUCCI Stripe Long Sleeve Shirt would be a welcome addition to any capsule wardrobe. This oversized piece features a pointed collar and long button cuffed sleeves. Boasting a central button down closure and chest pocket. Finished with a stripe pattern all over and the brands logo printed to the hemline.",
            "info": "Machine washable. Cotton.",
            "image_id": "1_ECY3U8K",
            "image_thumbnail_id": "1_ECY3U8K_T",
            "brand": "GUCCI",
            "price": "490.00",
            "color_image_map": {
                "BLUE/WHITE": [
                    "1_ECY3U8K",
                    "2_ECY3U8K"
                ]
            }
        }
    ],
    "MENS_SHIRTS": [
        {
            "product_id": 'DF517XM',
            "name": 'Button Down Collar Red',
            "long_description": 'Check Button Down Collar Western Shirt',
            "info": 'Machine washable. Cotton.',
            "image_id": 'DF517XM',
            "image_thumbnail_id": 'DF517XM-T',
            "price": '52.52',
            "brand": 'INTERNAL',
            "color_image_map": {
                "RED": ["DF517XM", "DF517XM-1", "DF517XM-2", "DF517XM-3", "DF517XM-4"],
                "BLUE": ["DF517XM-3", "DF517XM-4"]
            }
        }, {
            "product_id": 'ID816BN',
            "name": 'Ben Sherman Short Oxford',
            "long_description": 'From Ben Sherman. As British as bangers and mash, this timeless Oxford shirt is as classic now as it was back in the swinging ?60s.',
            "info": 'Please be aware, Ben Sherman shirts are made to a more tailored fit, therefore please look at the chest size in inches before placing your order. You may need to order a size up compared to your usual size. Machine washable.78% Cotton, 22% Polyester.',
            "image_id": 'DF517XM',
            "image_thumbnail_id": 'DF517XM-T',
            "price": '52.52',
            "brand": 'BEN_SHERMAN',
            "color_image_map": {
                "BLUE": ["ID816BN", "ID816BN-1"],
                "WHITE": ["ID816BN-2"],
                "BLACK": ["ID816BN-3"]
            },
        }
    ],
    "WOMENS_DRESSES": [
        {
            "product_id": 'MB229XM',
            "name": 'MB229XM',
            "long_description": 'MB229XM',
            "info": 'MB229XM',
            "image_id": 'MB229XM',
            "image_thumbnail_id": 'MB229XM-T',
            "price": '52.52',
            "brand": 'MB229XM',
            "color_image_map": {
                "RED": ["MB229XM", "MB229XM-1"],
                "BLUE": ["MB229XM-1", "MB229XM-3"],
                "BLACK": ["MB229XM-4"]
            },
        }, {
            "product_id": 'MB709SN',
            "name": 'MB709SN',
            "long_description": 'MB709SN',
            "info": 'MB709SN',
            "image_id": 'MB709SN',
            "image_thumbnail_id": 'MB709SN-T',
            "price": '52.52',
            "brand": 'MB709SN',
            "color_image_map": {
                "BLACK": ["MB709SN", "MB709SN-1", "MB709SN-2", "MB709SN-3"]
            }
        }
    ],
    "MENS_SHOES": [
        {
            "product_id": 'KD092JS',
            "name": 'KD092JS',
            "long_description": 'KD092JS',
            "info": 'KD092JS',
            "image_id": 'KD092JS',
            "price": '52.52',
            "image_thumbnail_id": 'KD092JS-T',
            "brand": 'KD092JS',
            "color_image_map": {
                "BLACK": ["KD092JS", "KD092JS-1"]
            }

        }, {
            "product_id": 'VV639JS',
            "name": 'VV639JS',
            "long_description": 'VV639JS',
            "info": 'VV639JS',
            "image_id": 'VV639JS',
            "image_thumbnail_id": 'VV639JS-T',
            "price": '52.52',
            "brand": 'VV639JS',
            "color_image_map": {
                "BLACK": ["VV639JS", "VV639JS-1", "VV639JS-2", "VV639JS-3"]
            },
        }
    ],
    "WOMENS_BAGS": [
        {
            "product_id": 'NL117CN',
            "name": 'NL117CN',
            "long_description": 'NL117CN',
            "info": 'NL117CN',
            "image_id": 'NL117CN',
            "image_thumbnail_id": 'NL117CN-T',
            "price": '52.52',
            "brand": 'NL117CN',
            "color_image_map": {
                "CREME": ["NL117CN", "NL117CN-1"]
            },

        }, {
            "product_id": 'NL616HN',
            "name": 'NL616HN',
            "long_description": 'NL616HN',
            "info": 'NL616HN',
            "image_id": 'NL616HN',
            "image_thumbnail_id": 'NL616HN-T',
            "price": '52.52',
            "brand": 'NL616HN',
            "color_image_map": {
                "CREME": ["NL616HN", "NL616HN-1"]
            },
        }
    ],
}

# print(json.dumps(product_data, indent=4))
