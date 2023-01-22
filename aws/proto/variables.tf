variable "region" {}
variable "project_name" {}
variable "profile" {}
variable "dwh_account_arn" {}
variable "dwh_account_id" {}


# https://www.terraform.io/docs/language/values/locals.html

locals {
  environment = "proto"
  symbol = {
    env     = local.environment
    service = var.project_name
    prefix  = "${var.project_name}-${local.environment}"
  }
  profile = var.profile
  dwh_account = {
    arn = var.dwh_account_arn
    id  = var.dwh_account_id
  }
}
