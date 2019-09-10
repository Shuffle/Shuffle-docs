# Triggers
Documentation for triggers, running workflow executions

# Table of contents
* [Introduction](#introduction)
* [How they work](#howtheywork)
* [Development](#development)
* [API](#api)

## Introduction
Triggers are the cloud operators used to run a [workflow](/docs/workflow) execution. They are (for now) always connected to the starting node of the workflow, and will execute based on a few perimeteres. An example trigger is the Scheduler, which gives you the option to schedule when to run a workflow. Triggers usually have a field to specify what data to put execute the workflow with. 

![logos-triggers](https://github.com/frikky/shuffle-docs/blob/master/assets/logos-triggers.PNG?raw=true)

## About
Triggers, along side apps and variables, can be found on the left hand side, in a tab called "Triggers".

![Trigger button](https://github.com/frikky/shuffle-docs/blob/master/assets/trigger-button.PNG?raw=true)

Triggers are special case items put into a workflow, developed by Shuffle to give the user access to multiple ways to run a workflow. There are currently two triggers, with a third (hidden) one:
* Webhook - Handle realtime HTTP requests from anywhere
* Schedule - Runs your workflow on a schedule
* Rest API - Essentially a trigger from either: 1. Another workflow. 2. Any third party 

### Webhook
[Webhooks](https://en.wikipedia.org/wiki/Webhook) is the real-time handler for Shuffle data. It was initially implemented to handle data from [Office365 connectors](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/connectors/connectors-using) and [TheHive](https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md), but turned into a generic trigger as we saw the use-case for it. To start using this trigger, you should have a service that supports webhooks (e.g. the two above mentioned). Once you have a service ready:
1. Drag the "Webhook" trigger from the left hand side into the main view, and you should see it automatically connect to your starting node. 
2. Click "start" to deploy this webhook. This will also be stopped if you remove the node or the workflow. A webhook can not be in multiple workflows, but you can deploy as many as you want.
3. Find your webhook URI in the "Webhook URI" window, and copy it to your service

Test it! Say your URI is: https://shuffler.io/functions/webhooks/webhook_336a7aa2-e785-47cc-85f4-31a4ab5b28b8 and you want to use {"test": "testing"} in your workflow:
```bash
curl -XPOST https://shuffler.io/functions/webhooks/webhook_336a7aa2-e785-47cc-85f4-31a4ab5b28b8 --data '{"test": "testing"}'
```

![Webhook image](https://github.com/frikky/shuffle-docs/blob/master/assets/webhook-image.PNG?raw=true)

### Schedule 
Schedules are based on [google's cloud scheduler](https://cloud.google.com/scheduler/) and are schedules that run based on [cron](https://en.wikipedia.org/wiki/Cron). It takes two arguments - the schedule you want to run it on and the Execution argument used in the workflow. A simple cron converter can be found [here](https://en.wikipedia.org/wiki/Cron). When you are ready to run, click "start". 

![Schedule image](https://github.com/frikky/shuffle-docs/blob/master/assets/schedule-image.PNG?raw=true)

### Pricing
TBD - 

## API 
