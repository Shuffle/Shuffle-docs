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

![Create workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/create-workflow.png)

If you lose your way and want to edit it at a later point, it can always be found at [https://shuffler.io/workflows](https://shuffler.io/workflows).

![Edit workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/edit-workflow.png)

### Edit
Once your workflow is created, you will be presented with the following view, which we will explain in the following section. 

![New workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/new-workflow.png)

Workflows are entirely based on [apps](https://shuffler.io/docs/apps), [triggers](https://shuffler.io/docs/triggers), [variables](https://shuffler.io/docs/variables) and [conditions](https://shuffler.io/docs/conditions). All of these except conditions can be seen in the bottom left corner of the screen, and are items that are avidly used within any workflow. Apps and triggers are draggable, where apps make up the actions that are ran, while triggers chooses what the workflow as a whole does. 

To run your first workflow, find the workflow "Testing" on the left hand side, and drag it into the view. This will create a clickable node, which you can freely edit.  

![First node](https://github.com/frikky/shuffle-docs/blob/master/assets/first-node.png)

If you clicked the node, you are now presented with a new view on the right hand side containing information about the node you are currently viewing. Herein you can specify exactly how the node is to behave, which in our example case has the name "testing_1", will be running in the cloud and will be running the action "Hello world". If the app has more than one action, the latter item is clickable, and you can choose whichever action best presents what you want to perform. Please note that this node is now also considered the "starting node", meaning that any execution will start at this point.

![Node action options](https://github.com/frikky/shuffle-docs/blob/master/assets/node-action-options.png)

#### Save 
Now that we have a working workflow, click the "save" button in the upper left corner of your screen, which will present with a notification at the bottom of the screen that saving is in progress. Saving is required to make your latest edits available for execution.

#### Execute
Now that your workflow is saved, its time to execute. There is a button in the bottom left corner, which you can execute your workflow with. Once clicked, this will start execution at your "starting" node, indicated by a round icon with a turquoise border. Whether successful or not, you will be presented with another notification indicating that the node has executed.

![Node indicate success](https://github.com/frikky/shuffle-docs/blob/master/assets/node-indicate-success.png)

If you want to see all your previous executions, you can go back to [workflows](https://shuffler.io/workflows), click the name of your workflow (in our case Example workflow), and see the status and result of all previous executions.

![Execution view](https://github.com/frikky/shuffle-docs/blob/master/assets/execution-view.png)

### Further edits - send email on a schedule
Now that you have a working example workflow, lets move onto something a little more advanced. We will perform the following actions:
1. Change action in our testing node from "Hello world" to "Repeat back to me" 
2. Set the input for "Repeat back to me" to be the argument we supply when executing
3. Test!
4. Add an email node and set the recipient to be the data from "Repeat back to me" in our testing node
5. Test!
6. Schedule the email to be sent every 15 minutes to your supplied email.

#### Change testing action 
Once changed, you will see a new item, [arguments](https://shuffler.io/docs/argument), which can be of a few different sorts, including but not limited to: static values, data from other nodes, internal variables, global variables and more. 
![Change action repeat](https://github.com/frikky/shuffle-docs/blob/master/assets/change-action-repeat.png)

To change the argument to be the argument we supply when executing, click the "action" button next to our new node, and "Execution argument" will automatically show up. Below you can see us running the node with the argument "This is a test" 

![Repeat execution argument](https://github.com/frikky/shuffle-docs/blob/master/assets/repeat-execution-arg.png)

Click save, then "execute", and you should see the result pop like below.
![Repeat success](https://github.com/frikky/shuffle-docs/blob/master/assets/repeat-success.png)

#### Add a new node!
Its 

### Export 
### Import 
### Copy 
### Delete

## Examples
Test

## Testing
Test

## API
