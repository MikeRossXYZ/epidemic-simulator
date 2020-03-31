from multiprocessing import Queue
from output.output_manager import OutputManager

class ExecutionContext:
    """
    Execution context that is initialized before simulation time
    and passed to execution threads (once multi-threading is enabled).
    Members of the structure should be considered immutable once simulation
    begins.
    """

    def __init__(self):
        # Output manager initialization
        self.q_output = Queue()
        p_output = OutputManager(self.q_output)
        p_output.daemon = True
        p_output.start()

        # Dictionary of tables available.
        # Keyed on the type of value stored in the table or name.
        # Values are Table objects
        self.tables = {}

    def output(self, item):
        self.q_output.put(item)
