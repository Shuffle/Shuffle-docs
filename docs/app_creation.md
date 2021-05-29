# Shuffle App Creation in Python
Documentation for app development with Python (as opposed to creating them with the app editor, e.g. with an OpenAPI specification).

## Table of contents
* [Introduction](#introduction)
* [Why create a custom app?](#why-create-a-custom-app)
* [Development Instructions](#development-instructions)
  * [Directory structure](#directory-structure)
  * [Authentication/actions/logo in api.yaml](#apiyaml)
  * [App documentation](#docsmd)
  * [Python dependencies](#requirementstxt)
  * [src/app.py](#srcapppy)
* [Hotloading Your App](#hotloading-your-app)
* [Debugging](#debugging)

## App development process
This page is about how to (technically) develop a new Shuffle app. Want to know how to decide whether to make something new? Checkout the [process document](https://github.com/frikky/shuffle-docs/blob/master/handbook/engineering/app_development.md) and then come back here.

## Prerequisites
We assume you have a base understanding of Python 3.x (3.7+ used).

## Introduction
Apps are how you complete work in Shuffle. At a high level, you define a Workflow that starts based on a schedule, or some expected event (webhook received, etc), and that in turn runs one or more apps. An app takes input (argument data to act on, credentials, etc), uses that to complete some work, and returns resulting data to Shuffle to store, display, or feed into another app for further processsing.

The underlying design of Apps in Shuffle are based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html) with minor differences. Most of the documentation below will therefore be close to their approach.

**PS: There is no way of creating a Python app easily in the cloud yet**

[More about apps](/docs/apps)

The premise behind all apps that run in Shuffle, is that they each run in an isolated Docker container, for security purposes. You provide arguments to an app in a Shuffle workflow, and when the workflow is run, your app is reached in the control flow, it will be launched as a new container. Shuffle then sends the apps argument data, and the container destroyed when the app's work is completed.

## Why create a custom app?
There are many prebuilt apps in Shuffle, and all complete some action. There may be an integration you need that doesn't exist yet. This guide will walk you through the process.
Always remember the key components of the app:
* What functions are available in the app?
* What arguments are needed for the app to function? - e.g. authentication arguments, json data structure arguments.
* What is the output of this function, and what are we doing with that resulting data? e.g. send an email, create a ticket, send to another app for conditional 		processing.


## Development Instructions

In our example, we are going to develop an app that connects to an API for Office365, pulls some log data and returns it as a JSON data structure.
We first think about the 3 primary elements:<br>
* What **actions / functions** will we create?
	* We will have a function to poll the last 10 minutes of audit logs from the Office API.
	* We will have a function to poll the last 23 hours of audit logs from the Office API -- testing only purposes.
* What **arguments** are needed for the app to run?
	* We need some arguments for authentication (based on Office365 authentication, we have planType, tenantID, clientID, clientSecret).
	* Note that your app may also receive json_data structure arg as part of a prior app action -- you are not limited here.
* What is the **output data**?
	* The app outputs a JSON data structure that contains one audit log entry per JSON object.

With our 3 elements in mind, you can build the script on your own. This example is Python3, but some additional work would allow any app type/language. For now, the expectation is that you would build this in Python3.

Build your Python functions with the expected arguments, and ensure they return the expected output. Once the code works in your environment, you can then integrate it into Shuffle's apps directory to integrate as an app.

Don't forget to document your app in the docs.md file in each version's directory (see below)!

### Directory structure

With your Python script built, we must build a directory structure, some metadata files and modify a base app.py file to run your code from Shuffle.
In your shuffle server, there is a shuffle-apps directory, typically under the top level dir where you cloned the github repo.

/Shuffle/shuffle-apps/

This directory contains a list of folders, one per app in Shuffle. The minimal directory structure for a Shuffle app is as follows:

```
Shuffle
+-- shuffle-apps
  +-- app_name (virustotal)
    +-- version_number (1.0.0)
      |-- api.yml           # Has the full app configuration - must match app.py
      |-- Dockerfile        # Contains Shuffle build instructions
      |-- docs.md           # Your documentation of this app in markdown format
      |-- requirements.txt  # Extra packages to be used by the app
      +-- src 							
        +-- app.py          # The base python file for everything related to your application
        +-- yourcustom_app.py		# More complex apps can have an entire directory stucture, imported and called by app.py
  +-- another_app_1
  +-- another_app_2
```

There is a template app called python-playground that we will clone and edit.
First make your app folder. Note: This folder should not contain spaces.

```
cd /Shuffle/shuffle-apps
mkdir office365mgmt
cd office365mgmt
cp -R /Shuffle/shuffle-apps/python-playground/* .
```

The above will make your app folder and copy the template files from python-playground to your app. Upload your python code files to the /src/ directory of your app's folder.

Now that your app's .py script is uploaded under /Shuffle/shuffle-apps/office365mgmt/src, you'll tell Shuffle how to use it.

We will modify 4 files:
* api.yaml
* docs.md
* requirements.txt -- Specify any modules that your app uses, which will be installed via pip
* src/app.py -- The base app that is called by Shuffle, which in turn will call your python script's functions

### api.yaml

api.yaml is what provides Shuffle information about your app. Here we define your app's name, description, author info, actions (functions available) and the parameters that each function takes.

This example shows the office365mgmt app settings, but feel free to explore other app's api.yaml to see other obscure options.

* name: Office365 Mgt API -- This is your app's display name as seen in Shuffle GUI. You can put whitespace here, but _ may be better
* description: Some description -- Your app's description that will display in the Shuffle GUI
* contact_info: If you are maintaining this, please share your details with users

```
app_version: 1.0.0
name: Office365 Mgt API
description: Collect AzureActiveDirectory,Exchange,Sharepoint,General, DLP audit logs
contact_info:
  name: "@RobertEvans"
  url: https://shuffler.io
  email: rob.evans512@gmail.com
```

#### Authentication

Not all apps need this step, but if yours requires a key, secret, or password, it is recommended to use a specialized "authentication" declaration in api.yaml, so those credentials are stored safely and not displayed in cleartext in your Shuffle workflow.

Here I define that my app requires authentication and a list of parameters, which is a list of arguments specified by -name. The name value can be anything you want, but note this is the name of the argument when passed to app.py and ultimately to your app.

My app expects 4 arguments that should be stored as an authentication object. When this app is run, this credential object once configured in Shuffle will be sent to the app to use.

My first argument is a string called "planType". When the app is used in a workflow, this would be populated by workflow parameters and it would get sent to the app to use (e.g. "Enterprise").
* name: case sensitive authentication argument name
* description: The description should display common values for this argument
* example: The example is a placeholder syntax in absence of a value in user interface.
* required: specifies whether it is mandatory to run the app
* schema: The type of variable can be specified, string is the only one tested but ideally any type could be used here. You can also do type casting in your app from string later.

```
authentication:
  required: true
  parameters:
    - name: planType
      description: Enterprise, GCC , GCCHigh, DoD
      example: "Enterprise"
      required: true
      schema:
        type: string
    - name: tenantID
      description: xxxx-xxxx-xxxx-xxxx
      example: "xxxx-xxxx-xxxx-xxxx"
      required: true
      schema:
        type: string
    - name: clientID
      description: xxxx-xxxx-xxxx-xxxx
      example: "xxxx-xxxx-xxxx-xxxx"
      required: true
      schema:
        type: string
    - name: clientSecret
      description: xxxx-xxxx-xxxx-xxxx
      example: "*****"
      required: true
      schema:
        type: string

```

#### Actions

Actions define the functions of your app, the args it accepts and the options available (static list of values for a given arg).
* name: the python function name
* description: string description of the function
* parameters: The args the function accepts, note this is in addition to the authentication args specified above.

Note that one value, json_data, seems to be sent even if I don't need it, so I account for it, although it is unused at this time. You could send a JSON object here.
This app has 1 function (action) called run_o365poller. This app only pulls logs, so it is limited.

The app's single function takes 2 args (besides the 4 from the authentication included above for every function), which are a string json_data arg and string PollInterval.
The PollInterval string arg has a dropdown selection in GUI, listed by options, of poll_10min or poll_23hours. This is one method to give clients a limited set of options for arg values. The json_data structure, although unused, can insert any value from a prior app or input.

```
actions:
  - name: run_o365poller
    description: Run Office365 audit poller for defined interval
    parameters:
      - name: json_data
        description: The JSON to handle
        required: false
        multiline: true
        example: 'No args for now, insert credentials and get returned data'
        schema:
          type: string
      - name: PollInterval
        description: The selected Python function to run
        required: true
        multiline: true
        example: '1'
        options:
          - poll_10min
          - poll_23hours
        schema:
          type: string
    returns:
      schema:
        type: string
```

#### Logos
The app's logo can be encoded here using a base64 encoded representation of the image, listed after large_image, see example below, but omitted for brevity:
```
large_image: data:image/jpg;base64,/9j/4AAQSkZJR

```
### docs.md
Use this file to document your app. This includes any prerequisites for using it as well as what the actions are for and how specific data objects are handled. Until we have created a nice documentation template, [here's an example](https://github.com/frikky/security-openapis/blob/master/docs/discord.md) you can use.

### requirements.txt
This is your standard python module list that will get installed on Docker container launch

### src/app.py

Now that your api.yaml file is modified, there is a base app.py script that is called from Shuffle when your app is run. This script will receive the configured arguments and options configured in your Shuffle workflow for the given app.

You must handle this appropriately and pass the arguments to the appropriate function. Note that we can handle this many ways.
You can:
* Build your entire app into app.py, and expand with logic to run the right function requested
* Put minimal code in app.py to call your python script app.py calls office365poller.py (imported into app.py)

When our Office365 app is called, Shuffle assumes that app.py has an inherited class object containing a function matching the ones in our api.yaml file:

1. Shuffle workflow starts
2. Your configured app is called
3. app.py's PythonPlayground.run() function is called. This then runs the selected function name and supplies the arguments.
4. We then parse the arguments, and run the appropriate function calling our script.

This is where many things are possible, I'll post the code below, but will describe it in detail.

```
class PythonPlayground(AppBase):
    __version__ = "1.0.0"
    app_name = "Office365_Mgt_API"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def run_me_1(self, planType,tenantID,clientID,clientSecret):
        #Poll last 10 min Office365
        #Parse json_data with key value data
        #planType = json_data['planType']
        #tenantID = json_data['tenantID']
        #clientID = json_data['clientID']
        #clientSecret = json_data['clientSecret']
        pollInterval = 10 #Assume minutes
        return office365poller.pollOffice(planType,tenantID,clientID,clientSecret,pollInterval)

    def run_me_2(self,planType,tenantID,clientID,clientSecret):
        #Poll last 23 horus or 1380 min Office365
        #Parse json_data with key value data
        #planType = json_data['planType']
        #tenantID = json_data['tenantID']
        #clientID = json_data['clientID']
        #clientSecret = json_data['clientSecret']
        pollInterval = 1380 #Assume minutes
        return office365poller.pollOffice(planType,tenantID,clientID,clientSecret,pollInterval)


    def run_me_3(self, json_data):
        return "Ran function 3"

    # Write your data inside this function
    async def run_o365poller(self, planType,tenantID,clientID,clientSecret, PollInterval,json_data):
        # It comes in as a string, so needs to be set to JSON
        try:
            #json_data = json.loads(json_data)
            #We are not using json_data structure at this time, getting creds directly
            pass
        except json.decoder.JSONDecodeError as e:
            return "Couldn't decode json: %s" % e

        # These are functions
        switcher = {
            "poll_10min" : self.run_me_1,
            "poll_23hours" : self.run_me_2,
        }

        func = switcher.get(PollInterval, lambda: "Invalid function")
        return func(planType,tenantID,clientID,clientSecret)

if __name__ == "__main__":
    asyncio.run(PythonPlayground.run(), debug=True)
```

Our app's api.yaml specifies we have a function called "run_o365poller" that accepts our 4 authentication args + 2 additional args (unused json_data and PollInterval), all string values.

In order for the app to run, app.py must have an async function the same name as each function in api.yaml. We only have one above. Note that I intentionally left some commented json handling in place to show other ways to get args, you could send a json structure into the function for parsing, but should only be done for non-privileged info. The authentication data comes in as separate args.

Lastly, ensure your script returns the data you require, after mine is processed, I return a singular JSON array, with one JSON object per log entry. Another app will be written to parse this and take some action on this data, or it could simply be expanded on this app.

I have the function below, as specified in my api.yaml, that accepts the args I expect. From this script, I run my poll script, with different args based on the value of arg PollInterval.

```
   # Write your data inside this function
    async def run_o365poller(self, planType,tenantID,clientID,clientSecret, PollInterval,json_data):
```

## Hotloading your app
Once your app has been tested, you've created the necessary metadata files and directory structure under your shuffle-apps folder, there is no need to restart your containers!

Shuffle has an app hot reloading feature in the GUI. Go to Apps on the top left hand tool bar of the GUI, and then look for a Double Arrow refresh.
Give the system 20 or so seconds, and you'll see a pop up saying it was successful.

Once complete, any workflows you have that use the existing app, you'll have to delete old versions of the app and re-add them in the workflow.


## Debugging
As Shuffle has a lot of individual parts, debugging can be quite tricky. To get started, here's a list of the different parts, with the latter three being modular / location-independent.

| Type     | Container name    | Technology       | Note |
| -------- | ----------------  | ---------------- | ---- |
| Frontend | shuffle-frontend  | ReactJS          | Cytoscape graphs & Material design |
| Backend  | shuffle-backend   | Golang           | Rest API that connects all the different parts |
| Database | shuffle-database  | Google Datastore | Has all non-volatile information. Will probably move to elastic or similar. |
| Orborus  | shuffle-orborus   |Golang 						| Runs workers in a specific environment to connect locations. Defaults to the environment "Shuffle" onprem. |
| Worker   | worker-id         | Golang 					| Deploys Apps to run Actions defined in a workflow |
| app sdk  | appname_appversion_id | Python           | Used by Apps to talk to the backend |
worker-8a666e4f-e544-440e-bf0f-4220e7cc9e25

### Execution debugging
Execution debugging might be the most notable issue you might explain. This is because there are a ton of reasons that it might crash. Before going into techniques to find what's going on, you'll need to understand what exactly happens when you click the big execution button.

**Frontend click -> Backend verifies and deploys executions -> (based on environments) orborus deploys a new worker -> worker finds actions to execute -> your app is executed.**

1. A workflow is executed
2. The backend verifies whether you can execute and deploys to environment
3. Orborus is listening to environment and deploys worker if it's the correct one
4. Worker deploys actions if they have the right environment
5. App executes and returns data back to the execution

As previously stated, a lot can go wrong. Here's the most common issues:
* Networking (firewalls / proxies)
* Badly formed apps.
* Bad environment

#### General debugging
This part is mean to describe how to go about finding the issue you're having with executions. In most cases, you should start from the top of the list previously described in the following way:


1. Find out what environment your action(s) are running under by clicking the App and seeing "Environment" dropdown. In this case (and default) is "Shuffle". Environments can be specified / changed under the path /admin
![Check execution 3](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_3.png?raw=true)

2. Check if the workflow executed at all by finding the execution line in the shuffle-backend container. Take note that it mentions environment "Shuffle", as found in the previous step.
```
docker logs -f shuffle-backend
```

![Check execution 1](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_1.png?raw=true)

3. If it executed, check whether Orborus is running, before checking it's logs for "Container \<container_id\> is created. The container_id is the worker it has deployed. Take not of the environment again at the end of the line. If you don't see this line, it's most likely because it's running in the wrong environment.

Check if shuffle-orborus is running
```
docker ps # Check if shuffle-orborus is running
```

Find whether it was deployed or not
```
docker logs -f shuffle-orborus  # Get logs from shuffle-orborus
```

![Check execution 2](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_2.png?raw=true)

Check environment of running shuffle-orborus container.
```
docker inspect shuffle-orborus | grep -i "ENV"
```

Expected env result where "Shuffle" corresponds to the environment
![Check execution 4](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_4.png?raw=true)

4. Check whether the worker executed your app. Remember that we found \<container_id\> previously by checking the logs of shuffle-orborus? Now we need that one. Workers are and will always be verbose, specifically for the reason of potential debugging.

Find logs from a docker container
```
docker logs -f CONTAINER_ID
```

![Check execution 5](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_5.png?raw=true)

As can be seen in the image above, is shows the exact execution order it takes. It starts by finding the parents, before executing the child process after it's finished. Take note of the specific apps being executed as well. It says "Time to execute \<app_id\> with app \<app_name:app_version\>. This indicates the app THAT WILL be executed. The following lines saying "Container \<container_id\> is the container created with this app.

5. App debugging in itself might be the trickiest. There are a lot of factors like branches, bad workflow building etc that might come into play. This builds on the same concept as the worker, where you pass the container ID it specified.

Get the app logs
```
docker logs -f CONTAINER_ID # The CONTAINER_ID found in the previous worker logs
```

As you will notice, app logs can be quite verbose (optional in a later build). In essence, if you see "RUNNING NORMAL EXECUTION" in the end, there's a 99.9% chance that it worked, otherwise some issue might have occurred.

Please [notify me](https://twitter.com/frikkylikeme) if you need help debugging app executions ASAP, as I've done a lot of it, but it's more tricky than the other steps.
