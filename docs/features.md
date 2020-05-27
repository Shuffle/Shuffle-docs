# Features 
Describes the features we already have or plan to build. 

There are two versions:
SaaS: [Shuffle Cloud](https://shuffler.io)
Open Source: [Shuffle onprem](https://github.com/frikky/shuffle)

These have slightly different features, with active development focused on the Open Source version for now.

# Table of contents
* [Introduction](#introduction)
* [Automation builder](#automation_builder)
* [App builder](#app_builder)
* [Default playbooks](#default_playbooks)
* [Open frameworks](#open_frameworks)
* [Automated compliance](#automated_compliance)

## Introduction
With the problems described in [our about page](/docs/about) in mind, these are some of the features we want to help solve. With part of our overall goal being to move the bottom part of the security industry into the upper echelon, a lot needs to be automated, but that's not enough. You also need to build working implementations, do staff training in the service itself,

To tackle these issues, we give you an Open Ecosystem, leveraging OpenAPI and Mitre Att&ck. With the use of OpenAPI, we hope that the rest of the community can join us in further specifying it for their services. Future looking services all specify this for their services, but IT and security companies seem to lack behind.

## Automation builder - workflows
Our automation builder is the tool that makes it all fit together. It gives you access to unlimited automation possibilities together with the [App builder](/apps/new), while also giving you an overview of bad and good automation options.

![Automation-builder](https://github.com/frikky/shuffle-docs/blob/master/assets/shuffle-workflow-1.png?raw=true)

## App builder
The app builder is a simple way to connect to another web service. It's based on OpenAPI and can therefore be shared among your colleagues simply, whether or not you choose to use Shuffle in the future. Your developers will love you for this in both the short and longrun. 

Our apps can also be built from scratch however. If you know how to code, or are interested in learning more, [please read on here](/docs/apps).

![App-builder](https://github.com/frikky/shuffle-docs/blob/master/assets/app-builder-example-1.png?raw=true)

## Default playbooks = compliance
Default playbooks give you access to start off the bat. Whether you just want to take the service for a spin or have a working implementation in mind, we want to support you usng these playbooks. To further develop your ecosystem, you can build custom ones (with the capabilities to do anything), use one playbook inside another playbook, which are also self-documenting.

Most of our playbooks will be defined based on Mitre Att&ck, and use the latest in threat hunting to make testing as easy as possible. With this in mind, we also build towards what kind of compliance requirements you might have.

[Playbooks](https://github.com/frikky/shuffle-workflows)

## Open frameworks
### OpenAPI
With OpenAPI in mind, we started building out Shuffle. OpenAPI is a specification used to standardize the way web services talk to each other. In other words, we already have thousands of integrations available, just not loaded for every user. [Contact us for more info](/docs/contact)

[Our definition](https://github.com/frikky/OpenAPI-security-definitions)

### Mitre Att&ck
With security being one of our specialities, we are building capabilities to leverage Mitre Att&ck to help with detection and hunting. It's hard to get started when the framework doesn't know anything about your environment.. But what if it did?

## Self documenting, reporting and compliance
Stuck manually giving information to your boss, your auditors or colleagues? Don't worry, we got it covered. We can quickly check whether you fill most or all the required complaince needs for your SOC. This can be anything from GDPR to PCI-DSS.

With OpenAPI, Mitre Att&ck and open playbooks, you have all the points necessary to fill any and all of your operations documentation requirements. 
