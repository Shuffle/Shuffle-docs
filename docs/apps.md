# Apps
Documentation for apps

# Table of contents
* [Introduction](#introduction)
* [How they work](#howtheywork)
* [Actions](#actions)
* [Development](#development)
* [API](#api)

## Introduction
Apps, also referred to actions actions in some cases, are the heavy lifters of [workflows](/docs/workflows) within Shuffle. They give the user access to a library of pre-defined integrations, and are also easy to recreate for any user. Apps are based on the same format as [WALKOFF](https://walkoff.readthedocs.io/en/latest/apps.html), and are therefore interchangable between the two. 

## How they work
Apps are the building blocks used of workflows, and are either made by us (Shuffle) or our users. These can be auto-generated from [OpenAPI](https://swagger.io/specification/) specifications or through predefined python libraries, and are (for now) made in Python. Currently available apps can be found at [https://shuffler.io/apps](https://shuffler.io/apps). To enforce stability and usability, we use a versioning system to prevent sudden updates to apps. This also enforced that the developers change version of an app before a new one is uploaded. Apps contain actions, which again have parameters, explained in the next section. Apps also have the ability to be in any environment, where a default (e.g. cloud execution) is predefined by the developer, but the apps have the availability to execute both in the cloud and on-premise.

![Apps saved](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-saved.PNG?raw=true)
![Workflow app](https://github.com/frikky/shuffle-docs/blob/master/assets/workflow-app.PNG?raw=true)

### Actions
An app can perform more than one task based on predefined actions. These actions are defined by the developer, and are easily reusable and modifyable by the user of the application. An action should (for now) be a one-to-one representation of the function to run, and usually has parameters for authentication with the target application. Actions can contain multiple parameters.

![App actions](https://github.com/frikky/shuffle-docs/blob/master/assets/app-actions.PNG?raw=true)

### Parameters
Parameters are the variables used to perform an action. Some parameters are required, defined by the <div style={{color: "orange"}}>orange</div> colored dot next to it, while <div style={{color: "yellow"}}>yellow</div> means its optional. Parameters usually have example text, indicating the expected value. The first arguments of an app are _usually_ related to authentication or the target URL, which you can save as variables.

![App action parameters](https://github.com/frikky/shuffle-docs/blob/master/assets/app-action-parameters.PNG?raw=true)

![Parameter required](https://github.com/frikky/shuffle-docs/blob/master/assets/parameter-required.PNG?raw=true)

### Variables
Variables are the data points used in a parameter. They can be of four different types;
1. Static - User-defined data, default field
2. Action Result - Takes the result of another previous action or the [execution argument for the workflow](/docs/workflow#execution). This is the main one used for dynamic data between apps, and can handle e.g [JSON values](https://www.impressivewebs.com/what-is-json-introduction-guide-for-beginners/).
3. Local variable - Unencrypted variable defined in the workflow, mainly used for e.g. ID's or URL's that will be reused.
4. Global variable - Encrypted global variable which are decrypted during execution, mainly used for authentication schemes. (TBD - this should work well together with App-specific authentication)

These can quickly be swapped between by clicking the buttons right next to the value.

![Variable choise](https://github.com/frikky/shuffle-docs/blob/master/assets/variable-choice.PNG?raw=true)

### Authentication 
TBD - currently done in parameters 
<!--App authentication-->


## Development
TBD, but this is pretty accurate: [app development](https://walkoff.readthedocs.io/en/latest/apps.html)

## Release

### Pricing 
TBD - Calculated per execution
<!--App authentication-->

## API 
TBD
