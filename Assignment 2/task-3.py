from os import read

class Sensor_reading:
    def __init__(self, id: int, covid_level: int):
        self.id = id
        self.covid_level = covid_level


def add_value(readings_by_date, date, sensor_reading):
    ''' Adds a key-value pair to the dictionary.
    If the key already exists in the dictionary,
    it will associate multiple values with that
    key instead of overwritting its value'''
    if date in readings_by_date:
        readings_by_date[date].append(sensor_reading)
    else:
        readings_by_date[date] = [sensor_reading]



# get maximum for specific day
def get_max(readings_by_date, date):
    """

    :param dic: Dictionary from function above
    :param date: Date (string format: 'yyyy-mm-dd')
    :return: Sensory ID and value of the maximum measurement
    """
    readings = readings_by_date[date]
    max_reading = readings[0]

    for element in readings:
        if element.covid_level > max_reading.covid_level:
            max_reading = element
    
    return max_reading

if __name__ == "__main__":
    input = input()
    input = input.split(";")
    requested_date = input[0]
    input.pop(0)
    data = []
    for d in input:
        date, id, value = d.split(',', 2)

        instance = (date.strip(), Sensor_reading(int(id), int(value)))
        data.append(instance)

    # TODO: create empty dictionary and fill it.

    readings_by_date = {}
    for instance in data:
        add_value(readings_by_date, instance[0], instance[1])

    max_reading = get_max(readings_by_date, requested_date)

    print(f'{max_reading.id},{max_reading.covid_level}')
