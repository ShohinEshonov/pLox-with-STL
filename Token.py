from .TokenType import TokenType


class Token:
    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        literal_str = str(self.literal) if self.literal is not None else "null"
        return f"{self.type} {self.lexeme} {literal_str}"
