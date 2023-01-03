# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, MetaData, String, Table

metadata = MetaData()


t_customer = Table(
    'customer', metadata,
    Column('c_custkey', DECIMAL(38, 0), nullable=False),
    Column('c_name', String(25), nullable=False, comment='Customer Name'),
    Column('c_address', String(40), nullable=False),
    Column('c_nationkey', DECIMAL(38, 0), nullable=False),
    Column('c_phone', String(15), nullable=False),
    Column('c_acctbal', DECIMAL(12, 2), nullable=False),
    Column('c_mktsegment', String(10)),
    Column('c_comment', String(117)),
    comment='Customer data as defined by TPC-H'
)


t_lineitem = Table(
    'lineitem', metadata,
    Column('l_orderkey', DECIMAL(38, 0), nullable=False),
    Column('l_partkey', DECIMAL(38, 0), nullable=False),
    Column('l_suppkey', DECIMAL(38, 0), nullable=False),
    Column('l_linenumber', DECIMAL(38, 0), nullable=False),
    Column('l_quantity', DECIMAL(12, 2), nullable=False),
    Column('l_extendedprice', DECIMAL(12, 2), nullable=False),
    Column('l_discount', DECIMAL(12, 2), nullable=False),
    Column('l_tax', DECIMAL(12, 2), nullable=False),
    Column('l_returnflag', String(1), nullable=False),
    Column('l_linestatus', String(1), nullable=False),
    Column('l_shipdate', Date, nullable=False),
    Column('l_commitdate', Date, nullable=False),
    Column('l_receiptdate', Date, nullable=False),
    Column('l_shipinstruct', String(25), nullable=False),
    Column('l_shipmode', String(10), nullable=False),
    Column('l_comment', String(44), nullable=False),
    comment='Lineitem data as defined by TPC-H'
)


t_nation = Table(
    'nation', metadata,
    Column('n_nationkey', DECIMAL(38, 0), nullable=False),
    Column('n_name', String(25), nullable=False),
    Column('n_regionkey', DECIMAL(38, 0), nullable=False),
    Column('n_comment', String(152)),
    comment='Nation data as defined by TPC-H'
)


t_orders = Table(
    'orders', metadata,
    Column('o_orderkey', DECIMAL(38, 0), nullable=False),
    Column('o_custkey', DECIMAL(38, 0), nullable=False),
    Column('o_orderstatus', String(1), nullable=False),
    Column('o_totalprice', DECIMAL(12, 2), nullable=False),
    Column('o_orderdate', Date, nullable=False),
    Column('o_orderpriority', String(15), nullable=False),
    Column('o_clerk', String(15), nullable=False),
    Column('o_shippriority', DECIMAL(38, 0), nullable=False),
    Column('o_comment', String(79), nullable=False),
    comment='Orders data as defined by TPC-H'
)


t_part = Table(
    'part', metadata,
    Column('p_partkey', DECIMAL(38, 0), nullable=False),
    Column('p_name', String(55), nullable=False),
    Column('p_mfgr', String(25), nullable=False),
    Column('p_brand', String(10), nullable=False),
    Column('p_type', String(25), nullable=False),
    Column('p_size', DECIMAL(38, 0), nullable=False),
    Column('p_container', String(10), nullable=False),
    Column('p_retailprice', DECIMAL(12, 2), nullable=False),
    Column('p_comment', String(23)),
    comment='Part data as defined by TPC-H'
)


t_partsupp = Table(
    'partsupp', metadata,
    Column('ps_partkey', DECIMAL(38, 0), nullable=False),
    Column('ps_suppkey', DECIMAL(38, 0), nullable=False),
    Column('ps_availqty', DECIMAL(38, 0), nullable=False),
    Column('ps_supplycost', DECIMAL(12, 2), nullable=False),
    Column('ps_comment', String(199)),
    comment='Partsupp data as defined by TPC-H'
)


t_region = Table(
    'region', metadata,
    Column('r_regionkey', DECIMAL(38, 0), nullable=False),
    Column('r_name', String(25), nullable=False),
    Column('r_comment', String(152)),
    comment='Region data as defined by TPC-H'
)


t_supplier = Table(
    'supplier', metadata,
    Column('s_suppkey', DECIMAL(38, 0), nullable=False),
    Column('s_name', String(25), nullable=False),
    Column('s_address', String(40), nullable=False),
    Column('s_nationkey', DECIMAL(38, 0), nullable=False),
    Column('s_phone', String(15), nullable=False),
    Column('s_acctbal', DECIMAL(12, 2), nullable=False),
    Column('s_comment', String(101)),
    comment='Supplier data as defined by TPC-H'
)
