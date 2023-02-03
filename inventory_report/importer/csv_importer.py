from inventory_report.importer.importer import Importer
from csv import DictReader
from typing import List, Dict


class CsvImporter(Importer):
    def import_data(path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                reader_csv = list(DictReader(file))
                return reader_csv
            else:
                raise ValueError("Arquivo inválido")
