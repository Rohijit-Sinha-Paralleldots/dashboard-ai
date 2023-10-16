from .text_class_base import BaseTextClass


class MondelezMTIndiaPromptText(BaseTextClass):
    table_schema: str = "\n\
CREATE TABLE `mondelez_mt_asset_dump` (\n\
`id` int(11) NOT NULL AUTO_INCREMENT,\n\
`date` date DEFAULT NULL,\n\
`user_id` varchar(255) DEFAULT NULL,\n\
`username` varchar(255) DEFAULT NULL,\n\
`outlet_id` varchar(255) DEFAULT NULL,\n\
`outlet_name` varchar(255) DEFAULT NULL,\n\
`format_value` varchar(255) DEFAULT NULL,\n\
`category` varchar(255) DEFAULT NULL,\n\
`visibility_element` varchar(255) DEFAULT NULL,\n\
`competition` varchar(255) DEFAULT NULL,\n\
`sku_name` varchar(255) DEFAULT NULL,\n\
`facings` int(11) DEFAULT NULL,\n\
`msl_sku` int(11) DEFAULT NULL,\n\
`total_msl_applicable` int(11) DEFAULT NULL,\n\
`Is MSL Sufficient` int(11) DEFAULT NULL,\n\
`Category Level total Mdlz facings` float DEFAULT NULL,\n\
`Category Level total facings` float DEFAULT NULL,\n\
`mdlz skus best selling shelves` int(11) DEFAULT NULL,\n\
`total skus best selling shelves` int(11) DEFAULT NULL,\n\
`charging` int(11) DEFAULT NULL,\n\
`mdlz_facings` int(11) DEFAULT NULL,\n\
`total_facings` int(11) DEFAULT NULL,\n\
`Assetwise_Mdlz_Facings` int(11) DEFAULT NULL,\n\
`Asset Has atleast 5 Mdlz Facings` int(11) DEFAULT NULL,\n\
`Total Checkouts` int(11) DEFAULT NULL,\n\
`Outlet Mdlz Facings` int(11) DEFAULT NULL,\n\
`Outlet Total Facings` int(11) DEFAULT NULL,\n\
`Outlet_Asset_Gold_Compliance` int(11) DEFAULT NULL,\n\
`created_at` datetime DEFAULT CURRENT_TIMESTAMP,\n\
`modified_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,\n\
`shop_type` varchar(30) DEFAULT NULL,\n\
`total_msl_sufficiency_applicable` int(10) DEFAULT NULL,\n\
`Category MSL Sufficient` int(10) DEFAULT NULL,\n\
`Is MSL OSA present` int(10) DEFAULT NULL,\n\
`Region` varchar(30) DEFAULT NULL,\n\
`secondary_asset_presence` tinyint(1) DEFAULT NULL,\n\
`hz_Element_presence` tinyint(1) DEFAULT NULL,\n\
`Outlet_Hotzone_Display_Score_Num` int(11) DEFAULT NULL,\n\
`Outlet_Hotzone_Display_Score_Den` int(11) DEFAULT NULL,\n\
`Outlet Checkout with min 5 mdlz facings` int(11) DEFAULT NULL,\n\
`Category_MSL_OSA_Compliance` decimal(5,2) DEFAULT NULL,\n\
`Category_MSL_OSA_Score` decimal(5,2) DEFAULT NULL,\n\
`Category_SOS_Percentage` decimal(5,2) DEFAULT NULL,\n\
`Category_SOS_Score` decimal(5,2) DEFAULT NULL,\n\
`asset_sos_percentage` decimal(5,2) DEFAULT NULL,\n\
`asset_purity` varchar(20) DEFAULT NULL,\n\
`asset_mscore` decimal(5,2) DEFAULT NULL,\n\
`outlet_mscore` decimal(5,2) DEFAULT NULL,\n\
`Gold_SKU` decimal(5,2) DEFAULT NULL,\n\
`Asset_SoS` decimal(5,2) DEFAULT NULL,\n\
`Asset_Gold_compliance_score` decimal(5,2) DEFAULT NULL,\n\
`Hz_Asset_display_score` decimal(5,2) DEFAULT NULL,\n\
`Outlet_Hotzone_Display_Score` decimal(5,2) DEFAULT NULL,\n\
`Outlet_Hotzone_Coverage` decimal(5,2) DEFAULT NULL,\n\
`Outlet_Hotzone_Coverage_Score` decimal(5,2) DEFAULT NULL,\n\
`Outlet_Hotzone_Gold_Compliance_Score` decimal(5,2) DEFAULT NULL,\n\
`SE` varchar(30) DEFAULT NULL,\n\
`MDM` varchar(30) DEFAULT NULL,\n\
`BSM` varchar(30) DEFAULT NULL,\n\
`Account` varchar(30) DEFAULT NULL,\n\
`State` varchar(30) DEFAULT NULL,\n\
`City` varchar(30) DEFAULT NULL,\n\
`KAM` varchar(80) DEFAULT NULL,\n\
`GrKAM` varchar(80) DEFAULT NULL,\n\
`KAM_1` varchar(80) DEFAULT NULL,\n\
PRIMARY KEY (`id`)\n\
) ENGINE=InnoDB AUTO_INCREMENT=40230811 DEFAULT CHARSET=latin1\n\
\n\
CREATE TABLE `mondelez_mt_gallery_dump` (\n\
`id` int(11) NOT NULL AUTO_INCREMENT,\n\
`date` date DEFAULT NULL,\n\
`user_id` varchar(255) DEFAULT NULL,\n\
`username` varchar(255) DEFAULT NULL,\n\
`Format` varchar(255) DEFAULT NULL,\n\
`Account` varchar(255) DEFAULT NULL,\n\
`State` varchar(255) DEFAULT NULL,\n\
`City` varchar(255) DEFAULT NULL,\n\
`SE` varchar(255) DEFAULT NULL,\n\
`MDM` varchar(255) DEFAULT NULL,\n\
`BSM` varchar(255) DEFAULT NULL,\n\
`outlet_id` varchar(255) DEFAULT NULL,\n\
`outlet_name` varchar(255) DEFAULT NULL,\n\
`category_name` varchar(255) DEFAULT NULL,\n\
`shelf_type` varchar(255) DEFAULT NULL,\n\
`image_id` int(11) DEFAULT NULL,\n\
`image_link` varchar(255) DEFAULT NULL,\n\
`thumbnail_link` varchar(255) DEFAULT NULL,\n\
`invalid_reason` varchar(255) DEFAULT NULL,\n\
`created_at` datetime DEFAULT CURRENT_TIMESTAMP,\n\
`modified_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,\n\
`image_type` varchar(255) DEFAULT NULL,\n\
`Region` varchar(30) DEFAULT NULL,\n\
`shop_type` varchar(30) DEFAULT NULL,\n\
`validity_status` varchar(30) DEFAULT NULL,\n\
`mdlz_facings` int(5) DEFAULT NULL,\n\
`competitor_facings` int(5) DEFAULT NULL,\n\
`total_facings` int(5) DEFAULT NULL,\n\
`is_stitched` tinyint(1) DEFAULT NULL,\n\
`KAM` varchar(80) DEFAULT NULL,\n\
`GrKAM` varchar(80) DEFAULT NULL,\n\
`KAM_1` varchar(80) DEFAULT NULL,\n\
PRIMARY KEY (`id`)\n\
) ENGINE=InnoDB AUTO_INCREMENT=5713347 DEFAULT CHARSET=latin1\n\
\n\
CREATE TABLE `mondelez_mt_outlet_dump` (\n\
`id` int(11) NOT NULL AUTO_INCREMENT,\n\
`date` date DEFAULT NULL,\n\
`user_id` varchar(100) DEFAULT NULL,\n\
`username` varchar(100) DEFAULT NULL,\n\
`scheduled_stores` int(11) DEFAULT NULL,\n\
`audited_stores` int(11) DEFAULT NULL,\n\
`compliance_percentage` float DEFAULT NULL,\n\
`Total Images` int(11) DEFAULT NULL,\n\
`Non-Analyzable Images` int(11) DEFAULT NULL,\n\
`Non-Analyzable Images percentage` float DEFAULT NULL,\n\
`outlet_id` varchar(255) DEFAULT NULL,\n\
`outlet_name` varchar(255) DEFAULT NULL,\n\
`format_value` varchar(255) DEFAULT NULL,\n\
`Account` varchar(255) DEFAULT NULL,\n\
`State` varchar(255) DEFAULT NULL,\n\
`City` varchar(255) DEFAULT NULL,\n\
`SE` varchar(255) DEFAULT NULL,\n\
`MDM` varchar(255) DEFAULT NULL,\n\
`BSM` varchar(255) DEFAULT NULL,\n\
`Incomplete Main Aisle Audits Chocolate` int(11) DEFAULT NULL,\n\
`Incomplete Main Aisle Audits Biscuit` int(11) DEFAULT NULL,\n\
`Incomplete Main Aisle Audits MFD` int(11) DEFAULT NULL,\n\
`Incomplete Secondary Assets Audits` int(11) DEFAULT NULL,\n\
`Incomplete Hotzone Audits` int(11) DEFAULT NULL,\n\
`category` varchar(255) DEFAULT NULL,\n\
`Category MSL OSA Score` decimal(5,2) DEFAULT NULL,\n\
`Category MSL_Sufficiency_Mscore` decimal(5,2) DEFAULT NULL,\n\
`Category SOS Mscore` decimal(5,2) DEFAULT NULL,\n\
`Category Best_Selling_Shelf Mscore` decimal(5,2) DEFAULT NULL,\n\
`Secondary Asset Mscore` decimal(5,2) DEFAULT NULL,\n\
`Hotzone coverage Mscore` decimal(5,2) DEFAULT NULL,\n\
`Hotzone display Mscore` decimal(5,2) DEFAULT NULL,\n\
`Gold Compliance Mscore` decimal(5,2) DEFAULT NULL,\n\
`Category total Mscore` decimal(5,2) DEFAULT NULL,\n\
`Outlet Mscore` decimal(5,2) DEFAULT NULL,\n\
`created_at` datetime DEFAULT CURRENT_TIMESTAMP,\n\
`modified_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,\n\
`manual_scheduled_stores` int(10) DEFAULT NULL,\n\
`digital_scheduled_stores` int(10) DEFAULT NULL,\n\
`manual_audited_stores` int(10) DEFAULT NULL,\n\
`digital_audited_stores` int(10) DEFAULT NULL,\n\
`shop_type` varchar(30) DEFAULT NULL,\n\
`Region` varchar(30) DEFAULT NULL,\n\
`Other_Secondary_Asset_Mscore` decimal(5,2) DEFAULT NULL,\n\
`Visicooler_Secondary_Asset_Mscore` decimal(5,2) DEFAULT NULL,\n\
`audited_unscheduled_stores` int(5) DEFAULT NULL,\n\
`manual_audited_unscheduled_stores` int(5) DEFAULT NULL,\n\
`digital_audited_unscheduled_stores` int(5) DEFAULT NULL,\n\
`Secondary_Assets_Images` int(5) DEFAULT NULL,\n\
`A_Chocolate_Images` int(5) DEFAULT NULL,\n\
`B_Biscuit_Images` int(5) DEFAULT NULL,\n\
`C_MFD_Images` int(5) DEFAULT NULL,\n\
`Hotzone_Assets_Images` int(5) DEFAULT NULL,\n\
`KAM` varchar(80) DEFAULT NULL,\n\
`GrKAM` varchar(80) DEFAULT NULL,\n\
`KAM_1` varchar(80) DEFAULT NULL,\n\
PRIMARY KEY (`id`)\n\
) ENGINE=InnoDB AUTO_INCREMENT=2298196 DEFAULT CHARSET=latin1"

    column_descriptions: str = "\
        Category_SOS_Percentage is Category share of shelf percentage,\n\
        Category_SOS_Score is Category share of shelf score,\n\
        asset_sos_percentage is Asset share of shelf percentage,\n\
        Asset_SoS is Asset share of shelf"
