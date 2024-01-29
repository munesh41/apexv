import io
import csv
from abc import (
    ABC,
    abstractmethod,
)


#Class implements export data
class DataExporter:

    def __init__(self, file_format='csv'):
        self.file_format = file_format


    #Export data to a file
    def export_data(self, data_source):


        file_writers = {
            'csv': CSVFileWriter,
        }

        file = None

        if self.file_format in file_writers:
            file_writer = file_writers[self.file_format]()
            file = file_writer.write(data_source)
        else:
            raise ValueError("Invalid export file format has been set.")

        return file



#FileWriter interface is responsible for writing data to a file
class FileWriter(ABC):

    @abstractmethod
    def write(self, data):
        pass



#CSVFileWriter class is responsible for writing data to a csv file
class CSVFileWriter(FileWriter):

    def __init__(self):
        pass


    #Write data to a csv file
    def write(self, data):
        string_buffer = io.StringIO()
        current_headers = None
        csv_writer = csv.DictWriter(string_buffer, fieldnames=current_headers)

        for row in data:

            if row.keys() != current_headers:
                current_headers = row.keys()
                csv_writer.fieldnames = current_headers
                csv_writer.writeheader()

            csv_writer.writerow(row)

        # Retrieve the content of the StringIO object
        csv_content = string_buffer.getvalue()

        # Convert the CSV content to bytes
        csv_bytes = csv_content.encode()

        # Create a BytesIO object to handle binary data
        binary_buffer = io.BytesIO(csv_bytes)

        return binary_buffer
