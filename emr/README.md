# Elastic Map Reduce (EMR)

Let's create an EMR Cluster and submit a Spark job to it.

* Head to the EMR page
* Click on **Create cluster**
* Give a name to the cluster
* Select the **Spark** application in the software configuration
* Select the appropriate instance type
* Select the properties for the Security and Access
* Click on **Create cluster**

Once the cluster is created, you need to connect to the EC2 instance and submit the job. There are many ways, in which you can connect to the cluster and one of them is using SSH.
Follow the instructions mentioned under Master public DNS to connect to the cluster.

Before connecting to the cluster, we have to add port 22 to the security group, as that is a port, with which we are going to communicate with the cluster.

* Click on the *Security groups for Master* link under Security and Access section
* Click on the **Edit inbound rules** button
* Click on **Add rule**
* Select **SSH** in the type
* Select **Anywhere/your IP address** in the source

Connect to the cluster using the following command:

```bash
ssh -i <path to pem file> hadoop@<Master public DNS>
```

Once you are connected to the cluster, you can submit the job using the following command:

```bash
spark-submit <path to the python file>
```

**_Once everything is done, you can terminate the cluster by clicking on the Terminate button._**