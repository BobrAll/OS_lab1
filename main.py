from subsystems.cpu import test_cpu
from subsystems.memory import test_memory

import numpy as np
import matplotlib.pyplot as plt

commands = {'cpu': test_cpu, 'memory': test_memory}

if __name__ == '__main__':
    while True:
        available_commands = ', '.join(commands.keys())
        print('Enter parameter name from list: ' + available_commands)

        command_name = input('>>>')

        if command_name not in commands.keys():
            print('Incorrect command name')
        else:
            time = int(input('Enter time per test >>>'))
            min_val = int(input('Enter min range value >>>'))
            max_val = int(input('Enter max range value >>>')) + 1

            x, y, info = commands[command_name](time, min_val, max_val)

            print(np.array(x))
            print(np.array(y))

            line = plt.plot(np.array(x), np.array(y))
            plt.xlabel(info['x_label'])
            plt.ylabel(info['y_label'])
            plt.title(info['title'])
            plt.savefig('{} {}s.png'.format(info['parameter'], time))
            plt.clf()

