import signal

import click

from abst.oci_bastion import Bastion


# Press the green button in the gutter to run the script.
def main():
    cli()


@click.group()
def cli():
    pass


@cli.group()
def create():
    pass


@create.command("single")
def single():
    """Creates only one bastion session
     ,connects and reconnects until its ttl runs out"""
    Bastion.create_bastion()


@create.command("fullauto")
def fullauto():
    """Creates and connects to bastion sessions
     automatically until terminated"""

    while True:
        print("Creating New Bastion Session")
        Bastion.create_bastion()
        print("Bastion session deprecated")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Bastion.kill_bastion)
    signal.signal(signal.SIGTERM, Bastion.kill_bastion)
    cli()
