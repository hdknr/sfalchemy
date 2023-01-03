# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, MetaData, String, Table

metadata = MetaData()


t_call_center = Table(
    'call_center', metadata,
    Column('cc_call_center_sk', DECIMAL(38, 0), nullable=False),
    Column('cc_call_center_id', String(16), nullable=False),
    Column('cc_rec_start_date', Date),
    Column('cc_rec_end_date', Date),
    Column('cc_closed_date_sk', DECIMAL(38, 0)),
    Column('cc_open_date_sk', DECIMAL(38, 0)),
    Column('cc_name', String(50)),
    Column('cc_class', String(50)),
    Column('cc_employees', DECIMAL(38, 0)),
    Column('cc_sq_ft', DECIMAL(38, 0)),
    Column('cc_hours', String(20)),
    Column('cc_manager', String(40)),
    Column('cc_mkt_id', DECIMAL(38, 0)),
    Column('cc_mkt_class', String(50)),
    Column('cc_mkt_desc', String(100)),
    Column('cc_market_manager', String(40)),
    Column('cc_division', DECIMAL(38, 0)),
    Column('cc_division_name', String(50)),
    Column('cc_company', DECIMAL(38, 0)),
    Column('cc_company_name', String(50)),
    Column('cc_street_number', String(10)),
    Column('cc_street_name', String(60)),
    Column('cc_street_type', String(15)),
    Column('cc_suite_number', String(10)),
    Column('cc_city', String(60)),
    Column('cc_county', String(30)),
    Column('cc_state', String(2)),
    Column('cc_zip', String(10)),
    Column('cc_country', String(20)),
    Column('cc_gmt_offset', DECIMAL(5, 2)),
    Column('cc_tax_percentage', DECIMAL(5, 2))
)


t_catalog_page = Table(
    'catalog_page', metadata,
    Column('cp_catalog_page_sk', DECIMAL(38, 0), nullable=False),
    Column('cp_catalog_page_id', String(16), nullable=False),
    Column('cp_start_date_sk', DECIMAL(38, 0)),
    Column('cp_end_date_sk', DECIMAL(38, 0)),
    Column('cp_department', String(50)),
    Column('cp_catalog_number', DECIMAL(38, 0)),
    Column('cp_catalog_page_number', DECIMAL(38, 0)),
    Column('cp_description', String(100)),
    Column('cp_type', String(100))
)


t_catalog_returns = Table(
    'catalog_returns', metadata,
    Column('cr_returned_date_sk', DECIMAL(38, 0)),
    Column('cr_returned_time_sk', DECIMAL(38, 0)),
    Column('cr_item_sk', DECIMAL(38, 0), nullable=False),
    Column('cr_refunded_customer_sk', DECIMAL(38, 0)),
    Column('cr_refunded_cdemo_sk', DECIMAL(38, 0)),
    Column('cr_refunded_hdemo_sk', DECIMAL(38, 0)),
    Column('cr_refunded_addr_sk', DECIMAL(38, 0)),
    Column('cr_returning_customer_sk', DECIMAL(38, 0)),
    Column('cr_returning_cdemo_sk', DECIMAL(38, 0)),
    Column('cr_returning_hdemo_sk', DECIMAL(38, 0)),
    Column('cr_returning_addr_sk', DECIMAL(38, 0)),
    Column('cr_call_center_sk', DECIMAL(38, 0)),
    Column('cr_catalog_page_sk', DECIMAL(38, 0)),
    Column('cr_ship_mode_sk', DECIMAL(38, 0)),
    Column('cr_warehouse_sk', DECIMAL(38, 0)),
    Column('cr_reason_sk', DECIMAL(38, 0)),
    Column('cr_order_number', DECIMAL(38, 0), nullable=False),
    Column('cr_return_quantity', DECIMAL(38, 0)),
    Column('cr_return_amount', DECIMAL(7, 2)),
    Column('cr_return_tax', DECIMAL(7, 2)),
    Column('cr_return_amt_inc_tax', DECIMAL(7, 2)),
    Column('cr_fee', DECIMAL(7, 2)),
    Column('cr_return_ship_cost', DECIMAL(7, 2)),
    Column('cr_refunded_cash', DECIMAL(7, 2)),
    Column('cr_reversed_charge', DECIMAL(7, 2)),
    Column('cr_store_credit', DECIMAL(7, 2)),
    Column('cr_net_loss', DECIMAL(7, 2))
)


t_catalog_sales = Table(
    'catalog_sales', metadata,
    Column('cs_sold_date_sk', DECIMAL(38, 0)),
    Column('cs_sold_time_sk', DECIMAL(38, 0)),
    Column('cs_ship_date_sk', DECIMAL(38, 0)),
    Column('cs_bill_customer_sk', DECIMAL(38, 0)),
    Column('cs_bill_cdemo_sk', DECIMAL(38, 0)),
    Column('cs_bill_hdemo_sk', DECIMAL(38, 0)),
    Column('cs_bill_addr_sk', DECIMAL(38, 0)),
    Column('cs_ship_customer_sk', DECIMAL(38, 0)),
    Column('cs_ship_cdemo_sk', DECIMAL(38, 0)),
    Column('cs_ship_hdemo_sk', DECIMAL(38, 0)),
    Column('cs_ship_addr_sk', DECIMAL(38, 0)),
    Column('cs_call_center_sk', DECIMAL(38, 0)),
    Column('cs_catalog_page_sk', DECIMAL(38, 0)),
    Column('cs_ship_mode_sk', DECIMAL(38, 0)),
    Column('cs_warehouse_sk', DECIMAL(38, 0)),
    Column('cs_item_sk', DECIMAL(38, 0), nullable=False),
    Column('cs_promo_sk', DECIMAL(38, 0)),
    Column('cs_order_number', DECIMAL(38, 0), nullable=False),
    Column('cs_quantity', DECIMAL(38, 0)),
    Column('cs_wholesale_cost', DECIMAL(7, 2)),
    Column('cs_list_price', DECIMAL(7, 2)),
    Column('cs_sales_price', DECIMAL(7, 2)),
    Column('cs_ext_discount_amt', DECIMAL(7, 2)),
    Column('cs_ext_sales_price', DECIMAL(7, 2)),
    Column('cs_ext_wholesale_cost', DECIMAL(7, 2)),
    Column('cs_ext_list_price', DECIMAL(7, 2)),
    Column('cs_ext_tax', DECIMAL(7, 2)),
    Column('cs_coupon_amt', DECIMAL(7, 2)),
    Column('cs_ext_ship_cost', DECIMAL(7, 2)),
    Column('cs_net_paid', DECIMAL(7, 2)),
    Column('cs_net_paid_inc_tax', DECIMAL(7, 2)),
    Column('cs_net_paid_inc_ship', DECIMAL(7, 2)),
    Column('cs_net_paid_inc_ship_tax', DECIMAL(7, 2)),
    Column('cs_net_profit', DECIMAL(7, 2))
)


t_customer = Table(
    'customer', metadata,
    Column('c_customer_sk', DECIMAL(38, 0), nullable=False),
    Column('c_customer_id', String(16), nullable=False),
    Column('c_current_cdemo_sk', DECIMAL(38, 0)),
    Column('c_current_hdemo_sk', DECIMAL(38, 0)),
    Column('c_current_addr_sk', DECIMAL(38, 0)),
    Column('c_first_shipto_date_sk', DECIMAL(38, 0)),
    Column('c_first_sales_date_sk', DECIMAL(38, 0)),
    Column('c_salutation', String(10)),
    Column('c_first_name', String(20)),
    Column('c_last_name', String(30)),
    Column('c_preferred_cust_flag', String(1)),
    Column('c_birth_day', DECIMAL(38, 0)),
    Column('c_birth_month', DECIMAL(38, 0)),
    Column('c_birth_year', DECIMAL(38, 0)),
    Column('c_birth_country', String(20)),
    Column('c_login', String(13)),
    Column('c_email_address', String(50)),
    Column('c_last_review_date', String(10))
)


t_customer_address = Table(
    'customer_address', metadata,
    Column('ca_address_sk', DECIMAL(38, 0), nullable=False),
    Column('ca_address_id', String(16), nullable=False),
    Column('ca_street_number', String(10)),
    Column('ca_street_name', String(60)),
    Column('ca_street_type', String(15)),
    Column('ca_suite_number', String(10)),
    Column('ca_city', String(60)),
    Column('ca_county', String(30)),
    Column('ca_state', String(2)),
    Column('ca_zip', String(10)),
    Column('ca_country', String(20)),
    Column('ca_gmt_offset', DECIMAL(5, 2)),
    Column('ca_location_type', String(20))
)


t_customer_demographics = Table(
    'customer_demographics', metadata,
    Column('cd_demo_sk', DECIMAL(38, 0), nullable=False),
    Column('cd_gender', String(1)),
    Column('cd_marital_status', String(1)),
    Column('cd_education_status', String(20)),
    Column('cd_purchase_estimate', DECIMAL(38, 0)),
    Column('cd_credit_rating', String(10)),
    Column('cd_dep_count', DECIMAL(38, 0)),
    Column('cd_dep_employed_count', DECIMAL(38, 0)),
    Column('cd_dep_college_count', DECIMAL(38, 0))
)


t_date_dim = Table(
    'date_dim', metadata,
    Column('d_date_sk', DECIMAL(38, 0), nullable=False),
    Column('d_date_id', String(16), nullable=False),
    Column('d_date', Date),
    Column('d_month_seq', DECIMAL(38, 0)),
    Column('d_week_seq', DECIMAL(38, 0)),
    Column('d_quarter_seq', DECIMAL(38, 0)),
    Column('d_year', DECIMAL(38, 0)),
    Column('d_dow', DECIMAL(38, 0)),
    Column('d_moy', DECIMAL(38, 0)),
    Column('d_dom', DECIMAL(38, 0)),
    Column('d_qoy', DECIMAL(38, 0)),
    Column('d_fy_year', DECIMAL(38, 0)),
    Column('d_fy_quarter_seq', DECIMAL(38, 0)),
    Column('d_fy_week_seq', DECIMAL(38, 0)),
    Column('d_day_name', String(9)),
    Column('d_quarter_name', String(6)),
    Column('d_holiday', String(1)),
    Column('d_weekend', String(1)),
    Column('d_following_holiday', String(1)),
    Column('d_first_dom', DECIMAL(38, 0)),
    Column('d_last_dom', DECIMAL(38, 0)),
    Column('d_same_day_ly', DECIMAL(38, 0)),
    Column('d_same_day_lq', DECIMAL(38, 0)),
    Column('d_current_day', String(1)),
    Column('d_current_week', String(1)),
    Column('d_current_month', String(1)),
    Column('d_current_quarter', String(1)),
    Column('d_current_year', String(1))
)


t_dbgen_version = Table(
    'dbgen_version', metadata,
    Column('dv_version', String(16)),
    Column('dv_create_date', Date),
    Column('dv_create_time', String(10)),
    Column('dv_cmdline_args', String(200))
)


t_household_demographics = Table(
    'household_demographics', metadata,
    Column('hd_demo_sk', DECIMAL(38, 0), nullable=False),
    Column('hd_income_band_sk', DECIMAL(38, 0)),
    Column('hd_buy_potential', String(15)),
    Column('hd_dep_count', DECIMAL(38, 0)),
    Column('hd_vehicle_count', DECIMAL(38, 0))
)


t_income_band = Table(
    'income_band', metadata,
    Column('ib_income_band_sk', DECIMAL(38, 0), nullable=False),
    Column('ib_lower_bound', DECIMAL(38, 0)),
    Column('ib_upper_bound', DECIMAL(38, 0))
)


t_inventory = Table(
    'inventory', metadata,
    Column('inv_date_sk', DECIMAL(38, 0), nullable=False),
    Column('inv_item_sk', DECIMAL(38, 0), nullable=False),
    Column('inv_warehouse_sk', DECIMAL(38, 0), nullable=False),
    Column('inv_quantity_on_hand', DECIMAL(38, 0))
)


t_item = Table(
    'item', metadata,
    Column('i_item_sk', DECIMAL(38, 0), nullable=False),
    Column('i_item_id', String(16), nullable=False),
    Column('i_rec_start_date', Date),
    Column('i_rec_end_date', Date),
    Column('i_item_desc', String(200)),
    Column('i_current_price', DECIMAL(7, 2)),
    Column('i_wholesale_cost', DECIMAL(7, 2)),
    Column('i_brand_id', DECIMAL(38, 0)),
    Column('i_brand', String(50)),
    Column('i_class_id', DECIMAL(38, 0)),
    Column('i_class', String(50)),
    Column('i_category_id', DECIMAL(38, 0)),
    Column('i_category', String(50)),
    Column('i_manufact_id', DECIMAL(38, 0)),
    Column('i_manufact', String(50)),
    Column('i_size', String(20)),
    Column('i_formulation', String(20)),
    Column('i_color', String(20)),
    Column('i_units', String(10)),
    Column('i_container', String(10)),
    Column('i_manager_id', DECIMAL(38, 0)),
    Column('i_product_name', String(50))
)


t_promotion = Table(
    'promotion', metadata,
    Column('p_promo_sk', DECIMAL(38, 0), nullable=False),
    Column('p_promo_id', String(16), nullable=False),
    Column('p_start_date_sk', DECIMAL(38, 0)),
    Column('p_end_date_sk', DECIMAL(38, 0)),
    Column('p_item_sk', DECIMAL(38, 0)),
    Column('p_cost', DECIMAL(15, 2)),
    Column('p_response_target', DECIMAL(38, 0)),
    Column('p_promo_name', String(50)),
    Column('p_channel_dmail', String(1)),
    Column('p_channel_email', String(1)),
    Column('p_channel_catalog', String(1)),
    Column('p_channel_tv', String(1)),
    Column('p_channel_radio', String(1)),
    Column('p_channel_press', String(1)),
    Column('p_channel_event', String(1)),
    Column('p_channel_demo', String(1)),
    Column('p_channel_details', String(100)),
    Column('p_purpose', String(15)),
    Column('p_discount_active', String(1))
)


t_reason = Table(
    'reason', metadata,
    Column('r_reason_sk', DECIMAL(38, 0), nullable=False),
    Column('r_reason_id', String(16), nullable=False),
    Column('r_reason_desc', String(100))
)


t_ship_mode = Table(
    'ship_mode', metadata,
    Column('sm_ship_mode_sk', DECIMAL(38, 0), nullable=False),
    Column('sm_ship_mode_id', String(16), nullable=False),
    Column('sm_type', String(30)),
    Column('sm_code', String(10)),
    Column('sm_carrier', String(20)),
    Column('sm_contract', String(20))
)


t_store = Table(
    'store', metadata,
    Column('s_store_sk', DECIMAL(38, 0), nullable=False),
    Column('s_store_id', String(16), nullable=False),
    Column('s_rec_start_date', Date),
    Column('s_rec_end_date', Date),
    Column('s_closed_date_sk', DECIMAL(38, 0)),
    Column('s_store_name', String(50)),
    Column('s_number_employees', DECIMAL(38, 0)),
    Column('s_floor_space', DECIMAL(38, 0)),
    Column('s_hours', String(20)),
    Column('s_manager', String(40)),
    Column('s_market_id', DECIMAL(38, 0)),
    Column('s_geography_class', String(100)),
    Column('s_market_desc', String(100)),
    Column('s_market_manager', String(40)),
    Column('s_division_id', DECIMAL(38, 0)),
    Column('s_division_name', String(50)),
    Column('s_company_id', DECIMAL(38, 0)),
    Column('s_company_name', String(50)),
    Column('s_street_number', String(10)),
    Column('s_street_name', String(60)),
    Column('s_street_type', String(15)),
    Column('s_suite_number', String(10)),
    Column('s_city', String(60)),
    Column('s_county', String(30)),
    Column('s_state', String(2)),
    Column('s_zip', String(10)),
    Column('s_country', String(20)),
    Column('s_gmt_offset', DECIMAL(5, 2)),
    Column('s_tax_precentage', DECIMAL(5, 2))
)


t_store_returns = Table(
    'store_returns', metadata,
    Column('sr_returned_date_sk', DECIMAL(38, 0)),
    Column('sr_return_time_sk', DECIMAL(38, 0)),
    Column('sr_item_sk', DECIMAL(38, 0), nullable=False),
    Column('sr_customer_sk', DECIMAL(38, 0)),
    Column('sr_cdemo_sk', DECIMAL(38, 0)),
    Column('sr_hdemo_sk', DECIMAL(38, 0)),
    Column('sr_addr_sk', DECIMAL(38, 0)),
    Column('sr_store_sk', DECIMAL(38, 0)),
    Column('sr_reason_sk', DECIMAL(38, 0)),
    Column('sr_ticket_number', DECIMAL(38, 0), nullable=False),
    Column('sr_return_quantity', DECIMAL(38, 0)),
    Column('sr_return_amt', DECIMAL(7, 2)),
    Column('sr_return_tax', DECIMAL(7, 2)),
    Column('sr_return_amt_inc_tax', DECIMAL(7, 2)),
    Column('sr_fee', DECIMAL(7, 2)),
    Column('sr_return_ship_cost', DECIMAL(7, 2)),
    Column('sr_refunded_cash', DECIMAL(7, 2)),
    Column('sr_reversed_charge', DECIMAL(7, 2)),
    Column('sr_store_credit', DECIMAL(7, 2)),
    Column('sr_net_loss', DECIMAL(7, 2))
)


t_store_sales = Table(
    'store_sales', metadata,
    Column('ss_sold_date_sk', DECIMAL(38, 0)),
    Column('ss_sold_time_sk', DECIMAL(38, 0)),
    Column('ss_item_sk', DECIMAL(38, 0), nullable=False),
    Column('ss_customer_sk', DECIMAL(38, 0)),
    Column('ss_cdemo_sk', DECIMAL(38, 0)),
    Column('ss_hdemo_sk', DECIMAL(38, 0)),
    Column('ss_addr_sk', DECIMAL(38, 0)),
    Column('ss_store_sk', DECIMAL(38, 0)),
    Column('ss_promo_sk', DECIMAL(38, 0)),
    Column('ss_ticket_number', DECIMAL(38, 0), nullable=False),
    Column('ss_quantity', DECIMAL(38, 0)),
    Column('ss_wholesale_cost', DECIMAL(7, 2)),
    Column('ss_list_price', DECIMAL(7, 2)),
    Column('ss_sales_price', DECIMAL(7, 2)),
    Column('ss_ext_discount_amt', DECIMAL(7, 2)),
    Column('ss_ext_sales_price', DECIMAL(7, 2)),
    Column('ss_ext_wholesale_cost', DECIMAL(7, 2)),
    Column('ss_ext_list_price', DECIMAL(7, 2)),
    Column('ss_ext_tax', DECIMAL(7, 2)),
    Column('ss_coupon_amt', DECIMAL(7, 2)),
    Column('ss_net_paid', DECIMAL(7, 2)),
    Column('ss_net_paid_inc_tax', DECIMAL(7, 2)),
    Column('ss_net_profit', DECIMAL(7, 2))
)


t_time_dim = Table(
    'time_dim', metadata,
    Column('t_time_sk', DECIMAL(38, 0), nullable=False),
    Column('t_time_id', String(16), nullable=False),
    Column('t_time', DECIMAL(38, 0)),
    Column('t_hour', DECIMAL(38, 0)),
    Column('t_minute', DECIMAL(38, 0)),
    Column('t_second', DECIMAL(38, 0)),
    Column('t_am_pm', String(2)),
    Column('t_shift', String(20)),
    Column('t_sub_shift', String(20)),
    Column('t_meal_time', String(20))
)


t_warehouse = Table(
    'warehouse', metadata,
    Column('w_warehouse_sk', DECIMAL(38, 0), nullable=False),
    Column('w_warehouse_id', String(16), nullable=False),
    Column('w_warehouse_name', String(20)),
    Column('w_warehouse_sq_ft', DECIMAL(38, 0)),
    Column('w_street_number', String(10)),
    Column('w_street_name', String(60)),
    Column('w_street_type', String(15)),
    Column('w_suite_number', String(10)),
    Column('w_city', String(60)),
    Column('w_county', String(30)),
    Column('w_state', String(2)),
    Column('w_zip', String(10)),
    Column('w_country', String(20)),
    Column('w_gmt_offset', DECIMAL(5, 2))
)


t_web_page = Table(
    'web_page', metadata,
    Column('wp_web_page_sk', DECIMAL(38, 0), nullable=False),
    Column('wp_web_page_id', String(16), nullable=False),
    Column('wp_rec_start_date', Date),
    Column('wp_rec_end_date', Date),
    Column('wp_creation_date_sk', DECIMAL(38, 0)),
    Column('wp_access_date_sk', DECIMAL(38, 0)),
    Column('wp_autogen_flag', String(1)),
    Column('wp_customer_sk', DECIMAL(38, 0)),
    Column('wp_url', String(100)),
    Column('wp_type', String(50)),
    Column('wp_char_count', DECIMAL(38, 0)),
    Column('wp_link_count', DECIMAL(38, 0)),
    Column('wp_image_count', DECIMAL(38, 0)),
    Column('wp_max_ad_count', DECIMAL(38, 0))
)


t_web_returns = Table(
    'web_returns', metadata,
    Column('wr_returned_date_sk', DECIMAL(38, 0)),
    Column('wr_returned_time_sk', DECIMAL(38, 0)),
    Column('wr_item_sk', DECIMAL(38, 0), nullable=False),
    Column('wr_refunded_customer_sk', DECIMAL(38, 0)),
    Column('wr_refunded_cdemo_sk', DECIMAL(38, 0)),
    Column('wr_refunded_hdemo_sk', DECIMAL(38, 0)),
    Column('wr_refunded_addr_sk', DECIMAL(38, 0)),
    Column('wr_returning_customer_sk', DECIMAL(38, 0)),
    Column('wr_returning_cdemo_sk', DECIMAL(38, 0)),
    Column('wr_returning_hdemo_sk', DECIMAL(38, 0)),
    Column('wr_returning_addr_sk', DECIMAL(38, 0)),
    Column('wr_web_page_sk', DECIMAL(38, 0)),
    Column('wr_reason_sk', DECIMAL(38, 0)),
    Column('wr_order_number', DECIMAL(38, 0), nullable=False),
    Column('wr_return_quantity', DECIMAL(38, 0)),
    Column('wr_return_amt', DECIMAL(7, 2)),
    Column('wr_return_tax', DECIMAL(7, 2)),
    Column('wr_return_amt_inc_tax', DECIMAL(7, 2)),
    Column('wr_fee', DECIMAL(7, 2)),
    Column('wr_return_ship_cost', DECIMAL(7, 2)),
    Column('wr_refunded_cash', DECIMAL(7, 2)),
    Column('wr_reversed_charge', DECIMAL(7, 2)),
    Column('wr_account_credit', DECIMAL(7, 2)),
    Column('wr_net_loss', DECIMAL(7, 2))
)


t_web_sales = Table(
    'web_sales', metadata,
    Column('ws_sold_date_sk', DECIMAL(38, 0)),
    Column('ws_sold_time_sk', DECIMAL(38, 0)),
    Column('ws_ship_date_sk', DECIMAL(38, 0)),
    Column('ws_item_sk', DECIMAL(38, 0), nullable=False),
    Column('ws_bill_customer_sk', DECIMAL(38, 0)),
    Column('ws_bill_cdemo_sk', DECIMAL(38, 0)),
    Column('ws_bill_hdemo_sk', DECIMAL(38, 0)),
    Column('ws_bill_addr_sk', DECIMAL(38, 0)),
    Column('ws_ship_customer_sk', DECIMAL(38, 0)),
    Column('ws_ship_cdemo_sk', DECIMAL(38, 0)),
    Column('ws_ship_hdemo_sk', DECIMAL(38, 0)),
    Column('ws_ship_addr_sk', DECIMAL(38, 0)),
    Column('ws_web_page_sk', DECIMAL(38, 0)),
    Column('ws_web_site_sk', DECIMAL(38, 0)),
    Column('ws_ship_mode_sk', DECIMAL(38, 0)),
    Column('ws_warehouse_sk', DECIMAL(38, 0)),
    Column('ws_promo_sk', DECIMAL(38, 0)),
    Column('ws_order_number', DECIMAL(38, 0), nullable=False),
    Column('ws_quantity', DECIMAL(38, 0)),
    Column('ws_wholesale_cost', DECIMAL(7, 2)),
    Column('ws_list_price', DECIMAL(7, 2)),
    Column('ws_sales_price', DECIMAL(7, 2)),
    Column('ws_ext_discount_amt', DECIMAL(7, 2)),
    Column('ws_ext_sales_price', DECIMAL(7, 2)),
    Column('ws_ext_wholesale_cost', DECIMAL(7, 2)),
    Column('ws_ext_list_price', DECIMAL(7, 2)),
    Column('ws_ext_tax', DECIMAL(7, 2)),
    Column('ws_coupon_amt', DECIMAL(7, 2)),
    Column('ws_ext_ship_cost', DECIMAL(7, 2)),
    Column('ws_net_paid', DECIMAL(7, 2)),
    Column('ws_net_paid_inc_tax', DECIMAL(7, 2)),
    Column('ws_net_paid_inc_ship', DECIMAL(7, 2)),
    Column('ws_net_paid_inc_ship_tax', DECIMAL(7, 2)),
    Column('ws_net_profit', DECIMAL(7, 2))
)


t_web_site = Table(
    'web_site', metadata,
    Column('web_site_sk', DECIMAL(38, 0), nullable=False),
    Column('web_site_id', String(16), nullable=False),
    Column('web_rec_start_date', Date),
    Column('web_rec_end_date', Date),
    Column('web_name', String(50)),
    Column('web_open_date_sk', DECIMAL(38, 0)),
    Column('web_close_date_sk', DECIMAL(38, 0)),
    Column('web_class', String(50)),
    Column('web_manager', String(40)),
    Column('web_mkt_id', DECIMAL(38, 0)),
    Column('web_mkt_class', String(50)),
    Column('web_mkt_desc', String(100)),
    Column('web_market_manager', String(40)),
    Column('web_company_id', DECIMAL(38, 0)),
    Column('web_company_name', String(50)),
    Column('web_street_number', String(10)),
    Column('web_street_name', String(60)),
    Column('web_street_type', String(15)),
    Column('web_suite_number', String(10)),
    Column('web_city', String(60)),
    Column('web_county', String(30)),
    Column('web_state', String(2)),
    Column('web_zip', String(10)),
    Column('web_country', String(20)),
    Column('web_gmt_offset', DECIMAL(5, 2)),
    Column('web_tax_percentage', DECIMAL(5, 2))
)
