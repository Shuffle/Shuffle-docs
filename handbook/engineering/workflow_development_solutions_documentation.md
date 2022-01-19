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
* Start Node
* Subflows
* Shuffle Cache
* Shuffle File Storage


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

* Create a Greynoise API querying app via Shuffle's easy to use App Creator 
* Use Shuffle's inbuilt Http App and query Greynoise directly from here, using curl commands.
* Use a pre-built Greynoise querying app (You can search for an app you want to use exists)


### 2. Cases: Issue management with Jira 
Here we'll learn about using filters, files and loops. We also learn how to solve typical API problems.

* Make sure you are signed up on [Jira](https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=95003655569&campaign=9124878867&creative=415542762940&device=c&keyword=jira%20software%20sign%20up&matchtype=e&network=g&placement=&ds_kids=p51242194601&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=CjwKCAiA5t-OBhByEiwAhR-hmx8BfX8_S0SEAnN5pj0Lka1qmQ7G0-IqZOrwkL3JZYe_Rxp1i3RwBRoCLuwQAvD_BwE&gclsrc=aw.ds) (Signup)
* Using the Jira App in Shuffle, create an issue using the create issue action, ensure your authentication is correct and then execute. (App Auth)
*  Using the HTTP app in Shuffle, use the get action to download the file from https://secure.eicar.org/eicar.com.txt, no authentication is required (Files)
* Using Shuffle's file system within the Shuffle tools app we download the remote file and it's assigned a file id. (Files)
* We then proceed to create a node with the Jira App to add an attachment on the issue we created in the previous Jira App node, here we use the add attachment action to do this, we furthermore have to choose our desired attachment which at this point is in the Shuffle file system and has an assigned id. Enter this id under the file id field under the parameters, then your Jira issue id in which you want to attach the file. (Files)
* We then list all issues made and from here, we use the filter list action found in the versatile Shuffle App to filter bringing forward issues with attachments within them, then finally the issue we just made. (Filter & Loop)
* With this step done, we go ahead and re-download the attachment. (Files)


### 3. Intel: Continuous analysis for changes

The point of this workflow is to make a list of indicators, and searching for if their data changes.

* Upload a file with a list of IP's and upload it to shuffle by going to the admin tab and you'll see an upload files button. Proceed to upload the file. (Files)
* After your file uploads, it is given a unique file ID, copy this value by heading to the right most button under the action columns under the uploaded files. (Files)
* From the versatile Shuffle tools app, use the get file value action.
* Paste the file ID under the file data, run to see if your file uploaded successfully. (Files)   
* If you get a problem parsing in the list Liquid Formatting is at your service, you can clean up your list and then proceed. See [shopify](https://shopify.github.io/liquid/) or check out our documentation on liquid formatting [here](https://github.com/Shuffle/Shuffle-docs/blob/master/docs/liquid.md) (Liquid)
* Moving on using the HTTP App we query the [IP info's API](https://ipinfo.io/signup) getting back info about the uploaded IP's
* We then set a trigger to automate this process every 30 minutes. So this workflow is executed each and every 30 minutes. (Triggers)
* We then set the cache to match our data and set a condition if there is any deviation in the info got from infoip an email is sent to our email notifying us of a change in IP info and we should check it out. (Cache, Notification)
