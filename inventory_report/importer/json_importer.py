from inventory_report.importer.importer import Importer
from typing import List, Dict
import json


class JsonImporter(Importer):
    def import_data(path: str) -> List[Dict]:
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader_json = json.load(file)
            return reader_json
