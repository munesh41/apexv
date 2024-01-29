from pilot_data_api.models import (Aircraft, Flights)  # noqa: F401

#This class imports data from a data source and persists it into the system's database
class DataImporter:

    def __init__(self, data_source, data_mapper):
        self.data_source = data_source
        self.data_mapper = data_mapper

    #Import data from data source and persist it in the database
    def import_data(self):

        mapped_data = self.data_mapper.map_data(self.data_source)

        # persist data in the database
        for row in mapped_data:
            model = self._get_model(row["model_name"])

            if model:
                # remove model name from row as it's not a db field
                del row["model_name"]

                # create model instance and save it
                obj = model.objects.create(**row)
                obj.save()

        return mapped_data

    #Get model by name
    def _get_model(self, model_name):

        models = {
            "aircraft": "Aircraft",
            "flight": "Flight",
        }

        if model_name in models:
            return eval(models[model_name])