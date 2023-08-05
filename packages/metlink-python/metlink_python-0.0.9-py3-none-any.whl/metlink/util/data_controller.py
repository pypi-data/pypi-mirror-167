import csv
from metlink.util.standard_table import print_standard_table
from metlink.util.rich_table import print_rich_table
from metlink.data.agency import agency
from metlink.data.routes import routes
from metlink.data.stops import stops
from metlink.data.trips import trips
from metlink.data.stop_times import stop_times
from metlink.data.calendar import calendar
from metlink.data.calendar_dates import calendar_dates
from metlink.data.feed_info import feed_info
from metlink.data.transfers import transfers
from metlink.data.stop_patterns import stop_patterns


def get_data(name: str):
    """Returns data from data folder"""
    if name == 'agency':
        return agency
    elif name == 'routes':
        return routes
    elif name == 'stops':
        return stops
    elif name == 'trips':
        return trips
    elif name == 'stop_times':
        return stop_times
    elif name == 'calendar':
        return calendar
    elif name == 'calendar_dates':
        return calendar_dates
    elif name == 'feed_info':
        return feed_info
    elif name == 'transfers':
        return transfers
    elif name == 'stop_patterns':
        return stop_patterns
    return None


class DataController:
    class Data:
        def __init__(self, name, variables, data):
            self.data = data
            self.variables = variables
            self.name = name

    data = {}

    def print_data(self, name: str, rich, filters=None):
        """
        Prints the data in a nice table

        Args:
            name: str - The name of the data to print
            filters: dict - A dictionary of filters to apply to the data
        """
        if name in self.data:
            if filters is not None:
                data = self.data[name].data
                for key, value in filters.items():
                    data = [row for row in data if row[key] == value]
            else:
                data = self.data[name].data
            if len(data) > 0:
                if rich:
                    print_rich_table(
                        self.data[name].name,
                        self.data[name].variables,
                        data,
                        lines=False)
                else:
                    print_standard_table(
                        self.data[name].name,
                        self.data[name].variables,
                        data,
                        lines=False)
        else:
            if get_data(name):
                self.print_data(name, filters)

    def print_possible_data(self):
        import os
        for file in os.listdir('data/'):
            if file.endswith('.csv'):
                with open('data/' + file, 'r') as f:
                    csv_file = csv.reader(f)
                    variables = next(csv_file)
                    print(file.split('.')[0] + ': ' + ', '.join(variables))
