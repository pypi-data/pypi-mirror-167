# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Script to bulk retrieve data from the django-decide-host server """

import sys
import argparse
import logging
import csv
import json
import datetime

from decide_analysis import __version__
from decide_analysis import core

log = logging.getLogger("decide-analysis")  # root logger


def setup_log(log, debug=False):
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    loglevel = logging.DEBUG if debug else logging.INFO
    log.setLevel(loglevel)
    ch.setLevel(loglevel)
    ch.setFormatter(formatter)
    log.addHandler(ch)


class ParseKeyVal(argparse.Action):
    def parse_value(self, value):
        import ast

        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value

    def __call__(self, parser, namespace, arg, option_string=None):
        kv = getattr(namespace, self.dest)
        if kv is None:
            kv = dict()
        if not arg.count("=") == 1:
            raise ValueError("-k %s argument badly formed; needs key=value" % arg)
        else:
            key, val = arg.split("=")
            kv[key] = self.parse_value(val)
        setattr(namespace, self.dest, kv)


class JsonWriter(object):
    def writerow(self, record):
        json.dump(record, fp=sys.stdout)
        sys.stdout.write("\n")


def main(argv=None):
    p = argparse.ArgumentParser(
        description="""Retrieve trial records from decide-host and ouput them to
        standard output as line-delimited JSON or CSV. Optional arguments allow
        filtering of the records to specific date ranges or on any of the fields
        of the records.""",
        epilog="""Example: %(prog)s -r http://pholia.lab:4000/decide/api
        --from-date 2022-03-01 --to-date 2022-03-09 -k experiment=2ac-config-segmented10 C14"""
    )
    p.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )
    p.add_argument(
        "--format",
        help="format of the output",
        default="csv",
        choices=("csv", "json"),
    )
    p.add_argument(
        "-r",
        dest="host_url",
        help="URL of the decide-host service. "
        "Default is to use the environment variable '%s'" % core.env_host,
        default=core.default_host(),
    )
    p.add_argument("--debug", help="show verbose log messages", action="store_true")
    p.add_argument(
        "--from-date",
        "-f",
        help="only retrieve records on or after %(metavar)s",
        metavar="DATE",
        type=datetime.date.fromisoformat,
    )
    p.add_argument(
        "--to-date",
        "-t",
        help="only retrieve records up to (and not including) %(metavar)s",
        metavar="DATE",
        type=datetime.date.fromisoformat,
    )
    p.add_argument(
        "--exclude-date",
        "-e",
        help="exclude records on %(metavar)s",
        action="append",
        default=list(),
        metavar="DATE",
        type=datetime.date.fromisoformat,
    )
    p.add_argument(
        "-k",
        help="only retrieve records with %(metavar)s (use multiple -k for multiple values)",
        action=ParseKeyVal,
        default=dict(),
        metavar="KEY=VALUE",
        dest="data_params",
    )
    p.add_argument(
        "--name",
        "-n",
        help="only retrieve records with name=%(metavar)s",
        metavar="NAME",
    )
    p.add_argument("subject", help="retrieve records for this subject")

    args = p.parse_args(argv)
    setup_log(log, args.debug)
    log.debug(args)

    if args.host_url is None:
        p.error("host URL not specified as argument or environment variable")
    params = {
        "subject": args.subject,
        "name": args.name,
        "date_after": args.from_date,
        "date_before": args.to_date,
    }
    for k, v in args.data_params.items():
        params[f"data__{k}"] = v
    query_params = {k: v for k, v in params.items() if v is not None}
    log.debug("query parameters: %s", query_params)
    endpoint = core.get_endpoint(args.host_url, "trials")
    log.info("Retrieving records from %s", endpoint)

    writer = None
    for record in core.iter_records(endpoint, **query_params):
        rectime = datetime.datetime.fromisoformat(record["time"])
        if rectime.date() in args.exclude_date:
            continue
        if writer is None:
            if args.format == "csv":
                writer = csv.DictWriter(
                    sys.stdout, fieldnames=record.keys(), extrasaction="ignore"
                )
                writer.writeheader()
            elif args.format == "json":
                writer = JsonWriter()
        writer.writerow(record)


if __name__ == "__main__":
    main()
