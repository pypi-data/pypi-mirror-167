import argparse
import sys
from . import _aak
from loguru import logger

parser = argparse.ArgumentParser(description="access_azure_keyvault")
parser.add_argument('--keyvault', '-v',
                    help="Name of Azure Key Vault",
                    required=True)
parser.add_argument('--secretname', '-s',
                    help='Name of secret to query',
                    required=True)
args = parser.parse_args()
keyVaultName = args.keyvault
secretName = args.secretname

logger.debug(f"Trying to retrieve secret {secretName} from keyvault {keyVaultName}")

try:
    secretValue = _aak.getSecret(keyVaultName, secretName)
    logger.debug(f"Retrieved {secretValue}")
    print(secretValue)
except Exception as e:
    logger.error(f"Error: <{e.__class__.__name__}> <{e}>")
    sys.exit(1)

