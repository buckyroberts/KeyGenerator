from django.core.management.utils import get_random_secret_key
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

"""
Running this script will produce all keys necessary for deploying a new node.

Account Number Signing Key:
2ea2542cb0b1176bd773beb58051c8baba832df30fe1f853e62ec9628032e087

Account Number:
a007f798fe362a3fc891f48dcee52fb8278f65821c55275d726a8e4f53a96536

NID Signing Key:
642df386806978baf63d660773983d13f19a714615c8acab74a0e16b775ca6c8

NID:
4a1331c318325ee601757aa4be45b34260fedf2f42071a871e16479b6cfd4746

SECRET_KEY:
okjd6yv)7wt#+ir#v2-j$9w!brgw3(k1#a28is5i7puk59itptm
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
