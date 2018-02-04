import random


class DataGatherer:

    def __init__(self):
        pass

    @staticmethod
    def get_temperature_data():
        # TODO: read actual data from station folders
        # for datefolder in datefolders:
        #     for stationfolder in datefolder:
        #         for hourfile in stationfolder:

        def data():
            """ Temperature between 15 and 30 degrees """
            return [round(random.uniform(15, 30), 2) for x in range(7)]

        return [data() for x in range(3)]

        # measurement_list = []
        # for i in range(21):
        #     measurement = Measurement()
        #     measurement.temperature = random.randint(0, 40)
        #     measurement_list.append(measurement.temperature)
        #
        # chart_list = []
        # for measurements in measurement_list:
        #     chart_list.append(measurements)
        #
        # return [chart_list]

    @staticmethod
    def get_wind_data():
        # TODO: read actual data from folders
        # for datefolder in datefolders:
        #     for stationfolder in datefolder:
        #         for hourfile in stationfolder:

        def data():
            """ Wind is between 25 and 40 """
            return [round(random.uniform(25, 40), 2) for x in range(10)]

        return [data() for x in range(3)]

    @staticmethod
    def get_rainfall_data():
        # TODO: read actual rainfall data
        # for datefolder in datefolders:
        #     for stationfolder in datefolder:
        #         for hourfile in stationfolder:

        def data():
            """ Rainfall between 0 and 5 """
            return [round(random.uniform(0, 5), 2) for x in range(10)]

        return [data() for x in range(3)]
