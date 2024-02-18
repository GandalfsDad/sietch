"""Main cli entry point for the application"""

import click

from ..environment import (
    create_environment,
    remove_environment,
    prepare_activate_environment,
)
from ..directory import list_environments
from ..cli import parameters as p


@click.group()
def cli():
    """CLI entrypoint"""


@cli.command("create")
@p.name
def create(name: str):
    """Create a new environment"""
    click.echo(f"Creating environment {name}")
    create_environment(name)


@cli.command("remove")
@p.name
def remove(name: str):
    """Delete an environment"""
    remove_environment(name)


@cli.command("list")
def list_():
    """List all environments"""
    envs = list_environments()

    if len(envs) == 0:
        click.echo("No environments found")
    else:
        click.echo("Environments: \n-------------")
        for env in envs:
            click.echo(f"{env}")


@cli.command("activate")
@p.name
def activate(name: str):
    """Activate an environment"""

    click.echo("Run the following command to activate the environment:")
    prepare_activate_environment(name)
