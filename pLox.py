from sys import exit, argv, stdin
from .Scanner import Scanner


class Lox:
    def __init__(self):
        self.hadError: bool = False

    def runfile(self, path: str):
        with open(path, "r") as file:
            data: str = "".join(file.readlines())

            self.run(data)
            if self.hadError:
                exit(65)

    def run_prompt(self):
        reader = stdin  # sys.stdin

        while True:
            print(">", end="", flush=True)
            line: str = reader.readline()

            if line is None:
                pass

            self.run(line.strip())
            self.hadError = False

    def run(self, source: str):
        scanner = Scanner(source, error_handler=self.error)
        tokens: list = scanner.scanTokens()

        for token in tokens:
            print(token)

    def error(self, line: int, message: str):
        self.report(line, "", message)

    def report(self, line: int, where: str, message: str):
        print(f"[line {line}] Error {where}: {message}")
        self.hadError = True


if __name__ == "__main__":
    # checking for right params
    flags = argv[1:]
    if len(flags) > 1:
        print("Usage: pLox [script]")
        exit(64)
    elif len(flags) == 1:
        lox = Lox()
        lox.runfile(flags[0])
    else:
        lox = Lox()
        lox.run_prompt()
