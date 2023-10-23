cpu_commands = [{'command': 'stress-ng --cpu {} --cpu-method int32float -t 5 --metrics',
                'range': [1, 2]},
                {'command': 'stress-ng --cpu {} --cpu-method rand -t 5 --metrics',
                'range': [1, 2]}]

cache_commands = [{'command': 'stress-ng --cache 1 --l1cache-size {} -t 5 --metrics',
                   'range': [1, 2]},
                  {'command': 'stress-ng --cache 1 --cache-ways {} -t 5 --metrics',
                   'range': [1, 2]}]

io_commands = [{'command': 'stress-ng --ioport {} -t 5 --metrics',
                'range': [1, 2]},
               {'command': 'stress-ng --io-uring {} -t 5 --metrics',
                'range': [1, 2]}]

memory_commands = [{'command': 'stress-ng --fork-vm --memrate {} -t 5 --metrics',
                    'range': [1, 2]}]

network_commands = [{'command': 'stress-ng --netdev {} -t 5 --metrics',
                     'range': [1, 2]},
                    {'command': 'stress-ng --dccp {} -t 5 --metrics',
                     'range': [1, 2]}]

pipe_commands = [{'command' : 'stress-ng --pipeherd {} --pipeops 1000 -t 5 --metrics',
                  'range': [1, 2]}]

shed_commands = [{'command': 'stress-ng --resched {} --sched-period 5000000000 -t 5 --metrics',
                  'range': [1, 2]}]

commands = {'cpu': cpu_commands,
            'cache': cache_commands,
            'io': io_commands,
            'memory': memory_commands,
            'network': network_commands,
            'pipe': pipe_commands,
            'shed': shed_commands,}
