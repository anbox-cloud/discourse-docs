The Anbox Cloud Appliance is available through the AWS marketplace which simplifies the installation and deployment process and also allows billing directly handled through AWS. The following steps will guide you through all relevants steps to the Anbox Cloud Appliance deployed in your AWS account.

# Choose Instance Architecture

As a first step you have to decide if you're going to deploy the Anbox Cloud Appliance on an x86 or Arm instance type. AWS supports both and the decision should factor in the follow aspects:

* GPUs are currently available for x86. Nvidia GPUs will only become available for Arm instances [later in 2021](https://aws.amazon.com/blogs/machine-learning/aws-and-nvidia-to-bring-arm-based-instances-with-gpus-to-the-cloud/)
* Not all Android applications support the x86 ABI and therefor can only run on Arm

Once you have decided for an instance architecture, you can find the right marketplace page below:

* [Anbox Cloud Appliance for x86](https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4)
* [Anbox Cloud Appliance for Arm](https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk)

After subscribing to the marketplace product you can go and create an instance using the AMI and the [AWS EC2 wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html).

# Choose an Instance Type

AWS offers various instance types with different advantages. The Anbox Cloud Appliance images are only listed for a reasonable subset and as a next step you have to select the most suitable one for you're going to do. If you're just going to try the Anbox Cloud Appliance, choosing one with GPU support and less CPU and memory might be right.

![00_appiance-aws-instance-type|690x532](upload://AskBufPuBZg586bSaI6Eg39XGqy.png) 

In this example we picked the *g4dn.xlarge* which provides 4 vCPUs, 16 GB of memory and a singel NVIDIA Tesla T4 GPU.

# Configure Instance Details

For the instance details we don't have to customize any of the settings but you can to fine tune things. In some cases you may want to put the instance onto a different VPC or subnet. This can be configured at this stage of the instance creation process. 

![01_appliance_configure_instance|690x533](upload://pnZxItbD6stRmcpunjQxCOjqwfn.png) 

# Add Storage

Adding storage to the instance is important for the Anbox Cloud Instance to work correctly. The root disk should have at minimum 50 GB and for best performance you should create an additional EBS volume of at least 50 GB. The additional volume will be exclusively used by Anbox Cloud to store all of its containers. Using a separate volume isolates them from a performance perspective from the operating system. If no additional EBS volume is added, the Anbox Cloud Appliance will automatically create an image on the root disk which is then used to store all containers. It is recommended to always us a separate EBS volume.

![02_appliance_disk|690x533](upload://ztC8wxUxM4FFJXmXxz2ZKApNq5j.png) 

In this example we have `/dev/sda1` as the root disk with a size of 50 GB, an ephemeral `/dev/nvme0n1` disk (part of the g4dn instances), which will be ignored by the Anbox Cloud Appliance, and a second 100 GB sized EBS volume `/dev/sdb`. If you don't have any specific requirements, choosing the same configuration is recommended.

# Configure Security Group

To allow external access you need to open several ports in the security group attached to the AWS instance. The AMI already comes with the needed ones configured so you don't have to add them manually. For reference, all required ports are documented [here](https://discourse.ubuntu.com/t/requirements/17734).

![03_appliance_security_types|690x534](upload://9KG97kpHpVdvvMDIp7qdQFnO6zT.png) 

# Review and Launch

Now you have to review the instance configuration and if everything is correct, launch the instance. When the instance is successfully launched you can find it's public IP address in the instance details page and from there directly access the appliance at `https://<instance public IP address / DNS name>` which will show the following welcome page

![](https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/original/2X/f/f35744dc18ebf5b7f1d3a65788348bf0d9c1f443.png)

# Configure and Bootstrap

As last step we have to configure and bootstrap the Anbox Cloud Appliance. 

TBD: Link to what is currently on https://discourse.ubuntu.com/t/install-appliance/22681
