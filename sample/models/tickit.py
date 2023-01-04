# coding: utf-8
from sqlalchemy import (
    CHAR,
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    MetaData,
    Numeric,
    SmallInteger,
    String,
    Table,
    text,
)

metadata = MetaData()


t_category = Table(
    "category",
    metadata,
    Column("catid", SmallInteger, nullable=False),
    Column("catgroup", String(10)),
    Column("catname", String(10)),
    Column("catdesc", String(50)),
    Column("memo", String(100)),
)


t_date = Table(
    "date",
    metadata,
    Column("dateid", SmallInteger, nullable=False),
    Column("caldate", Date, nullable=False),
    Column("day", CHAR(3), nullable=False),
    Column("week", SmallInteger, nullable=False),
    Column("month", CHAR(5), nullable=False),
    Column("qtr", CHAR(5), nullable=False),
    Column("year", SmallInteger, nullable=False),
    Column("holiday", Boolean, server_default=text("false")),
)


t_event = Table(
    "event",
    metadata,
    Column("eventid", Integer, nullable=False),
    Column("venueid", SmallInteger, nullable=False),
    Column("catid", SmallInteger, nullable=False),
    Column("dateid", SmallInteger, nullable=False),
    Column("eventname", String(200)),
    Column("starttime", DateTime),
)


t_listing = Table(
    "listing",
    metadata,
    Column("listid", Integer, nullable=False),
    Column("sellerid", Integer, nullable=False),
    Column("eventid", Integer, nullable=False),
    Column("dateid", SmallInteger, nullable=False),
    Column("numtickets", SmallInteger, nullable=False),
    Column("priceperticket", Numeric(8, 2)),
    Column("totalprice", Numeric(8, 2)),
    Column("listtime", DateTime),
)


t_sales = Table(
    "sales",
    metadata,
    Column("salesid", Integer, nullable=False),
    Column("listid", Integer, nullable=False),
    Column("sellerid", Integer, nullable=False),
    Column("buyerid", Integer, nullable=False),
    Column("eventid", Integer, nullable=False),
    Column("dateid", SmallInteger, nullable=False),
    Column("qtysold", SmallInteger, nullable=False),
    Column("pricepaid", Numeric(8, 2)),
    Column("commission", Numeric(8, 2)),
    Column("saletime", DateTime),
)


t_users = Table(
    "users",
    metadata,
    Column("userid", Integer, nullable=False),
    Column("username", CHAR(8)),
    Column("firstname", String(30)),
    Column("lastname", String(30)),
    Column("city", String(30)),
    Column("state", CHAR(2)),
    Column("email", String(100)),
    Column("phone", CHAR(14)),
    Column("likesports", Boolean),
    Column("liketheatre", Boolean),
    Column("likeconcerts", Boolean),
    Column("likejazz", Boolean),
    Column("likeclassical", Boolean),
    Column("likeopera", Boolean),
    Column("likerock", Boolean),
    Column("likevegas", Boolean),
    Column("likebroadway", Boolean),
    Column("likemusicals", Boolean),
)


t_venue = Table(
    "venue",
    metadata,
    Column("venueid", SmallInteger, nullable=False),
    Column("venuename", String(100)),
    Column("venuecity", String(30)),
    Column("venuestate", CHAR(2)),
    Column("venueseats", Integer),
)
