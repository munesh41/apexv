import datetime

import pytest

from pilot_data_api.data_importer import DataImporter
from pilot_data_api.data_mapper import DataMapper
from pilot_data_api.models import (
    Aircraft,
    Flight,
)


# Test import_data method
@pytest.mark.django_db
class TestDataImporter:

    def test_import_data(self, mapper_configs):

        test_data_mapper = DataMapper()

        test_data_source = [
            # aircraft model data source
            {
                '_modified': 1616317613,
                'guid': '00000000-0000-0000-0000-000000000367',
                'meta': {
                    'Active': True,
                    'Aerobatic': False,
                    'AircraftCode': '00000000-0000-0000-0000-000000000367',
                    'Category': 1,
                    'Class': 5,
                    'Company': 'Other',
                    'Complex': False,
                    'CondLog': 69,
                    'DefaultApp': 0,
                    'DefaultLaunch': 0,
                    'DefaultLog': 2,
                    'DefaultOps': 0,
                    'DeviceCode': 1,
                    'Efis': False,
                    'FNPT': 0,
                    'FavList': False,
                    'Fin': '',
                    'HighPerf': False,
                    'Kg5700': False,
                    'Make': 'Cessna',
                    'Model': 'C150',
                    'Power': 1,
                    'Rating': '',
                    'Record_Modified': 1616320991,
                    'RefSearch': 'PHALI',
                    'Reference': 'PH-ALI',
                    'Run2': False,
                    'Sea': False,
                    'Seats': 0,
                    'SubModel': '',
                    'TMG': False,
                    'Tailwheel': False
                },
                'platform': 9,
                'table': 'Aircraft',
                'user_id': 125880
            },
            # flight model data source
            {
                '_modified': 1616317613,
                'guid': '00000000-0000-0000-0000-000000009940',
                'meta': {'AircraftCode': '00000000-0000-0000-0000-000000000427',  # noqa
                         'ArrCode': '00000000-0000-0000-0000-000000009512',
                         'ArrOffset': 60,
                         'ArrRwy': '',
                         'ArrTimeSCHED': 0,
                         'ArrTimeUTC': 735,
                         'BaseOffset': 120,
                         'CrewList': '',
                         'DateBASE': datetime.date(2008, 8, 14),
                         'DateLOCAL': datetime.date(2008, 8, 14),
                         'DateUTC': datetime.date(2008, 8, 14),
                         'DeIce': False,
                         'DepCode': '00000000-0000-0000-0000-000000009971',
                         'DepOffset': 120,
                         'DepRwy': '',
                         'DepTimeSCHED': 0,
                         'DepTimeUTC': 617,
                         'FlightCode': '00000000-0000-0000-0000-000000009940',
                         'FlightNumber': '551',
                         'FlightSearch': '20080814:551WROLTN',
                         'Fuel': 0,
                         'FuelPlanned': 0,
                         'FuelUsed': 0,
                         'HobbsIn': 0,
                         'HobbsOut': 0,
                         'Holding': 0,
                         'LdgDay': 1,
                         'LdgNight': 0,
                         'LdgTimeUTC': 0,
                         'LiftSW': 0,
                         'NextPage': False,
                         'NextSummary': False,
                         'P1Code': '00000000-0000-0000-0000-000000000780',
                         'P2Code': '00000000-0000-0000-0000-000000000001',
                         'P3Code': '00000000-0000-0000-0000-000000000000',
                         'P4Code': '00000000-0000-0000-0000-000000000000',
                         'PF': True,
                         'Pairing': '',
                         'Pax': 0,
                         'Record_Modified': 1616320991,
                         'Remarks': 'ILS26 manual, a/thrust off',
                         'Report': '',
                         'Route': '',
                         'SignBox': 0,
                         'TagApproach': '401',
                         'TagDelay': '',
                         'TagLaunch': '',
                         'TagLesson': '',
                         'TagOps': '',
                         'ToDay': 1,
                         'ToEdit': False,
                         'ToNight': 0,
                         'ToTimeUTC': 0,
                         'Training': '',
                         'UserBool': False,
                         'UserNum': 0,
                         'UserText': '',
                         'minAIR': 0,
                         'minCOP': 118,
                         'minDUAL': 0,
                         'minEXAM': 0,
                         'minIFR': 118,
                         'minIMT': 0,
                         'minINSTR': 0,
                         'minNIGHT': 0,
                         'minPIC': 0,
                         'minPICUS': 0,
                         'minREL': 0,
                         'minSFR': 0,
                         'minTOTAL': 118,
                         'minU1': 0,
                         'minU2': 0,
                         'minU3': 0,
                         'minU4': 0,
                         'minXC': 118},
                'platform': 9,
                'table': 'Flight',
                'user_id': 125880
            },
        ]

        expected_model_values = {
            # aircraft expected values
            'aircraft': {
                'AircraftID': '00000000-0000-0000-0000-000000000367',
                'Category': '1',
                'Class': '5',
                'Complex': False,
                'EngineType': None,
                'EquipmentType': None,
                'GearType': None,
                'HighPerformance': False,
                'Make': 'Cessna',
                'Model': 'C150',
                'Pressurized': None,
                'TAA': None,
                'TypeCode': '1',
                'Year': None,
            },
            'flight': {
                # flight expected values
                'ActualInstrument': None,
                'AircraftID': '00000000-0000-0000-0000-000000000427',
                'AllLandings': None,
                'Approach1': None,
                'Approach2': None,
                'Approach3': None,
                'Approach4': None,
                'Approach5': None,
                'Approach6': None,
                'Checkride': None,
                'CrossCountry': 118,
                'CustomFieldNameCounter': None,
                'CustomFieldNameDate': None,
                'CustomFieldNameDateTime': None,
                'CustomFieldNameHours': None,
                'CustomFieldNameNumeric': None,
                'CustomFieldNameText': None,
                'CustomFieldNameToggle': None,
                'Date': datetime.date(2008, 8, 14),
                'DayLandingsFullStop': None,
                'DayTakeoffs': 1,
                'Distance': None,
                'DualGiven': 0,
                'DualReceived': None,
                'FAA6158': None,
                'FlightReview': None,
                'From': '00000000-0000-0000-0000-000000009971',
                'GroundTraining': None,
                'HobbsEnd': 0,
                'HobbsStart': 0,
                'Holds': 0,
                'IPC': None,
                'InstructorComments': 'ILS26 manual, a/thrust off',
                'InstructorName': None,
                'NVG': None,
                'NVGOps': None,
                'NVGProficiency': None,
                'Night': None,
                'NightLandingsFullStop': None,
                'NightTakeoffs': 0,
                'OffDuty': None,
                'OnDuty': None,
                'PIC': 0,
                'Person1': None,
                'Person2': None,
                'Person3': None,
                'Person4': None,
                'Person5': None,
                'Person6': None,
                'PilotComments': None,
                'Route': '',
                'SIC': None,
                'SimulatedFlight': None,
                'SimulatedInstrument': None,
                'Solo': None,
                'TachEnd': None,
                'TachStart': None,
                'TimeIn': datetime.time(0, 12, 15),
                'TimeOff': None,
                'TimeOn': None,
                'TimeOut': datetime.time(0, 10, 17),
                'To': '00000000-0000-0000-0000-000000009512',
                'TotalTime': None,
            },
        }

        data_importer = DataImporter(
            data_source=test_data_source,
            data_mapper=test_data_mapper
        )

        # import data
        data_importer.import_data()

        assert Aircraft.objects.count() == 1
        assert Flight.objects.count() == 1

        for field in expected_model_values['aircraft']:
            assert (
                getattr(
                    Aircraft.objects.first(), field
                ) == expected_model_values['aircraft'][field]
            )

        for field in expected_model_values['flight']:
            assert (
                getattr(
                    Flight.objects.first(), field
                ) == expected_model_values['flight'][field]
            )

    #Tests _get_model method by checking that the correct model is returned
    def test_get_model(self):

        test_data_mapper = DataMapper()

        data_importer = DataImporter(
            data_source={},
            data_mapper=test_data_mapper,
        )

        assert data_importer._get_model('invalid_model') is None
        assert data_importer._get_model('aircraft') == Aircraft
        assert data_importer._get_model('flight') == Flight
