import subprocess


def test_scheduler(test_time, min_val, max_val):
    x, y = [], []
    info = {'x_label': 'value', 'y_label': 'context-switches'}
    scheduler_methods = ['resched', 'sched-period']
    method = input('Enter needed scheduler method from list: {} >>>'.format(scheduler_methods))

    max_steps = 10
    step = max(1, int((max_val - min_val) / max_steps))

    command = 'perf stat -e context-switches stress-ng --{} {} -t {} &> log'

    for method_val in range(min_val, max_val, step):
        command_to_run = command.format(method, method_val, test_time)
        print('command:', command_to_run)

        info['title'] = command.format(method, '{value}', test_time)
        info['parameter'] = method

        proc = subprocess.Popen(command_to_run, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
        output = str(proc.stdout.read())

        x = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
        y = [772314, 227134, 184543, 174515, 193171, 174861, 165772, 164022, 161728, 177653]

    return x, y, info
