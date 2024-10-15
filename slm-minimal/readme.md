# LLM - First demo for LLM(Or SLM - Small Language Model)

This repository contains configuration files to deploy and demonstrate of minimal SLM in action at the edge

## Repository Contents

- **qwen2-llm.yaml**: container configuration of SLM, the model is qwe2-1.5b
- **llm-frontend.yaml**: SLM frontend application to provide GUI interaction for the users
- **ec-worker.yaml**: Since SLM requires decent amount of RAM, the worker node needs to be updated - 16-24GB should work fine as well

## What SLM(Small Language Model) means in manufacturing?

Traditional AI in manufacturing often relies on task-specific machine learning models that focus on individual functions like predictive maintenance, anomaly detection, or process optimization. These models are typically designed for narrow applications and require separate models for each task, which can be rigid and lack flexibility.

Small Language Models (SLMs), on the other hand, are more versatile. While smaller, they can handle various language-related tasks—such as interpreting operator commands, generating insights from reports, and facilitating human-machine interaction—within a single model. SLMs bring flexibility and adaptability to edge deployments, allowing manufacturers to streamline multiple tasks with a unified AI, reducing the need for separate, specialized systems.

## Getting Started

1. Clone this repository
2. Depending on the timing, the host restart might be required to reflect the changes made on ec-worker
3. Access the frontend via `http://<worker-node>:30850`
4. enjoy!

<img width="1023" alt="Screenshot 2024-10-15 at 9 47 20" src="https://github.com/user-attachments/assets/4dc78f2c-1fe2-4e31-84bc-6b291a096dd5">

<img width="1018" alt="Screenshot 2024-10-15 at 9 48 30" src="https://github.com/user-attachments/assets/bc495f9e-7a8b-4c1b-958b-16897e126410">

