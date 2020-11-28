from django.core.management.utils import get_random_secret_key
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

"""
Running this script will produce all keys necessary for deploying a new node.

Account Number Signing Key:
1a39089ad26ed05ad9329e880f0df3fdd6681d5102a342e1828b58bf9d348865

Account Number:
2ac4d35a74e8146f65007c3603af23591df158e3165ade812be65ac481fe9fd6

NID Signing Key:
937a38c891e73d214f593cb8b11cce5cf07d12c0550961f779cc5d7ada520f4b

NID:
feca95b78fb42f6da1293855bcc0265224f81693d83cd32c0530f372def61a33

SECRET_KEY:
+y15h+q5v-)r)_wf7+&bb1)o+3i1e#8tcw5^hc5e07*n4l*+^=
"""


def create_key_pair():
    """
    Create and return private_key, public_key
    """

    private_key = SigningKey.generate()
    public_key = private_key.verify_key
    return private_key, public_key


def display_key_pair(*, label):
    """
    Create and display key pair information
    """

    private_key, public_key = create_key_pair()
    private_key = private_key.encode(encoder=HexEncoder).decode('utf-8')
    public_key = public_key.encode(encoder=HexEncoder).decode('utf-8')

    print(f'\n{label} Signing Key:\n{private_key}')
    print(f'\n{label}:\n{public_key}')


def run():
    """
    Run main application
    """

    display_key_pair(label='Account Number')
    display_key_pair(label='NID')

    random_secret_key = get_random_secret_key()
    print(f'\nSECRET_KEY:\n{random_secret_key}')


if __name__ == '__main__':
    run()
