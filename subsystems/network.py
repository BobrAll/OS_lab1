import subprocess
import time

def test_memory(test_time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'value', 'y_label': 'R/W speed (Mb)'}
    network_methods = ['dccp', 'netdev']
    method = input('Enter needed network method from list: {} >>>'.format(network_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --{} {} -t {}'

    for method_val in range(min_val, max_val, step):
        command_to_run = command.format(method, method_val, test_time)
        print('command:', command_to_run)

        info['title'] = command_to_run
        info['parameter'] = method

        proc = subprocess.Popen('ip -h -s link show lo | head -4 | tali -1',
                                stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        first_mem = get_first_int(str(proc.stdout.read()))

        stress_ng = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        stress_ng.stdout.read()

        proc = subprocess.Popen('ip -h -s link show lo | head -4 | tali -1',
                                stdout=subprocess.PIPE, shell=True, executable="/bin/bash")

        second_mem = get_first_int(str(proc.stdout.read()))

        x.append(method_val)
        y.append((second_mem - first_mem) / test_time)

    return x, y, info

def get_first_int(full_string):
    for str in full_string.split(' '):
        if str.isdigit():
            return int(str)
