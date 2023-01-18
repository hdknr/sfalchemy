# Database migration sample
sample/alembic_migrate/env.py:

~~~py


~~~

## Schema 

~~~bash
export $(cat .env|xargs)
modelgen createmodel -s database --outfile models/tpch.py -p $TPCH_SF10_URL -a
modelgen createmodel -s database --outfile models/tpcds.py -p $TPCDS_SF10TCL_URL -a
modelgen createmodel -s database --outfile models/tickit.py -p $AWS_TICKIT_URL -a --schema tickit
~~~

## Migrations(Redshift to MySQL)

`scheme` parameter:

- drop all `schema` parameters from `tickit.py` if migrate to other database architectures.


make migration:

~~~bash
modelgen migrate revision --autogenerate -m "COMMIT_MESSAGE" -p  $MYSQL_TICKIT_URL
~~~

execute migration:

~~~bash
modelgen migrate upgrade head -p $MYSQL_TICKIT_URL
~~~

~~~sql
select * from alembic_version;

+--------------+
| version_num  |
+--------------+
| a82b89ad4982 |
+--------------+
~~~

## Modify schema

~~~bash
modelgen migrate revision --autogenerate -m "add memo to t_category" -p  $MYSQL_TICKIT_URL
modelgen migrate upgrade head -p $MYSQL_TICKIT_URL
~~~

~~~sql
desc category;

+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| catid    | smallint     | NO   |     | NULL    |       |
| catgroup | varchar(10)  | YES  |     | NULL    |       |
| catname  | varchar(10)  | YES  |     | NULL    |       |
| catdesc  | varchar(50)  | YES  |     | NULL    |       |
| memo     | varchar(100) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
~~~


## Migration to Snowflake

sample/alembic_migrate/env.py:

~~~py
...

from alembic.ddl.impl import DefaultImpl

class SnowflakeImpl(DefaultImpl):
    __dialect__ = "snowflake"

...
~~~

samples/.env:

~~~ini
SNOW_TICKIT_URL=snowflake://hdknr:PASSWORD@LOCATOR.ap-northeast-1.aws/TICKIT/TICKIT?warehouse=COMPUTE_WH&role=ACCOUNTADMIN&numpy=True
~~~

~~~bash
% modelgen migrate upgrade head -p $SNOW_TICKIT_URL
~~~


~~~bash
% python ../sfalchemy/run.py query-df sql/snowflake/show_tables.sql -u SNOW_TICKIT_URL
~~~


| name            | database_name | schema_name | kind  |
| --------------- | ------------- | ----------- | ----- |
| ALEMBIC_VERSION | TICKIT        | TICKIT      | TABLE |
| CATEGORY        | TICKIT        | TICKIT      | TABLE |
| USERS           | TICKIT        | TICKIT      | TABLE |
| VENUE           | TICKIT        | TICKIT      | TABLE |


## Notice

### primary keys

- primary key constraints were not detected. manually edit `primary_key=True` attribute.


### `scheme` parameter

- drop all `schema` parameters from `tickit.py` if migrate to other database architectures.
