# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""calculates and checks activity statistics from the trial log

Copyright (C) 2014 Dan Meliza <dmeliza@gmail.com>
Created Thu Sep 11 14:02:23 2014
"""

# python 3 compatibility
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys
import argparse
from collections import Counter
import datetime
from six.moves import cStringIO as stringio

from decide_analysis.core import parse_iso, logger, list_kv, email_queue
import decide_analysis.host as host

log = logger("activity-stats")

def trial_hour(trial):
    """Returns the hour of the day when trial occurred"""
    dt = parse_iso(trial["time"])
    return datetime.datetime.combine(dt.date(), datetime.time(hour=dt.hour))


def count_trials(seq):
    """Returns dict of trial counts by response and result.

    By default, None is returned if there are no log messages in seq. If
    NA is False, zero counts are returned instead of None.
    """
    keys = ("correct", "response", "result",)
    d = {k: Counter() for k in keys}
    for trial in seq:
        # any trial log message means the data are not excluded
        for key in keys:
            counter = d[key]
            counter[trial.get(key, None)] += 1
    return d


def block_stats(seq, key=trial_hour):
    """Counts trials and feeds in each block of trials. Returns iterator (hour, counts)

    Trials are grouped by key function, and must be sorted prior to grouping or
    the behavior is undefined. If NA is True and no trial log messages
    occurred in an hour, counts is None. Otherwise empty hours get zero counts.
    """
    from itertools import groupby
    for hour, trials in groupby(seq, key=trial_hour):
        counts = count_trials(trials)
        if counts is not None:
            yield hour, counts
        else:
            yield hour, None


def pprint_subject(subject, file=sys.stdout):
    # TODO fix this somewhere else
    if "experiment" not in subject:
        subject["experiment"] = ""
    print("\n" \
          "Subject:    {_id}\n" \
          "Controller: {controller}\n" \
          "Procedure:  {procedure}\n" \
          "Experiment: {experiment}\n" \
          "User:       {user}".format(**subject), file=file)


def pprint_totals(stats, file=sys.stdout):
    lk = (("Responses", "response"),
          ("Results", "result"),
          ("Correct", "correct"))
    for l,k in lk:
        ct = sum((v[k] for h, v in stats), Counter())
        print("{:<11} {}".format(k + ":", list_kv(ct)), file=file)


def pprint_hours(stats, file=sys.stdout):
    template = "{:>6} {:>4} | {:>10} {:>5} {:>7}"
    header = template.format("date", "hour", "correct", "fed", "trials")
    sep = "-" * len(header)
    print("\n".join((sep, header, sep)), file=file)

    last_day = None
    for hour, values in stats:
        if hour.date() != last_day:
            dd = hour.strftime("%m/%d")
            last_day = hour.date()
        else:
            dd = ""
        trials = sum(v for k, v in values["response"].items() if k is not None)
        print(template.format(dd,
                              hour.strftime("%H"),
                              values["correct"][True],
                              values["result"]["feed"],
                              trials),
              file=file)
    print(sep, file=file)


def main():
    p = argparse.ArgumentParser(description="caclulate and check operant activity statistics")
    p.add_argument("url", help="the url of a decide-host server")

    p.add_argument("-H", "--hours", default=24, type=int,
                   help="the number of hours back to analyze")
    p.add_argument("-s", "--subject",
                   help="restrict analysis to specific subjects",
                   action="append")

    p.add_argument("-e", "--send-email",
                   help="if true, sends email to the subject's user",
                   action="store_true")
    p.add_argument("-a", "--admins",
                   help="email address of admin to send copy of error emails; can specify more than once",
                   action='append', default=[])
    p.add_argument("-q", "--quiet",
                   help="don't output anything to the console. Most useful in conjuction with -e",
                   action="store_true")

    opts = p.parse_args()

    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(hours=opts.hours)

    try:
        subjects = tuple(host.find_subjects(opts.url))
    except host.HTTPError as e:
        log.error("unable to contact %s: %s", opts.url, e)
        if e.response.status_code == 401:
            log.error("add authentication info to URL or .netrc file")
        return -1

    if opts.subject is not None:
        subjects = filter(lambda m: m["_id"] in opts.subject, subjects)

    header = "Daily Operant Summary: {0:%Y-%b-%d %H:%M} to {1:%Y-%b-%d %H:%M}".format(cutoff,
                                                                                      now)
    hsep   = "=" * len(header)
    if not opts.quiet:
        print(header, file=sys.stdout)
        print(hsep, file=sys.stdout)

    emails = email_queue()
    for subject in subjects:
        msg = stringio()
        id = subject["_id"]
        trials = host.find_trials(opts.url, id, after=cutoff, before=now, comment=True)
        stats = tuple(block_stats(trials))
        if len(stats) == 0:
            log.debug("no trials for %(_id)s", **subject)
            continue
        pprint_subject(subject, file=msg)
        try:
            users = opts.admins + [subject["user"]]
        except (IndexError, KeyError):
            users = opts.admins

        pprint_totals(stats, file=msg)
        # TODO print historical statistics?
        pprint_hours(stats, file=msg)

        msg = msg.getvalue()
        if not opts.quiet:
            print(msg, file=sys.stdout)

        for user in set(users):
            emails.enqueue(user, subject["controller"], msg)

    if opts.send_email:
        emails.send("decide-activity-stats", header, "\n".join([header, hsep]), opts.quiet)
