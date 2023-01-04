# SNOWFLAKE_SAMPLE_DATA 

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