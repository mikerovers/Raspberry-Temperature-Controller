import time

def read_temp_raw(sensor_id):
    f = open(get_directory(sensor_id), 'r')
    lines = f.readlines()
    f.close

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
    equal_pos = lines[1].find('t=')
    if equal_pos != -1:
        temp_string = lines[1][equal_pos+2:]
        temp_c = float(temp_string) / 1000.0

        return temp_c

def get_directory(sensor_id):
    directory = []
    directory.append('/sys/bus/w1/devices/')
    directory.append(sensor_id)
    directory.append('/w1_slave')

    return ''.join(directory)
