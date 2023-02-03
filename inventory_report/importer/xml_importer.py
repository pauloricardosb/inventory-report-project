from inventory_report.importer.importer import Importer
import xmltodict
from typing import List, Dict


class XmlImporter(Importer):
    def import_data(path: str) -> List[Dict]:
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader_xml = xmltodict.parse(file.read())["dataset"]["record"]
            return reader_xml
