# Glue

## Glue Crawler

**How to create a Glue Crawler**

* Create an S3 bucket to store the information which can be used by the crawler and store extracted data from the crawler.
* Head to the Glue page
* Under the crawlers section, click on **Add crawler**
    * Enter a name for the crawler
    * Select **Data stores** as the source type(In this case we are using S3)
    * Select **S3** as the data store
    * Select all the properties for your source.
* Now create an IAM role for the crawler
    * Click on the **IAM role** dropdown
    * Click on **Create new IAM role**
    * Enter a name for the role
* Now you need to configure the output destinations
    * Choose the target database
    * Create a new database or use an existing one
    * Next schedule the crawler
    * Review and Create Crawler
* Now run the crawler

After the crawler is run, you can see the tables in the tables section. The information, which is extracted from the crawler is stored in the S3 bucket which you created earlier. You can use S3 Select Query to query the data.

You can also use Athena to query the data.

## Glue Jobs

**How to Create a Glue Job**

Glue Studio provides a way to create a job with no or minimal coding.

* Head to the Glue page
* Click on ETL Jobs.
    * Select the Job type
    * Click Create
* Now you can see a visual representation of the job.
    * You can add sources, targets, and transforms to the job. (under visual tab)
    * You can view the script of the job. You can also customize the script based on your needs. (under script tab)
    * Provide your job details and IAM role. (under Job details tab)
        * For the IAM you need to create a role such that it has read and write permissions to the source and target.
        * Click on Create a Role
        * Select the Glue Service as the service that will use this role
        * Click on Next: Permissions
        * Select the pre-defined policy or create a custom policy (For all access you can select AdministratorAccess)
    * You can also give a few more settings like number of workers, number of retries and so on.
* Save our Job
* Run the Job
* You can check the run details under the Runs tab.

You can verify the output in the target location. (If S3 use S3 Select Query to query the data)

## Glue DataBrew

**How to preprocess using Glue DataBrew**

Glue DataBrew provides a way to preprocess the data without writing any code. It is a visual interface to perform data preparation tasks. It provides appromixately 250 transformations, like anomaly detection, data validation, data cleansing, data normalization, and so on.

* Head to the Glue DataBrew page
* Create the Dataset
    * Select the source(in our case it is S3)
    * Provide the link to the S3 bucket
    * Click on the **Create Dataset**
* Now we need to do a project
    * Click on **Create Project**
    * Enter a name for the project(it will also create a recipe with a similar name)
    * Select the dataset which you created earlier
    * Create a role for this project
        * Create an IAM role
    * Click on **Create Project**
