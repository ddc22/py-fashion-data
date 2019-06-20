not_working = {
    "productId": "ZIFTSBH-41",
    "colourKey.colourId": "MULTI",
    "mmGroupName": "MC_JACKETS_COATS",
    "compoundProductStyleColourSize": "ZIFTSBH-41 Bandana Tracksuit J LIVE ZIFTSBH   ",
    "mmGroupParent": [" FASHION;FASHION FASHION;MENS FASHION;CLOTHING FASHION;MC_JACKETS_COATS "],
    "brandKey.groupId": "PALM ANGELS",
    "mmGroupKey.groupId": "MC_JACKETS_COATS",
    "mmGroupKey.groupHierarchyId": "FASHION",
    "type": "skuProduct",
    "compound": " ZIFTSBH-41 Bandana Tracksuit J",
    "brandKey.groupHierarchyId": "FASHION",
    "sizeKey.sizeRangeId": "MC_JACKETS_COATS",
    "styleId": "ZIFTSBH",
    "price": 0,
    "imageURL": "image://PRODUCT/11_ZIFTSBH.jpg",
    "lastIndexed": "2019-06-20T09:52:41Z",
    "colourKey.colourRangeId": "MC_JACKETS_COATS",
    "sizeKey.sizeId": "S",
    "productDescription": "Bandana Tracksuit J",
    "status": "LIVE",
    "mmGroupParentKey": ["groupTypeId=mmGroup;groupId=FASHION;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                         "groupTypeId=mmGroup;groupId=MENS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                         "groupTypeId=mmGroup;groupId=CLOTHING;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                         "groupTypeId=mmGroup;groupId=MC_JACKETS_COATS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;"],
    "id": "2e74796e-2537-4007-8c6d-8ca40ef625d9",
    "currentVersion": 0,
    "_version_": 1636852680908341248
}

working = {
    "productId": "DF517XM",
    "lowestCurrentOrderablePrice": 0,
    "productGroupKey": ["groupTypeId=productGroup;groupId=MENS_SHIRTS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;"],
    "mmGroupName": "Mens Shirts",
    "compoundProductStyleColourSize": "DF517XM Button Down Collar LIVE    ",
    "mmGroupParent": [" FASHION;FASHION FASHION;MENS FASHION;MENS_SHIRTS "],
    "brandKey.groupId": "INTERNAL",
    "productGroupName": ["Mens Shirts"],
    "mmGroupKey.groupId": "MENS_SHIRTS",
    "highestCurrentPrice": 0,
    "mmGroupKey.groupHierarchyId": "FASHION",
    "type": "styleColourSizeProduct",
    "compound": " DF517XM Button Down Collar",
    "brandKey.groupHierarchyId": "FASHION",
    "lowestCurrentPrice": 0,
    "productGroupParentKey": ["groupTypeId=productGroup;groupId=FASHION;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                              "groupTypeId=productGroup;groupId=MENS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                              "groupTypeId=productGroup;groupId=MENS_SHIRTS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;"],
    "price": 0,
    "highestCurrentOrderablePrice": 0,
    "imageURL": "image://PRODUCT/DF517XM.jpg",
    "lastIndexed": "2019-06-20T09:52:43Z",
    "productDescription": "Button Down Collar",
    "status": "LIVE",
    "mmGroupParentKey": ["groupTypeId=mmGroup;groupId=FASHION;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                         "groupTypeId=mmGroup;groupId=MENS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;",
                         "groupTypeId=mmGroup;groupId=MENS_SHIRTS;groupHierarchyId=FASHION;variantGroupTypeId=region;variantGroupId=All;variantGroupHierarchyId=All;"],
    "id": "fe5e9f4d-3c56-4d81-a25d-84940fc90673",
    "currentVersion": 0,
    "brand_option_set.brand_option_path_str": "Brand_INTERNAL",
    "stars_option_set.stars_option_path_int": 3,
    "_version_": 1636852682560897024
}

for key, value in working.items():
    if key not in not_working:
        print("not working missing: ", key)
for key, value in not_working.items():
    if key not in working:
        print("working missing: ", key)
