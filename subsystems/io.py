import subprocess
import time


def test_io(test_time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'value', 'y_label': 'Kb/s'}
    io_methods = ['ioport', 'io-uring']
    method = input('Enter needed io method from list: {} >>>'.format(io_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --{} {} -t {}'

    for method_val in range(min_val, max_val, step):
        command_to_run = command.format(method, method_val, test_time)
        print('command:', command_to_run)

        info['title'] = command_to_run
        info['parameter'] = method

        stress_ng = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        time.sleep(test_time / 2)
        proc = subprocess.Popen('iotop -bk -n 1 | head -2', stdout=subprocess.PIPE, shell=True, executable="/bin/bash")

        output = str(proc.stdout.read())
        stress_ng.stdout.read()

        print(output.split(' '))

        float_count = 0
        for val in output.split(' '):
            try:
                val = float(val)
                float_count += 1
            except:
                continue
            if float_count == 2:
                x.append(method_val)
                y.append(int(val))
                break

    return x, y, info