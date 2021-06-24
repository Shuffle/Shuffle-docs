# Triggers
Documentation for triggers, running workflow executions

# Table of contents
* [Introduction](#introduction)
* [About](#about)
* [Webhook](#webhook)
* [Shuffle Subflow](#subflow)
* [Schedule](#schedule)
* [User Input](#user_input)
* [Email](#email)

## Introduction
Triggers are the operators used to execute a [workflow](/docs/workflow) automatically. They are connected to a actions within workflows - often the starting node. Triggers usually take an execution argument that will be used to execute the workflow in question.

This image shows a simple workflow with two triggers: Webhook & Scheduler. 
![logos-triggers](https://github.com/frikky/shuffle-docs/blob/master/assets/logos-triggers.png?raw=true)

## About
Triggers, along side apps and variables, can be found on the left hand side, in a tab called "Triggers". 

![Triggers-view-1](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-1.png?raw=true)

Triggers are developed for and by Shuffle specifically to give the user access to multiple ways to run a workflow. There are currently five ways to execute workflows:

* Cloud: Webhook, User Input, Schedule, Email, Rest API
* Onprem: Webhook, User Input, Schedule, Rest API

There are currently four triggers, with a fifth "hidden" one:
* Webhook 		- Handle realtime HTTP requests from anywhere. 
* Schedule 		- Runs your workflow on a schedule. Cronjob or seconds.
* User Input 	- Waits for user input before continuing. You can answer yes/no.
* Rest API 		- Essentially a trigger from either: 1. Another workflow. 2. Any third party software

Cloud only:
* Email 			- 23.05.2020: Can listen to office365 incoming mails

### Webhook
[Webhooks](https://en.wikipedia.org/wiki/Webhook) is the real-time handler for Shuffle data. Webhooks were initially implemented to handle data from [Office365 connectors](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/connectors/connectors-using) and [TheHive](https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md), but turned into a generic trigger as we saw the use-case for it. 

HTTP Method(s):
* POST

PS: Data in the POST request will be the execution argument.

#### Authentication
In later versions of Shuffle, you further have access to an authentication field. This field is based on the headers of the request, and any header added to this field will be **REQUIRED** from the sender of the webhook.

One header for each line. In the image below, the request would need to contain the headers "authorization" and "authorization2" with the exact valus specified.
![Triggers-view-6](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-6.png?raw=true)

#### Webhook Example
To start using webhooks, you should have a service that supports webhooks (e.g. the two above mentioned). If you just want to test, you can also use cron.

Once you have a service ready:
1. Drag the "Webhook" trigger from the left hand side into the main view, and you should see it automatically connect to your starting node. 
2. Click "start" to deploy this webhook (it might be auto-started). This will also be stopped if you remove the node or the workflow. A webhook can not be in multiple workflows, but you can deploy as many as you want.
3. Find your webhook URI in the "Webhook URI" window, and copy it to your service

![Triggers-view-2](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-2.png?raw=true)

Test it! Say your URI is: https://shuffler.io/functions/webhooks/webhook_336a7aa2-e785-47cc-85f4-31a4ab5b28b8 and you want to use {"test": "testing"} in your workflow:
```bash
curl -XPOST https://shuffler.io/functions/webhooks/webhook_336a7aa2-e785-47cc-85f4-31a4ab5b28b8 --data '{"test": "testing"}'
```

### Subflow 
Subflows is a trigger made to run workflows within other workflows. There's further a "parent/child" element to it where there's always a reference to where the execution came from. This can also run a subflow within itself or be recursive (infinite loops).

Purposes we'll cover:
* Create standard workflows that can be used within other workflows. E.g. checking an IoC in a standardized way every time.
* Handle loops well. This is to avoid multiple nested for-loops and instead make a new workflow to handle it. E.g. list of emails with list of attachments with list of sub-attachments (e.g. Zip).

Requirements:
* shuffle-subflow app. This is automatically installed.

[Here are the known missing features for subflows](https://github.com/frikky/Shuffle/issues/223)

#### Extra subflow information 
- Subflows can be in the same Workflow. When selecting, it will show up as red.

![Triggers-subflow-7](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-7.png?raw=true)

- Parent nodes of the subflow trigger show up as red. When using these, make sure you stop the workflow. We will add a warning for this, as it can run you out of resources easily.

![Triggers-subflow-8](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-8.png?raw=true)

- After choosing a subflow - if you right-click the subflow node in the workflow UI, it will import the subflow. When saving, this will NOT be a part of the workflow. 
- PS: We will make this part of the workflow visual and non-interactive at a later stage.

![Triggers-subflow-9](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-9.png?raw=true)

#### Subflow Example
1. Drag a subflow into the PARENT view from the left side and click it
![Triggers-subflow-1](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-1.png?raw=true)

2. Choose a workflow to run. This will use the STARTNODE as default, which can be changed. The red workflow is the one you're currently working on.
![Triggers-subflow-2](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-2.png?raw=true)

3. We'll decide a startnode and the information to send to the subflow. In our case, we'll use the list below, and send one item at a time with the IP to be searched for in Virustotal. The data with the list is named Repeat_list in our case, hence we use $Repeat_list.#
```
[{"ip": "1.2.3.4", "malicious": true}, {"ip": "4.3.2.1", "malicious": false}, {"ip": "1.2.3.5", "malicious": true}]
```
![Triggers-subflow-3](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-3.png?raw=true)

4. It's time we explore the results. In total, this should execute FOUR times: 1 for the first workflow and once for EACH of the objects in the list.
![Triggers-subflow-4](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-4.png?raw=true)

5. Here's a view of the total workflows. Notice how three of them have a different icon? This is because they are subflows. PS: It will always show the maximum amount of nodes in the workflow, whether it's a subflow or not.
![Triggers-subflow-5](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-5.png?raw=true)

6. Exploring the subflows, we find that the IP's have been searched for in Virustotal, and that we have a reference to the parent. Clicking the reference will take you to the parent execution.
![Triggers-subflow-6](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-subflow-6.png?raw=true)


### Schedule 
**On-prem**
Schedules on-prem are ran on the webserver itself. Rather than cron, it uses a scheduler that runs it every X seconds. This will become more sophisticated over time. Schedules persists in the database even when you turn off Shuffle, so don't be afraid to update.

**Cloud**
Schedules are based on [google's cloud scheduler](https://cloud.google.com/scheduler/) and are schedules that run based on [cron](https://en.wikipedia.org/wiki/Cron). It takes two arguments - the schedule you want to run it on and the Execution argument used in the workflow. A simple cron converter can be found [here](https://en.wikipedia.org/wiki/Cron). When you are ready to run, click "start". 

#### Schedule Example
1. Drag a schedule into the view from the left side
2. Click the schedule
3. Type in the amount of seconds between execution (down to every 1 second)
4. Type the execution argument you want to execute with. This can be used by actions.
5. Click "Start"

![Triggers-view-3](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-3.png?raw=true)

### User input
The user input node is a way to temporarily pause an execution until someone MANUALLY clicks something. This can currently be through Email and SMS, but we will introduce many other options, including chat systems and running other workflows.

The point of the node is to wait for manual approval before running some automation. E.g. management approval for new scan schedule. E.g. analyst approval for cleanup up a host. 

![User input node Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-4.png?raw=true)

* Email		- What emails do you want to send the workflow information to?
* SMS 		- What numbers do you want to send the workflow information to?

When the email/sms is sent, it will look like the image below. We will optimize this over time to reflect everything from Shuffle, but during our initial proof of concept, this is for you to understand. You will get to answer: yes or no? If you answer yes, the workflow execution will continue from where it left off. If you answer no, it will be stopped. This action can be sent to multiple people, but the link will only work once.
![User input email Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/triggers-view-5.png?raw=true)

### Email
TBD: This has been made to work with both cloud and hybrid version of Shuffle. Can't work 100% onprem because webhooks from Office365 and Google Workspaces can't reach your host.
