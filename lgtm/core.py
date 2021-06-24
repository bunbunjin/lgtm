import click

@click.command()
def cli():
    lgtm()
    click.echo('lgtm')

def lgtm():
    pass

