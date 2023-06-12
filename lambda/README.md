# AWS Lambda

**How to create a sample lambda function**

Before the start of this process, you need to perform a few things, They are:

* Create an S3 bucket and upload a sample file to it.
* Create a dynamodb table
* Create an IAM role with the following permissions:
    * AWSLambdaBasicExecutionRole
    * AmazonDynamoDBFullAccess
    * AmazonS3FullAccess
    * Also a custom policy called lambda_csv_reader with the following permissions:
    * ```json
    {
        "version": "2012-10-17",
        "statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "cloudwatch:*",
                    "s3:*",
                    "dynamodb:*"
                ],
                "Resource": "*"
            }
        ]
    }
    ```


* Head to the Lambda page
* Click on **Create function**
* Select **Author from scratch**
* Enter the function name
* Select the runtime as **Python 3.9**
* Select the IAM role that you have created
* Click on **Create function**

* Under the Code tab, you can see the code editor, where you can place from the file csv2table.py
* Click on deploy to deploy the function

As it is a serverless application, we need to create a trigger to invoke the function. Here, we are going to use S3 as the trigger.

* Select the PUT event, as the trigger.
* Give the suffix as .csv, to only invoke the function when a csv file is uploaded to the bucket.
* Click on **Add**, to create the trigger.
