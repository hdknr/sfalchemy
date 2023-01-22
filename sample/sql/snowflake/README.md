# Snowflake

## `CREATE STORAGE INTEGRATION` with fake user ARN and ID:

~~~sql
CREATE STORAGE INTEGRATION shaper_datastage
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::0123456789AB:role/fake'
  STORAGE_ALLOWED_LOCATIONS = ('s3://');
~~~

check `STORAGE_AWS_IAM_USER_ARN` and `STORAGE_AWS_EXTERNAL_ID`

~~~sql
DESC INTEGRATION shaper_datastage;
~~~

## Edit .env and create AWS

with `STORAGE_AWS_IAM_USER_ARN` and `STORAGE_AWS_EXTERNAL_ID` 

~~~ini
TF_VAR_region=ap-northeast-1
TF_VAR_project_name=dwh
TF_VAR_profile=shaper
TF_VAR_dwh_account_arn=STORAGE_AWS_IAM_USER_ARN_copied
TF_VAR_dwh_account_id=STORAGE_AWS_EXTERNAL_ID_copied
TF_LOG=TRACE
TF_LOG_PATH='./terraform.log' 
~~~

run Terraform to  create AWS resources(S3, IAM Policy & Role):

~~~bash
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto init
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto plan -out all.plan
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto apply all.plan
~~~


## `ALTER STORAGE INTEGRATION` after AWS resoruces were created:

IAM Role:

~~~sql
ALTER STORAGE INTEGRATION shaper_datastage 
SET STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::0123456789AB:role/dwh-proto-role-datastage';
~~~

S3 buckets:

~~~sql
ALTER STORAGE INTEGRATION shaper_datastage 
SET STORAGE_ALLOWED_LOCATIONS = ('s3://dwh-proto-datastage/', 's3://dwh-proto-datastage/snowflake/');
~~~

## `CREATE STAGE` from import data.

~~~sql
CREATE STAGE tickt_s3_stage
  STORAGE_INTEGRATION = shaper_datastage
  URL = 's3://dwh-proto-datastage/snowflake/';
~~~


## Upload JSON(NDJSON) files to S3

For example, unload `VENUE` talbe from Redshift sample database TICKIT to S3(with Redshift Role):

~~~sql
UNLOAD ('select * from venue')   
TO 's3://dwh-proto-datastage/snowflake/venue_' 
FORMAT JSON 
IAM_ROLE 'arn:aws:iam::......';
~~~

## Load JSON files form S3:

NDJSON format(Newline-delimited JSONl):

~~~sql
COPY INTO VENUE(venueid, venuename, venuecity, venuestate,venueseats) 
FROM (SELECT $1:venueid, $1:venuename, $1:venuecity, $1:venuestate, $1:venueseats FROM @tickt_s3_stage)
FILE_FORMAT = (TYPE = JSON, COMPRESSION=NONE, STRIP_OUTER_ARRAY=TRUE) ;
~~~


