from datetime import datetime
import time
import sys
import re
import click

FMT = "%Y-%m-%d %H:%M:%S"
 
def validate_date(ctx, param, value):
    if isinstance(value, tuple):
        return value
    try:
        datetime.strptime(value, FMT)
    except ValueError as err:
        raise click.BadParameter("format must be '%Y-%m-%d %H:%M:%S'")
    return value


def dateDiff(since, until) -> int:
    d1 = datetime.strptime(since, FMT)
    d2 = datetime.strptime(until, FMT)

    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())
    minutesDiff = int((d2_ts - d1_ts) / 60)
    return minutesDiff


@click.command()
@click.option(
    "--since",
    type=click.UNPROCESSED,
    required=True,
    callback=validate_date,
    help="Start date",
)
@click.option(
    "--until",
    type=click.UNPROCESSED,
    required=True,
    callback=validate_date,
    help="End date",
)
def main(since, until):
    minDiff = dateDiff(since, until)
    print(f"Minutes between {since} and {until}: {minDiff}m")


if __name__ == "__main__":
    main()
