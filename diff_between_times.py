from datetime import datetime
import time
import sys
import re
import click


def validate_date(ctx, param, value):
    if isinstance(value, tuple):
        return value

    p = re.compile("^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]) ([01][0-9]|2[0-3])(:[0-5][0-9]){2}$")
    if p.match(value) is None:
        raise click.BadParameter("format must be '%Y-%m-%d %H:%M:%S'")
    return value


def dateDiff(since, until) -> int:
    fmt = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(since, fmt)
    d2 = datetime.strptime(until, fmt)

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
