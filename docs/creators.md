# Creators 
Documentation for everything about creators. Become a creator by [signing up here](https://shuffler.io/creators) and join the [Discord community here](https://discord.com/invite/B2CBzUm)

![image](https://user-images.githubusercontent.com/5719530/187564027-0ec68080-82bd-44ac-972f-cb7f85b8c0ad.png)

## Table of contents
* [Introduction](#introduction)
* [FAQ](#FAQ)
* [Become a creator](#become_a_creator)
	* [Your Creator Profile](#your_creator_profile)
	* [Get verified](#get_verified)
	* [Verified perks](#verified_perks)

## Introduction
The Shuffle ecosystem is built on open source code, and since the start, we've focused on openness and building as good a service as we can. We do however know that we don't know everything, and need help from the community to create as good of a service for our customers as possible. That's why we've launched the creator program - a way we can share revenue with everyone who spend time helping Shuffle grow by creating content like Apps, Workflows and Documentation, along with Blogposts, videos and who do support and github contributions.

We will share 5% of our revenue in the calendar year of 2023.

## FAQ
You can see our interactive Creator FAQ on the [creator pages](https://shuffler.io/creators#faq).

## What you need to know
There are no specific prerequisites to become a Creator, but we encourage you to at least [know how to build Workflows](/docs/workflows#what-you-need-to-know). 

## Become a creator
The first thing necessary to become a creator is to sign up to the Shuffle platform. These are the requirements:
- A [Shuffle account](https://shuffler.io/register?message=Sign up%20to%20become%20a%20creator)
- A [Github account](https://github.com)
- A [Discord account](https://discord.com/invite/B2CBzUm) (required to get Verified)

With these in place, you can go to the [Creator](/creators) pages and sign up! It only takes a minute. In order to get verified, you will further have to provide your First Name and Last name, along with other optional information.

## Your Creator Profile 
What and how you can change, what people are interested in, what you can earn from, how it's calculated, where dashboards are....
TBD

## Get verified
To earn with Shuffle, you need to get verified. This is a manual process, as we need certain information in order to transfer money to you. 

**Qualifications**
- Must have published 5 Workflows in the last 3 months
- Must have chosen at least 5 [Specialized apps](#specialized_apps)
- Must have provided us with your Firstname and Lastname
- Set up a [Github sponsors](https://github.com/sponsors/accounts) account. We will use this for payouts.

If you feel ready to get verified, send us an email at [support@shuffler.io](mailto:support@shuffler.io?subject=Become%20a%20Verified%20Creator). This process will be fully automated in the future.

## Verified perks
As a verified Creator, you get access to more information. We share with you the following:
- A monthly update on how your apps, workflows and other content is doing
- We provide suggestions for what to do next
- A dashboard with information about being verified
- We provide you with full visibility into searches, clicks and conversions for all apps and workflows within Shuffle

## What to share
You can build and share anything that may be relevant to other users. The focus is on Workflows and Apps, but the following are also a part of earning with Shuffle:
- Support tickets
- Github contributions
- Articles & Blogposts
- Videos

Our goal with Shuffle as a platform is to help you earn and get reach for your workflows and apps, along with other content, such as Blogs, Articles, and Videos. The normal starting point is with building Workflows and Apps, then releasing them.

- [Building Workflows](/docs/workflows#workflow_basics)
- [Building Apps](/docs/apps#workflow_basics)

## Correct information 
It's important that content shared through Shuffle has sufficient information, as to help other users find what they're looking for. The search engine is always the starting point, and it's up to you to discoverable.

![image](https://user-images.githubusercontent.com/5719530/187629553-bbc97b43-8d61-44f2-ab73-cbe8ad6a0ad4.png)

## Workflow Release
[![Publishing Workflows and New Workflow Types](https://user-images.githubusercontent.com/5719530/187566365-ebc054bc-393b-439f-9649-76df707c581b.png)](https://www.loom.com/embed/4f9ee793e4fd4c9fbdc040d37d0309a4)

After [releasing a workflow](https://github.com/Shuffle/Shuffle-docs/blob/8e4e7bbe2ce5a4ee86c8aed9e7c80a9d9ab9cd17/handbook/engineering/workflow_release_process.md), this happens:

1. We send a notification to Shuffle's team to verify the Workflow
2. We release sensitive content that maybe shouldn't be there, or any "test" nodes.
3. Your Creator user gets assigned as the owner of the Workflow. This means you can edit the workflow. You can find your creator user [on the creator pages](https://shuffler.io/creators). From here, you can find the Workflow in the "Workflows" tab, or you can search for it in the search engine. 

![image](https://user-images.githubusercontent.com/5719530/187559714-1b0f5b8c-95ce-490b-bc7e-d95a9bac3bab.png)

4. When inside a Workflow you own, and which is public, you will see the buttons for jumping to the Workflow Editor in the bottom left of your screen. By clicking "Edit Workflow", you will have full access to modifying the Workflow the work the best for other users. You can also test it. Make sure it doesn't contain any sensitive information.
![image](https://user-images.githubusercontent.com/5719530/187559912-591943bc-5200-45fd-98a7-dd4a4c640ef3.png)

5. By clicking the "Edit" button on the bottom bar, you can make further changes to the workflow. This is the most important information, and is where you should make sure to fill out all significant fields. This also means to link to related documentation, blogposts and other info.

![image](https://user-images.githubusercontent.com/5719530/187560076-45e0dca8-c6ed-4015-810a-466e37d36ff6.png)

6. To make sure you get maximum impact, both in our search engine's priority system, along with on Google and other search engines, make sure to AT LEAST have these fields filled out extensively:
- Name 
- Description
- Tags
- Type (If you don't know, choose "Standalone")
- Usecase

Additionally, if the workflow's type is "Subflow", make sure to add relevant return values in case of failure to the "Default return value" field.

### Publishing subflows and trigger-workflows
Trigger workflows are workflows that act as "Triggers" for a specific App. The goal with trigger workflows is to get specific information from an App, then hand it over to a Subflow. Subflows are Workflows that receive some "Standard" inforamtion, using our [Standardized Data scripts](https://github.com/Shuffle/python-apps/blob/4ba237a8d9483b34d1a3de83c16920dc9dde502a/shuffle-tools/1.2.0/src/app.py#L2270). Trigger and Subflows exist to help all users build and experience workflows faster, by acting as templates that Shuffle itself as a platform can stitch together. 

A good example of this is Email. A typical usecase is "When I get an email, enrich it and send it to a ticketing system". This is then split into two main sections, and a last section for enrichment:

1. A trigger worfklow: "When I get an email"
2. A subflow: "Send it to the ticketing system"
3. A subflow system for enrichment: "enrich it"

Here's how the baseline looks before you can modify it:
![image](https://user-images.githubusercontent.com/5719530/187560930-d33ea7bd-1691-4dc3-83a4-a427f0ca3fe4.png)

After it's been modified, it will automatically grab relevant apps from the App Framework. [More about that here](https://github.com/Shuffle/Shuffle-docs/blob/master/handbook/engineering/usecase_mapping.md).

![image](https://user-images.githubusercontent.com/5719530/187562470-032245db-7185-4cf7-bc06-1a4dc72e4188.png)

### Trigger Workflows
Trigger workflows start something for an app. A good example is to get new emails and sending them to a subflow ("When I get an email"). They are defined by a few key pieces:
- They start from a trigger (Schedule, Webhook, Email)
- They end with a subflow to run in the next workflow

### Subflows
Subflows are workflows that receive some data from a Trigger workflow. They use [Standardized Data scripts](https://github.com/Shuffle/python-apps/blob/4ba237a8d9483b34d1a3de83c16920dc9dde502a/shuffle-tools/1.2.0/src/app.py#L2270) to get data in the same format every time. They are defined by:
- Always start with standardized data, or with the first node being standardized data
- Does not have its own trigger. Should be triggered AS A SUBFLOW


## Workflow types

## Release Workflows
TBD

## Release Apps
TBD

## Track Workflows and Apps
TBD

## Tips and Tricks
TBD

