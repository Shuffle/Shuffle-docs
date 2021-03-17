# Security Category Framework 
This document outlines our categories and their sub-categories, and is intended for anyone who wants to build and understand more about Shuffle and security. Original presentation: [Developer Intro](https://docs.google.com/presentation/d/1Se2NLPK-CjzccOZjRtfLzqrKG63QOgN1tAp35gWmZlU/edit?usp=sharing)

## Introduction
Security is hard. So hard in fact, that the only way to really be secure is by not having anything online. But that doesn't lead to anything. A major issue with security operation teams today is that they don't necessarily know how secure they are, nor how they can become "more secure". That's what we intend to solve with this framework. It's made to outline what we're basic everything on, and how each type of platform can be used. This will further lead to proper process and process implementation in the ways of Workflows, as well as KNOWING what is and isn't secure.

## What is a SOC?
As we're building for a SOC, we need to know what a SOC is. Here's the definition from [Wikipedia](https://en.wikipedia.org/wiki/Security_operations_center):

"A security operations center (SOC) is a centralized unit that deals with security issues on an organizational and technical level. It comprises the three building blocks people, processes, and technology for managing and enhancing an organization's security posture. Thereby, governance and compliance provide a framework, tying together these building blocks. A SOC within a building or facility is a central location from where staff supervises the site, using data processing technology. Typically, a SOC is equipped for access monitoring, and controlling of lighting, alarms, and vehicle barriers."

### Key points
- They are protecting a unit, whether that is their own company or a customer
- Attackers vs. Defenders. _When_ someone is in your network, you should know evil. 
- Housed by Security Analysts, Threat Intel Analysts, Malware Analysts and experts at DFIR among others.
- Typically "firefighting" - AKA doing the same thing every day, which leads to quick burnout.

Other resources:
[What is a SOC? (McAfee)](https://www.mcafee.com/enterprise/en-us/security-awareness/operations/what-is-soc.html)
[What is a Security Operations Center (SOC)?](https://digitalguardian.com/blog/what-security-operations-center-soc)

Here's our starting point:
![Shuffle-workflow-categories](https://github.com/frikky/shuffle-workflows/blob/master/images/categories_circle_dark.png)

## Our categories 
These are the categories you saw in the image above. They are in order of "difficulty to understand". You can read more about each one further down in this document

1. [Communication](https://github.com/frikky/Shuffle-apps/issues/26) 		- Any way to chat; WhatsApp, SMS, Email etc. 
2. [Case Management](https://github.com/frikky/Shuffle-apps/issues/22)	- The central hub for operation teams.
3. [SIEM](https://github.com/frikky/Shuffle-apps/issues/21)							- Search engine for logs in an enterprise. Used to find evil.
4. [Assets](https://github.com/frikky/Shuffle-apps/issues/25) 					- Discover endpoint information. Vulnerabilities, owners, departments etc.
5. [IAM](https://github.com/frikky/Shuffle-apps/issues/86)  						- Access Management. Active Directory, Google Workspaces, Single Sign-on etc.
6. [Intelligence](https://github.com/frikky/Shuffle-apps/issues/24) 		- Typically a vendor explaining what you should be looking for.
7. [Network](https://github.com/frikky/Shuffle-apps/issues/27)					- Anything BETWEEN your connected devices. Firewalls, WAF, Switches, Bluetooth...
8. [Eradication](https://github.com/frikky/Shuffle-apps/issues/23) 			- Control machines directly to eradicate evil. Hard and undefined (EDR & AV)

TBD: Everything below here

### Communication (Comms)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Case Management (Cases)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Security Incident and Event Management (SIEM)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Asset Management (Assets)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Identity Access Management (IAM) 
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Threat Intelligence (Intel)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Network (Network)
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:

### Eradication (Eradication) 
Sub-categories:
Synonyms:
What is it?
How can it be used?
How is it connected?
Typical problems:
