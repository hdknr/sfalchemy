
# S3
module "s3" {
  source = "../modules/s3"
  symbol = local.symbol
  #
  dwh_account = local.dwh_account
}
