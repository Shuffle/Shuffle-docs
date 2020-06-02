# API 
Documentation to understand the Shuffle architecture and thoughts behind choices. Important to understand if you want to contribute.

TBD: Add images, and describe architecture properly

# Table of contents
* [Introduction](#introduction)
* [Frameworks](#frameworks)
* [Technologies](#technologies)

## Introduction
With a long-term vision of having an Open(API) ecosystem that's that's a hybrid model between cloud and on-prem, this document will be a guide to understand some underlying aspects of Shuffle and how things fit together. 

## Frameworks
Shuffle uses existing, well established frameworks to help the Security community move forward, rather than just increase complexity. Here's a

* OpenAPI - Used to load and generate API specifications that's applicable for other platforms that just Shuffle. This is a standard that's widely used by almost every enterprise, but the security industry are lacking behind.
* Mitre Att&ck - Used to create general purpose workflows to make onboarding and usage as smooth as possible. Mitre Att&ck detections are directly proportional to risk, and can be used for KPI's to sell reasons for investment in the platform to leadership etc.

## Technologies
The fundamental building blocks of Shuffle are all designed to be modular Docker images, meaning they can run separately in different environments. The list below contains all the necessary parts execute a workflow. In case you want to contribute, I've added the programming languages as well.

The reason behind the usage of Golang is simple: Stability. Bash scripts and Python are prone to crashing, while Golang is fun, stable and easy to understand.

| Type | Technology | Note |
| ---- | ---------- | ---- |
| Frontend | ReactJS | Cytoscape graphs & Material design |
| Backend  | Golang | Rest API that connects all the different parts |
| Database | Google Datastore | Has all non-volatile information. Will probably move to elastic or similar. |
| Orborus  | Golang | Runs workers in a specific environment to connect locations |
| Worker   | Golang | Deploys Apps to run Actions defined in a workflow |
| app sdk  | Python | Used by Apps to talk to the backend |

## Architecture overview
