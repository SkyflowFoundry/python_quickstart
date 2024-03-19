# Import the client and types
from skyflow.vault import Client, Configuration, InsertOptions
# Set your bearer token to get started. Don't do this in Prod :)
def bearer_token():
    return '{bearer_token}'
# Configuration: 1. Vault ID, 2. Vault URL, 3. bearer_token
config = Configuration('{vault_id}', '{vault_url}', bearer_token)
# Create the client
skyflow = Client(config)

# Fake some data to insert & tokenize
data = {"records": [{
  "table": "users",
  "fields": {
      "name": "Joe Doe",
      "email": "joe@example.com"
  }}]
}
# Tell Skyflow we want tokens back
options = InsertOptions(tokens=True)
# Insert the data into the vault 🔒
response = skyflow.insert(data, options=options)

print('Response:\n', response)