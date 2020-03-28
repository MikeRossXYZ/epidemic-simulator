#!/usr/bin/env python3

from setup import setup
from simulate import run_simulation
from execution_context import ExecutionContext

def main():
    ctx = ExecutionContext()
    setup(ctx)
    run_simulation(ctx)

if __name__ == "__main__":
    main()
