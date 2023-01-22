variable "symbol" {}
variable "dwh_account" {}
# 
# https://docs.snowflake.com/ja/user-guide/data-load-s3-config-storage-integration.html#aws-access-control-requirements
locals {
  access = [
    "s3:GetBucketLocation",
    "s3:GetObject",
    "s3:GetObjectVersion",
    "s3:ListBucket",
  ]

  sql_action = [
    "s3:PutObject",
    "s3:DeleteObject",
  ]

  bucket_prefix = "snowflake"
}
