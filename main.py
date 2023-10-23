from stress_ng_commands import commands

if __name__ == '__main__':
    for name in commands:
        for command in commands[name]:
            min_val = command['range'][0]
            max_val = command['range'][1] + 1

            max_steps = 10
            step = max(1, int((max_val - min_val) / max_steps))

            for value in range(min_val, max_val, step):
                print(command['command'].format(value))
        print('-----------------------------')


def run_stress_ng():
    pass
