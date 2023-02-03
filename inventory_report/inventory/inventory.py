import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path) as file:
            if path.endswith(".csv"):
                reader = csv.DictReader(file)
                data = list(reader)

            elif path.endswith(".json"):
                data = json.load(file)

            else:
                reader = file.read()
                data = xmltodict.parse(reader)["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
