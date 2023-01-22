# https://www.terraform.io/language/modules/develop/providers
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.72.0"
    }
  }
}
