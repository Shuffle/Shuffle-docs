# Shuffle extensions
This is documentation for integrating and sending data from third-party services to Shuffle. Not to be confused with [apps](/apps) and [workflows](/workflows)

## Table of contents
* [Introduction](#introduction)
* [Single Signon](#single_signon_sso)
  * [Okta](#okta)
  * [Auth0](#auth0)
  * [PingIdentity](#ping_id)
  * [Keycloak](#keycloak)
* [Webhooks](#webhooks)
  * [Wazuh Webhook](#wazuh)
  * [TheHive Webhook](#thehive)
  * [Logz.io Webhook](#logzio)
  * [MISP forwarder](#misp)
  * [AWS S3 forwarder](#aws_s3_forwarder)
  * [QRadar Webhook](#qradar)
  * [FortiSIEM Webhook](#fortisiem)
  * [ELK Webhook](#elk)
  * [Cortex Webhook](#cortex)

## Introduction
From the start, Shuffle has been a platform about integrations. We've focused on making them as open and usable as possible, but were missing one part; inbound data. The general way Shuffle handles this has been through third-party API's, where we poll for data on a schedule. There are however some cases where this doesn't do the trick. That's what extensions are. 

These integrations will typically entail third party services connecting to Shuffle with inbound Webhooks as triggers in a workflow.

## Single Signon SSO
Shuffle added Single Signon (SAML) from version 0.9.16. This allows you to log into Shuffle from other sources, entirely controlled by your external environment. SSO is available for **onprem**, even without the Enterprise version of Shuffle cloud. It works by setting an Entrypoint (IdP) and X509 Certificate, both used to validate the requests. This can be added under /admin, and **only works for your PRIMARY organization**.

![Single Signon button](https://github.com/frikky/shuffle-docs/blob/master/assets/sso-3.png?raw=true)

How it works:
- Every user gets the role "user" by default.
- If the user DOESN'T exist, it will be created, based on an identifier provided from the SSO provider.
- If the user DOES exist, it will simply log them in.
- After login, each user is redirected to /workflows as per a normal login.

**PS**: In some cases, the persons' username may be appear an ID in Shuffle. If so, an admin should login to Shuffle and change their username. SSO should still work.
**PPS**: The callback URL/redirect URL/recipient URL is `https://<URL>:<PORT>/api/v1/login_sso`

![Single signon configuration](https://github.com/frikky/shuffle-docs/blob/master/assets/sso-1.png?raw=true)

### Okta
To use Okta SSO with Shuffle, first make an app in Okta. Their guide for making an app [can be found here](https://developer.okta.com/docs/guides/build-sso-integration/saml2/create-your-app/). 

Once an application is made, it's time to find the required information. Go to the app > Sign On > Click "View Setup Instructions" under SAML 2.0. This will open a new page with the credentials.
![Okta SSO setup](https://github.com/frikky/shuffle-docs/blob/master/assets/sso-2.png?raw=true)

**Move these fields over to Shuffle:**
* Identity Provider Single Sign-On URL 	-> SSO Entrypoint (IdP)
* X.509 																-> SSO Certificate (X509)

After adding them, click "Save", saving the configuration. After saving, log out of your user to verify the SSO configuration. If you don't see a button for "Use SSO", you most likely configured the wrong organization.

### Auth0 
To use Auth0 SSO with Shuffle, first make an app on [https://manage.auth0.com](https://manage.auth0.com). Documentation can be found [here](https://auth0.com/docs/configure/saml-configuration/configure-auth0-saml-identity-provider).

After the app is made, click "Addons" > "SAML2 Web App". 
![Auth0 SSO setup](https://github.com/frikky/shuffle-docs/blob/master/assets/sso-4.png?raw=true)

**In the popup, move the data of these fields to Shuffle:**
* Identity Provider Login URL 				-> SSO Entrypoint (IdP)
* Identity Provider Certificate 			-> SSO Certificate (X509)

Open the Certificate file in a text editor, and copy it's contents.

After adding them, click "Save", saving the configuration. After saving, log out of your user to verify the SSO configuration. If you don't see a button for "Use SSO", you most likely configured the wrong organization.

### PingIdentity 
To use PingID SSO with Shuffle, first make an app on [https://console.pingone.eu/](https://docs.pingidentity.com/bundle/pingoneforenterprise/page/xsh1564020480660-1.html). Documentation can be found [here](https://docs.pingidentity.com/bundle/pingoneforenterprise/page/xsh1564020480660-1.html).

After the app is made, click the dropdown for it on the right side > Configuration > find these fields.
![PingID SSO setup Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/sso-5.png?raw=true)

**In the view above, move the data of these fields to Shuffle:**
* INITIATE SINGLE SIGN-ON URL 			-> SSO Entrypoint (IdP)
* DOWNLOAD METADATA 								-> SSO Certificate (X509)

Open the Certificate file in a text editor, and copy it's contents in the field.

After adding them, click "Save", saving the configuration. After saving, log out of your user to verify the SSO configuration. If you don't see a button for "Use SSO", you most likely configured the wrong organization.

### Keycloak
Open ID SSO setup with Keycloak:
- Click on clients 
- Create new client
- Set client id 
- Ensure client protocol is openid-connect
- Hit save

You now have a client. Click on settings and configure them as follows
-Your client ID
-Set up a name
-Client Protocol set to openid-connect
-Access Type set to public
-Standard Flow Enabled toggled to ON
-Direct access grants toggled to ON 

![Valid redirect URI](https://user-images.githubusercontent.com/31187099/162692070-ccc54692-6793-4331-adc7-2356d0fd5397.jpg)

For the Valid Redirect URI http://<URL>:<PORT>/api/v1/login_openid
-Backchannel Logout URL http://<URL>:<PORT>/*
-Backchannel Logout Session toggled to ON

Under the Fine Grain OpenID Connect Configuration
Valid Request URIs http://<URL>:<PORT>/login?autologin=true

![Auto login = true](https://user-images.githubusercontent.com/31187099/162692186-6ac71b93-01be-4cb1-83f4-b7cb17758378.jpg?raw=true)

Once this is done head over to your shuffle instance.
1. Click on Admin button
2. Scroll down and click on the downward facing arrow beneath Organization overview
3. Scroll down again to OpenID connect
4. Fill in the client ID (It should be the same as what you entered in Keycloak)
5. Authorization URL http://<Your_Keycloak_URL>:<port>/auth/realms/openid/protocol/openid-connect/auth
6. Token URL http://<Your_Keycloak_URL>:<port>/auth/realms/openid/protocol/openid-connect/token

![OIDC shuffle-side](https://user-images.githubusercontent.com/31187099/162689392-51fcb2e9-3d89-4066-8b99-6074065f9c2a.png?raw=true)

If you keep getting redirected to your backend url, head on to your Shuffle folder on your server.
1. Vim .env

![vim env](https://user-images.githubusercontent.com/31187099/164943744-981638cf-6149-42e1-a455-3d12927ec24c.png)

2. In vim change the BASE URL to your server link; i.e BASE_URL=http://<URL>:<PORT>

![baseurl](https://user-images.githubusercontent.com/31187099/164943748-96217836-6b7d-42e7-8c25-fae3d3294b30.png)

Finally go back to shuffle and use SSO button to login.

![shuffle SSO](https://user-images.githubusercontent.com/31187099/162689445-8db0766c-6f18-4463-8a92-f6ae62213918.png?raw=true)

### Other
As long as you can create an identity and acquire an Entrypoint (IdP) and X509, paste them into the Shuffle fields, and it should work with any SAML/SSO provider.

## Webhooks
### Wazuh
Wazuh is a SIEM platform for security operations. We've used it through their API multiple ways, but were missing an important component; alerting. That's why we've developed a simple alert forwarder from Wazuh to Shuffle. 

[Wazuh extension documentation](https://documentation.wazuh.com/current/user-manual/manager/manual-integration.html)

**PS: If you expect more than 10 alerts per second, you should add multiple workflows AND webhook forwarders to Wazuh**

These are the steps to set it up:
1. Create a Workflow which will receive alerts
2. Add a Webhook to the Workflow
3. Configure Wazuh with the Webhook URL
4. Test the integration

**1. Create a Workflow which will receive alerts**
This one is pretty easily explained. Go to Shuffle an make a new Workflow.

**2. Add a Webhook to the workflow**
[Add a webhook](/docs/triggers#webhook) and find the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with Wazuh](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with Wazuh 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**3. Configure Wazuh with the Webhook URL**
Start by logging into your Wazuh management console with access to edit the ossec.conf file. We'll first start by adding the Shuffle webhook forwarder. 

1. Transfer [these integration files](https://github.com/frikky/Shuffle/tree/master/functions/extensions/wazuh) to the server. Ignore the file named "ossec.conf" for now.
2. Move the custom-\* files to the location /var/ossec/integrations

```
[root@wazuh]# pwd
/var/ossec/integrations
[root@wazuh]# ls -alh
total 76K
drwxr-x---.  2 root  ossec  187 Apr 25 04:34 .
drwxr-x---. 19 root  ossec  242 Dec 14 09:40 ..
-rwxr-x---   1 ossec ossec 1.1K Dec 20 04:50 custom-shuffle
-rwxr-x---   1 ossec ossec 4.5K Jan 19 09:32 custom-shuffle.py
-rwxr-x---.  1 root  ossec 4.3K Nov 30 08:41 pagerduty
-rwxr-x---.  1 root  ossec 1.1K Nov 30 08:42 slack
-rwxr-x---.  1 root  ossec 3.8K Nov 30 08:41 slack.py
-rwxr-x---.  1 root  ossec 1.1K Nov 30 08:42 virustotal
-rwxr-x---.  1 root  ossec 6.3K Nov 30 08:41 virustotal.py
```

3. Change the files' ownership and access rights. This MAY be necessary if Wazuh doesn't have root privileges (it shouldn't)
```
$ chown root:ossec custom-shuffle
$ chown root:ossec custom-shuffle.py
$ chmod 750 custom-shuffle
$ chmod 750 custom-shuffle.py
```

4. Configure ossec.conf to forward to Shuffle 

Go to the location /var/ossec/etc/ossec.conf (or where the ossec.conf file is). Take the information below (including <integration>) and paste it in. Find the webhook URL from earlier, copy it and add it to the <hook_url> section. 

Find more fields like [levels, groups and rule_id here](https://documentation.wazuh.com/current/user-manual/manager/manual-integration.html).

```
	<integration>
		<name>custom-shuffle</name>
		<level>5</level>
		<hook_url>http://IP:PORT/api/v1/hooks/webhook_hookid</hook_url>
		<alert_format>json</alert_format>
	</integration>
```

5. Restart ossec manager. Every time you change ossec.conf, you need to restart the ossec manager.
```
systemctl restart wazuh-manager.service
```

You should now start seeing data sent from Wazuh into Shuffle which can be used. If data is NOT sent, make sure of a few things:
- If https in the Shuffle URL: is the certificate of Shuffle signed? Default: no.
- Check /var/ossec/logs for logs: grep -R custom-shuffle

**4. Test the integration**
There are many ways to test the integration, but you can simplify it by setting the "level" part of the configuration to a lower number (3~), as that would trigger it in a lot of cases, including when you SSH into the Wazuh manager. After an alert is supposed to have triggered, go to Shuffle, and you'll see something like the image below.

![Extend Shuffle with Wazuh 3](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_3.png?raw=true)

#### Running custom commands with Wazuh
Active response can be used with the command "Run Command" in the Wazuh app in Shuffle. This requires an Agent (Agent list) and Command ([Active response](https://documentation.wazuh.com/current/getting-started/use-cases/active-response.html) command). Below, we will show how to set up the custom command "reboot".

- Wazuh API logs will be on the manager in: /var/ossec/logs/api.log
- Wazuh agent logs can be found in /var/ossec/logs

**Testing custom active response from Shuffle**:
The goal with this section is to set up a bash script that can run custom commands from within Shuffle.

1. Log into the Wazuh agent of choice (Linux), and add the following script to the active-response folder. Give it the name "shuffle.sh". Full path: /var/ossec/active-response/bin/shuffle.sh PS: Once done, make sure it's executable: chmod +x /var/ossec/active-response/bin/shuffle.sh
```
#!/bin/bash
# Extra arguments

# Installing jq
if ! command -v jq &> /dev/null
then
    echo "jq could not be found - installing"
    sudo apt install jq -y 
    sudo yum install jq -y 
fi


read -r INPUT_JSON
CMD=$(echo $INPUT_JSON | jq -r .parameters.alert.cmd)
CALLBACK=$(echo $INPUT_JSON | jq -r .parameters.alert.callback)
OUTPUT=$($CMD)
curl -XPOST $CALLBACK -d """$OUTPUT""" -k
``` 

2. Open /var/ossec/etc/shared/ar.conf and ADD the following line to the bottom of the file:
```
shuffle - shuffle.sh - 0
```

3. Restart the wazuh agent
```
/var/ossec/bin/wazuh-control restart 
```

4. Log into Shuffle and import [this public workflow](https://shuffler.io/workflows/44bc4e93-ba6e-4895-8294-424fd2a1d169). Make sure to change the following:
- Activate the Wazuh app if it's not already
- Add a Wazuh username & password to the HTTP node
- Add the Wazuh URL to the HTTP node, as well as Get_agents and other Wazuh nodes.
- Make sure the last block after "Get_agents" runs the command "shuffle" with the "Agent list" containing your specific agent's ID.

The default from this workflow is that it will reboot the server.

### TheHive
TheHive is a case management platform for and by security professionals. One of their key capabilities is webhooks, which can send realtime updates to a third party system whenever ANYTHING is changed within TheHive (e.g. a new alert or a case task is written). Shuffle has an ideal way of handling this, [outlined in this blogpost (TheHive4)](https://medium.com/shuffle-automation/indicators-and-webhooks-with-thehive-cortex-and-misp-open-source-soar-part-4-f70cde942e59).

**PS: There is a difference between TheHive3 and TheHive 4 on how to set this up. We are referring to TheHive4 in this section.**

1. Create a Workflow in Shuffle 
2. Add a Webhook to the Workflow
3. Configure TheHive with the Webhook URL
4. Test the integration

**1. Create a Workflow in Shuffle**
This one is pretty easily explained. Go to Shuffle an make a new Workflow.

**2. Add a Webhook to the workflow**
[Add a webhook](/docs/triggers#webhook) and find the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with TheHive](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with TheHive 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**3. Configure TheHive with the Webhook URL**
Configuring TheHive is the only unique step here, and is different between versions. Full documentation about [TheHive4 webhooks can be found here](https://github.com/TheHive-Project/TheHiveDocs/blob/master/TheHive4/Administration/Webhook.md).

As can be seen in the documentation, there are three steps to setting up TheHive webhooks: 
1. Define the webhook forwarder:

Find the [application.conf](https://docs.thehive-project.org/thehive/installation-and-configuration/configuration/manage-configuration/) file and scroll to the webhook section. If it doesn't exist, add the following:
```
notification.webhook.endpoints = [
  {
    name: Shuffle
    url: "http://IP:PORT/api/v1/hooks/webhook_hookid"
    version: 0
    wsConfig: {}
    includedTheHiveOrganisations: ["*"]
    excludedTheHiveOrganisations: []
  }
]
```

Modify it to have the URL you found making the webhook in Shuffle. You can also use https by adding certificate references to wsConfig{}

2. Restart TheHive
```
systemctl restart THeHive
```

3. Activate the webhook
Run this curl command (change the URL, username and password), which activates TheHive forwarding to Shuffle. 
**PS: Make sure you have access to the organization you want the Webhook for**
```
curl -XPUT -u$thehive_user:$thehive_password -H 'Content-type: application/json' $thehive_url/api/config/organisation/notification -d '
{
  "value": [
    {
      "delegate": false,
      "trigger": { "name": "AnyEvent"},
      "notifier": { "name": "webhook", "endpoint": "Shuffle" }
    }
  ]
}'
```

**4. Test the integration**
In TheHive UI (NOT CLI), create a new case, or add a comment to an existing case. This will then be seen within Shuffle. After the webhook is supposed to have triggered, go to Shuffle, and you'll see something like the image below.

![Extend Shuffle with TheHive 3](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_3.png?raw=true)

### Logzio 
**1. Create a Workflow which will receive alerts**
This one is pretty easily explained. Go to Shuffle an make a new Workflow.

**2. Add a Webhook to the workflow**
[Add a webhook](/docs/triggers#webhook) and find the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with Wazuh](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with Wazuh 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**3. Configure Logz.io forwarding**
After logging into app.logz.io, hover Settings Icon > Settings > click Notifications Endpoint. This will make all rules send alerts to the assigned webhook target.

![Extend Shuffle with Logz.io](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_4.png?raw=true)

Once in the notification endpoint view, click "Add Endpoint". Configure the following elements:
* Type: Custom
* Name: Shuffle (or some other identifier)
* URL: The Webhook URL from step 2
* Method: POST
* Data (should be autofilled): 
```
{
    "alert_title": "{{alert_title}}",
    "alert_description": "{{alert_description}}",
    "alert_severity": "{{alert_severity}}",
    "alert_event_samples": "{{alert_samples}}"
}
```

Custom data will be parsed into the field "alert_event_samples"

![Extend Shuffle with Logz.io 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_5.png?raw=true)

**4. Test the integration**
Click "Run the test" at the bottom before saving. This allows for it to send a sample payload to Shuffle.

If the data payload is configured as in step 3, the custom data will be available as such:
```
$exec.alert_event_samples
```

![Extend Shuffle with Logz.io 3](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_6.png?raw=true)

### MISP
MISP, short for Malware Information Sharing Platform, is one of the best Open Source alternatives for Threat Intelligence. For that reason, a lot of our users have wanted a way to handle data in realtime from MISP. What kind of data? Event updates, indicator updates, IDS flag edits, Organization edit etc.

That's why we released an extension for Shuffle which can read ZMQ messages from MISP in realtime and send them to a webhook.

[More information here](https://www.circl.lu/doc/misp/misp-zmq/)

**Steps to set it up:**
1. Enable ZMQ in MISP by going to Server Settings -> Plugins in MISP. Make sure to enable the options for forwarding Events and Attributes.
2. Install pyzmq and redis on the MISP server: 
```
pip3 install pyzmq redis
```
3. Go to Shuffle and create a new Webhook
4. [Install Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) on a host with access to ZMQ (localhost:50000 by default). This can be on the MISP server, but at scale, it preferably shouldn't be.
5. Copy the docker-compose [found here](https://github.com/frikky/Shuffle/tree/master/functions/extensions/misp/docker-compose.yml) and edit the environment variables to point to your ZMQ instance (PS: Don't use localhost, even if it's on the MISP server)
```
version: '3'
services:
  zmq:
    image: ghcr.io/frikky/shuffle-zmq:latest
    container_name: shuffle-zmq
    hostname: shuffle-zmq
    environment:
      - ZMQ_HOSTNAME=10.1.2.3
      - ZMQ_PORT=9000
      - ZMQ_FORWARD_URL=<WEBHOOK_URL>
    restart: unless-stopped
```
6. Run the docker-compose!
```
docker-compose up -d
```
7. Test it by going to your MISP instance and changing an event or attribute

### AWS S3 forwarder
Ever wanted to run an action as soon as something is uploaded to your S3 Bucket? Maybe you just want to build an S3 honeypot? If so, this part is for you. Herein we describe how you can get information about files being uploaded or changed from an S3 bucket into Shuffle.

**Basic overview:**
User -> Upload to S3 -> S3 triggers Lambda function -> Lambda function triggers Webhook -> File is downloaded from within Shuffle

Steps to set it up:
1. Create a Workflow with Webhook inside Shuffle
2. Create a Lambda function that triggers on S3 changes
3. Configure the workflow to download the file
4. **Optional**: Scan file with Yara

![AWS lambda overview](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-1.png?raw=true)

**1. Create a Workflow which will receive alerts**
This one is pretty easily explained. Go to Shuffle an make a new Workflow. [Add a webhook](/docs/triggers#webhook) and find the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with webhook](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with webhook2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**2. Create the lambda function**
- After logging into your AWS, go to [Lambda functions](https://console.aws.amazon.com/lambda/home) and click "Create function" in the top right corner. 

- Use "Author from scratch", and type in a name like "Shuffle-forwarding" and make sure to choose Runtime as Python 3.8. Click "Create function" in the bottom right corner.
![Author S3 from scratch](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-2.png?raw=true)

- Click "Add trigger" in the window, left of the function. In the next menu find "S3", before choosing the bucket you want and the "Event type". Click "Add trigger"
**PS: The bucket and cloud function have to be in the same location**
![Add trigger](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-3.png?raw=true)

- Under Configuration > Environment variables, click "Edit". Add variable with key "SHUFFLE_WEBHOOK", and the value from step 1. Click "Save".
![Configure s3 environment](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-4.png?raw=true)

- Time to add some code. Go to the "code" tab and paste in the code below. Click "deploy". This should now forward the request to Shuffle. 
```
import json
import urllib.parse
import requests
import os

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    #bucket = event['Records'][0]['s3']['bucket']['name']
    
    webhook = os.environ.get("SHUFFLE_WEBHOOK")
    if not webhook:
        return "No webhook environment defined: SHUFFLE_WEBHOOK"
        
    ret = requests.post(webhook, json=event["Records"][0])
    if ret.status_code != 200:
        return "Bad status code for webhook: %d" % ret.status_code
        
    print("Status code: %d\nData: %s" % (ret.status_code, ret.text))
```

**3. Configure and test the workflow**
To test the previous step, we have to upload a file to the chosen S3 bucket. If everything is connected correctly, this will trigger an event to come into Shuffle. If it doesn't, have a look at the Lambda function's logs, or [contact us](https://shuffler.io/contact).
![S3 data in Shuffle](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-6.png?raw=true)

Now all we need is to do is actually download the file. This requires access rights to the bucket itself from the API in use. The app we use for this is the "AWS S3" app, with the action "Download file from bucket". See the next image for how to configure this action after authenticating it. (We may add file uploads to webhooks in the future).
![Configure s3 environment](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-5.png?raw=true)

And that's it! All file updates should now come into Shuffle, including a way to download the file.


**4. Extra: Scan the file with Yara**
In a lot of cases you would want to analyze the files somehow. But how..? Shuffle has a built in way to run Yara on files, and get results based on built-in rules (or your own). Most of the time, you would also want a response to that search, hence we've created a way to also delete the file if it matches too many Yara rules.
![Basic s3 analysis](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-7.png?raw=true)

To do this, add in the "Yara" node with the action "Analyze file", and put "$get_s3_file.file_id" in the "File Id" field. This should match the file downloaded from the bucket.

After this, add another S3 node, and choose the action "Delete file from bucket" with these parameters:
- Bucket Name: $exec.s3.bucket.name
- Bucket Path: {{ "$exec.s3.object.key" | url_decode | replace: "+", " " }}

Last but not least, we need a way [to see IF](/docs/workflows#conditions) the file should be deleted. This can be done by clicking the branch between Yara and the S3 delete action > "New Condition" > with the following data: 
```
{{ $run_yara.matches | size }} > 3
```
![S3 condition yara](https://github.com/frikky/shuffle-docs/blob/master/assets/s3_function-8.png?raw=true)

Done! Whenever a file is downloaded, it will be analyzed by Yara, checking matches, then removing the file if it's more than 3.

### QRadar

**QRadar send offense webhook to Shuffle.**

***STEP 1: Add the Script to QRadar & Config***

> **Bash Code:**
```
#!/bin/bash
# Version 1.0.0

shuffle_url=$1
api_token=$2
offense_id=${3%.*}

auth_header="SAuthorization:$api_token"

output=$(curl --insecure -H $auth_header $shuffle_url -d "$(cat <<EOF
{
        "offense_id": $offense_id
}
EOF
)")

# Basic print out of the output of the command
echo $output
```

a) Log In to QRadar;
			
b) Go to Admin > Custom Actions > **Define Actions**;	
			
c) Click **Add**;
			
d) Fill the Basic Information (name & description);
			
e) In the Script Configuration set **bash** as interpreter, and import the bash script attached to this message;	
			
f) For the Script Parameters, add the parameters in the following order:
			
1. [Fixed Property] **shuffle_url** - As value insert the Shuffle Webhook URI, for example https://shuffle.local/api/v1/hooks/webhook_15acc....
			
2. [Fixed Property] **authorization** - Insert the Required headers (**SAuthorization**), for example in Shuffle webhook if you set **SAuthorization=s873hn872n_s298ns2-98ns2ns** in the Required headers you authorization value will be "s873hn872n_s298ns2-98ns2ns". *If you change the token name, don't forget to change it in the bash code too*.
			
3. [Network Event Property] **offense_id** - Insert **offense_id** as value 
			
g) Save
			
h) Deploy Changes

![image](https://user-images.githubusercontent.com/21691729/152444978-d360680a-a0b1-40b0-bd04-fa7395cf4d85.png)
![image](https://user-images.githubusercontent.com/21691729/152445000-0d2a1828-ee1d-41b1-a549-5417c9a48c75.png)
		
***STEP 2: Create new offense alert rule***
			
a) Go to Offenses > **Rules**;
			
b) Click Actions > **New Event Rule**:
```
    Rule Description
      Apply Shuffle new offense alert on events which are detected by the Local system
and when the event QID is one of the following (28250369) Offense Created
 
    Rule Responses
      Execute Custom Action QRadar to Shuffle  (previous added script)

This Rule will be: Enabled
```

***Conclusion***
>  **Why use this use case?**
			
 Easy, this way each time a new offense dispatches in QRadar it will send a webhook to Shuffle containing the offense_id, then the webhook node will receive this info and pass it to the next node (QRadar App) that will perform a **get offense** ~~data~~ action using the received offense id as key.
			
 This way you won't need to execute an api call every x time and save the last offense id. This is a better solution and improves the SLA, coz if you set 1 minute as you x time, you may have 1 minute delay or less, besides you are getting all "ungotten" offenses at once, when you can use shuffle to handle with multiple at the same time if it happen to dispatch more than one offense in QRadar at the same time or with just some seconds of difference.

### FortiSIEM
FortiSiEM is the SIEM of Fortigate. It has the possibility of notifying Shuffle through a webhook when a rule triggers, which is exatly what this documentation section is for. The main caveat: all data is XML and needs to be transformed with the Shuffle Tools "XML to JSON" formatter.
	
**1. Create a Workflow which will receive alerts**
This one is pretty easily explained. Go to Shuffle an make a new Workflow.

**2. Add a Webhook to the workflow**
[Add a webhook](/docs/triggers#webhook) and get the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with Wazuh](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with Wazuh 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**3. Configure FortiSIEM forwarding**
Log into the UI. When inside, go to ADMIN > Settings > Incident Notification. In the "Incident HTTP Notification", paste in the webhook from the previous step. Click "save", then "Test". After the test, check the workflow in Shuffle whether it triggered. If it didn't, your FortiSIEM can't access the Shuffle instance.
	
![image](https://user-images.githubusercontent.com/5719530/162085936-58a44de4-0289-4cf9-8f72-7b3229857448.png)
	
With the Notification Endpoint specified in the previous step, we need to decide what rules to add. By default, we add all of them. To do this, go to ADMIN > Settings > Notification Policy, and add a new policy. In here, select the "Send XML file over HTTP(S) to the destination set in...". This will make sure all alerts are sent to Shuffle.
	
![image](https://user-images.githubusercontent.com/5719530/162086144-8bbfb6fa-d512-4c36-81db-f830bcf9c204.png)

That's it! It's now time to wait for an alert to actually trigger. When it has, make sure to send Execution Argument from the webhook ($exec) straight into an XML to JSON parser. That way you can use it easily in Shuffle.

	
### ELK
TBD: Kibana forwarding & ElastAlert
	
### Cortex 
TBD: Responder executions
