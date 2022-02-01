# Keycloak Saml SSO

* Go create a realm in your keycloak by clicking the add realm button

![31 01 2022_19 01 10_REC](https://user-images.githubusercontent.com/31187099/151965784-1798e815-1e57-4720-a875-ba379610a38e.png)

* Enter a name for your realm
* Click create and your realm is created
* Under configure, move down to identity providers, on the pop up, click on the drop down select SAML v2.0

* An add identity provider window pops up where you can configure your identity provider and SAML configs.
* Here you will fill the:
    - Alias field
    - Display name
    - Ensure Enabled field is turned on
    - Ensure Trust Email field is turned on
    
![01 02 2022_11 39 39_REC](https://user-images.githubusercontent.com/31187099/151965938-3bddb6e8-6819-41dc-b6ae-85cd0b56b31e.png)

* Still on this window scroll down to SAML Config and click on this to drop down the settings

![01 02 2022_11 45 52_REC](https://user-images.githubusercontent.com/31187099/151966312-33b75cec-3906-4485-8c58-26d77dd2ef84.png)

* Here you will fill the:
    - Service Provider Entity ID - Scroll up to the Redirect URI and copy everything BEFORE /broker/(your-alias)/endpoint and paste it in this field.
    - Single Sign-On Service URL - In this field paste https://<URL>:<PORT>/api/v1/login_sso 
    - Scroll down and ensure Allow create is on 
    - Ensure HTTP-POST Binding Response is on
    - Ensure HTTP-POST Binding for AuthnRequest is on
    - Ensure Validate Signature is on, paste your X509 certificate see [here](https://lightbend.github.io/ssl-config/CertificateGeneration.html)

* Proceed to hit save

* Copy the service Provider Entity ID and paste it in your Shuffle instance under the SSO Entrypoint (IdP) proceed to add /account at the end of your URI

![01 02 2022_14 59 32_REC](https://user-images.githubusercontent.com/31187099/151966347-d56f78d5-9a04-4719-b55e-4e5d3ed6e703.png)
