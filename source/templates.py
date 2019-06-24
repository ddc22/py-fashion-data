from utils import util
SafeDict = util.SafeDict

sku_product = """
    <retail:skuProduct xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:ns12="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns4="http://www.enactor.com/crm" xmlns:ns6="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns8="http://www.enactor.com/addressLookup/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <retail:productId>{sku_product_id}</retail:productId>
        <retail:type>skuProduct</retail:type>
        <retail:productDescription>
            <core:string variant="" language="en" country="GB">{name}</core:string>
        </retail:productDescription>
        <retail:productLongDescription>
            <core:string variant="" language="en" country="GB">{long_description}</core:string>
        </retail:productLongDescription>
        <retail:productLongDescriptionURL></retail:productLongDescriptionURL>
        <retail:productInfo>{info}</retail:productInfo>
        <retail:fasciaId></retail:fasciaId>
        <retail:imageURL>image://PRODUCT/{image_id}.jpg</retail:imageURL>
        <retail:imageFilenameId type="jpg" category="PRODUCT">{image_id}</retail:imageFilenameId>
        <retail:productInformationURL></retail:productInformationURL>
        <retail:posDetails>
            <retail:operatorMessage/>
            <retail:customerMessage/>
            <retail:cashierAgeRestrict>0</retail:cashierAgeRestrict>
            <retail:numberCopyReceipts>0</retail:numberCopyReceipts>
            <retail:maxDiscount>0.0</retail:maxDiscount>
            <retail:maxEmployeeDiscount>0.0</retail:maxEmployeeDiscount>
            <retail:returnsTimeLimit>0</retail:returnsTimeLimit>
            <retail:maxQtyPerTransaction>0.0</retail:maxQtyPerTransaction>
            <retail:customerAgeRestriction>0</retail:customerAgeRestriction>
            <retail:receiptMessage/>
            <retail:productOptionSetDetails>
                <retail:isTemplate>false</retail:isTemplate>
            </retail:productOptionSetDetails>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:posDetails>
        <retail:isTemplate>false</retail:isTemplate>
        <retail:status>LIVE</retail:status>
        <retail:taxGroupId>A</retail:taxGroupId>
        <retail:exportDetails>
            <retail:notForExport>false</retail:notForExport>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:exportDetails>
        <retail:mmGroupId variantGroupHierarchyId="All" variantGroupId="All" variantGroupTypeId="region" groupHierarchyId="FASHION" groupTypeId="mmGroup">{category}</retail:mmGroupId>
        <retail:brandId variantGroupHierarchyId="All" variantGroupId="All" variantGroupTypeId="region" groupHierarchyId="FASHION" groupTypeId="brand">{brand}</retail:brandId>
        <retail:rangeId/>
        <retail:inventoryDetails>
            <retail:allowForLoan>false</retail:allowForLoan>
            <retail:allowCustomerOrder>true</retail:allowCustomerOrder>
            <retail:allowPurchaseOrder>true</retail:allowPurchaseOrder>
            <retail:customerOrderOnly>false</retail:customerOrderOnly>
            <retail:directToStoreDelivery>false</retail:directToStoreDelivery>
            <retail:warehouseUnitOfMeasureId>1</retail:warehouseUnitOfMeasureId>
            <retail:isStocked>true</retail:isStocked>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:inventoryDetails>
        <retail:productDimensions>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:productDimensions>
        <retail:warrantyDetails>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:warrantyDetails>
        <retail:measureSystemId>CASE_PACK</retail:measureSystemId>
        <retail:salesUnitOfMeasureId>1</retail:salesUnitOfMeasureId>
        <retail:inventoryUnitOfMeasureId>1</retail:inventoryUnitOfMeasureId>
        <retail:seasonId>ALL</retail:seasonId>
        <retail:standardCostPrice>0.0</retail:standardCostPrice>
        <retail:standardMargin>0.0</retail:standardMargin>
        <retail:colourId colourRangeId="{category}">{color}</retail:colourId>
        <retail:sizeId sizeRangeId="{category}">{size}</retail:sizeId>
        <retail:styleId>{product_id}</retail:styleId>
    </retail:skuProduct>
"""


def sku_product_sample():
    sample = sku_product.format_map(SafeDict(
        sku_product_id='DF517XM-1-2',
        name='Button Down Collar Red',
        long_description='Check Button Down Collar Western Shirt',
        info='Machine washable. Cotton.',
        image_id='DF517XM',
        category='MENS_SHIRTS',
        brand='INTERNAL',
        color='RED',
        size='XL',
        product_id='DF517XM'
    ))
    print("###### sku_product #######")
    print(sample)
# sku_product_sample()


product = """
    <retail:styleColourSizeProduct xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns10="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns12="http://www.enactor.com/addressLookup/service" xmlns:ns13="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns4="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:ns5="http://www.enactor.com/crm" xmlns:ns9="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <retail:productId>{product_id}</retail:productId>
        <retail:type>styleColourSizeProduct</retail:type>
        <retail:productDescription>
            <core:string variant="" language="en" country="GB">{name}</core:string>
        </retail:productDescription>
        <retail:productLongDescription>
            <core:string variant="" language="en" country="GB">{long_description}</core:string>
        </retail:productLongDescription>
        <retail:productLongDescriptionURL></retail:productLongDescriptionURL>

        <retail:productInfo>{info}</retail:productInfo>
        <retail:fasciaId></retail:fasciaId>
        <retail:imageURL>image://PRODUCT/{image_id}.jpg</retail:imageURL>
        <retail:imageFilenameId type="jpg" category="PRODUCT">{image_id}</retail:imageFilenameId>

        <retail:productInformationURL></retail:productInformationURL>
        <retail:posDetails>
            <retail:productOptionSetDetails>
                <retail:isTemplate>false</retail:isTemplate>
            </retail:productOptionSetDetails>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:posDetails>
        <retail:isTemplate>false</retail:isTemplate>
        <retail:status>LIVE</retail:status>
        <retail:taxGroupId>A</retail:taxGroupId>
        <retail:exportDetails>
            <retail:notForExport>false</retail:notForExport>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:exportDetails>
        <retail:mmGroupId variantGroupHierarchyId="All" variantGroupId="All" variantGroupTypeId="region" groupHierarchyId="FASHION" groupTypeId="mmGroup">{category}</retail:mmGroupId>
        <retail:brandId variantGroupHierarchyId="All" variantGroupId="All" variantGroupTypeId="region" groupHierarchyId="FASHION" groupTypeId="brand">{brand}</retail:brandId>
        <retail:rangeId></retail:rangeId>
        <retail:inventoryDetails>
            <retail:allowForLoan>false</retail:allowForLoan>
            <retail:allowCustomerOrder>true</retail:allowCustomerOrder>
            <retail:allowPurchaseOrder>true</retail:allowPurchaseOrder>
            <retail:customerOrderOnly>false</retail:customerOrderOnly>
            <retail:directToStoreDelivery>false</retail:directToStoreDelivery>
            <retail:isStocked>true</retail:isStocked>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:inventoryDetails>
        <retail:productDimensions>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:productDimensions>
        <retail:warrantyDetails>
            <retail:isTemplate>false</retail:isTemplate>
        </retail:warrantyDetails>
        <retail:seasonId>ALL</retail:seasonId>
        <retail:standardCostPrice>0.0</retail:standardCostPrice>
        <retail:standardMargin>0.0</retail:standardMargin>
        <retail:sizeRangeId>{category}</retail:sizeRangeId>
        <retail:colourRangeId>{category}</retail:colourRangeId>
    </retail:styleColourSizeProduct>
"""


def sample_product():
    sample = product.format_map(SafeDict(
        product_id='DF517XM',
        name='Button Down Collar Red',
        long_description='Check Button Down Collar Western Shirt',
        info='Machine washable. Cotton.',
        image_id='DF517XM',
        category='MENS_SHIRTS',
        brand='INTERNAL',
    ))
    print("###### stylecolorsize_product #######")
    print(sample)
# sample_product()


product_media = """ 
    <retail:productMedia xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns3="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:ns6="http://www.enactor.com/crm" xmlns:ns8="http://www.enactor.com/addressLookup/service" xmlns:ns9="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <retail:productMediaId>{media_id}</retail:productMediaId>
        <retail:productId>{product_id}</retail:productId>
        <retail:mediaType>IMAGE</retail:mediaType>
        <retail:mediaSubtype>{sub_type}</retail:mediaSubtype>
        <retail:name>{media_id}</retail:name>
        <retail:imageKey type="jpg" category="PRODUCT">{image_id}</retail:imageKey>
    </retail:productMedia>
"""


def sample_product_media():
    sample = product_media.format_map(SafeDict(
        media_id='DF517XM',
        product_id='DF517XM',
        image_id='DF517XM'
    ))
    print("###### stylecolorsize_product #######")
    print(sample)
# sample_product_media()


supplier_product = """ 
    <retail:supplierProduct xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns12="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns4="http://www.enactor.com/crm" xmlns:ns6="http://www.enactor.com/addressLookup/service" xmlns:ns7="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <retail:supplierProductId>{supplier_product_id}</retail:supplierProductId>    
        <retail:supplierId>{supplier_id}</retail:supplierId>
        <retail:productId>{product_id}</retail:productId>
        <retail:costUnitOfMeasureId>1</retail:costUnitOfMeasureId>
        <retail:description>Apex Supplier</retail:description>
        <retail:orderUnitOfMeasureId>1</retail:orderUnitOfMeasureId>
    </retail:supplierProduct>
"""


def sample_supplier_product():
    sample = supplier_product.format_map(SafeDict(
        supplier_product_id='0001ID816BN-1',
        product_id='ID816BN',
        image_id='ID816BN-1'
    ))
    print("###### supplier_product #######")
    print(sample)


# sample_supplier_product()


supplier_product_cost = """ 
    <retail:supplierProductCost xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns12="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns4="http://www.enactor.com/crm" xmlns:ns6="http://www.enactor.com/addressLookup/service" xmlns:ns7="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <retail:cost>{cost}</retail:cost>
        <retail:currencyId>{currency_id}</retail:currencyId>
        <retail:productId>{product_id}</retail:productId>
        <retail:supplierId>{supplier_id}</retail:supplierId>
        <retail:supplierProductId>{supplier_product_id}</retail:supplierProductId>
    </retail:supplierProductCost>
"""


def sample_supplier_product_cost():
    sample = supplier_product_cost.format_map(SafeDict(
        cost='400.00',
        product_id='ID816BN',
        supplier_product_id='ID816BN-SP1'
    ))
    print("###### supplier_product #######")
    print(sample)
# sample_supplier_product_cost()


product_price = """
<retail:productPrice xmlns:core="http://www.enactor.com/core" xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" xmlns:ns11="http://www.enactor.com/addressLookup/service" xmlns:ns12="http://www.enactor.com/crm/customerLoyalty/service" xmlns:ns13="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" xmlns:ns5="http://www.enactor.com/crm" xmlns:ns6="http://www.enactor.com/retail/restaurantTableStatus/service" xmlns:ns9="http://www.enactor.com/retail/storedRetailTransaction/service" xmlns:retail="http://www.enactor.com/retail" xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" xmlns:tools="http://www.enactor.com/tools" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <retail:productId>{product_id}</retail:productId>
    <retail:locationId></retail:locationId>
    <retail:priceGroupId variantGroupHierarchyId="All" variantGroupId="All" variantGroupTypeId="region" groupHierarchyId="ALL" groupTypeId="priceGroup">UK</retail:priceGroupId>
    <retail:currencyId>{currency_id}</retail:currencyId>
    <retail:priceType>{price_type}</retail:priceType>
    <retail:price>{price}</retail:price>
    <retail:pricingMethod></retail:pricingMethod>
    <retail:equivalentMeasureSystemId></retail:equivalentMeasureSystemId>
    <retail:equivalentUnitOfMeasureId></retail:equivalentUnitOfMeasureId>
    <retail:equivalentPrice>0</retail:equivalentPrice>
</retail:productPrice>
"""


def sample_product_price():
    sample = product_price.format_map(SafeDict(
        price='400.00',
        product_id='ID816BN',
        currency_id='GBP',
        price_type='R'
    ))
    print("###### supplier_product #######")
    print(sample)


# sample_product_price()


group = """
<retail:productGroup xmlns:core="http://www.enactor.com/core" 
    xmlns:hta="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/api/200803" 
    xmlns:htd="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/200803" 
    xmlns:htt="http://docs.oasis-open.org/ns/bpel4people/ws-humantask/types/200803" 
    xmlns:ns11="http://www.enactor.com/retail/storedRetailTransaction/service" 
    xmlns:ns13="http://www.enactor.com/crm/customerLoyalty/service" 
    xmlns:ns4="http://www.enactor.com/crm" 
    xmlns:ns7="http://www.enactor.com/retail/storedRestaurantSaleTransaction/service" 
    xmlns:ns8="http://www.enactor.com/addressLookup/service" 
    xmlns:ns9="http://www.enactor.com/retail/restaurantTableStatus/service" 
    xmlns:retail="http://www.enactor.com/retail" 
    xmlns:sref="http://docs.oasis-open.org/wsbpel/2.0/serviceref" 
    xmlns:tools="http://www.enactor.com/tools" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <retail:groupId>{group_id}</retail:groupId>
    <retail:groupTypeId>{group_type_id}</retail:groupTypeId>
    <retail:groupHierarchyId>{group_hierarchy_id}</retail:groupHierarchyId>
    <retail:level>{level}</retail:level>
    <retail:level10GroupId>{level_10}</retail:level10GroupId>
    <retail:level1GroupId>{level_1}</retail:level1GroupId>
    <retail:level2GroupId>{level_2}</retail:level2GroupId>
    <retail:level3GroupId>{level_3}</retail:level3GroupId>
    <retail:level4GroupId>{level_4}</retail:level4GroupId>
    <retail:level5GroupId>{level_5}</retail:level5GroupId>
    <retail:level6GroupId>{level_6}</retail:level6GroupId>
    <retail:level7GroupId>{level_7}</retail:level7GroupId>
    <retail:level8GroupId>{level_8}</retail:level8GroupId>
    <retail:level9GroupId>{level_9}</retail:level9GroupId>
    <retail:name>{name}</retail:name>
    <retail:variantGroupId>All</retail:variantGroupId>
    <retail:variantGroupTypeId>region</retail:variantGroupTypeId>
    <retail:variantGroupHierarchyId>All</retail:variantGroupHierarchyId>
    <retail:variantLevel>1</retail:variantLevel>
    <retail:allowPriceEntry>false</retail:allowPriceEntry>
    <retail:concession>false</retail:concession>
    <retail:forceMessageAcknowledgement>false</retail:forceMessageAcknowledgement>
    <retail:operatorMessage/>
    <retail:quantityEntry>false</retail:quantityEntry>
    <retail:receiptMessage/>
    <retail:exportWarningMessage></retail:exportWarningMessage>
    <retail:fasciaId groupTypeId="fascia"></retail:fasciaId>
</retail:productGroup>
"""


def sample_group():
    sample = product_group.format_map(SafeDict(
        group_id='MC_JACKETS_COATS',
        level_1='FASHION',
        level_2='WOMENS',
        level_3='M_CLOTHING',
        level_4='MC_JACKETS_COATS',
        level_5='',
        level_6='',
        level_7='',
        level_8='',
        level_9='',
        level_10='',
        group_type_id='productGroup',
        group_hierarchy_id='FASHION',
        name='Mens Clothing Jackets and Coats',
        level=4
    ))
    print("###### supplier_product #######")
    print(sample)


# sample_product_group()