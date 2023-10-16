from .text_class_base import BaseTextClass


class TwiningsPromptText(BaseTextClass):
    table_schema: str = "\n\
CREATE TABLE `TWININGS_UK_TESTING` (\n\
  `id` int(11) NOT NULL AUTO_INCREMENT,\n\
  `capture_date` datetime DEFAULT NULL,\n\
  `shop_id` int(11) DEFAULT NULL,\n\
  `retailer` varchar(64) DEFAULT NULL,\n\
  `shop_name` varchar(250) DEFAULT NULL,\n\
  `client_shop_id` varchar(250) DEFAULT NULL,\n\
  `ideal_sku_overall_osa` float DEFAULT NULL,\n\
  `overall_sos` float DEFAULT NULL,\n\
  `plano_compliance` float DEFAULT NULL,\n\
  `asset_compliance` float DEFAULT NULL,\n\
  `brand` varchar(250) DEFAULT NULL,\n\
  `group_name` varchar(250) DEFAULT NULL,\n\
  `class_name` varchar(250) DEFAULT NULL,\n\
  `availability_status` tinyint(1) DEFAULT NULL,\n\
  `sku_annotations` int(11) DEFAULT NULL,\n\
  `total_annotations` int(11) DEFAULT NULL,\n\
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\n\
  `image_count` int(11) DEFAULT NULL,\n\
  `invalid_count` int(11) DEFAULT NULL,\n\
  `image_link` varchar(255) DEFAULT NULL,\n\
  `extra_shelf_image_link` varchar(255) DEFAULT NULL,\n\
  `planogram` varchar(64) DEFAULT NULL,\n\
  `planogram_link` varchar(255) DEFAULT NULL,\n\
  `competition` varchar(64) DEFAULT NULL,\n\
  `invalid_reason` varchar(64) DEFAULT NULL,\n\
  `manufacturer` varchar(50) DEFAULT NULL,\n\
  `subcategory` varchar(50) DEFAULT NULL,\n\
  `planogram_availability` varchar(11) DEFAULT NULL,\n\
  `latitude` float DEFAULT NULL,\n\
  `longitude` float DEFAULT NULL,\n\
  `posm_availability` float DEFAULT NULL,\n\
  `width` int(11) DEFAULT NULL,\n\
  `linear_sos` float DEFAULT NULL,\n\
  `plano_compliance_2` float DEFAULT NULL,\n\
  PRIMARY KEY (`id`)\n\
) ENGINE=InnoDB AUTO_INCREMENT=1191001 DEFAULT CHARSET=latin1 \n\
\n\
CREATE TABLE `TWININGS_UK_TESTING_ERROR_DUMP` (\n\
  `id` int(11) NOT NULL AUTO_INCREMENT,\n\
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,\n\
  `modified_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\n\
  `capture_date` datetime DEFAULT NULL,\n\
  `shop_name` varchar(64) DEFAULT NULL,\n\
  `client_shop_id` varchar(64) DEFAULT NULL,\n\
  `shelf_no` int(11) DEFAULT NULL,\n\
  `planogram_shelf_score` float DEFAULT NULL,\n\
  `asset_shelf_score` float DEFAULT NULL,\n\
  `asset_presence_check` int(11) DEFAULT NULL,\n\
  `ideal_planogram` json DEFAULT NULL,\n\
  `realogram_planogram` json DEFAULT NULL,\n\
  `ideal_asset` json DEFAULT NULL,\n\
  `realogram_asset` json DEFAULT NULL,\n\
  `planogram_product_placement_incorrect` tinyint(4) DEFAULT NULL,\n\
  `planogram_product_out_of_stock` tinyint(4) DEFAULT NULL,\n\
  `asset_product_out_of_stock` tinyint(4) DEFAULT NULL,\n\
  `asset_product_placement_incorrect` tinyint(4) DEFAULT NULL,\n\
  `total_asset_product_placement_incorrect` tinyint(4) DEFAULT NULL,\n\
  `count_asset_annotations` int(11) DEFAULT NULL,\n\
  `count_asset_out_of_stock` int(11) DEFAULT NULL,\n\
  `count_asset_product_placement_incorrect` int(11) DEFAULT NULL,\n\
  `planogram_1_non_ideal_check` tinyint(4) DEFAULT NULL,\n\
  `planogram_2_incorrect_check` tinyint(4) DEFAULT NULL,\n\
  PRIMARY KEY (`id`)\n\
) ENGINE=InnoDB AUTO_INCREMENT=36282 DEFAULT CHARSET=latin1\n\
"
    column_descriptions: str = "\n\
        overall_sos is Overall share of shelf,\n\
        plano_compliance is Planogram compliance,\n\
        shop in column names can be considered as outlets\n\
        "