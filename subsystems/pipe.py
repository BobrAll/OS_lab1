import subprocess
import time


def test_pipe(test_time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'value', 'y_label': 'B/s'}
    pipe_methods = ['pipeherd', 'pipe-ops']
    method = input('Enter needed pipe method from list: {} >>>'.format(pipe_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --{} {} -t {} | pv | tail -2'

    for method_val in range(min_val, max_val, step):
        command_to_run = command.format(method, method_val, test_time)
        print('command:', command_to_run)

        info['title'] = command.format(method, '{value}', test_time)
        info['parameter'] = method

        time.sleep(test_time / 2)
        proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")

        output = str(proc.stdout.read())
        print(output.split(' '))
        for val in output.split(' '):
            try:
                val = float(val[1:])
            except:
                continue

            x.append(method_val)
            y.append(val)
            break

    return x, y, info