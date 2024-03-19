# Skyflow Python Speedrun

A guide to getting started with skyflow for Python, fast.

## Getting started

### 1. Install the Skyflow Python SDK

```python
pip install skyflow
```

If you get an error here, check that you have Python installed in your development environment. Note: if you have issues with dependencies make sure that you're installing the packages into the same Python environment (interpreter version) that you're using to run the code.

### 2. Generate an API access token from Skyflow Studio.

1. Sign in to your Skyflow trial account. If you don't have one yet, [get a trial here.](https://www.skyflow.com/try-skyflow)

2. Log in to Skyflow Studio.

3. Create a new vault for this, and upload the sample schema found [here](users_demo_schema.json).

4. Click your profile (top right), then 'Generate API Bearer Token' and follow instructions. 
Copy the token.

### 3. Import and Initialize the Skyflow SDK

```py
# Import the client and types
from skyflow.vault import Client, Configuration, InsertOptions
# Set your bearer token to get started. Don't do this in Prod :)
def bearer_token():
    return '{bearer token}'
# Configuration: 1. Vault ID 2. Vault URL 3. your bearer_token function
config = Configuration('{vault_id}', '{vault_url}', bearer_token)
# Create the client
skyflow = Client(config)
```
Replace the {bearer_token}, {vault_id}, and {vault_url} placeholders with the bearer token, Vault ID, and Vault URL from Skyflow. To find those values in Skyflow follow [Get vault information](https://docs.skyflow.com/get-started/#get-vault-information).

Congrats! You've set up Skyflow in Python. 🎉

### 4. Hello, Vault

Now let's secure some data in the vault.

Here we'll create some sample data, and get ready to insert it into the vault.

```py
# Fake some data to insert & tokenize
data = {"records": [{
  "table": "users",
  "fields": {
      "name": "Joe Doe",
      "email": "joe@example.com"
  }}]
}

```
Now that you have a Skyflow client and some test data, all you need to do is:
```py
# Tell Skyflow we want tokens back
options = InsertOptions(tokens=True)
# Insert the data into the vault 🔒
response = skyflow.insert(data, options=options)
print('Response:\n', response)
```

Now save that file and run it in Terminal!

```
python script.py
```

Remember, the command may depend on your installation of Python. You may need to try `python3 script.py`. When it works, you'll see this:

```
Response:
 {'records': [{'table': 'table1', 'fields': {'email': 'e3bee1c7-91f4-42de-a675-fb4dd4c4f6e1', 'skyflow_id': '77ef6423-e840-49e9-8fef-a15aa91f5ef7'}, 'request_index': 0}]}
```

And just like that, you've secured some PII in the Skyflow Vault and got tokens back!

Well done, Privacy Engineer. 🫡

### 5. Conclusion and next steps.

Now if this was a real application you'd insert the tokens into some storage layer and finish the user sign up logic. Then add some robust error handling, instrumentation, and tests. You can do that on your own time :)