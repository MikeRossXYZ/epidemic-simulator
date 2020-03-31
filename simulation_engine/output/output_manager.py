from multiprocessing import Process

class OutputManager(Process):
    """Output manager class will accept all values that are to be output
    and correctly decide how to write them to file or send to another program.

    Currently, it operates as a pass through to standard out, but in the future
    it can route traffic to various files and network requests.
    """

    def __init__(self, queue):
        super(Process, self).__init__()
        self.q_output = queue

    def run(self):
        while True:
            out_item = self.q_output.get()
            if (out_item == None):
                break
            else:
                print(out_item)
