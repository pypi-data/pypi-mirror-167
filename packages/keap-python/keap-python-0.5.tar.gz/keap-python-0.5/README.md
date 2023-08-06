# README #

This library makes it easy to set up a Keap authorization without needing a frontend client using CLI utilities.

### What do I get set up? ###

* A [Keap Sandbox App](https://developer.infusionsoft.com/resources/sandbox-application/)
* A [Keap Developer App](https://keys.developer.keap.com/)

### How do I get set up? ###

#### Setting up Keap Developer App ####

* Once you are signed in to the Keap Developer Portal, visit [your apps page](https://keys.developer.keap.com/my-apps)
* Click "+New App" in the top right corner
* Give your app a name and description
* Click "Enable" next to the API listed at the bottom of the page
* Click "Save"

#### Setting up Keap SDK in a project ####

* Run `pip install keap-auth-python`
* If using in Django, add "keap" to the list of INSTALLED_APPS
* Activate your python VENV
* If using virtual environment
  * Activate your virtual environment
  * `${sript_prefix} = python venv/bin/keap`
* If you are using Docker
  * `${sript_prefix} = docker compose -f local.yml exec django keap`
* Run `${sript_prefix} generate-client-config`
    * It will ask you for information obtained above: You can use all the defaults
        * Client ID
        * Client Secret
        * Redirect URL
        * Client Name
        * Use Datetime
        * File path for token storage
        * File path for keap credentials
    * To confirm, check the keap credentials path you entered, or the default, and there should be a json file with all
      the info you entered. Verify the details.
* Run `${sript_prefix} get-access-token`
    * Use the defaults or repeat the info used above for
        * Path to Keap Credentials
        * Client Name
    * It will generate a URL, copy and visit this url and complete the signin flow. You will end up at the Redirect URL
      used above, copy this value.
        * e.g. `https://theapiguys.com/?code=GdRGbcuo&scope=full%7Chl214.infusionsoft.com&state=hl214`
    * Paste this url back into the terminal.
    * To confirm, view the file where you said to save token, it should be a json object with your {client_name|default}
      as a key with and related info in another object.
      ```json
          {
              "default": {
                  "access_token": "xxxxxxxxxxxxxxxxxxxxx",
                  "refresh_token": "xxxxxxxxxxxxxxxxxxxx",
                  "expires_in": 86399,
                  "end_of_life": 1661361510,
                  "scope": "full|hl214.infusionsoft.com"
              }
          }```
* That's it! You should now have a valid token to use with the Keap API.

### Usage ###

It is pretty simple to get started using the SDK once you have a valid token.

```python 
# Set up Keap
keap = Keap(settings.BASE_DIR / 'cache' / 'keap_credentials.json')
keap.refresh_access_token()  # This will also save the newly refreshed token

# Add a contact
contact = {'FirstName': 'John', 'LastName': 'Doe', 'Email': 'johndoe@email.com'}
contact = keap.XML.ContactService.add(contact)
print(contact) # 1552

# Query a contact 
keap = Keap(settings.BASE_DIR / 'cache' / 'keap_credentials.json')
keap.refresh_access_token()  # This will also save the newly refreshed token
email = 'johndoe@email.com'
query = {'Email': email}

# Method 1 usind DataService
contact = keap.XML.DataService.load("Contact", 1552, ['FirstName', 'LastName', "Id"])
print(contact)

# Method 2 using ContactService
contact = keap.XML.ContactService.load(1552, ['FirstName', 'LastName', "Id"])
print(contact)
```

### Helpful Documentation ###

* [XML RPC Docs](https://developer.infusionsoft.com/docs/xml-rpc/#contact-create-a-contact)
    * Although out of data on the Python side, they still provide mostly correct info on parameters and such.
* [Keap Table Schema](https://developer.infusionsoft.com/docs/table-schema/) Will help with any DataService queries
