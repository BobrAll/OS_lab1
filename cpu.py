import subprocess


def test_cpu(time):
    result = []

    command = 'stress-ng --cpu {} --cpu-method int32float -t {} --metrics | head -5 | tail -1'
    min_val = int(input('Enter min range value >>>'))
    max_val = int(input('Enter max range value >>>')) + 1

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    for value in range(min_val, max_val, step):
        command_to_run = command.format(value, time)
        print('command:', command_to_run)

        proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        output = str(proc.stdout.read())
        #print(output)

        for val in output.split(' '):
            if val.isdigit():
                result.append(val)
                print('bogo ops:', val)
                break

    return result