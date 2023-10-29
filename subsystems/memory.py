import subprocess


def test_memory(time, min_val, max_val):
    x, y = [], []
    info = {'x_label': '%MEM\'s', 'y_label': 'bogo ops'}
    memory_methods = ['memrate']
    method = input('Enter needed memory method from list: {} >>>'.format(memory_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --fork-vm --{} {} -t {}'

    for val in range(min_val, max_val, step):
        command_to_run = command.format(method, val, time)
        print('command:', command_to_run)

        info['title'] = command_to_run
        info['parameter'] = method

        subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        proc = subprocess.Popen('top -b -n 1 | grep stress-ng', stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        output = str(proc.stdout.read())

        for val in output.split(' '):
            if val.isdigit():
                x.append(val)
                y.append(int(val))
                break

    return x, y, info