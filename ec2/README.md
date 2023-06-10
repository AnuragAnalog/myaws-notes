# Elastic Compute Cloud(EC2)

**Host a Website in EC2 Instance**

Steps to host a website in EC2 Instance

* Login to AWS Console
* Create an EC2 Instance

  * Click on Launch Instance
  * Give a name to it(may not be unique)
  * Select the OS(preferrably Amazon Linuz as it is in free tier)
  * Select the 64bit option and Amazon 2 AMI
  * Select the t2.micro instance type(free tier)
  * Create a Key-pair to login to the instance
  * Default the network and configure storage options
  * Click on Review and Launch
    > It will take a couple of minutes to launch the instance, instance state should be running and status checks should be 2/2 checks passed

* Connect to the instance

  * Click on the Connect button
  * Select the EC2 Instance Connect option
  * Click on the Connect button
  * It will open a new tab in the browser(connecting to the instance)

* Get all the files

  * Now, you get a prompt of the instance
  * Run the below commands
  ```bash
  $sudo su - # to get the root access
  $yum update -y # to update the packages
  $yum install httpd -y # to install the apache server
  $systemctl start httpd # to start the apache server
  $systemctl enable httpd # to enable the apache server
  ```
  * Get the files using git or wget
  * place the files in the /var/www/html directory

* Modify the security group
  * Go to the EC2 details page
  * Click on the Security Groups
  * Click on the Inbound Rules
  * Click on the Edit button
  * Click on Add Rule
  * Select the HTTP/HTTPS option
  * Select the Anywhere option under the Source
  * Click on Save Rules