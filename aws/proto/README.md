# proto



## Create `STORATGE INTEGRATION`

with dummy STORAGE_AWS_ROLE_ARN & STORAGE_ALLOWED_LOCATIONS:

~~~sql
CREATE STORAGE INTEGRATION shaper_datastage
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam:0::role/role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://');
~~~

describe:

~~~sql
DESC INTEGRATION shaper_datastage;
~~~

~~~py
('ENABLED', 'Boolean', 'true', 'false')
('STORAGE_PROVIDER', 'String', 'S3', '')
('STORAGE_ALLOWED_LOCATIONS', 'List', 's3://', '[]')
('STORAGE_BLOCKED_LOCATIONS', 'List', '', '[]')
('STORAGE_AWS_IAM_USER_ARN', 'String', 'arn:aws:iam::0123456789AB:root', '')
('STORAGE_AWS_ROLE_ARN', 'String', 'arn:aws:iam::0:role/role', '')
('STORAGE_AWS_EXTERNAL_ID', 'String', 'XX14860_SFCRole=33_ppcGWQCKpwCicUqLE8Wd8+oQ/hI=', '')
('COMMENT', 'String', '', '')
~~~


## .env

~~~ini
TF_VAR_region=ap-northeast-1
TF_VAR_project_name=dwh
TF_VAR_profile=myaws
TF_VAR_dwh_account_arn=arn:aws:iam::0123456789AB:root
TF_VAR_dwh_account_id=XX14860_SFCRole=33_ppcGWQCKpwCicUqLE8Wd8+oQ/hI=
TF_LOG=TRACE
TF_LOG_PATH='./terraform.log' %         
~~~


## Create AWS Resource

~~~bash
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto init
~~~

~~~bash
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto plan -out all.plan
~~~

~~~bash
$ env $(cat ../sample/.env|xargs) terraform -chdir=proto apply all.plan
~~~


## Alter `STORATGE INTEGRATION`

with created STORAGE_AWS_ROLE_ARN & STORAGE_ALLOWED_LOCATIONS:


~~~sql
ALTER STORAGE INTEGRATION shaper_datastage SET STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::BA9876543210:dwh-proto-role-datasage';
~~~

~~~sql
ALTER STORAGE INTEGRATION shaper_datastage SET STORAGE_ALLOWED_LOCATIONS = ('s3://dwh-proto-role-datastage/');
~~~



## Articles

- https://dev.classmethod.jp/articles/snowflake-storage-integration-s3load/
