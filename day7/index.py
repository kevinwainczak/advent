import copy

class InstructionGraph:
    def __init__(self, instrs):
        self.graph = dict()
        self.keys = []
        for instr in instrs:
            (pre,post) = instr
            if pre in self.graph:
                self.graph[pre].append(post)
            else:
                self.graph[pre] = [post]
                self.keys.append(pre)
        self.keys.append('P')
        self.graph['P'] = []
        self.numSteps = len(self.keys)
        self.in_progress = []

    def get_num_steps(self):
        return self.numSteps

    # A step that can be completed is one that does not appear
    # in any of the graph's lists. We need to remove keys that
    # appear in the graph's lists.
    def get_available_steps(self):
        avail_keys = copy.copy(self.keys)
        for item in self.graph:
            for step in self.graph[item]:
                if step in avail_keys:
                    step_index = avail_keys.index(step)
                    if step_index != -1:
                        avail_keys.pop(step_index)
        for step in self.in_progress:
            if step in avail_keys:
                avail_keys.pop(avail_keys.index(step))
        return sorted(avail_keys)

    # Completing a step means that we delete the item from the graph.
    def complete_step(self, step):
        self.graph.pop(step)
        self.keys.pop(self.keys.index(step))
    
    def put_in_progress(self, step):
        self.in_progress.append(step)
    
    def remove_in_progress(self, step):
        self.in_progress.pop(self.in_progress.index(step))


def get_instr_data():
    file = open('input.txt', 'r')
    results = []
    for line in file.readlines():
        # decode the line
        line = line.splitlines()[0]
        data = line.split(' ')
        pre_req = data[1]
        step = data[7]
        results.append((pre_req, step))
    return sorted(results)

def instruction_order():
    instrs = get_instr_data()
    graph = InstructionGraph(instrs)
    order=''
    num_steps = graph.get_num_steps()
    while len(order) < num_steps:
        avail_steps = graph.get_available_steps()
        order += avail_steps[0]
        graph.complete_step(avail_steps[0])
    return order

def task_time(step):
    return 60 + ord(step) - 64
    #return ord(step) - 64


def time_to_complete():
    instrs = get_instr_data()
    graph = InstructionGraph(instrs)
    order = ''
    avail_workers = 5
    num_steps = graph.get_num_steps()
    in_progress = []
    second = 0
    while len(order) < num_steps:
        # get the available steps
        avail_steps = graph.get_available_steps()
        
        # assign tasks to available workers
        while avail_workers > 0 and len(avail_steps) > 0:
            step = avail_steps.pop(0)
            in_progress.append((step, task_time(step)))
            graph.put_in_progress(step)
            avail_workers -= 1
            
        # perform progress on tasks
        to_remove = []
        for task in in_progress:
            (step, time) = task
            index = in_progress.index(task)
            if time - 1 == 0:
                graph.complete_step(step)
                graph.remove_in_progress(step)
                avail_workers += 1
                to_remove.append(index)
                order += step
                # assign tasks to available workers
                while avail_workers > 0 and len(avail_steps) > 0:
                    step = avail_steps.pop(0)
                    in_progress.append((step, task_time(step)))
                    graph.put_in_progress(step)
                    avail_workers -= 1
            else:
                in_progress[index] = (step, time - 1)
        for index in reversed(sorted(to_remove)):
            in_progress.pop(index)
        to_remove = []
        
        second += 1
    return second



print(instruction_order())
print(time_to_complete())

