import click
import core
from util import validate_date


@click.command()
@click.option('--date', callback=validate_date,
              help="Date of match. Format:YYYYMMDD")
@click.option('--venue', type=click.Choice(['ST', 'HV']),
              help="Venue: ST or HV")
@click.option('--table', default='result')
@click.pass_context
def cli(ctx, date, venue, table):
    '''A command tool to capture the result table from Hong Kong Jockey Club'''

    if date and venue and table == 'result':
        core.capture_result(date, venue)

    if not date and not venue:
        click.echo(ctx.get_help())
