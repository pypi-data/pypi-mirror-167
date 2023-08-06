import string
import random

import boto3
from aws_encryption_sdk.key_providers.kms import BaseKMSMasterKeyProvider, StrictAwsKmsMasterKeyProvider
from get_docker_secret import get_docker_secret
import os
import aws_encryption_sdk
from aws_encryption_sdk import LocalCryptoMaterialsCache, CachingCryptoMaterialsManager, CommitmentPolicy
import base64


# Cache capacity (maximum number of entries) is required
MAX_CACHE_SIZE = 10
cache = LocalCryptoMaterialsCache(MAX_CACHE_SIZE)

MAX_ENTRY_AGE_SECONDS = 60.0*60.0
MAX_ENTRY_MESSAGES = 100

FAKE_ENCRYPTION = os.environ.get('AWS_FAKE_ENCRYPTION', 'False') == 'True'

client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)

class CachingCMM():
    '''
    Actual encrypting CMM for use via AWS in prod
    '''

    def __init__(self, region = None, account_number = None, key_id = None):

        region = region or get_docker_secret('AWS_REGION')
        account_number = account_number or get_docker_secret('AWS_ACCOUNT_NUMBER')
        key_id = key_id or get_docker_secret('AWS_KEY_ID')


        key_arn = 'arn:aws:kms:{0}:{1}:key/{2}'.format(region, account_number, key_id)
        kms_kwargs = dict(key_ids=[key_arn])
        master_key_provider = StrictAwsKmsMasterKeyProvider(**kms_kwargs)
        self.caching_cmm = CachingCryptoMaterialsManager(
            master_key_provider=master_key_provider,
            cache=cache,
            max_age=MAX_ENTRY_AGE_SECONDS,
            max_messages_encrypted=MAX_ENTRY_MESSAGES
        )

    def encrypt(self, source_plaintext, **kwargs):
        ciphertext, encryptor_header = self._encrypt(source_plaintext, **kwargs)
        return ciphertext

    def _encrypt(self, source_plaintext, **kwargs):
        """Encrypts and then decrypts a string using a KMS customer master key (CMK)

        :param str key_arn: Amazon Resource Name (ARN) of the KMS CMK
        (http://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html)
        :param bytes source_plaintext: Data to encrypt
        :param botocore_session: Existing Botocore session instance
        :type botocore_session: botocore.session.Session
        """

        # Encrypt the plaintext source data
        return client.encrypt(
            source=source_plaintext,
            materials_manager=self.caching_cmm,
            **kwargs
        )

    def decrypt(self, ciphertext, **kwargs):
        plaintext_bytes, decrypted_header = self._decrypt(ciphertext, **kwargs)
        return plaintext_bytes.decode("utf-8")

    def _decrypt(self, ciphertext, **kwargs):

        # Decrypt the ciphertext
        return client.decrypt(
            source=ciphertext,
            materials_manager=self.caching_cmm,
            **kwargs
        )


class FakeCMM():
    '''
    Fake CMM for faking encryption / decryption in dev
    '''

    def encrypt(self, source_plaintext, **kwargs):
        return str.encode(source_plaintext)

    def decrypt(self, ciphertext, **kwargs):
        return ciphertext.decode()

if FAKE_ENCRYPTION:
    cmm = FakeCMM()
else:
    cmm = CachingCMM()

def encrypt(source_plaintext, key_id=None, **kwargs):
    if key_id and not FAKE_ENCRYPTION:
        temp_cmm = CachingCMM(key_id=key_id)
        return temp_cmm.encrypt(source_plaintext, **kwargs)
    else:
        return cmm.encrypt(source_plaintext, **kwargs)

def decrypt(ciphertext, key_id=None, **kwargs):
    if key_id and not FAKE_ENCRYPTION:
        temp_cmm = CachingCMM(key_id=key_id)
        return temp_cmm.decrypt(ciphertext, **kwargs)
    else:
        return cmm.decrypt(ciphertext, **kwargs)



def _create_data_key(region=get_docker_secret('AWS_REGION'), account_number=get_docker_secret('AWS_ACCOUNT_NUMBER'), key_id=get_docker_secret('AWS_KEY_ID'), key_spec="AES_256"):
    """Generate a data key to use when encrypting and decrypting data"""

    key_arn = 'arn:aws:kms:{0}:{1}:key/{2}'.format(region, account_number, key_id)

    # Create data key
    kms_client = boto3.client("kms", region_name=region)
    response = kms_client.generate_data_key(KeyId=key_arn, KeySpec=key_spec)

    # Return the encrypted and plaintext data key
    return response["CiphertextBlob"], base64.b64encode(response["Plaintext"]).decode('utf-8')

def _create_data_key_fake():
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for i in range(24))
    return bytes(key, 'utf-8'), key



if FAKE_ENCRYPTION:
    create_data_key = _create_data_key_fake
else:
    create_data_key = _create_data_key