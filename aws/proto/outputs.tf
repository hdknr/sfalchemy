output "s3_buckets" {
  sensitive = true
  value     = module.s3.buckets
}

