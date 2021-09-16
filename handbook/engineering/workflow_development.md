# Workflow Development
This document outlines a process for workflow development in Shuffle. 

## Introduction
Workflows are at the core of Shuffle, together with apps. Workflows attach App actions together, ensuring we can perform actions between platforms. Apps themselves can handle a single tool, while Workflows makes them work as a team. The end goal of most workflows is a fully automated service, starting with a trigger, followed by actions that perform actions according to your need. The typical starting points are from Webhooks (external system -> Shuffle) and Schedules (polling for information).

## Documentation sources
* [Workflow documentation](https://shuffler.io/docs/workflows)
* [Shuffle Architecture](https://shuffler.io/docs/architecture)
* [Shuffle Extensions](https://shuffler.io/docs/extensions)
* [App creation with Shuffle](https://shuffler.io/docs/app_creation)

## Basic Process
1. Define the goal of the Workflow.
	- What's the overarching goal?
	- What actions are needed?
	- What tools, and kind of tools are in use?
2. Identify ways to standardize
	- Can any parts be standardized as subflows? E.g. IP and URL lookups
	- e.g. Analyzing an email - can it handle .MSG and .EML
3. Document what the Workflow is supposed to do. What's the end goal from step 1? 
4. Start building! Build out the Workflow step by step, and remember to test ALL THE TIME. Some tips:
	- Start with authentication. Can you connect the tool(s) at all? If not, ask for help, as we may need to further develop and app.
	- Find the action(s), and ensure you get the information you REALLY need from an app before connecting it to another one.
	- Check if you need any kind of text-formatting or conditions. Remember that [liquid formatting](https://shopify.github.io/liquid/filters/size/) exists with lots of filters..
	- Don't use triggers before step 5 (debugging). Instead, get the information you expect, and run it manually with the execution arguments.
	- If you want to re-use the same execution argument, click the "Rerun Workflow" instead of playing it again.
5. Debug and test! Identify potential issues with the Workflow.
	- Send in random data 					- does it behave the same?
	- Disconnect from the internet 	- does it fail as expected?
	- Set CLEANUP=True for Orborus 	- does it behave the same?
	- Run it with trigger(s) 				- does it behave the same?
	- Run it with the same data 50 times REALLY fast - does it ever crash/fail?
	- Does it require a default return value?
6. Production readiness! Ensure it works in production before sharing.
	- Write a description and tags. What is the goal of the Workflow? Is it a part of preparration or response? Are there specific Mitre Att&ck techniqeus attached?
	- Are all the apps running the latest version?
	- Run it locally for a while. Does it ever fail? If so; why?
	- Talk to others: can any part of it be improved? E.g. reducing the amount of nodes, or improving the text provided to analysts.
7. Release!
	- Share the workflow with the community. Share the workflow with the community by clicking "Publish Workflow". This will automatically clean up authentication and certain fields, before putting it in our searchable Workflows, and sharing information Discord, Twitter and other social media platforms. 
	- Publish the Workflow(s) on [Github](github.com/frikky/shuffle-workflows)

## What happens next?
Someone from the Shuffle team will validate the Workflow you submitted and accept it. More about how we do testing can be found in our  [testing documentation](https://github.com/frikky/shuffle-docs/blob/master/handbook/engineering/testing.md).

## Workflow Credits
We want YOU to get the credits for what you create and celebrate you. This means you'll be highlighted when the workflow is published on shuffler.io as well as on Github (if you want). This can be down to the granular level of "actions". This will long-term be reflected with your user on Github/Shuffler.io.

## Learnings
TBD
