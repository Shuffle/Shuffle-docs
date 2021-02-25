# App Development 
This document outlines a process for app development. [Developer Intro](https://docs.google.com/presentation/d/1Se2NLPK-CjzccOZjRtfLzqrKG63QOgN1tAp35gWmZlU/edit?usp=sharing)

## Introduction
App development is at the heart of how we grow. Without apps, Shuffle as a product and solution is useless. Together with Workflows, Apps can solve can solve any problems our customers, and users may be seeking. Our goal is to make automation accessible to everyone through collaboration, and app development a huge part of that. 

## Who we're building for
Our target market are the people running [security operation centers](https://digitalguardian.com/blog/what-security-operations-center-soc). These exist around the world and at the frontlines, stopping bad behavior from malicious actors trying to cause harm. This means they're always on their toes - which in turn means they don't have much time for process and automation. That's where Shuffle comes in. We make it as simple as possible to get their existing platforms up and running, which giving them actionable advice on how to improve their defenses. Cybersecurity isn't a competition.

## Categories
We have defined eight (8) main categories of tools that are necessary to tackle any cybersecurity threat. They are as follows:
1. Communication 		- Any way to chat; WhatsApp, SMS, Email etc. 
2. Case Management	- The central hub for operation teams.
3. SIEM							- Search engine for logs in an enterprise. Used to find evil.
4. Assets 					- Discover endpoint information. Vulnerabilities, owners, departments etc.
5. IAM  						- Access Management. Active Directory, Google Workspaces, Single Sign-on etc.
6. Intelligence 		- Typically a vendor explaining what you should be looking for.
7. Network					- Anything BETWEEN your connected devices. Firewalls, WAF, Switches, Bluetooth...
8. Eradication 			- Control machines directly to eradicate evil. Hard and undefined (EDR & AV)

### Difficulty of creation 
The categories above are sorted as per their percieved difficulty to understand and build for, from easiest to hardest. This doesn't just include the platforms individually, but how they're integrated with other platforms. If you're new to security, we highly encourage starting in range 1-5, but if you wan't a challenge - move on :)

## Before you start  
We want to make security a more collaborative space, but everyones trying to lock you into their services. We're trying to stop that by using standards that work outside of Shuffle. Apps that are shared are made public through [Security-Openapi](https://github.com/frikky/security-openapis) [Shuffle-Apps (Python)](https://github.com/frikky/shuffle-apps), then searchable with the help of Algolia.com. By making it and sharing using our app creator you will also stop any gatekeeping in the automation industry, as we also allow others to automate in a good way. 

Create a new app with HTTP here: 			[https://shuffler.io/apps](https://shuffler.io/apps)
Learn about Python App Creation here: [https://shuffler.io/docs/app_creation](https://shuffler.io/docs/app_creation)

Last but not least; make sure to document every step and have fun :D

## Basic Process
1. [Find an app of interest in the todo](https://github.com/frikky/Shuffle-apps/projects/1) that hasn't been made yet.
2. Validate: Does it actually exists or not with [shuffler.io](https://shuffler.io/search), [openapi](https://github.com/frikky/security-openapis) or [python](https://github.com/frikky/shuffle-apps)
3. Find: Explore the applicable services' website and get access through either: 
	* Sign up for an account
	* Set it up locally (open source)
	* Ask for a demo (they'll usually send a mail in minutes)
	* Other options (please share)
4. Discover: Get access to their API documentation, and search for OpenAPI/Swagger if possible.
5. Decide: if you should make it with the App Creator or Python. Always use the App Creator when possible. There are certain authentication mechanisms we can't do with Shuffle yet, but which we may have long-term (oAuth2, AWS boto3 timestamps etc.)
6. Creation: This is where we rely on your expertise for ease of use. Remember that we're making this for non-developers, and less mandatory fields is always better. Don't forget:
	* Add examples to the API-call 
	* Write down anything that was confusing. It may be useful.
	* Simplify
7. **TEST**: This is an increasingly important step as we get more integrations on our hand. Don't just test it individually, but test it with other apps in a Workflow. Example: try to syncronize data from what you made with a case management system. Or send a webhook to Shuffle which adds data to it. KEEP these use-cases and make them clear - they can be shared as test-examples.
8. Document: Throughout the process, we expect you to document steps. In most cases, we want it in Markdown format. [Here's a very simple example](https://github.com/frikky/security-openapis/blob/master/docs/discord.md) This may seem tedious, but is EXTREMELY important to keep everyone else up to speed with what you do. 
9. Sharing: Congrats, you're done! All your hard work can now be shared with the world, and we're all that tiny bit more secure. Sharing can be done by:
	OpenAPI: Export the app from the GUI, then make a pull request to the [security-openapi](https://github.com/frikky/security-openapis/compare) repository. Add documentation to the ./docs folder with the same name.
	Python: Make a pull request to the [shuffle-apps](https://github.com/frikky/shuffle-apps/compare) repository. 

## What happens next?
Someone from the Shuffle team will validate the app you submitted and accept it. The last part may become possible through https://shuffler.io at some point.

## Credits
We want YOU to get the credits for what you create and celebrate you. This means you'll be highlighted when the app is published on shuffler.io as well (if you want).
