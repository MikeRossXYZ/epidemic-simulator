import table
import config

def setup(ctx):
    """
    Accepts a configuration context and sets it up for execution

    Setup model assumptions, load tables, and configure other settings
    before starting the execution loop
    """

    # Infection probability loading
    tbl = table.Table()
    tbl.name = "infection_probability"
    for entry in config.INFECTION_TRANSMISSION_RECORDS:
        table.tbl_insert_record(tbl, entry[0], entry[1])
    ctx.tables[tbl.name] = tbl
    