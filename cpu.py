import subprocess


def test_cpu(time, min_val, max_val):
    result = {}
    command = 'stress-ng --cpu {} --cpu-method int32float -t {} --metrics | head -5 | tail -1'
    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    for cpu_val in range(min_val, max_val, step):
        command_to_run = command.format(cpu_val, time)
        print('command:', command_to_run)

        proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        output = str(proc.stdout.read())

        for val in output.split(' '):
            if val.isdigit():
                result[cpu_val] = val
                break

    return result
