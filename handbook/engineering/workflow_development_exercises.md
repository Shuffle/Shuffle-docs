# Workflow development exercises 
This document contains exercises for learning to use the various tools of Shuffle. It's a work in progress.

## Introduction
Please start by following our [introductory tutorial on Medium](https://medium.com/shuffle-automation/introducing-shuffle-an-open-source-soar-platform-part-1-58a529de7d12) and reading the [Workflow documentation](http://shuffler.io/docs/workflows).

## Techniques to understand in depth
1. Variables
2. JSON
3. Loops
4. Nestedloops
5. Start node
6. Triggers
7. Liquid formatting
8. Subflows
9. Shuffle Cache
10. Shuffle File storage 
11. App Authentication

## Use-case exercises
To learn about how to do common things with Shuffle, we suggest trying to make the following use-cases.

### 1. Communication: Email!
The goal of this workflow is to get emails, and analyze whether the sender's IP is malicious, and adding it to Shuffle cache for whether it's analyzed. 

1. Make a Workflow that gets your new emails, and marks them as read. Use either Gmail, Outlook, the Email app OR any of the email triggers.
2. From the same emails, parse out indicators of compromise (IoC's)
3. Parse out any IPs and run a GreyNoise community search for whether they're malicious IF 
4. If it's found to be malicious, add it to the cache list "malicious_ips", otherwise add it to "benign_ips"

- Schedules, Whois

### 2. Cases: Issue management with Jira 
The point of this usecase is to learn to make jira, list them, and analyze their contents, before taking action.

1. Make a user on Jira here: [Jira download](https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=95003655569&campaign=9124878867&creative=415542762940&device=c&keyword=jira%20software%20sign%20up&matchtype=e&network=g&placement=&ds_kids=p51242194601&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=CjwKCAiA5t-OBhByEiwAhR-hmx8BfX8_S0SEAnN5pj0Lka1qmQ7G0-IqZOrwkL3JZYe_Rxp1i3RwBRoCLuwQAvD_BwE&gclsrc=aw.ds)
2. Use Shuffle to create a issue with the title "This is a test issue for handling malware"
3. Use the file system in Shuffle to create AND upload the Eicar test file to the same issue: https://secure.eicar.org/eicar.com.txt
4. List ALL issues (NOT JUST ONE) on your Jira account. Look for whether they have attachments in them.
5. Based on the previous issues with attachments, find THE issue that you just made in step 2.
6. With the ticket in hand, re-download the file to Shuffle.

### 3. Intel: Continuous analysis for changes
The point of this workflow is to make a list of indicators, and searching for if their data changes.

1. Make a file with 5 IPs inside of it, then upload it to Shuffle 					(Files)
2. Parse the file into a JSON list within Shuffle, making it usable 				(Liquid / Shuffle Tools)
3. Use [IPInfo](https://ipinfo.io/signup) to analyze them every 30 minutes 	(Cache & Schedule)
4. If the data changes between those 30 minutes, send yourself an email notifying you. 

PS: You can test whether it changed by setting the value manually in the next iteration.

### 4. SIEM: Run a search in Wazuh and add IP to list
The point of this exercise is to use Wazuh to create a threat list, and alert on matches.

1. Create a threat list within Wazuh (?)
2. Create a rule for that threat list in Wazuh, and forward alerts for that rule to Shuffle (webhook, extensions)
3. Take a list of 5 IPs, and add them to the threat list in Wazuh
4. Modify the threat list with 5 new IPs, and ensure it alerts you from an Email.

### 5. Networking: Block IP based on user input
PS: Do #4 first. 

From #4, WHEN an alert is created, ALSO block that IP in Amazon AWS s3 AND Amazon AWS VPC where the server is if a user wants it based on SMS or Email (?).

### 6. Eradication: Run a script on a host
With Wazuh, we want to run a script on a host to block all incoming network traffic

### 7. Asset Management: Find asset, and ask their owner whether you can auto-patch it in the background
### 8. Identity Access Management:
