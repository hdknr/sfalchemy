import click
from . import models


@click.group()
@click.pass_context
def tickit(ctx):
    pass


@tickit.command()
@click.pass_context
def user_count(ctx):
    qs = ctx.obj["session"].query(models.User)
    print(qs.count())
