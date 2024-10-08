# Local Data Cache - OT First Hands-on Experience
This repository contains configuration files and sample flows designed to simulate a simple OT (Operational Technology) environment.
The purpose is to provide hands-on experience with everyday tasks performed by an onsite operator, such as reading sensor values using Node-RED.

# For End Users
Youo can use this repository to quickly start visualizing OT in your factory without need of subscribing to external service to keep your data safe and agile. There's no need to install an operating system separately or configure services individually. Simply start using it and begin your digital transformation journey with an all-in-one solution.

# Repository Contents
* chemical-plant.yaml: Configuration files for the chemical plant simulator's virtual machine.
* metallb.yaml: Kubernetes LoadBalancer configuration for exposing services.
* node-red.yaml: Configuration files for deploying the Node-RED container.
* sample_flows.json: Sample Node-RED flow that can be imported into the Node-RED container to demonstrate typical sensor data flows.
* postgresql.yaml:
* grafana.yaml: 

# Purpose
This repository allows users to practice setting up and interacting with a simple OT environment. By following the provided configurations and using Node-RED, you will gain first-hand experience with:

Setting up basic OT configurations using tools like Node-RED.
Reading values from sensors and processing them.
Simulating real-world operational technology scenarios that onsite operators deal with daily.

# Getting Started
1. Clone this repository
2. Configure VECO and ECS to use this path as a repository source
3. Wait for all the components are deployed
4. Login to chemicalplant VM via console * not necessary if you demo only opc-ua
5. Update network settings to align with your environment * not necessary if you demo only opc-ua
6. Access node-red service, it should be available at port 31880 of your worker node e.g. http://192.168.50.200:31880
7. enjoy!

![image](https://github.com/user-attachments/assets/f8d24918-d1cd-4908-bf8c-b4657622af96)

![image](https://github.com/user-attachments/assets/6f93858c-f850-4157-9209-57b13812c182)

![image](https://github.com/user-attachments/assets/e81d7d67-017f-4721-8073-6cf4481995c2)

![Screenshot 2024-10-08 at 10 10 25](https://github.com/user-attachments/assets/37902981-6892-416d-9a65-f35819e73d05)
