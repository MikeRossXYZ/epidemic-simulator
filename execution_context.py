class ExecutionContext:
    """
    Execution context that is initialized before simulation time
    and passed to execution threads (once multi-threading is enabled).
    Members of the structure should be considered immutable once simulation
    begins.
    """

    # Dictionary of tables available.
    # Keyed on the type of value stored in the table or name.
    # Values are Table objects
    tables = {}
