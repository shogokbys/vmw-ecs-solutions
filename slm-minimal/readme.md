# LLM - First demo for LLM(Or SLM - Small Language Model)

This repository contains configuration files to deploy and demonstrate of minimal SLM in action at the edge

## Repository Contents

- **qwen2-llm.yaml.yaml**: container configuration of SLM, the model is qwe2-1.5b
- **llm-frontend.yaml**: SLM frontend application to provide GUI interaction for the users
- **ec-worker.yaml**: Since SLM requires decent amount of RAM, the worker node needs to be updated - 16-24GB should work fine as well

## Purpose

## Getting Started

1. Clone this repository
2. Depending on the timing, the host restart might be required to reflect the changes made on ec-worker
3. Access the frontend via http://<worker-node>:30850
4. enjoy!


