# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role
resource "aws_iam_role" "datastage" {
  name               = "${var.symbol.prefix}-role-datastage"
  assume_role_policy = data.aws_iam_policy_document.dwh.json
}

data "aws_iam_policy_document" "dwh" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "AWS"
      identifiers = [var.dwh_account.arn]
    }

    condition {
      test     = "StringEquals"
      variable = "sts:ExternalId"
      values = [
        var.dwh_account.id,
      ]
    }
  }
}


resource "aws_iam_role_policy_attachment" "datastage" {
  role       = aws_iam_role.datastage.name
  policy_arn = aws_iam_policy.datastage.arn
}
