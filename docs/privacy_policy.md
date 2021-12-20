# Privacy Policy
This is the initial privacy policy for Shuffle cloud. Valid as of this file's last change date on [Github](https://github.com/frikky/shuffle-docs/blob/master/docs/privacy_policy.md).

## Table of contents
* [Introduction](#introduction)
* [Analytics](#analytics)
* [Data Location](#data_location)
* [Infrastructure Monitoring](#infrastructure_monitoring)
* [External social media platforms](#external_social_media_platforms)
* [External platforms](#external_platforms)
* [User Data Management](#user_data_management)
* [Contact Information](#contact_information)

## Introduction
We are Shuffle AS, and this privacy policy will tell you how we use and protect your personal data.

## How we protect your personal data
We understand the importance of the data we collect on our customers, and the sensitivity of what our customers may want to use our platform for. The following items 

### Encryption
Shuffle utilizes [Google Cloud Platform's Datastore](https://cloud.google.com/datastore/docs/concepts/encryption-at-rest) and [Google Cloud Storage](https://cloud.google.com/storage). We encrypt all your data by default, and have extra mechanisms for API-keys and secrets inserted. [All our code for encryption can be accessed here.](https://github.com/Shuffle/shuffle-shared)

### Session Management
Utilizing Google Cloud Platform and internal audit logs, we track all sessions and changes in Google Cloud's [Cloud Logging](https://cloud.google.com/logging). 

### Two-factor authentication and Single Sign-on
Shuffle has added SSO and Two-factor authentication to any user for free, protecting from fraudulent access of your Shuffle account. [Read more here on SSO and MFA](https://shuffler.io/docs/extensions#single_signon_sso).

### Organization data access
We do not permit our team direct access your organization or data within the Shuffle platform without your explicit consent. During support investigations, we may utilize internal tools to simulate your user, but will never directly get information about you or your organization from our data storage solutions. To learn more about organizations, [click here](https://shuffler.io/docs/organizations). 

### Data processing usage 
We store your data for 3 years by default, to be used in an anonymous and sanitized way, to create algorithms for better workflow autocompletion.

We intend to add a way for you to periodically clear your data in 2022.

### Sharing of data with 3rd parties
Shuffle does not share data with any 3rd parties, except our support partner [Infopercept](https://infopercept.com/). We do however have third party services where your data may be stored - all listed in the segmented details below.

## Segmented details 
### Analytics
* Platforms: Google Analytics, Segment
* Personal data: Cookies, Usage Data, Browser storage

### Data Location
* As of 18.12.2021, all information is saved in [Google's europe-west2 location (London)](https://cloud.google.com/compute/docs/regions-zones). We intend to add more regions and data-storage options from Q4 2022.

### Infrastructure Monitoring
* Snyk: Monitors for Infrastructure, Code and Container vulnerabilities.
* GitGuarding: Monitors for potential credentials lost within or outside our infrastructure.
* Google Cloud Platform: Alerts, Notifications and logs for up/downtime. 

### Payment processor
We use the third party payment processor [Stripe](https://stripe.com/us/privacy). We do not retain any of the information provided to them during a transaction.

### External Platforms 
1. Sendgrid: Emails used for email 
2. Twilio: Phone numbers used for SMS
3. Github: Apps and Workflows shared by our users
4. Stripe: Payments
5. Fiken: Accounting 
6. Google Drive: General storage
7. Discord & Signal: Communication

### User Data Management
* Collected data: Email addresses, Domains, Organization names, Firstname, Lastname, Authentication keys
* Usage: User signin and Email outreach 

### User Creations 
1. Apps: Optional sharing with everyone
2. Workflows: Optional sharing with everyone

### Customer detail storage
* Google Workspace: Google drive, Gmail

### Contact Information
Data Controller: Shuffle AS
Contact info: [frikky@shuffler.io](mailto:frikky@shuffler.io)
