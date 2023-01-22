output "buckets" {
  value = {
    datastage = {
      bucket = aws_s3_bucket.datastage
      policy = aws_iam_policy.datastage
    }
  }
  sensitive = false
}
