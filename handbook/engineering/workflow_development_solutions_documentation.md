# Workflow development solutions documentation

This document is curated from knowledge gotten by doing [workflow exercises](https://github.com/Shuffle/Shuffle-docs/blob/master/handbook/engineering/workflow_development_exercises.md), from a beginner's perspective. 

From the proverbial zero to hero in workflow development in Shuffle, here you gain core techniques and critical thinking skills equipping you with much needed skills in your arsenal for automation and workflow development using Shuffle. Techniques gained include but are not limited to:

* JSON
* Loops 
* Nested loops 
* Variables
* Loop filtering
* Liquid formatting
* App authentication
* Triggers
* App authentication
* Conditions


## Warnings

* If possible shy away from double looping, it usually causes problems. 
* When testing go as simple as possible, if possible test a node individually, making sure it works well then proceed to add it to your workflow.

## Use-cases

### 1. Communication: Email

The goal of this workflow is to get emails, and analyze whether the sender's IP is malicious, adding it to Shuffle's cache.

#### Getting emails into shuffle (App auth)

* Drag the email app into your workspace.
* Rename and configure it, in our case we want to get emails from our outlook address.
* Set your login credentials, imap server is imap-mail.outlook.com
* Choose your folder name, inbox, junk, archive or custom folder. 
* Pick the amount of emails you want to go through.
* Select fields you are interested in and continue

#### Parsing out the IP's (Variables)

* Using the versatile Shuffle Tools app, parse out the IP's or any other IOC that you deem usable in our case just the IP's.

#### Running a Greynoise search on IP's (Filtering and Search)

* Here we can choose to go either one of three ways;-

1. Create a Greynoise API querying app via Shuffle's easy to use App Creator 
2. Use Shuffle's inbuilt Http App and query Greynoise directly from here, using curl commands.
3. Use a pre-built Greynoise querying app (You can search for an app you want to use exists)


### 2. Cases: Issue management with Jira 


### 3. Intel: Continuous analysis for changes

The point of this workflow is to make a list of indicators, and searching for if their data changes.

* Upload a file with a list of IP's and upload it to shuffle by going to the admin tab and you'll see an upload files button. Proceed to upload the file.
* After your file uploads, it is given a unique file ID, copy this value by heading to the right most button under the action columns under the uploaded files.
* From the versatile Shuffle tools app, use the get file value action.
* Paste the file ID under the file data, run to see if your file uploaded successfully.   
* If you get a problem parsing in the list Liquid Formatting is at your service, you can clean up your list and then proceed. See [shopify](https://shopify.github.io/liquid/) or check out our documentation on liquid formatting [here](https://github.com/Shuffle/Shuffle-docs/blob/master/docs/liquid.md)
* Moving on using the HTTP App we query the [IP info's API](https://ipinfo.io/signup) getting back info about the uploaded IP's
*
