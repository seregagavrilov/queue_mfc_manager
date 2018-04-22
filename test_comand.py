import click


@click.command()
@click.group(invoke_without_command=True)
def foo():
    print('Hi all')