The Anbox Application Registry, or *AAR*, provides a central repository for applications created on Anbox Cloud.
It is very useful for larger deployments involving multiple regions in order to keep applications in sync.

## Deploying 

The Application Registry should be deployed on a single unit and connected with all `ams` units you want to synchronize.

```sh
$ juju deploy cs:~anbox-charmers/aar
$ juju config aar ua_token=<your UA token>
```

### Relating to AMS

The `aar` charm offers two principle relations: `client` and `publisher`.

 - `client` can hold many units. It only provides read only access
 - `publisher` can only be related to one `ams` unit. It provides read/write access

```sh
$ juju relate ams aar:publisher
```

For `ams` units deployed in another model, you can make use of [Juju cross model relations](https://juju.is/docs/cross-model-relations).

```sh
$ juju switch <model containing aar>
$ juju offer aar:client
my-controller/my-model.aar
$ juju switch <model containing ams>
$ juju relate ams my-controller/my-model.aar
```

### Using AWS S3 Storage Backend

The Application Registry has support to host images on AWS S3.
Next to that distribution of the images can be highly improved with additional support for the AWS CloudFront CDN.

When using the S3 storage backend image downloads will be redirect to S3 instead of being served by the registry.
The registry will be only asked for metadata by its clients.

##### Create and Configure a S3 bucket
You need to create a dedicated S3 bucket for the registry first. See the AWS documentation for more details on
this [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

If you don’t plan to use the CloudFront CDN you should use a region close to your Anbox Cloud deployment to keep download times low.

To allow the registry to access the S3 bucket you need to create an [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
user with the following policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketMultipartUploads",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::aar0"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::aar0/*"
        }
    ]
}
```

Replace `aar0` in the policy with the name of your bucket.

Once you created the IAM user you need to create an access key for the user which the registry will use.
See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for more details on this.

Finally you can update the registry configuration with the charm configuration:

```sh
$ cat config.yaml
aar:
  storage_config: |
    storage:
      s3:
        region: eu-west-3
        bucket: aar0
        access-key: <your access key>
        secret-access-key: <your secret access key>
juju config aar -f config.yaml
```

### AWS CloudFront CDN support

To bring the images closer to your Anbox Cloud deployments in a more world wide context you can use the AWS CloudFront CDN.
The [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html) describes all necessary setup steps.

Once you have setup a CloudFront distribution for your S3 bucket you only need the base URL, public key and key pair
id in order to configure the registry to use CloudFront to serve image downloads.

The registry configuration can now be updated via the charm configuration:

```sh
$ cat config.yaml
aar:
  storage_config: |
    storage:
      s3:
        region: eu-west-3
        bucket: aar0
        access-key: <your access key>
        secret-access-key: <your secret access key>
        cloudfront:
          base-url: d1dfsdfjmcefekdotjm.cloudfront.net
          private-key: |
            -----BEGIN RSA PRIVATE KEY-----
            ...
            -----END RSA PRIVATE KEY-----
          keypair-id: ADF443JOEF3423JF
          duration: 1m
$ juju config aar -f config.yaml
```
### Next Steps

* [Application Registry](https://discourse.ubuntu.com/t/installation-application-registry/17749)
