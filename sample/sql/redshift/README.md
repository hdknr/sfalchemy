# Redshift

## UNLOAD Data to S3 from Redshift Serverless

Redshift Serverless creates an IAM role like `AmazonRedshift-CommandsAccessRole-20230103T223820` :

~~~sql
UNLOAD ('select * from venue')   
TO 's3://dwh-proto-datastage/snowflake/venue_' 
FORMAT JSON 
IAM_ROLE 'arn:aws:iam::0123456789AB:role/service-role/AmazonRedshift-CommandsAccessRole-20230103T223820';
~~~


## Links

- https://blog.serverworks.co.jp/redshift_serverless_handson-2022
- [AWS Redshift Serverless: `ERROR: Not authorized to get credentials of role`](https://stackoverflow.com/questions/70659682/aws-redshift-serverless-error-not-authorized-to-get-credentials-of-role)