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

#### Using Shuffle subflows as a workaround

* There are many ways to acheive your end goal in Shuffle, this is just another work around to achieve the task above. Here we'll be using shuffle subflows.

* Drag the email app into your workspace.
* Rename and configure it, in our case we want to get emails from our outlook address.
* Set your login credentials, imap server is imap-mail.outlook.com
* Choose your folder name, inbox, junk, archive or custom folder. 
* Pick the amount of emails you want to go through.
* Select fields you are interested in and continue
* Below the list of apps in your workspace select the triggers button, you'll be presented with a new list of event triggers and schedulers that can kick start your workflow; drag the shuffle workflow app into your workspace, this is your subflow.
* Under the Shuffle workflow app you just dragged into your workspace, click on it to edit it and select your workflow in our case its the workflow we are working in, so it will be highlighted in a red font.
* Under the next parameter, selecting your start node; shuffle assumes that the way you get your mails and the subflow node is one workflow and the way you manipulate your emails after getting them into the subflow node are two different workflows so just keep that in mind. So under the select your start node parameter pick your next node (You'll have to drag the next app to your workspace and select it as your start node if you don't have your next node in your workspace).
* Under the execution argument, loop through your previous node to get all the emails you had previously selected.

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


### 8. Identity Access Management: Using Okta

* Sign up to Okta [here](https://www.okta.com/uk/free-trial/) for a free trial. If you get a this domain is already taken error just edit the available space in the domain and add more words there to make your domain different. 
* After signing up on Okta you will have your own domain with the format as follows; https://<yourdomain_here>.okta.com/
* With the above steps complete; go to your Okta dashboard, click on the admin button, a 2FA prompt should pop up asking you to verify with a code, and if you haven't signed up for 2FA you'll be prompted to download an okta authenticator on your phone and continue with the authentication process.
* Once done you should end up on a sight that looks like the image below.
* Now before using the Okta app in Shuffle you will have to aquire your token key from Okta in order to authenticate and verify your api calls. Still in Okta admin dashboard, go to the security drop down and select API, a new window pops up and then select tokens,then click on the create token button. Copy your token and lets head back to shuffle.
* Drag your Okta app into your workspace, authenticate using your api key/token and your Okta url which should look like this https://<yourdomain_here>.okta.com
* For our first task we want to create another useer in  our tenant in Shuffle using their API. Under the find actions, we go ahead ans select the create user action if the headers are not pre set you can paste these inside the headers field 
Content-Type: Application/json
Accept: application/json
* Next we jump into the body field and enter the details of the user we want to create in a json format as shown below.

{
  "profile": {
    "firstName": "Jimmy",
    "lastName": "Brock",
    "email": "isaac.brock@example.com",
    "login": "isaac.brock@example.com",
    "mobilePhone": "555-415-1337"
  }
}

* Save then run.
* Go back to your admin dashboard under directory then select people and you should see the new user you just created.
* The next task on our list is to block the same user's account, so we drag in a new node of the Okta app in your Shuffle workspace. Ensure authentication is in order, then select the deactivate user action under the find actions same headers as before.
* Save and execute, if you go back to your admin dashboard you should see the user status as deactivated. 
* The next task here is to make a csv of general user info. For this, we will have to start by listing all groups we drag the Okta app to the workspace, select the list all groups action and then proceed to drag a shuffle workflow found under the triggers section, we will use this in order to avoid the complexities involving nested loops and lists within lists.
* Drag a new Okta app in the workflow, this is going to be the next node and the start of our new workflow (See documentation about subflows) 
* Click on the shuffle workflow that you just dragged, under the select workflow to execute, select your current workflow; it should be highlighted in red. Under the select startnode select the Okta node you just dragged under the execution argument loop through the result you got from the node where you listed all groups as such $list_all_groups.#

* Moving to the next node, this is the node that we initially set up as the start node in the subflow node above. So here we take in the results from the above node and lists out all members of different groups obtained from the above node

* Using the versatile shuffle tools App, we select the repeat back to me action and list out the parameters that we want to see in our csv meanwhile separating them with commas to get them as csv

* We once more drag in the shuffle tools app and here we select the create file action and name our file in the file name field. Lastly, we use Liquid formatting to clean our data. After executing this node our file should be available under the admin tab in the files section, and a result giving you the file id of your lists in a csv format.

* We drag in the email app, use the send email action and then authenticate filling in our email details such as smtp host and port, the recipient and the message then adding our attachment under the attachments field and execute. In our email we should get our message and attachment delivered. 

* Using the scheduling app under the triggers we setup our schedule for when this cycle is repeated and email sent to us. Scheduling uses cron jobs thus we can easily setup anytime we want to run this workflow