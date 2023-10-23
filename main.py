from stress_ng_commands import commands
import subprocess
import sys

output = subprocess.check_output("cat /etc/os-release", shell=True)
output = output.decode('utf-8')


def run_stress_ng(name):
    for command in commands[name]:
        min_val = command['range'][0]
        max_val = command['range'][1] + 1

        max_steps = 10
        step = max(1, int((max_val - min_val) / max_steps))

        for value in range(min_val, max_val, step):
            command_to_run = command['command'].format(value)
            proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
            print(proc.stdout.read().split('\n'))
        print('-----------------------------')


if __name__ == '__main__':
    while True:
        available_commands = ', '.join(commands.keys())
        print('Enter parameter name from list: ' + available_commands)
        command_name = input('>>>')
        if command_name not in commands.keys():
            print('Incorrect command name')
        else:
            run_stress_ng(command_name)

