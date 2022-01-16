# Workflows
Documentation for workflows. 

## Table of contents
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
* [Passing lists](#passing_lists)
* [Parsing JSON](#parsing_json)
* [Casting values](#casting_values)
* [Authentication](#authentication)
* [Handling files](#file_handling)
* [API](#api)

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

**PS: Conditions are currently only AND, not OR, meaning you would need multiple branches to get OR.**
**PS: Conditions can NOT handle loops right now ($variable.#). Use the [Filter App action](#conditions_loop) to learn more.**

1. Click a branch / line
![conditions-example-1](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-1.png?raw=true)

2. Click "New condition"
![conditions-example-2](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-2.png?raw=true)

3. Configure the condition. Choose the value(s) you're looking for, and use the center piece ("DOES NOT EQUAL" in this example) to modify what you want. In the case of this image, it would NOT run, because "hello" (left side) equals "hello" (right side)
![conditions-example-3](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-3.png?raw=true)

4. Here's another example, where it would run IF the [execution argument](#execution_argument) contains "shuffle is cool". That also means it would run if you write "I don't think shuffle is cool.".
![conditions-example-4](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-4.png?raw=true)

5. Here's another way of writing the exact same condition as in step 4. Notice the difference? We didn't select the "execution argument" as a previous action, but use it as a static value (this is explained further in [passing values](#passing_values))
![conditions-example-5](https://github.com/frikky/shuffle-docs/blob/master/assets/conditions-example-5.png?raw=true)

## Condition Loops
**PS: Condition with Loops can be avoided if you use the "Subflow" trigger to run each item of a list in a [subflow](/docs/triggers#subflow). That however does require running new workflows, hence more CPU and RAM**

In this section, we'll be exploring how to use conditions for loops. As explained above, this is done using the "Filter List" action of the "Shuffle Tools" app. The goal if this app is to filter what DOES and DOESN'T fit your criteria within a list. This app action has the same functionality as a normal condition. These conditions are based on the "filter" mechanism of arrays in Javascript.

Take the example of the list below. How would we use the app to only find the section that IS malicious (where "malicious" = true)?
```
[{"ip": "1.2.3.4", "malicious": true}, {"ip": "4.3.2.1", "malicious": false}, {"ip": "1.2.3.5", "malicious": true}]
```

1. Create a node that can handles the list.
![condition-loop-1](https://github.com/frikky/shuffle-docs/blob/master/assets/condition-loop-1.png?raw=true)

2. Add another node that uses the "Filter List" action
![condition-loop-2](https://github.com/frikky/shuffle-docs/blob/master/assets/condition-loop-2.png?raw=true)

3. Add the right information to the fields. The first field is the list itself. 
**PS: DONT add # here. Pass the entire list, not one at a time.**
```
input_list: The ENTIRE list that we want to filter. In our case; "$repeat_list" 
field: The field we want to validate. In our case this is "malicious" as we want to see if malicious is true or false
check: How do you want to validate? In this case, we want it to check if EQUALS. Other options: Larger than, Less than, Is Empty, Contains, Starts With, Ends With, Files by extension
value: the value we want the value to be. In our case, it's "true" as we only want it to be true.
opposite: want to make it opposite? "equals" becomes "NOT equals" and "Larger than" becomes "Less than" etc.
```
![condition-loop-3](https://github.com/frikky/shuffle-docs/blob/master/assets/condition-loop-3.png?raw=true)

4. Get the output! The data is returned as such:
```
{
	"success": True,
	"valid": [..],
	"invalid": [..]
}
```

The "valid" field will match our criteria, while the "invalid" part has everything that doesn't. In our case (below), there are 2 that ARE malicious, and 1 that isn't.
![condition-loop-4](https://github.com/frikky/shuffle-docs/blob/master/assets/condition-loop-4.png?raw=true)


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
Passing values is what makes a solution like Shuffle work. It allows you to pass value from app X to app Y seamlessly. There are currently a couple of different ways to pass values between nodes, that also applies for conditions.

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

1. How would we go about getting "name"? execution_argument["name"]
2. How do we get "writer" under "extra"? execution_argument["extra"]["writer"]

* Action parameter:
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

3. Using the execution parameter from 2 items (testing_1 and execution argument). The execution argument is defined to be "Hey this is cool" as seen in the bottom left.
![passing-values-3](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-3.png?raw=true)

Result for #3:
![passing-values-4](https://github.com/frikky/shuffle-docs/blob/master/assets/passing-values-4.png?raw=true)

## Passing lists
**PS: If you deal with MULTIPLE loops (loop within a loop), please pass each element to a sub-workflow using the [Shuffle Workflow](/docs/triggers#subflow)**

Lists are a different ballgame, but are really important to a SOAR solution. One simple reason would be: what if you have some alerts you want from system X to system Y? That will most likely be a list.

In the same way a node is identified by $, a list is identified by #. Say we have the following json data, and we want parse the "users" list. The node name is repeat_list (more below in example). 

**Usage**:
```
				= Without #, it DOES NOT loop the data.
.# 			= Loops the entire list
.#0 		= Runs ONLY the first element of the list 
.#1 		= Runs ONLY the second element of the list
.#0-1 	= Runs the first AND second element of the list
.#.data = Runs the entire list, and gets the JSON key "data" from each item
.#0.data = Runs ONLY the first element, and gets the JSON key "data" from it 
.#max.data = Runs ONLY the LAST element, and gets the JSON key "data" from it 
.#min-max = Runs ALL elements. Same as just # or #0-max
```


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
Since version 0.9.25 of Shuffle, casting values and data formatting can be done using [Liquid formatting](/docs/liquid). All action parameters are supported.

Space stripping:
```
{{ "          So much room for activities          " | strip }}!
```

More details: [https://shopify.github.io/liquid/filters/strip/](https://shopify.github.io/liquid/filters/strip/)

## Authentication
Authentication is important for Shuffle and all API related software. The reason being that you can't connect to other services without authentication.

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

## File Handling
This section is dedicated to file handling in workflows. Files have always had a special place in security, which also means in automation, meaning this needs to be a fully developed solution to handle that. We've approached it from the standpoint of "what do you need as a security professional", and added basic features like timestamps and hashes.

Files are handled in the backend of Shuffle through our API, which is fully accessible to apps. It's also possible to use the app creator to make file download actions. 

### Useful file handling info 
* Files are handled using their ID. This is a reference to the file, and is automatically generated.
* Other useful fields: md5/sha256, Filename, Filesize, organization, origin workflow, created time, status...
* We will add S3 buckets and other storage mechanisms later.
* [File API can be found here](/docs/API#files)
* They're typically identified by the field "File_id"

A file can be in one of four statuses 
* Created 		- The meta is prepared, but no file upload has been started. The ID is ready to handle a file.
* Uploading 	- A file upload has started. No other file can be uploaded from this point.
* Active 			- This means the file exists, and the data can't be changed.
* Deleted 		- The file has been deleted through Shuffle, retaining the metadata.

### Learn to use files 
To get familiar with files, go to the /admin view under the "files" tab and upload a file of your liking. With a file uploaded to our system, click the File ID icon on the far right side in the view to copy the ID. This is our reference to it for our workflow. Files are typically created and used within apps themselves, but this is good for testing.

![workflow-files-1](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-1.png?raw=true)

Next up, we'll use the file we just got in a workflow. To do this, we recommend using the "Shuffle Tools" app. This has the following functionality:
* Get file value 			 - print file content
* Download remote file - wget, download from URL
* Get file meta 			 - used for getting file metadata
* Delete file 				 - deletes the file content from disk. Meta persists.

**PS: If you need to create a file directly, the "Testing" app has this functionality"**

Here's a simple workflow where we show the file's value (EICAR), as well as the metadata provided by Shuffle:
![workflow-files-2](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-2.png?raw=true)
![workflow-files-3](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-3.png?raw=true)

As seen above, this returns most of the data required related to files. This is the basis of how we do anything with files in Shuffle, and by using the API, we allow the possibility of connecting with other apps. 

Good examples of other apps that use the file upload API are Yara (for rule testing) and TheHive (for data uploads). 

### Upload file API with the app creator
Next up, we'll show you an example of how an app action can be made that can handle files. Here, we'll use virustotal as an example. First, start by going to the /apps view, and clicking "Edit App" on the Virustotal (or wanted app).

You'll then see a view like this, where we can add an action.

![workflow-files-4](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-4.png?raw=true)

Next up, click "New Action" to add a new one.
![workflow-files-5](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-5.png?raw=true)

As we're gonna upload a file, it requires us to use a POST request, which is where we see the new action - "Enable Fileupload". Click it, then enter "file" as seen in the image below. 

![workflow-files-6-virustotal](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-6.png?raw=true)

At the same time, copy the curl request into the "URL path" field, and see it convert the curl statement into the path we want.
![workflow-files-7-virustotal](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-7.png?raw=true)

As you save it, you'll also see this tiny icon representing that it handles files. 
![workflow-files-8-virustotal](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-8.png?raw=true)

With all that done, it's time to build it, and use it in a workflow. As you can see below, it shows the "File_id" field, telling you it wants a file.
![workflow-files-9-virustotal](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-9.png?raw=true)

Having ran it, we get the correct response, as expected from their documentation;
![workflow-files-10-virustotal](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-files-10.png?raw=true)

And with that, we're done with the basic part of files in Shuffle. If something is unclear, please tell us.

## API
[Click here to see the Workflow API](/docs/API#workflows)
