import subprocess


def test_cpu(time):
    command = 'stress-ng --cpu {} --cpu-method int32float -t {} --metrics'
    min_val = int(input('Enter min range value >>>'))
    max_val = int(input('Enter max range value >>>'))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    for value in range(min_val, max_val, step):
        command_to_run = command.format(value, time)
        print('command:', command_to_run)

        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        print(proc.stdout.read())
