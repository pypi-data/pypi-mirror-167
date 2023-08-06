import argparse
from csv2geojson.csv2geojson import csv2geojson
from csv2geojson import __version__


parser = argparse.ArgumentParser(
    prog="csv2geojson",
    description="Convert csv to geojson",
    epilog="",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "-v", "--version", action="version", version="%(prog)s " + "v" + __version__
)

parser.add_argument(
    "input",
    metavar="input",
    type=str,
    help="Input csv file path",
)

parser.add_argument(
    "output",
    metavar="output",
    type=str,
    help="Output geojson file path",
)

parser.add_argument(
    "-lat",
    metavar="lat",
    type=str,
    default="latitude",
    help="Specify the latitude column in csv",
)

parser.add_argument(
    "-long",
    metavar="long",
    type=str,
    default="longitude",
    help="Specify the longitude column in csv",
)

include_exclude_group = parser.add_mutually_exclusive_group()

include_exclude_group.add_argument(
    "-exclude_columns",
    metavar="column_name",
    nargs="*",
    help="Exclude these columns from geojson properties",
)

include_exclude_group.add_argument(
    "-include_columns",
    metavar="column_name",
    nargs="*",
    help="Include only these columns in the geojson properties",
)


def parse_args(args=None):
    return parser.parse_args(args)


def main(args=None):
    parsed_args = parse_args(args)
    csv2geojson(
        parsed_args.input,
        parsed_args.output,
        parsed_args.long,
        parsed_args.lat,
        parsed_args.exclude_columns,
        parsed_args.include_columns,
    )
