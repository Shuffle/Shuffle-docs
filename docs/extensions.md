# Shuffle extensions
This is documentation for integrating and sending data from third-party services to Shuffle. Not to be confused with [apps](/apps) and [workflows](/workflows)

# Table of contents
* [Introduction](#introduction)
* [Wazuh](#wazuh)
* [TheHive](#thehive)
* [Logz.io](#logzio)

## Introduction
From the start, Shuffle has been a platform about integrations. We've focused on making them as open and usable as possible, but were missing one part; inbound data. The general way Shuffle handles this has been through third-party API's, where we poll for data on a schedule. There are however some cases where this doesn't do the trick. That's what extensions are. 

These integrations will typically entail third party services connecting to Shuffle with inbound Webhooks as triggers in a workflow.

# Wazuh
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
Add a webhook and find the Webhook URL. Remember to start the Webhook!

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

3. Change their ownership to ossec:ossec. This MAY be necessary if Wazuh doesn't have root priviliges
```
$ chown ossec:ossec custom-shuffle
$ chown ossec:ossec custom-shuffle.py
```

4. Configure ossec.conf to forward to Shuffle 

Go to the location /var/ossec/etc/ossec.conf (or where the ossec.conf file is). Take the information below (including <integration>) and paste it in. Find the webhook URL from earlier, copy it and add it to the <hook_url> section. 

Find more fields like [levels, groups and rule_id here](https://documentation.wazuh.com/current/user-manual/manager/manual-integration.html).

```
	<integration>
		<name>custom-shuffle</name>
		<level>9</level>
		<hook_url>http://<IP>:<PORT>/api/v1/hooks/webhook_<HOOK_ID></hook_url>
		<alert_format>json</alert_format>
	</integration>
```

5. Restart ossec manager. Every time you change ossec.conf, you need to restart the ossec manager.
```
systemctl restart wazuh-manager.service
```

**4. Test the integration**
There are many ways to test the integration, but you can simplify it by setting the "level" part of the configuration to a lower number (3~), as that would trigger it in a lot of cases, including when you SSH into the Wazuh manager. After an alert is supposed to have triggered, go to Shuffle, and you'll see something like the image below.

![Extend Shuffle with Wazuh 3](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_3.png?raw=true)


# TheHive
TheHive is a case management platform for and by security professionals. One of their key capabilities is webhooks, which can send realtime updates to a third party system whenever ANYTHING is changed within TheHive (e.g. a new alert or a case task is written). Shuffle has an ideal way of handling this, [outlined in this blogpost (TheHive4)](https://medium.com/shuffle-automation/indicators-and-webhooks-with-thehive-cortex-and-misp-open-source-soar-part-4-f70cde942e59).

**PS: There is a difference between TheHive3 and TheHive 4 on how to set this up. We are referring to TheHive4 in this section.**

1. Create a Workflow in Shuffle 
2. Add a Webhook to the Workflow
3. Configure TheHive with the Webhook URL
4. Test the integration

**1. Create a Workflow in Shuffle**
This one is pretty easily explained. Go to Shuffle an make a new Workflow.

**2. Add a Webhook to the workflow**
Add a webhook and find the Webhook URL. Remember to start the Webhook!

![Extend Shuffle with TheHive](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_1.png?raw=true)

Copy the URL and keep it for the next steps
![Extend Shuffle with TheHive 2](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_2.png?raw=true)

**3. Configure TheHive with the Webhook URL**
Configuring TheHive is the only unique step here, and is different between versions. Full documentation about [TheHive4 webhooks can be found here](https://github.com/TheHive-Project/TheHiveDocs/blob/master/TheHive4/Administration/Webhook.md).

As can be seen in the documentation, there are three steps to setting up TheHive webhooks: 
1. Define the webhook forwarder:

Find the application.conf file and scroll to the webhook section. If it doesn't exist, add the following:
```
notification.webhook.endpoints = [
  {
    name: Shuffle
    url: "http://<IP>:<PORT>/api/v1/hooks/webhook_<HOOK_ID>"
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
Run this curl command (change the URL), which activates TheHive forwarding to Shuffle. 
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
There are many ways to test the integration, but you can simplify it by setting the "level" part of the configuration to a lower number (3~), as that would trigger it in a lot of cases, including when you SSH into the Wazuh manager. 

In TheHive, create a new case, or add a comment to an existing case. This will then be seen within Shuffle. After the webhook is supposed to have triggered, go to Shuffle, and you'll see something like the image below.

![Extend Shuffle with TheHive 3](https://github.com/frikky/shuffle-docs/blob/master/assets/extensions_example_3.png?raw=true)

# Cortex 
TBD: Responder 

# Logzio 
