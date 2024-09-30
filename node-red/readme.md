# NODE-RED - OT First Hands-on Experience

This repository contains configuration files and sample flows designed to simulate a simple OT (Operational Technology) environment. The purpose is to provide hands-on experience with everyday tasks performed by an onsite operator, such as reading sensor values using Node-RED. 

## Repository Contents

- **chemical-plant.yaml**: Configuration files for the chemical plant simulator's virtual machine.
- **metallb.yaml**: Kubernetes LoadBalancer configuration for exposing services.
- **node-red.yaml**: Configuration files for deploying the Node-RED container.
- **sample_flows.json**: Sample Node-RED flow that can be imported into the Node-RED container to demonstrate typical sensor data flows.

## Purpose

This repository allows users to practice setting up and interacting with a simple OT environment. By following the provided configurations and using Node-RED, you will gain first-hand experience with: 
- Setting up basic OT configurations using tools like Node-RED.
- Reading values from sensors and processing them.
- Simulating real-world operational technology scenarios that onsite operators deal with daily.

## Getting Started

1. Clone this repository
2. Modify address allocation at the last line of `metallb.yaml` to align with your environment, this is used to expose `node-red` service available to you
3. Configure VECO and ECS to use this path as a repository source
4. Wait for all the components are deployed
5. Login to `chemicalplant` VM via console
6. Update network settings to align with your environment
7. Access `node-red` service, it should be available within the address range you specified at step 2 at port 1880 e.g. http://192.168.50.240:1880
8. You can refer preconfigured flow into node-red by importing `sample_flow.json` provided in the same repository
9. enjoy!

![image](https://github.com/user-attachments/assets/b4c0b423-214a-4419-a2a2-3f2c231a8696)



![image](https://github.com/user-attachments/assets/16763531-f3e0-438d-a642-cee32df5d3d1)


