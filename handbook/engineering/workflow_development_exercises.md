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

### 2. Cases: Ticket management with PagerDuty 
The point of this usecase is to learn to make tickets, list them, and analyze their contents, before taking action.

1. Make a user on Pagerduty here: [https://www.pagerduty.com/sign-up/](https://www.pagerduty.com/sign-up/)
2. Use Shuffle to create a ticket with the title "This is a test ticket for handling malware"
3. Use the file system in Shuffle to create AND upload the Eicar test file to the same ticket: https://secure.eicar.org/eicar.com.txt
4. List ALL tickets on your Pagerduty account and look for whether they have files in them. You should find the ticket you made above. 
5. With the ticket, re-download the file to Shuffle.

### 3. Intel: Continuous analysis for changes
The point of this workflow is to make a list of indicators, and searching for if their data changes.

1. Make a file with 5 IPs inside of it, then upload it to Shuffle 					(Files)
2. Parse the file into a JSON list within Shuffle, making it usable 				(Liquid / Shuffle Tools)
3. Use [IPInfo](https://ipinfo.io/signup) to analyze them every 30 minutes 	(Cache & Schedule)
4. If the data changes between those 30 minutes, send yourself an email notifying you. 

PS: You can test whether it changed by setting the value manually in the next iteration.

**TBD:**
### 4. SIEM: Run a search and make a rule
### 5. Networking: User input to block an IP
### 6. Eradication: List alerts and clean up  
### 7. Asset Management: 
### 8. Identity Access Management:
