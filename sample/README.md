# Database migration sample

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