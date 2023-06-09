# AWS Notes

A repository which contains all the AWS Content which I have learned

## Setup

### CLI

Before running any of the cli commands to use the AWS resources, we need to first install and configure the AWS CLI.

You can find the installation instructions at [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### Python

To interactive with the aws, via python, you have to install `boto3`

```bash
$ pip3 install boto3
```

## Dynamo DB

### Command Line Interface(CLI)

**Create a table**

```bash
aws dynamodb\
  create-table\
    --table-name PetInventory\
    --attribute-definitions
      AttributeName=pet_species,AttributeType=S
      AttributeName=pet_id,AttributeType=N
    --key-schema
      AttributeName=pet_species,KeyType=HASH
      AttributeName=pet_id,KeyType=RANGE
    --billing-mode PAY_PER_REQUEST
```

**Describe a table**

```bash
aws dynamodb\
  describe-table\
    --table-name PetInventory
```

**List Tables**

```bash
aws dynamodb\
  list-tables
```

**Delete Table**

```bash
aws dynamodb\
  delete-table
    --table-name PetInventory
```
