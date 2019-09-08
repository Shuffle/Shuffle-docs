# Workflows
Documentation for [workflows](https://shuffler.io/workflows)

# Table of contents
* [About](#about)
* [Workflow control](#control)
* [Create](#create)
* [Edit](#edit)
* [Save](#save)
* [Execute](#execute)
* [Delete](#delete)
* [Examples](#examples)
* [Testing](#testing)
* [API](#api)


## About
Workflows are the backbone of any SOAR solution, empowering users to automate their daily tasks by simple drag-and-drop. Workflow use [apps](https://shuffler.io/docs/apps) and [triggers](https://shuffler.io/docs/triggers), created by the us and the community to make simple integrations between tools. Workflows have access to run both [on-premise and in the cloud](/docs/hybrid), meaning it can integrate with any solution available to you. Read on if you would like to learn more about how to create, test and automate your tasks. Workflows are based on how workflows are treated in [NSA's WALKOFF](https://github.com/nsacyber/WALKOFF), but is entirely rewritten.

## Control
The control of workflows is described below as a walkthrough from zero to hero.

### Create
Once logged in, creating a workflow can be done by going to the [workflows](https://shuffler.io/workflows) dashboard and clicking the "New workflow" button. This will create a popup window, where you have to fill in the name, and optionally, the description for your workflow. When this is filled, click the "submit" button, and you will be redirected to your newly generated workflow. 

![Create workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/create-workflow.PNG?raw=true)

If you lose your way and want to edit it at a later point, it can always be found at [https://shuffler.io/workflows](https://shuffler.io/workflows).

![Edit workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/edit-workflow.PNG?raw=true)

### Edit
Once your workflow is created, you will be presented with the following view, which we will explain in the following section. 

![New workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/new-workflow.PNG?raw=true)

Workflows are entirely based on [apps](https://shuffler.io/docs/apps), [triggers](https://shuffler.io/docs/triggers), [variables](https://shuffler.io/docs/variables) and [conditions](https://shuffler.io/docs/conditions). All of these except conditions can be seen in the bottom left corner of the screen, and are items that are avidly used within any workflow. Apps and triggers are draggable, where apps make up the actions that are ran, while triggers chooses what the workflow as a whole does. 

To run your first workflow, find the workflow "Testing" on the left hand side, and drag it into the view. This will create a clickable node, which you can freely edit.  

![First node](https://github.com/frikky/shuffle-docs/blob/master/assets/first-node.PNG?raw=true)

If you clicked the node, you are now presented with a new view on the right hand side containing information about the node you are currently viewing. Herein you can specify exactly how the node is to behave, which in our example case has the name "testing_1", will be running in the cloud and will be running the action "Hello world". If the app has more than one action, the latter item is clickable, and you can choose whichever action best presents what you want to perform. Please note that this node is now also considered the "starting node", meaning that any execution will start at this point.

![Node action options](https://github.com/frikky/shuffle-docs/blob/master/assets/node-action-options.PNG?raw=true)

#### Save 
Now that we have a working workflow, click the "save" button in the upper left corner of your screen, which will present with a notification at the bottom of the screen that saving is in progress. Saving is required to make your latest edits available for execution.

#### Execute
Now that your workflow is saved, its time to execute. There is a button in the bottom left corner, which you can execute your workflow with. Once clicked, this will start execution at your "starting" node, indicated by a round icon with a turquoise border. Whether successful or not, you will be presented with another notification indicating that the node has executed.

![Node execute success](https://github.com/frikky/shuffle-docs/blob/master/assets/node-execute-success.PNG?raw=true)

If you want to see all your previous executions, you can go back to [workflows](https://shuffler.io/workflows), click the name of your workflow (in our case Example workflow), and see the status and result of all previous executions.

![Execution view](https://github.com/frikky/shuffle-docs/blob/master/assets/execution-view.PNG?raw=true)

### Further edits - send email on a schedule
Now that you have a working example workflow, lets move onto something a little more advanced. We will perform the following actions:
1. Change action in our testing node from "Hello world" to "Repeat back to me" 
2. Set the input for "Repeat back to me" to be the argument we supply when executing
3. Test!
4. Add an email node and set the recipient to be the data from "Repeat back to me" in our testing node
5. Test!
6. Schedule the email to be sent every 15 minutes to your supplied email.
7. TBD: JSON parsing 

#### Change testing action 
Once changed, you will see a new item, [arguments](https://shuffler.io/docs/argument), which can be of a few different sorts, including but not limited to: static values, data from other nodes, internal variables, global variables and more. 
![Change action repeat](https://github.com/frikky/shuffle-docs/blob/master/assets/change-action-repeat.PNG?raw=true)

To change the argument to be the argument we supply when executing, click the "action" button next to our new node, and "Execution argument" will automatically show up. Below you can see us running the node with the argument "This is a test" 

![Repeat execution argument](https://github.com/frikky/shuffle-docs/blob/master/assets/repeat-execution-arg.PNG?raw=true)

Click save, then "execute", and you should see the result pop like below.
![Repeat success](https://github.com/frikky/shuffle-docs/blob/master/assets/repeat-success.PNG?raw=true)

#### A new action node!
As you now have a working example where we leverage actions, its time to add another node. Find the "Email" node in the app view (on the left hand side), and drag it into the view together with our old node. These will automatically connect, as that is a standard procedure for the second node added.

![Email connected](https://github.com/frikky/shuffle-docs/blob/master/assets/email-connected.PNG?raw=true)

As can be seen whenever the email node is selected, it takes three arguments; recipient, subject and body. As previously, we want to set the recipient to whatever our old node, "testing_1", returns. This means we do the same as previously:
1. Click "action" above the recipient argument
2. This field now has another argument that it did not previously have, namely one of the nodes it has access to data from. Choose "testing_1", if you didn't change our first nodes name.

Feel free to fill whatever you want into the subject and body field (and recipients too if you want). Click save, fill the "Execution Argument" to the email you want to send to, before clicking execute. Check your email inbox, and you should see an email.

![Edit email](https://github.com/frikky/shuffle-docs/blob/master/assets/edit-email.PNG?raw=true)
![Email success](https://github.com/frikky/shuffle-docs/blob/master/assets/email-success.PNG?raw=true)

#### Email scheduling trigger
With our newly created workflow for sending email, we now want a way to send the email every 15 minutes (or more often / less often). Close to the bottom left, there is a button, [Triggers](https://shuffler.io/docs/triggers), where you find all the available triggers. As with apps, these are draggable, but one keen difference is that they're (currently) always attached to the starting node of your workflow.

![Trigger added](https://github.com/frikky/shuffle-docs/blob/master/assets/trigger-added.PNG?raw=true)

A quick note about triggers: they need to be started and stopped. That means you need to configure them through the available arguments (Cron and Execution Argument) in this case, before clicking the "Start" button. The default schedule for schedules is every 15 minutes, but if you want to edit it, [click here to get a converter](http://www.cronmaker.com).

As triggers are used to run an entire workflow, they usually handle the "Execution Argument" somehow. Schedules has its own field you can fill here, where you again fill your email address, before clicking the "Start" button.

You should now be receiving an email with the data specified in the "email_1" node based on the schedule trigger you just made.

![Schedule started](https://github.com/frikky/shuffle-docs/blob/master/assets/schedule-started.PNG?raw=true)

#### Add json 

### Export 
### Import 
### Copy 
### Delete

## Examples
Test

## Testing
Test

## API
