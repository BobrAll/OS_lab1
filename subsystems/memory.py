import subprocess


def test_memory(time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'memrate\'s', 'y_label': 'used mem (Mb)'}
    memory_methods = ['memrate']
    method = input('Enter needed memory method from list: {} >>>'.format(memory_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'stress-ng --fork-vm --{} {} -t {}'

    for method_val in range(min_val, max_val, step):
        command_to_run = command.format(method, method_val, time)
        print('command:', command_to_run)

        info['title'] = command_to_run
        info['parameter'] = method + ' value'

        subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        proc = subprocess.Popen('free -m | tail -2 | head -1', stdout=subprocess.PIPE, shell=True,
                                executable="/bin/bash")
        output = str(proc.stdout.read())[:-3]

        digit_counter = 0
        for val in output.split(' '):
            if val.isdigit():
                print(val)
                digit_counter += 1
                if digit_counter == 2:
                    x.append(method_val)
                    y.append(int(val))
                    break

    return x, y, info
