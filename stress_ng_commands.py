io_commands = [{'command': 'stress-ng --ioport {} -t 5 --metrics',
                'range': [1, 2]},
               {'command': 'stress-ng --io-uring {} -t 5 --metrics',
                'range': [1, 2]}]


network_commands = [{'command': 'stress-ng --netdev {} -t 5 --metrics',
                     'range': [1, 2]},
                    {'command': 'stress-ng --dccp {} -t 5 --metrics',
                     'range': [1, 2]}]

pipe_commands = [{'command' : 'stress-ng --pipeherd {} --pipeops 1000 -t 5 --metrics',
                  'range': [1, 2]}]

shed_commands = [{'command': 'stress-ng --resched {} --sched-period 5000000000 -t 5 --metrics',
                  'range': [1, 2]}]

