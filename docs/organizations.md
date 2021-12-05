# Organizations 
Documentation for the Admin view of Shuffle. Best used by administrators.

## Table of contents
* [Introduction](#introduction)
* [Organization Overview](#organization_overview)
* [Cloud Syncronization](#cloud_syncronization)
* [Data collection](#data_collection)
* [Pricing](#pricing)
* [User Management](#user_management)
* [App Authentication](#app_authentication)
* [Environments](#environments)
* [Schedules](#schedules)
* [Files](#files)
* [User Roles](#user_roles)
* [App Categories](#app_categories)

## Introduction
With version 0.8.0, Shuffle was released with an Admin panel. This gives access to configure an organization, and will over time get more features. With the latest release, Shuffle introduced cloud syncronization, which gives access to certain cloud features on-premises. 

Keep in mind that everything in this document is **PER ORGANIZATION**. This is paramount to remember, as all features should be connected to a user within a specific organization.

## Organization overview
The organization overview gives access to a few things:
* Name Change
* Description Change
* Image change
* Cloud syncronization
* Hybrid Feature overview

The point of this view is to get access to new features more easily. It can tell you about new updates, features and more that we have in store. The view is slightly different from the cloud version to the on-premises version. Here's how:
* The **cloud** version shows you an API-key. This can be used in the open source version.
* The **open source** version gives you an API-key field. This can be used in the cloud version.
![Organization view](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-1.png?raw=true)

### Cloud Syncronization
Cloud syncronization is a feature used to get more capabilities on-premises that otherwise wouldn't be possible. These range from scalability to collaboration and accessibility. The goal is to give access to features that otherwise are impossible to get otherwise. See [Hybrid Features](#hybrid_features) for more info.

**Of note:**
* We will NOT send ANY of your data to the cloud. Not even your local organizations name or description. This is purely a system to give access to extra features that can work on a general scale.

![Cloud sync features](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-2.png?raw=true)

#### Setup 
Setting up cloud syncronization requires two things:
1. A user on [https://shuffler.io](https://shuffler.io). Get the API-key.
2. An open source version of Shuffle. [Here's how to set it up](https://github.com/frikky/shuffle/blob/master/install-guide.md)

1. Start by going to [https://shuffler.io/register](https://shuffler.io/register?view=admin) and create an account. 
![Register user](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-3.png?raw=true)
2. With an account made, go to [https://shuffler.io/admin](https://shuffler.io/admin). Here you'll find your API-key. Copy it.
![Cloud sync cloud](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-4.png?raw=true)
3. Go to your [local instance](http://localhost:3001/admin) at /admin and paste the API-key.
![Cloud sync local](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-5.png?raw=true)
4. See the features you get access to.
![Cloud sync local features](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-6.png?raw=true)

### Hybrid Features 
Updated 10.04.2020

Want to try it out? [Send us an email](mailto:frikky@shuffler.io)

There are many features that make Shuffle more usable. These are mainly related to accessibility, scalability and collaboration - in that order. For the initial release (v0.8) of Shuffle, we've decided to focus entirely on accessibility. Every feature comes with some of the same basic features, so that you know what you're getting into.

**These basic features are**
* Activation (true or false)
* Limits (none or 0-infinite)
* Privacy & Data sharing (none, minimal, high)
* Type (general, actions, triggers, editor, )
* Description

**These are the categories they fit into**
1. Accessibility - Makes Shuffle easier to use. We make every open source function open source, but some are hard or impossible to make easy for a user to have.
* Collaboration	 - Gives access to shared workflows, apps and general searching. This is to make it possible to learn from each other.
* Scalability 	 - Gives access to use our hardware and servers, e.g. through cloud executions. 

You can see most of our currently planned features on [https://shuffler.io/pricing](https://shuffler.io/pricing).

#### Activation
Activation tells you whether the feature is active. It's indicated by the red or green mark next to the feature on the admin page.
![Cloud sync features indicator](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-8.png?raw=true)

#### Limits
Some features have limits. These are features such as SMS and email sending, schedule creation, cloud executions and more. Click each item to learn more.

![Cloud sync features limits](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-7.png?raw=true)

#### Description
The description exists to specify what exactly an action does. This will become more granular over time. Access it by clicking each feature.

#### Data collection 
There are three types of data sharing, where the initial launch of Shuffle uses none. You can see the usage as per the image in [limits](#limits)

The three levels we'll keep to are:
* None 	- Shuffle doesn't collect any information about your on-premises organization. This is most features.
* Minimal - Shuffle collects a minimal amount of information necessary to execute the action. An example is a Workflow execution, where we'll need to gather information about the next steps in a workflow to properly execute it.
* High 	- Shuffle collects the necessary information to handle information. This is used for when full syncronization, meaning information used on-premises will also be used in the cloud. An example is having access to edit workflows in the cloud, that will execute on-premises. This requires access to all the same apps, workflows, credentials, triggers, organizational users and more. **PS: This will not happen for a while, and will be 100% OPTIONAL**

### Pricing 
[Our pricing tiers for Shuffle](https://shuffler.io/pricing) are currently split into three: Basic, Community and Pro. Basic is a support tier, and exists to make it possible for you to support us without having to use alternative means such as [github sponsors](https://github.com/sponsors/frikky). Everything we build out that can be priced is for us to further create a better offering for the open source community. 

Whenever we add new features that can help Shuffle work better by leveraging cloud resources, you'll automatically get access to it if you're on that tier.

These are our tiers:
* Basic
* Community 
* Pro 

#### Basic
The basic tier is meant as a way for people to support Shuffle. It will give more perks over time, but to start of, it gives you and your team an onboarding meeting with Shuffle to get you kickstarted as well as some community support features.

#### Community
Community is the tier where you may get core hybird features, as well as become a part of the community. The key starting features you'll get use of are the triggers and outbound features we've made: Schedules, Webhooks, User Input continuations and SMS / Email sending through Shuffle. We'll soon expand this to doing cloud executions with Shuffle. 

#### Pro
Pro is the full package. It is meant for those of you who want everything from support to auditlogging, datacenter choices, compliance overviews, data retention control, reporting, and more. This package is currently not available as 

Get in touch at [frikky@shuffler.io](mailto:frikky@shuffler.io) if you want something more specific.

## User management
![User management Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-9.png?raw=true)

User management is all about adding, listing, deleting and controlling users in general. Users are a part of a specific organization, and are created by organization admins. To add users you need the "admin" role.

Existing roles:
* Admin - Gives you access to control an organization, and see what everyone in the organization are doing.
* User  - Gives you access to YOUR resources within an organization. This is to prevent you from seeing what everyone else are doing.

**To come:**
* User control in cloud
* API generation for users by admin
* Creating API-only users (no login)
* Granular access

### Adding a user
Click the "ADD USER" button, and you'll get a popup. Type in their username (open source) or email (cloud), and you'll create an invite for them. Cloud will not allow an admin to set a password to share, but rather send them an email. This will also be a part of the hybrid offering later.

![Adding a user to shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-10.png?raw=true)

### Change a users' role
Click the "Role" dropdown and choose one. Defaults are Admin and User, but we'll add granular access for this now. To repeat, here's the current roles:
* Admin - Gives you access to control an organization, and see what everyone in the organization are doing.
* User  - Gives you access to YOUR resources within an organization. This is to prevent you from seeing what everyone else are doing.

### Deleting a user
A user in Shuffle can't be deleted, but deactivated. This is to keep all references available for when audits eventually require them. Click "Edit user", then "Deactivate". This prevents the user from being used. **A deactivated user can be reactivated.**

## App Authentication
App authentication is a way for Shuffle to keep track of what credentials you have for an app in a specific organization. It shows you information the most important information, and gives you access to modify or easily delete them. Authentication is specified at the app level, and applies to ALL functions of the the app, unless specified otherwise. Authentication is created during workflow editing.

![Basic app authentication](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-11.png?raw=true)

These are **NOT** editable outside of deletion as of november 2020, but we may add the possibility of changing without showing the previous value. 

### Authentication Field overview 
The fields of authentication
* Icon 					- The App's icon. This is 
* Label 				- The name of the authentication scheme. Make it helpful, e.g. "QRadar Datacenter Amsterdam" or similar. 
* App Name 			- The name of the app it belongs to
* Workflows 		- The amount of workflows it's being used in
* Action Amount - The amount of actions that use the authentication
* Fields 				- The fields specified by the app creator. It's usually a URL, an API key or username & password.
* Actions 			- What you can do to edit the app. As of 20.11.2020, only deletion is accessible. By deleting it, you'll also make the **workflow invalid**.

### Authentication in workflows 
Authentication is and should be defined the first time you use an app. We'll use the example of TheHive, which takes the fields "apikey" and "url". Start by [creating a workflow](/docs/workflows#create), before dragging in the app "TheHive". 

Once it's in, click the node, and you'll see a view like this. We've outlined three places that indicate this app requires authentication. All of these are also clickable.
![Authentication in workflow](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-14.png?raw=true)

By clicking either of these, a popup window will show. In this one, type in a DESCRIPTIVE name (to remember), before passing credentials. **PS: Never use localhost in an URL. Everything runs in a container, which has its own IP. Always use the system's IP/domain within the URL.**
![Authentication workflow popup](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-15.png?raw=true)

By clicking "submit", the authentication is now saved for your organization. This removes clutter in the UI, by having less required fields, and is also reusable. You can now make multiple nodes that use the same authentication.
![Authentication view after submit](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-16.png?raw=true)

Last, but not least, this can now be controlled on an organizational level. 
![The same authentication on](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-17.png?raw=true)

### App creation with authentication
The fields are specified by the app creator. This short section outlines how to create authentication as a creator. [More on this in the apps section](/docs/apps). An example is TheHive, which takes a URL and an API-key. These fields have to be specified as seen below. 
![App creation specification](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-12.png?raw=true)

Outer level: authentication
Inner level: parameters

These parameters are specified exactly as a parameter within an action. The function's code needs to reflect it as well, as can be seen with this python function, taking an apikey and URL.
![App creation python code](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-13.png?raw=true)

## Environments
Environments are a core part of Shuffle's open source build. Think of it as physical location where you want an agent of Shuffle running (Orborus). Orborus is the tool that keeps your workflow running. But Orborus needs to know what jobs to run. Afterall, we'd like it you to be able to run parts of a workflow in the cloud and parts of it in all your different datacenters. 

![Environments in Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-19.png?raw=true)

The default environment is called "Shuffle". You can add as many as you want, but you'll only get access to "cloud" environments through cloud syncronization.  

### Environment fields
* Name 						- The name to use. This is the identifier used by orborus. 
* Orborus running	- Shows whether Orborus is running or not.
* Type 						- Whether it's a cloud environment or not. Orborus can't attach to "cloud" environments.
* Default					- Whether it's the default environment to use for new actions. You should set this to the environment you use the most.
* Actions 				- Possible changes to an environment. Currently only archiving. You can't re-open an archived environment, and can't archive the default environment.
* Archived				- Tells you whether it's archived. There's a toggle at the top to edit it.

### Orborus configuration
If you would like to run Orborus towards a different environment, you'll have to specify the environment variables "ENVIRONMENT_NAME", "ORG_ID" and "BASE_URL".

Here's an example, where the environment's name is "Hallo" and backend is at http://192.168.3.6:3001
```
docker run -d \
	--volume /var/run/docker.sock:/var/run/docker.soc \
	-e ORG_ID="Hallo" \
	-e ENVIRONMENT_NAME="Hallo" \
	-e BASE_URL=http://192.168.3.6:3001 \
	ghcr.io/frikky/shuffle-orborus:0.8.0
```

## Schedules
This view is an overview of schedules created within workflows. You can stop them from here, but you'll have to visit the workflow itself to edit the schedule.
![Schedule view](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-18.png?raw=true)

## Files 
This view is an overview of files created within workflows. These are a way of looking for a specific file and downloading them (November 2020). Files are created from Actions in Workflows, and are restricted per Organization.

[Click here to see further usage documentation](/docs/workflows#file_handling) 

![File view](https://github.com/frikky/shuffle-docs/blob/master/assets/admin_example-19.png?raw=true)

## User Roles
**TBD** Granular access (role based) rights is an upcoming feature for organizations and users. It will allow you to control what specifically an account has access to.

## App Categories 
**TBD** App categories are a way to keep an overview of your current apps and their use-cases. SIEM is SIEM. EDR is EDR. Ticketing system is Ticketing system. VMS is VMS. That's what this is for. A way to swap your workflows in an easy fashion. 
