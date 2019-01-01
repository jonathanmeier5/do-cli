import digitalocean

from docli import config


class DOClient:

    def __init__(self, token):

        self.token = token

    def _block_on_create_droplet(self, droplet: digitalocean.Droplet) -> None:
        """
        Block on droplet creation.
        """

        actions = droplet.get_actions()

        for action in actions:
            action.load()
            # Once it shows complete, droplet is up and running
            print(f'Droplet Status: {action.status}')

    def create_droplet(self, *args, **kwargs) -> digitalocean.Droplet:
        """
        Create a DO droplet based on called specs.

        Optionally block on creation of the droplet.
        """

        droplet = digitalocean.Droplet(
                    token=self.token,
                    **kwargs,
                )

        droplet.create()

        print(f'droplet id: {droplet.id}')

        self._block_on_create_droplet(droplet)

        return droplet

    def destroy_droplet(self, *args, **kwargs) -> None:
        """
        Remove a DO droplet based on specified args.
        """

        droplet = digitalocean.Droplet(
                    token=self.token,
                    **kwargs,
                )

        print(f'destroying droplet id={droplet.id}, name={droplet.name}')

        droplet.destroy()
