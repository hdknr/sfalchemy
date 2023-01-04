# SNOWFLAKE_SAMPLE_DATA 

## Schema 

~~~bash
export $(cat .env|xargs)
modelgen createmodel -s database --outfile models/tpch.py -p $TPCH_SF10_URL -a
modelgen createmodel -s database --outfile models/tpcds.py -p $TPCDS_SF10TCL_URL -a
modelgen createmodel -s database --outfile models/tickit.py -p $AWS_TICKIT_URL -a --schema tickit
~~~