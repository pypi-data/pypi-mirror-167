import sys
import os
from typing import List

class Printer:
    def __init__(self, name, color = "") -> None:
        self.c = color
        self.name = name
    def __call__(self, *val: List[str], sep=" ", end="\n", flush=False, log=True) -> None:
        if (log):
            sys.stdout = sys.__stdout__
            sys.stdout.write(self.c + f"[{self.name}] ")
            print(*val, sep=sep, end=end, flush=flush)
            sys.stdout.write(f"{'-' * os.get_terminal_size().columns}\033[0m\n")

class Logging:
    def __init__(self) -> None:
        self.log = True
        self.error = Printer("ERROR", "\033[31m")
        self.success = Printer("SUCCESSFUL", "\033[32m")
        self.log = Printer("INFO")

logging = Logging()