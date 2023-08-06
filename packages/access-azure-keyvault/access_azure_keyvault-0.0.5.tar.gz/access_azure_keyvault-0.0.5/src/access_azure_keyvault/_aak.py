from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import AzureError

class LocalException (Exception): pass

def getSecret(keyVaultName, secretName):
  KVUri = f"https://{keyVaultName}.vault.azure.net"

  try:
      credential = DefaultAzureCredential()
      client = SecretClient(vault_url=KVUri, credential=credential)
      retrieved_secret = client.get_secret(secretName)
      return retrieved_secret.value
  except AzureError as e:
      raise LocalException(f"AzureError: <{e.__class__.__name__}> <{e}>")

