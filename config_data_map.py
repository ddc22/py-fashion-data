import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

cat_sizes = {
    "MENS_SHIRTS": ["XL", "M", "L", "S"],
    "MENS_SHOES": ["8", "9", "10", "11", "12"],
    "WOMENS_BAGS": ["S"],
    "WOMENS_DRESSES": ["8", "10", "12", "14", "16", "18"]
}

product_data = {
    "MENS_SHIRTS": [
        {
            "product_id": 'DF517XM',
            "name": 'Button Down Collar Red',
            "long_description": 'Check Button Down Collar Western Shirt',
            "info": 'Machine washable. Cotton.',
            "image_id": 'DF517XM',
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
            "brand": 'NL117CN',
            "color_image_map": {
                "CREME": ["NL117CN", "NL117CN-1"]
            },

        }, {
            "product_id": 'NL117CN',
            "name": 'NL117CN',
            "long_description": 'NL117CN',
            "info": 'NL117CN',
            "image_id": 'NL117CN',
            "brand": 'NL117CN',
            "color_image_map": {
                "CREME": ["NL616HN", "NL616HN-1"]
            },
        }
    ],
}

print(json.dumps(product_data, indent=4))
