"""
Hacky way to expose sub-parser functionality without too much work.
"""

import argparse
import inspect
import sys

from docli.client import DOClient
from docli.config import DO_SECRET_TOKEN


def do_cli():
    """
    Primary entrypoint
    """
    workflow = Workflow()

    try:
        workflow.run()
    except AttributeError:
        print('too few arguments')


class SubCommand:
    
    def __init__(self, *args, **kwargs):

        self.client = DOClient(DO_SECRET_TOKEN)

    def parser_init(self, *args, **kwargs):

        attrs = dir(self)

        for attr in attrs:
            if attr.startswith('parser_init_'):
                method = getattr(self, attr)
                method()



class Workflow:

    def __init__(self, *args, **kwargs):

        self.parser = argparse.ArgumentParser()
        subparsers = self.parser.add_subparsers()
        subcommand_classes = inspect.getmembers(sys.modules[__name__], self.is_subcommand)

        for _, subcommand_class in subcommand_classes:
            subcommand = subcommand_class(subparsers)
            subcommand.parser_init()

    @staticmethod
    def is_subcommand(obj):
        if inspect.isclass(obj):
            return issubclass(obj, SubCommand) and obj != SubCommand
        else:
            False

    def run(self, *args, **kwargs):
        args = self.parser.parse_args()
        args.func(**vars(args))


class Droplet(SubCommand):

    def __init__(self, subparsers, *args, **kwargs):
        droplet = subparsers.add_parser('droplet')

        self.subparser = droplet.add_subparsers()

        super().__init__(subparsers, *args, **kwargs)

    def parser_init_create(self, *args, **kwargs):

        parser_create = self.subparser.add_parser('create')
        parser_create.set_defaults(func=self.client.create_droplet)

        parser_create.add_argument('-n', '--name')
        parser_create.add_argument('-r', '--region', default='nyc3')
        parser_create.add_argument('-i', '--image', default='ubuntu-18-04-x64')
        parser_create.add_argument('--size_slug', default='1gb')
        parser_create.add_argument('-b', '--backups', default=False)

    def parser_init_destroy(self, *args, **kwargs):

        parser_destroy = self.subparser.add_parser('destroy')

        parser_destroy.set_defaults(func=self.destroy)

        parser_destroy.add_argument('ids', type=int, nargs='+', help='Droplet ids to destroy')

    def parser_init_list(self, *args, **kwargs):

        parser_list = self.subparser.add_parser('list')

        parser_list.set_defaults(func=self.client.list_droplets)

    def destroy(self, *args, **kwargs):
        """
        Destroy DO droplets by id
        """

        for droplet_id in kwargs.get('ids'):

            self.client.destroy_droplet(**{'id': droplet_id})


class Image(SubCommand):

    def __init__(self, subparsers, *args, **kwargs):

        image = subparsers.add_parser('image')

        self.subparser = image.add_subparsers()

        super().__init__(subparsers, *args, **kwargs)

    def parser_init_list(self, *args, **kwargs):

        parser_list = self.subparser.add_parser('list')

        parser_list.set_defaults(func=self.client.list_images)

