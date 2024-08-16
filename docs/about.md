# About Shuffle
Shuffle started as a project in mid-2019 because of a few automation related problems that needed more attention in the [CERT/SIRT](https://en.wikipedia.org/wiki/Computer_emergency_response_team) community. Available automation solutions in the security industry are trying to do everything at once; handle tickets, indicators, threat intel and much more in a single platform, while our goal is to build the best solution to fit all your existing tools following the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well): "Do One Thing and Do It Well". 

[![Shuffle Overview PDF](https://raw.githubusercontent.com/Shuffle/Shuffle-docs/master/assets/Shuffle%20Overview.png)](https://raw.githubusercontent.com/Shuffle/Shuffle-docs/master/assets/Shuffle%20Overview.pdf)

## Mission
To make every security operations center share their processes, automations and detections in a standardized way. Cybersecurity is not a competiton, and shouldn't treated as such.

## Open Source
Focus for Shuffle has moved to an entirely open ecosystem. This includes, but is not limited to; the Shuffle product, open workflows, open apps, open standards (OpenAPI, Swagger).

## Roadmap
The Roadmap is our high level guide to the future, and may be reorganized without notice according to more immediate needs. 

* 0.1 - 0.5: Created basic features for automation, as well as use cases and frontend. This was before the project was open sourced.
* 0.6 - Usability: High focus on the workflow and api editor, as well as bugfixing after open sourcing. 
* 0.7 - Improve: First larger release of Shuffle. Focus on organizations, users, schedules, app authentication and a better overview in general through the admin view.
* 0.8 - Integrate: Hybrid cloud features and file control/cross-workflow data management
* 0.9 - Features: Search engine for apps, workflows, executions etc. GCP (Storage & Functions) integration usage for cloud.
* 1.0 - Launch: Categorized apps, proper use-cases, and a real tutorial mapped to use-cases. Enterprise-ready (SSO/SAML, MFA, Reporting, Statistics, Replayability)
* **1.1 - [Creator onboarding](https://github.com/Shuffle/Shuffle/releases/tag/1.1.0):** Workflow, App & Usecase discovery. Stability & Scalability everywhere with multi-region deployments. HUGE focus on on-boarding and workflow templates. Expected release Q4 2022.
* 1.2 - Usability: Autocompletes, Suggestion engines, Dashboards, Auditing. Lambda & EKS integrations. Partnerships with top 5 relevant tools in each [App Category](https://shuffler.io/welcome?tab=2). Threat Intel management with Shuffle Datastore. Expected release Q2 2023. 
* 1.3 - Scale support, workflow statistics, stabilization and tracking.  Expected release Q4 2023.
  
* 1.4 - **Current release:** Realtime Workflow Collaboration (+support workflow support cloud->onprem), Workflow Generation based on text, MSSP Tenant & Workflow Management, Dynamic Authentication, Vaults, Improved Coding Editor with Code Generator & Shuffle Functions, Improved Trigger management and branding, Hybrid Workflow Access. Kubernetes support. Expected release Q2 2024.
  
* **In Development:** API Standardization & Security Infrastructure as a Service: **Schemaless**, Workflow & Usecase generation, Technology Partnerships, OpenID/SAML testing & management mechanisms, Developer Friendliness, Form & MQ Triggers, Mitre D3FEND and Att&ck tracking, automatic Sigma and Sublime detection mechanisms. AI for Documentation -> App generation + API action merging from forks. Auth Proxy tests and Multi-Tenant Workflows. Expected release: November-December 2024.

* After next release: OASIS OpenC2 & CACAO support. Creator & Community earning re-initialization. Focus on App, Workflow, Detection and Response ruleset sharing. Add Yara+Sandbox autoscans, Ansible response playbooks and OSQuery asset mapping. Expansive Mitre Att&ck & D3FEND support. Support for JSON-schema & Postman Collections. Optimize Realtime Workflow Collaboration. 
    
## Blogposts
* [Introducing Shuffle](https://medium.com/security-operation-capybara/introducing-shuffle-an-open-source-soar-platform-part-1-58a529de7d12)
* [Getting started with Shuffle](https://medium.com/@Frikkylikeme/getting-started-with-shuffle-an-open-source-soar-platform-part-2-1d7c67a64244)

## Problems Shuffle solves 
These included, but were not limited to (no specific order):
* [Alert fatigue](https://en.wikipedia.org/wiki/Alarm_fatigue) by giving analysts the tools to automate most alerts
* Remove menial tasks, decreasing employee turnover
* Quick integrations with new tools - OpenAPI
* Giving you a clear overview of your environment by tracking integration usage

Regards,

Fredrik Ødegårdstuen - [@frikkylikeme](https://twitter.com/Frikkylikeme) - [frikky@shuffler.io](mailto:frikky@shuffler.io)
