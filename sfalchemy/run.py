"""
https://django-environ.readthedocs.io/en/latest/
"""
from pathlib import Path
import click
import environ
from sqlalchemy import create_engine
import pandas as pd


@click.group(help="Tools Subcommand")
@click.option("--env_file", "-e", default=None)
@click.pass_context
def main(ctx, env_file):
    ctx.ensure_object(dict)
    env_file = env_file or str(Path.cwd() / ".env")
    ENV = environ.Env()
    ENV.read_env(env_file=env_file)
    ctx.obj["env"] = ENV


@main.command()
@click.argument("filename")
@click.option("--url_name", "-u", default="DB_URL")
@click.pass_context
def query(ctx, filename, url_name):
    sql = open(filename).read()
    env = ctx.obj["env"]

    engine = create_engine(env.str(url_name))
    try:
        connection = engine.connect()
        rs = connection.execute(sql)
        for row in rs:
            # sqlalchemy.engine.result.RowProxy
            print(row)
    finally:
        connection.close()
        engine.dispose()


RENDERER = dict(
    tsv=dict(func="to_csv", params=dict(index=False, sep="\t")),
    parquet=dict(func="to_parquet", params=dict(engine="auto")),
    # https://arrow.apache.org/docs/python/feather.html
    feather=dict(func="to_feather", params=dict()),
    json=dict(func="to_json", params=dict(orient="records", lines=True)),
)


@main.command()
@click.argument("filename")
@click.option("--url_name", "-u", default="DB_URL")
@click.option("--out", "-o", default="/tmp")
@click.option("--format", "-f", type=click.Choice(RENDERER.keys()), default="tsv")
@click.pass_context
def query_df(ctx, filename, url_name, out, format):
    sql = open(filename).read()
    env = ctx.obj["env"]
    name = filename.replace("/", "_")

    render = RENDERER[format]
    dst = Path(out) / f"{name}.{format}"
    engine = create_engine(env.str(url_name))
    connection = engine.connect()
    try:
        df = pd.read_sql_query(sql, engine)
        getattr(df, render["func"])(dst, **render["params"])
    except Exception as e:
        print(e)
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
