# Resource: aws_s3_bucket
# - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
resource "aws_s3_bucket" "datastage" {
  bucket = "${var.symbol.prefix}-datastage"
  versioning {
    enabled = true
  }
}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy
resource "aws_iam_policy" "datastage" {
  name   = "${var.symbol.prefix}-s3-datastage"
  policy = data.aws_iam_policy_document.datastage.json
}


# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document
data "aws_iam_policy_document" "datastage" {
  statement {
    actions   = local.access
    resources = ["${aws_s3_bucket.datastage.arn}/${local.bucket_prefix}/*"]
  }
  statement {
    actions   = local.sql_action
    resources = [aws_s3_bucket.datastage.arn, "${aws_s3_bucket.datastage.arn}/*"]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"
      values = [
        "${local.bucket_prefix}/*",
      ]
    }
  }
}

