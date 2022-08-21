# Introduction
This document outlines how we work with our apps and workflows to develop easy-to-use workflows for our customers and users.

## Direction
The first thing to know is that we use Algolia as our search engine, which is where we will be managing our apps and workflows. 
The reason we use Algolia to handle this rather than our own database is to make sure we can reach everyone, including open source users.

The goal of this document is entirely to understand:
1. How the App Framework and Usecases fit together
2. What types of Workflows exist and how to build them
3. How to find the most relevant workflows to build
4. How to map the Workflows to the App in order to make the workflow building process easier for our users

![image](https://user-images.githubusercontent.com/5719530/185791408-f61249db-6ff8-4e43-99ee-c3559ef34b81.png)

## Focus
Our focus for the rest of 2022 will most likely be on the following App categories:
- Email (Comms)
- Cases
- EDR
- SIEM

This is to ensure we can handle "normal" data in a structured way.

## 1. How the App Framework and Usecases fit together
When going to the welcome pages (https://shuffler.io/welcome), you will be presented with questions about what tools you use. 

![image](https://user-images.githubusercontent.com/5719530/185791587-507ff603-0f6e-472e-a7cd-df8fb5082f55.png)

When setting these up, you end up selecting an app from our search engine Algolia. Example with email:
- 1. When selecting "Email", the popup shows up. In this popup, you should choose between a few apps that represent "Email" for you. These apps are sorted by a PRIORITY which we can decide within Algolia. Further: If a tool that SHOULD show up doesn't show up, then it may be wrongly categorized, which can also be [changed in our Algolia](https://github.com/Shuffle/Shuffle-docs/blob/master/handbook/engineering/editing_algolia.md)

![image](https://user-images.githubusercontent.com/5719530/185791650-b361e150-c695-4e5c-ab6f-a16d7e3727fa.png)

- 2. The app is added to the App framework for their organization. This means we can further recommend workflows and usecases for them.

![image](https://user-images.githubusercontent.com/5719530/185791974-3714803a-e5ee-4bfd-acbd-62eb32547fb0.png)



