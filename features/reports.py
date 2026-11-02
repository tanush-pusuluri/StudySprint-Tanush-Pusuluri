"""Reporting helpers for StudySprint.

Heads up: this module is half-built on purpose. `deck_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"


def category_report(data):
    report = {}
    for card in data["cards"]:
        category = card["category"]
        report[category] = report.get(category, 0) + 1
    return report
