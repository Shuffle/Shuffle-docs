# Shuffle Architecture
Documentation to understand the Shuffle architecture and thoughts behind our choices. Important to understand if you want to contribute.

# Table of contents
* [Introduction](#introduction)
* [Frameworks](#frameworks)
* [Technologies](#technologies)

## Introduction
With a long-term vision of having an Open(API) ecosystem that's that's a hybrid model between cloud and on-prem, this document will be a guide to understand some underlying aspects of Shuffle and how things fit together. 

## Architecture overview
![Architecture](https://github.com/frikky/shuffle-docs/blob/master/assets/shuffle_architecture.png?raw=true)

## Frameworks
Shuffle uses existing, well established frameworks to help the Security community move forward, rather than just increase complexity. 

* OpenAPI - Used to load and generate API specifications that's applicable for other platforms that just Shuffle. This is a standard that's widely used by almost every enterprise, but the security industry are lacking behind.
* Mitre Att&ck - Used to create general purpose workflows to make onboarding and usage as smooth as possible. Mitre Att&ck detections are directly proportional to risk, and can be used for KPI's to sell reasons for investment in the platform to leadership etc.
* Cytoscape - A light-weight and scalable design system, used for node relationships in our Workflow view. Cytoscape provides us all the necessary parts to create a fully functional workflows for any use. 

## Automation Engine
The Shuffle automation engine is entirely built from scratch, relying heavily on Docker. The code for decision making of next nodes can be found [here](https://github.com/frikky/Shuffle/blob/d77ae8260fd32691d8942dece1957915ba1ff3d5/backend/go-app/walkoff.go#L1251), while the SDK for how Apps perform can be found [here](https://github.com/frikky/Shuffle/blob/master/backend/app_sdk/app_base.py).  

## Technologies
The fundamental building blocks of Shuffle are all designed to be modular Docker images, meaning they can run separately in different environments. The list below contains all the necessary parts to execute a workflow. In case you want to contribute, we've added the programming languages as well.

The reason behind the usage of Golang is simple: Stability. Bash scripts and Python are prone to crashing, while Golang is fun, stable and easy to understand.

| Type | Technology | Note |
| ---- | ---------- | ---- |
| Frontend | ReactJS | Cytoscape graphs & Material design |
| Backend  | Golang | Rest API that connects all the different parts |
| Database | Opensearch | A scalable, NoSQL database used as document store of everything. |
| Orborus  | Golang | Runs workers in a specific environment to connect locations |
| Worker   | Golang | Deploys Apps to run Actions defined in a workflow |
| app sdk  | Python | Used by Apps to talk to the backend |

## Frontend

## Backend




