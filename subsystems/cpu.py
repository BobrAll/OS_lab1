import subprocess


def test_cpu(time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'cpu\'s', 'y_label': 'bogo ops'}
    cpu_methods = ['int32float', 'rand']
    method = input('Enter needed cpu-method from list: {} >>>'.format(cpu_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --cpu {} --cpu-method {} -t {} --metrics | head -5 | tail -1'

    for cpu_val in range(min_val, max_val, step):
        command_to_run = command.format(cpu_val, method, time)
        print('command:', command_to_run)

        info['title'] = command_to_run
        info['parameter'] = method

        proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        output = str(proc.stdout.read())

        for val in output.split(' '):
            if val.isdigit():
                x.append(cpu_val)
                y.append(int(val))
                break

    return x, y, info
