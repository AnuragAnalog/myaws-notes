# Dynamo DB

## Command Line Interface(CLI)

**Create a table**

```bash
aws dynamodb\
  create-table\
    --table-name PetInventory\
    --attribute-definitions\
      AttributeName=pet_species,AttributeType=S\
      AttributeName=pet_id,AttributeType=N\
    --key-schema\
      AttributeName=pet_species,KeyType=HASH\
      AttributeName=pet_id,KeyType=RANGE\
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