.. _howto_aar_deploy:

====================
How to deploy an AAR
====================

An :ref:`Anbox Application Registry (AAR) <exp_aar>`
should be deployed on a single unit. After deploying, continue to
:ref:`configure it <howto_aar_configure>`
and connect it with all AMS units that you want to synchronise.

Use the following commands to deploy an AAR:

::

   juju deploy cs:~anbox-charmers/aar
   juju config aar ua_token=<your UA token>

Using the AWS S3 storage backend
================================

The AAR has support for hosting application images on AWS S3.

When using the S3 storage backend, image downloads will be redirected to
S3 instead of being served directly by the AAR. The AAR will only be
asked for metadata by its clients.

Create and configure an S3 bucket
---------------------------------

To use the AWS S3 storage backend, you must create a dedicated S3 bucket
for the AAR first. See `Create your first S3 bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>`_
in the AWS documentation for instructions on how to do this.

If you don’t plan to use the :ref:`CloudFront CDN <howto_aar_deploy-cloudfront>`, you
should use a region close to your Anbox Cloud deployment to keep
download times low.

To allow the AAR to access the S3 bucket, create an
`IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>`_
user with the following policy:

.. code::

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

Replace ``aar0`` in the policy with the name of your bucket.

Once you created the IAM user, create an access key for the user, which
the AAR will use. See `Managing access keys for IAM users <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html>`_
in the AWS documentation for more details on this.

Finally, update the AAR configuration via the charm configuration:

.. code:: sh

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

.. _howto_aar_deploy-cloudfront:

AWS CloudFront CDN support
--------------------------

The distribution of the images can be highly improved by adding support
for the AWS CloudFront CDN, which brings the images closer to your Anbox
Cloud deployments in a more world wide context. The `AWS documentation <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html>`_
describes all necessary setup steps.

Once you have set up a CloudFront distribution for your S3 bucket, you
only need the base URL, public key and key pair ID to configure the AAR
to use CloudFront to serve image downloads.

Update the AAR configuration via the charm configuration:

.. code:: sh

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
