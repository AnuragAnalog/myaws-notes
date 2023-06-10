# Simple Storage Service(S3)

**Host a Static Website in S3**

Steps to host a static website in S3

* Login to AWS Console
* Create a S3 bucket
  while creating a bucket, you need to follow these steps
  * Select a bucket name(the bucket name should be unique in the selected region)
  * Select a region
  * Object Lock should be always in the disabled state
  * Uncheck the block all public access checkbox
  * Click on Create bucket
* Go to the bucket
  * Upload all the necessary files to the bucket
  * Set the default permissions and properties for the files
  * Review the settings and click on upload
* Go to the bucket properties
  * Click on static website hosting
  * Select the Use this bucket to host a website Option
  * Enter the index.html file name
  * Enter the error.html file name
  * Click on save
* Go to the Bucket Permissions
  * Under the Bucket Policy, click on the Edit button
  * Copy the below code and paste it in the Bucket Policy editor
  * Click on save
  * ```json
    {
      "Version": "2012*10*17",
      "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": ["s3:GetObject"],
          "Resource": ["arn:aws:s3:::<Bucket-Name>/*"]
        }
      ]
    }
    ```
* Go to the bucket Overview
  * Click on the Actions dropdown
  * Select the Make Public option
  * Click on Make public

You can get the link to the website by clicking on the index.html file in the bucket