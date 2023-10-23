from cpu import test_cpu


commands = {'cpu': test_cpu}

if __name__ == '__main__':
    while True:
        available_commands = ', '.join(commands.keys())
        print('Enter parameter name from list: ' + available_commands)

        command_name = input('>>>')

        if command_name not in commands.keys():
            print('Incorrect command name')
        else:
            time = input('Enter time per test >>>')
            commands[command_name](time)

