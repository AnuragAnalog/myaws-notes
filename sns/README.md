# Simple Notification Service(SNS)

**How to create a simple sns**

Steps to create a simple sns which sends a email when a file is uploaded to a s3 bucket.

* Head to the SNS page
* Click on **Topics** on the left-hand side
    * Click on **Create topic**
    * Enter a name for the topic
    * Leave all the other options as default
* Click on **Create Subscription**
    * Select **Email** from the **Protocol** dropdown
    * Enter your email address in the **Endpoint** field
    * Go to your email and confirm the subscription
* Go to the Topic
    * Click on *Edit*
    * Go to the **Access Policy** section
      * ```json
        {
          "Version": "2012-10-17",
          "Id": "Policy1649527033453",
          "Statement": [
            {
              "Sid": "Stmt1649527028998",
              "Effect": "Allow",
              "Principal": "*",
              "Action": ["sns:Publish"],
              "Resource": ["arn:aws:sns:us-east-1:922925975910:S3PutEvent"]
            }
          ]
        }
        ```
    * Click on **Update policy**
* Go to the S3 bucket
    * Click on **Properties**
    * Click on **Create event notification**
    * Enter a name for the notification
    * Select **All object create events** from the **Events** dropdown
    * Select **SNS topic** from destination
    * Select the topic you created from the **SNS topic** dropdown
    * Click on **Save changes**