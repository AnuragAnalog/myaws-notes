# SageMaker

* It is a fully managed jupyter notebook service. It also comes with an EC2 and EBS instances, which are not going to be shown in the console. The dataset, which we store in the EBS volumes is persistent and will not be deleted even if the notebook instance is stopped.

## Required modules

* sagemaker - It is a library that is used to interact with all the Sagemaker Services.
* boto3 - It is a library that is used to interact with all the AWS Services.

## Required functions

Here are some of the required functions which are used from the **sagemaker** library.

* sagemaker.get_execution_role() - It is used to get the role of the notebook instance.
* sagemeker.Session() - It is used to get the session of the notebook instance.
    * sagemaker.Session().default_bucket() - It is used to get the default bucket of the notebook instance.

**Upload a file into the S3 using the boto3**

```python
import boto3

s3 = boto3.Session().resource('s3')
s3.Bucket('<bucket_name>').Object('<file_name>').upload_file('<file_path>')
```

**Download a file from the S3 using the boto3**

```python
import boto3

s3 = boto3.Client('s3')
s3.download_file('<bucket_name>', '<file_name>', '<file_path>')
```

**Get a Model container from the Sagemaker**

```python
from sagemaker import get_image_uris

container = get_image_uris.retrieve('<algo-name>', boto3.Session().region_name, '<Version>')
```

**Create a pointer that points to the S3 location**
    
```python
s3_input = TrainingInput(
    s3_data="s3://{}/{}/train".format(bucket, prefix), content_type="csv"
)
```