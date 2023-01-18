"""
https://django-environ.readthedocs.io/en/latest/
"""
from pathlib import Path
import click
import environ
from sqlalchemy import create_engine
import pandas as pd
from tickit import commands


from sqlalchemy.orm import sessionmaker


@click.group(help="Tools Subcommand")
@click.option("--env_file", "-e", default=None)
@click.option("--url", "-u")
@click.pass_context
def main(ctx, env_file, url):
    ctx.ensure_object(dict)
    env_file = env_file or str(Path.cwd() / ".env")
    ENV = environ.Env()
    ENV.read_env(env_file=env_file)
    ctx.obj["env"] = ENV

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    ctx.obj["session"] = Session()


main.add_command(commands.tickit)


if __name__ == "__main__":
    main()
