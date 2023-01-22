provider "aws" {
  # デフォルト
  region  = var.region
  profile = local.profile

  default_tags {
    tags = {
      terraform                        = "True"
      "${local.symbol.service}-deploy" = "${local.symbol.env}"
    }
  }
}


