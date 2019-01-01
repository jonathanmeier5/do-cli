"""
Hacky way to expose sub-parser functionality without too much work.
"""

import argparse

from docli.client import DOClient
from docli.config import DO_SECRET_TOKEN


def create():
    """
    Function that manages creation of DO droplets.
    """

    client = DOClient(DO_SECRET_TOKEN)

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--name')
    parser.add_argument('-r', '--region', default='nyc3')
    parser.add_argument('-i', '--image', default='ubuntu-18-04-x64')
    parser.add_argument('--size_slug', default='1gb')
    parser.add_argument('-b', '--backups', default=False)

    args = parser.parse_args()

    print(args)

    try:
        client.create_droplet(**vars(args))
    except Exception as e:
        print(e)

def destroy():
    """
    Destroy a DO droplet.
    """

    client = DOClient(DO_SECRET_TOKEN)

    parser = argparse.ArgumentParser()

    parser.add_argument('droplet_id', metavar='ID', type=int, nargs='1', help='Droplet id to destroy')

    args = parser.parse_args()

    client.destroy_droplet(**vars(args))

