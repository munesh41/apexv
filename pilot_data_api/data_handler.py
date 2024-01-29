import json

from pilot_data_api.data_importer import DataImporter
from pilot_data_api.data_exporter import DataExporter
from pilot_data_api.data_mapper import DataMapper
from pilot_data_api.exceptions import BadFileError



#This class facilitates data import and export
class DataHandler:

    ALLOWED_IMPORT_FILE_FORMATS = [
        'json',
    ]

    ALLOWED_EXPORT_FILE_FORMATS = [
        'csv',
    ]

    def __init__(self, import_format='json', export_format='csv'):
        self.import_format = import_format
        self.export_format = export_format



    #Process data from data source and return it in the specified format
    def process_data(self, data_source):
        parsed_data = self._parse_data_source(
            file_format=self.import_format,
            data_source=data_source,
        )
        imported_data = self._import_data(parsed_data)
        exported_data = self._export_data(imported_data)

        return exported_data

    #Import data from data source persist it to the database"""
    def _import_data(self, data_source):
        if self.import_format not in self.ALLOWED_IMPORT_FILE_FORMATS:
            raise ValueError("This file format set is invalid.")

        data_mapper = DataMapper()

        data_importer = DataImporter(
            data_source=data_source,
            data_mapper=data_mapper,
        )

        return data_importer.import_data()

    #Export data to a file
    def _export_data(self, data_source):
        if self.export_format not in self.ALLOWED_EXPORT_FILE_FORMATS:
            raise ValueError("Invalid export file format has been set.")

        data_exporter = DataExporter(file_format=self.export_format)
        exported_data = data_exporter.export_data(data_source=data_source)
        return exported_data


    #Parse data source based on the specified format
    def _parse_data_source(self, data_source, file_format='json'):

        if file_format not in self.ALLOWED_IMPORT_FILE_FORMATS:
            raise ValueError("Invalid file format.")

        if file_format == 'json':
            # Load the file and try to parse it as JSON
            try:
                parsed_data = json.load(data_source)
            except json.JSONDecodeError:
                raise BadFileError("Invalid JSON file.")

        return parsed_data