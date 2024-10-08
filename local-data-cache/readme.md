# Local Data Cache - OT First Hands-on Experience
This repository contains configuration files and sample flows designed to simulate a simple OT (Operational Technology) environment.
The purpose is to provide hands-on experience with everyday tasks performed by an onsite operator, such as reading sensor values using Node-RED.

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
2. Modify address allocation at the last line of metallb.yaml to align with your environment, this is used to expose node-red service available to you
3. Configure VECO and ECS to use this path as a repository source
4. Wait for all the components are deployed
5. Login to chemicalplant VM via console
6. Update network settings to align with your environment
7. Access node-red service, it should be available within the address range you specified at step 2 at port 1880 e.g. http://192.168.50.240:1880
8. You can refer preconfigured flow into node-red by importing sample_flow.json provided in the same repository. You will most likely need to change the ip address within the sample flow.
9. enjoy!

![image](https://github.com/user-attachments/assets/f8d24918-d1cd-4908-bf8c-b4657622af96)

![image](https://github.com/user-attachments/assets/6f93858c-f850-4157-9209-57b13812c182)

![image](https://github.com/user-attachments/assets/e81d7d67-017f-4721-8073-6cf4481995c2)

![Screenshot 2024-10-08 at 10 10 25](https://github.com/user-attachments/assets/37902981-6892-416d-9a65-f35819e73d05)
