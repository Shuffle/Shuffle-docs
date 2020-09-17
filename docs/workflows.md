# Workflows
Documentation for workflows. 

**PS: some of this migth NOT work on the CLOUD version.**

# Table of contents
* [Introduction](#introduction)
* [The Basics](#basics)
* [Create](#create)
* [Edit](#edit)
* [Save](#save)
* [Execute](#execute)
* [Delete](#delete)
* [Nodes](#nodes)
* [Conditions](#conditions)
* [Starting node](#starting_node)
* [Execution argument](#execution_argument)
* [Workflow Variables](#workflow_variables)
* [Execution variables](#execution_variables)
* [Passing values](#passing_values)
* [Parsing JSON](#parsing_json)
* [Casting values](#casting_values)
* [Authentication](#authentication)
* [API](#api)
* [How-to continuation (CLOUD)](#how-to_continuation)

## Introduction
Workflows are the backbone of Shuffle, empowering you to automate your daily tasks by with a simple interface. Workflows use [apps](/docs/apps), [triggers](/docs/triggers), [conditions](/docs/conditions) and [variables](/docs/apps/#variables) to make powerful automations in no time. 

If you would like to learn more about how to create, test and automate your tasks, read on. 

## Basics
The following section describes a basic workflow. 

### Create
Once logged in, creating a workflow can be done by going to the [workflows](/workflows) dashboard and clicking the "New" button next to "Workflows". It will ask you for a name and description. These can be changed at any time. 

![Create workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/create-workflow.PNG?raw=true)

If you lose your way or want to edit it at a later point, it can always be found at [/workflows](/workflows).

![Edit workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/edit-workflow.PNG?raw=true)

### Edit
Once a workflow is created, you will be presented with the following view: 

![New workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/new-workflow.PNG?raw=true)

Workflows are entirely based on [apps](/docs/apps), [triggers](/docs/triggers), [variables](/docs/apps#variables) and [conditions](/docs/conditions). You have access to all of these in the bottom left of the screen. Apps and triggers are draggable, meaning you can drag and drop them into the main window. 

To run your first workflow, find the app "Testing" on the left hand side, and drag it into the view. This will create a clickable node, which you can freely edit.  

![First node](https://github.com/frikky/shuffle-docs/blob/master/assets/first-node.PNG?raw=true)

Clicking the node presents you with a new view. This is the view to configure the node. In our example case, the default name should be "testing_1", running with the environment "Shuffle" (default). 

The default action for the "Testing" app is "hello_world". This can be changed by clicking the dropdown menu. More about editing an app's actions can be found [here](#edit actions)

![Node action options](https://github.com/frikky/shuffle-docs/blob/master/assets/node-action-options.PNG?raw=true)

### Save 
Now that we have a working workflow, click the "save" button next to the big play button (or click CTRL+S). This presents you with a notification at the bottom of the screen that saving is in progress. Saving is required to make your latest edits available for execution.

### Execute
With a saved workflow, you can now execute. The big orange play button will execute for you. Once clicked, this will start execution at your [starting node](#starting node), indicated by a round icon with a turquoise border. Whether successful or not, you will be presented with another notification indicating that the node has executed.

![Node execute success](https://github.com/frikky/shuffle-docs/blob/master/assets/node-execute-success.PNG?raw=true)

If you want to see all your previous executions, you can go back to [workflows](/workflows), click the name of your workflow (in our case Example workflow), and see the status and result of all previous executions in detail.

![Execution view](https://github.com/frikky/shuffle-docs/blob/master/assets/execution-view.PNG?raw=true)

If you want to test more, go to the bottom of this article [How-to continuation](#how-to).

## Nodes 
Nodes are the draggable parts from the left-side view - apps and triggers. Whenever you click of these, you will get the view on the right side of the screen with configurations. Apps are standardized, while triggers are all different. 

Most nodes use values that you can pass to them. These can be text specified by you (pencil icon), [an app result](#passing_values) or from [variables](#variables)(heart icon).

![argument-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/argument-example-1.png?raw=true)

### Starting node
The starting node is circular with a turquoise border. This node is the FIRST ACTION in an execution. The starting node is NOT a trigger, but rather the first action that a trigger sends data to. The starting node can be changed by clicking a different node, then the "SET STARTNODE" button in the top-right corner.

## Conditions 
Conditions use the same format as nodes, with the view popping up on the right side. To add a condition, you need to have a branch/line in the view, meaning you need at least two nodes. This line itself, is what will run the condition for you. Branches can use the same valeus as other nodes, meaning they can parse variables from previous node results.

PS: Conditions are currently only AND, not OR, meaning you would need multiple branches to get OR.

1. Click a branch / line
![conditions-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-1.png?raw=true)

2. Click "New condition"
![conditions-example-2](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-2.png?raw=true)

3. Configure the condition. Choose the value(s) you're looking for, and use the center piece ("DOES NOT EQUAL" in this example) to modify what you want. In the case of this image, it would NOT run, because "hello" (left side) equals "hello" (right side)
![conditions-example-3](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-3.png?raw=true)

4. Here's another example, where it would run IF the [execution argument](#execution argument) contains "shuffle is cool". That also means it would run if you write "I don't think shuffle is cool.".
![conditions-example-4](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-4.png?raw=true)

5. Here's another way of writing the exact same condition as in step 4. Notice the difference? We didn't select the "execution argument" as a previous action, but use it as a static value (this is explained further in [passing values](#passing_values))
![conditions-example-5](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-5.png?raw=true)

## Execution argument
The execution argument is what makes it possible for triggers to work. This is the argument that the whole execution is ran with. Manual executions can also have an execution argument. In essence, the execution argument can be anything - json, list, string, number. It's up to you.

![execution-argument-1](https://github.com/frikky/shuffle-docs/blob/master/assets/execution-argument-1.png?raw=true)

The execution argument acts like a node, meaning you can use its value anywhere.
These are the different names for it: 
* $exec
* $trigger
* $webhook
* $schedule
* $userinput
* $email_trigger

## Workflow Variables
Workflow variables is static reusable data decided before an execution. These are typically used for APIkeys, URL's or usernames. [Click here to see Executio variables](/docs/workflows#execution_variables)

Some things to keep in mind when using workflow variables:
* They are set BEFORE an execution
* They are unencrypted
* They are shared with everyone with access to the workflow 
* They are only accessible to the workflow you're in.

Use-case:
* Save URLs, API keys and more.

PS: We are working on a way to have encrypted global variables to be used for passwords and global APIkeys (and more) with IAM, but that might take a while to implement properly.

**How to create and use a workflow variable:**

1. Click "Variables" in the bottom left corner.
![variable-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-1.png?raw=true)

2. Click "Make a new workflow variable"
![variable-example-2](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-2.png?raw=true)

3. Write a name, description and value for the variable.
![variable-example-3](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-3.png?raw=true)

4. Use the variable in an action or condition
![variable-example-4](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-4.png?raw=true)

## Execution Variables
Execution variables work the same way as Workflow Variables, except they HAVE to be set during execution. These are temporary datapoints that will not be saved anywhere. They work by taking the RESULT of an action of your choosing (examples below), done with a single click. If you're looking for static data, [click here to see Workflow variables](/docs/workflows#workflow_variables)

Some things to keep in mind using execution variables:
* They are set DURING execution
* They are used during execution
* They are unencrypted

Use-case:
* E.g. basic multi-tenancy

**How to create, use and check execution variables:**

1. Click "Variables" in the bottom left corner.
![variable-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-1.png?raw=true)

2. Click "New execution variable".
![variable-example-5](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-5.png?raw=true)

3. Choose a unique name. It only requires a name as the variable is set DURING execution, in this case "Testing"
![variable-example-6](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-6.png?raw=true)

4. Now click an existing action and choose the variable. This will set the RESULT of the action to the execution variable. 
![variable-example-7](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-7.png?raw=true)

5. Add another node and USE the variable. The variable can also be used by typing "$testing" in the "Static data" textfield. The repeated value in this case will be the value from the "Hello World" node set in step 4.
![variable-example-8](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-8.png?raw=true)

6. If you're unsure whether the value is set during execution or not, check the results. The last three results are available in the web UI, and can be seen by clicking the variable on the left side.
![variable-example-9](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-9.png?raw=true)
![variable-example-10](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-example-10.png?raw=true)


## Passing values
Passing values is what makes a solution like Shuffle work. It allows you to pass value from app X to app Y seemlessly. There are currently a couple of different ways to pass values between nodes, that also applies for conditions.

* Use the "Data from previous actions" 
* Use the "static data" field

Using a previous action, you get a selection of all previous nodes, as well as the execution argument.

If you use the "static data" field (pencil), you have to write it out yourself. 
* "$testing_1" will get the data from the node "testing_1" OR variable "testing_1"
* "$exec" will get the execution argument. 

PS: it still only works with PREVIOUS nodes. This method is also error prone.

### Parsing JSON
Parsing JSON is essential to be able to get API data. Shuffle uses it's own schema, which seems to work quite well. 

$ 					= identifier for a previous node / execution argument 
$exec 			= execution argument chosen
$exec.name  = you choose the argument "name" from the execution argument

The first text after $ will always be the name of the previous node. If you add "." ($exec.name), it will look for "name" as a json value under "exec". If the node doesn't exist, it will just write $exec.name straight up.

Say you send the following data as our [execution argument](#execution argument):
```
execution_argument = {
	"name": "this is some data",
	"description": "Cool description",
	"extra": {
		"writer": "Fredrik"
	}
}
```

1. How would we go about getting "name" (execution_argument["name"])
2. How do we get "writer" under "extra" (execution_argument["extra"]["writer"]? 

* Action argument:
1. 
![json-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/json-example-1.png?raw=true)

2. 
![json-example-2](https://github.com/frikky/shuffle-docs/blob/master/assets/json-example-2.png?raw=true)

* Static data:
I've put both questions into one. Maybe you catch my drift.
![json-example-3](https://github.com/frikky/shuffle-docs/blob/master/assets/json-example-3.png?raw=true)

### Examples
1. We have two nodes, and want "testing_2" to use the data from "testing_1". With "testing_2" selected, choose "testing_1" as data source.
![passing-values-1](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-1.png?raw=true)

2. The same exact configuration, but using a static value.
![passing-values-2](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-2.png?raw=true)

3. Using the execution argument from 2 items (testing_1 and execution argument). The execution argument is defined to be "Hey this is cool" as seen in the bottom left.
![passing-values-3](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-3.png?raw=true)

Result for #3:
![passing-values-4](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-4.png?raw=true)

## Passing values - lists
Lists are a different ballgame, but are really important to a SOAR solution. One simple reason would be: what if you have some alerts you want from system X to system Y? That will most likely be a list. 

PS: lists currently use all items (may 2020), and can't be limited to a few. This will change.

In the same way a node is identified by $, a list is identified by #. Say we have the following json data, and we want parse the "users" list. The node name is repeat_list (more below in example.
```
repeat_list = {
	"users": [{
		"name": "fredrik",
		"username": "@frikky",
		"id": "12345"
	},
	{
		"name": "moomo",
		"username": "shuffle user 2",
		"id": "23456"
	}]
}
```

To get all the "ids" from the list, we would write:
* $exec.users.#.id

Explanation:
1. $repeat_list = execution_argument
2. .users 			= "users" in the json data 
3. .# 					= the list identifier. This means we want to check the list.
4. .id 					= get all the IDs

Return: ["12345", "23456"]

### Examples
Let's use the example above in a real test.

1. We define a node, repeat_list, that gives us the list we defined above.
![values-passing-list-1](https://github.com/frikky/shuffle-docs/blob/master/assets/values-passing-list-1.png?raw=true)

2. We define a second node that returns the ID's as described above.
![values-passing-list-2](https://github.com/frikky/shuffle-docs/blob/master/assets/values-passing-list-2.png?raw=true)

3. Check the results.
![values-passing-list-3](https://github.com/frikky/shuffle-docs/blob/master/assets/values-passing-list-3.png?raw=true)

4. To build upon what we just created, we want to recreate the data described above as such:
```
{
	"ids": ["12345", "23456"],
	"names": ["fredrik", "moomo"],
	"usernames": ["@frikky", "shuffle user 2"]
}
```

This should work:
```
{
		"ids": $repeat_list.users.#.id,
		"names": $repeat_list.users.#.name,
		"usernames": $repeat_list.users.#.username
}
```

PS: Shuffle might throw you a JSON error for this, but that's expected behavior.

Here, we build the json we want ourselves. This is powerful, as we can basically define whatever data we want.
![values-passing-list-4](https://github.com/frikky/shuffle-docs/blob/master/assets/values-passing-list-4.png?raw=true)

## Casting values
There are a multitude of reasons casting to exist. This might be that you want a string to be a number, in upper or lowercase or even a list. To do this, casting was implemented in the App SDK. Here are the currently existing casting methods:

| Operation | Input type | Example | Return value | Return type | Alias | Note  |
| --------- | ------- |------- | ------------ | ----------- | ---- | ----- | 
| number()  | string | number(10) | 10 | integer | int() | String to int casting |
| lower()   | string | lower(HELLO) | hello | string | | Makes a string lowercase |
| upper()   | string | upper(hello) | HELLO | string | | Makes a string uppercase |
| trim()    | string | trim( hello ) | hello | string | strip() | Removes whitespace around a string |
| split()   | string | split(hello you) | [hello,you] | list | | Splits a list by whitespace. Will have options in the future | 
| length()  | string | length(hello)  | 5 | integer | len() | Returns the length of a string |
| parse()   | list, string | parse(["hey", "how", "are", "you"], 1:2) | how are | string | | Uses python slice annotaion after list: https://stackoverflow.com/questions/509211/understanding-slice-notation |

## Authentication
Authetication is important for Shuffle and all API related software. The reason being that you can't connect to other services without authentication.

There are a few forms of authentication in Shuffle workflows:
* Authentication to other apps
* Authentication to execute a workflow

### App Authentication
As a user, authentication to an app should be pretty straight forward: Fill in some fields. These fields are usually the first arguments, including the endpoint URL, and will be required (orange circle). 

Here's and example for TheHive:
![thehive-authentication-1](https://github.com/frikky/shuffle-docs/blob/master/assets/thehive-authentication-1.png?raw=true)

If the app is generated using the App Creator in Shuffle, that uses OpenAPI, this should be consistent.

PS: If an app is self-made, this might not be the case, as the creator defines it.

**Advice: Use a workflow variable to control this**

### Workflow authentication
For each workflow execution, Shuffle generates a random authorization key that has to be used to interact with the execution itself. This is automated and here for informational reasons

In short: If you're not an admin and not a specific worker running the execution, you shouldn't be able to tamper with an execution.

## API
[Click here to see the Workflow API](/docs/api#workflows)


# CLOUD SPECIFIC example
Now that you have a working example workflow, lets move onto something a little more advanced. We will perform the following actions:
1. Change action in our testing node from "Hello world" to "Repeat back to me" 
2. Set the input for "Repeat back to me" to be the argument we supply when executing
3. Test!
4. Add an email node and set the recipient to be the data from "Repeat back to me" in our testing node
5. Test!
6. Schedule the email to be sent every 15 minutes to your supplied email.
7. TBD: JSON parsing 

#### Change testing action 
Once changed, you will see a new item, [arguments](/docs/argument), which can be of a few different sorts, including but not limited to: static values, data from other nodes, internal variables, global variables and more. 
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
With our newly created workflow for sending email, we now want a way to send the email every 15 minutes (or more often / less often). Close to the bottom left, there is a button, [Triggers](/docs/triggers), where you find all the available triggers. As with apps, these are draggable, but one keen difference is that they're (currently) always attached to the starting node of your workflow.

![Trigger added](https://github.com/frikky/shuffle-docs/blob/master/assets/trigger-added.PNG?raw=true)

A quick note about triggers: they need to be started and stopped. That means you need to configure them through the available arguments (Cron and Execution Argument) in this case, before clicking the "Start" button. The default schedule for schedules is every 15 minutes, but if you want to edit it, [click here to get a converter](http://www.cronmaker.com).

As triggers are used to run an entire workflow, they usually handle the "Execution Argument" somehow. Schedules has its own field you can fill here, where you again fill your email address, before clicking the "Start" button.

You should now be receiving an email with the data specified in the "email_1" node based on the schedule trigger you just made.

![Schedule started](https://github.com/frikky/shuffle-docs/blob/master/assets/schedule-started.PNG?raw=true)

#### Add json 

