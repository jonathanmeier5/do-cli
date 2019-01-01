from unittest import TestCase
from unittest import mock

from docli.subparsers.client import DOClient

class DOClientTestCase(TestCase):

    @mock.patch('docli.subparsers.client.DOClient._block_on_create_droplet')
    @mock.patch('docli.subparsers.client.digitalocean.Droplet.__init__')
    def test_create_droplet(self, *mocks):
        """
        Test that we can successfully create a droplet with passthrough args.
        """
        mocks[0].return_value = None

        token = 'test'
        client = DOClient(token)

        kwargs = {
                'name':'Example',
                'region':'nyc2', # New York 2
                'image':'ubuntu-14-04-x64', # Ubuntu 14.04 x64
                'size_slug':'512mb',  # 512MB
                'backups':False,
                }


        client.create_droplet(**kwargs)

        mocks[0].assert_called_with(token=client.token,**kwargs)

