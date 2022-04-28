# Workflow Release process

# Introduction

Creating an idea from scratch can be hectic at times, but it gets easier with a well formulated roadmap to attain whatever you intend. Different people employ the use of different tools and technologies daily to achieve somewhat similar results, similar case applies to Shuffle users. We intend in creating this structured process as a skeleton for you to build up on, from the moment an idea hits you to putting that idea into production in your own environment and even sharing it publicly.

## Overview

At Shuffle, we have grouped usecases into 5 main types, see [usecases](https://shuffler.io/usecases);
* Collect
* Enrich
* Detect
* Respond
* Verify


### Example 1:
Employees will be forwarding suspected phishing emails that hits their inbox or spam folder into a central company email for further analysis by the security team, and a reply forwarded to the employee who flagged the email as to whether the suspected phishing email was indeed a phishing email or not. 


We'll be using example 1 above to easily elaborate the whole processes 

## Step 1
* First and foremost, collect more information from colleagues or clients with regards to where they usually face challenges and how they would like the process to be improved and refined. 

## Step 2
* Know what tools you and your colleagues/clients use and in which category they fall under in [Shuffle's detection framework](https://shuffler.io/detectionframework)

![step2](https://user-images.githubusercontent.com/31187099/165753485-fdde8d2d-a8bc-4d54-be3b-b77bab6e13bd.png)

Working example:
* In our case above we use gmail as our companies email provider where our colleagues send suspected phishing emails, we take the emails and filter out the sender email address, sender ip, urls obtained and attachments for enrichment and analysis using MISP and yara. So matching our tools to the Shuffle detection framework: Gmail will fall under comms, MISP and Yara will fall under intel, as in the picture below.

![step2 1](https://user-images.githubusercontent.com/31187099/165753517-0a973462-9fbe-4143-bc62-68a8fa58a507.png)

## Step 3
* Are your tools available in Shuffle? You can search for your tools in our interactive search tab  which will bring you apps, workflows and documentation involving that particular search term you entered. If your app doesn't exist, don't fret you could easily build one using Shuffle's built in app creator more of this [here](https://shuffler.io/docs/app_creation#how_apps_are_built) or reach out to us and we'll work on it and have it released. 

![step3](https://user-images.githubusercontent.com/31187099/165753562-6e99dda7-388c-41c8-8788-dcf7ec164400.png)

## Step 4
* Once your tools are all ready you ought to know where your usecase falls under in the [shuffle usecases types](https://shuffler.io/usecases). At this point you could check the publicly released workflows that utilize the same tools you intend to use and are similar to the end goal you intend to achieve and draw inspiration or insight of how you would like to go about yours.
* You will notice when you search you get the app you searched for and any public workflow incorporating the said tool or workflow labeled with the search keyword you entered

![step4](https://user-images.githubusercontent.com/31187099/165753582-646db20c-2176-4481-b77d-af5bf36c9c1a.png)

## Step 5 
Go ahead and start building. More info about this [here](https://shuffler.io/docs/workflows)

