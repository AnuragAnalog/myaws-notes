# S3 to RDS MySQL via Lambda

## Services invloved
* S3
* RDS
* Lambda
* IAM

## Steps

### Setting up S3
1. Upload all the required files to the S3 bucket

### Setting up RDS
1. Create a RDS Instance
2. Make sure while creating RDS, you check public access button
3. Add one security group to inbound rules, to allow traffic from any IP address.

### Setting up IAM
> If you are not the root user, ask your admin to provide you with the access key and secret key, and skip the below steps.

1. Create a IAM user, with AmazonS3FullAccess and AmazonRDSFullAccess
2. Get the access key id and access secret key of that user and store it.

### Setting up Lambda
1. Create a lambda function
2. Set the environment variables in the configration tab with the access key and secret key.
3. Add two layers one is pandas and other is sqlalchemy.

> [How to add Pandas layer](https://www.youtube.com/watch?v=x9VT67dztpI), [How to add sqlalchemy layer](https://stackoverflow.com/questions/68189528/using-sqlalchemy-in-aws-lambda)

After setting up all the services, you can use the code from the file `load_s3tords.py` to load any csv file from s3 to rds.
