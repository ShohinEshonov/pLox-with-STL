from abc import ABC, abstractmethod
from pLox.Token import Token


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: "ExprVisitor"):
        pass


class ExprVisitor(ABC):
    @abstractmethod
    def visitBinaryExpr(self, expr: "Binary"):
        pass

    @abstractmethod
    def visitGroupingExpr(self, expr: "Grouping"):
        pass

    @abstractmethod
    def visitLiteralExpr(self, expr: "Literal"):
        pass

    @abstractmethod
    def visitUnaryExpr(self, expr: "Unary"):
        pass


class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitBinaryExpr(self)


class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitGroupingExpr(self)


class Literal(Expr):
    def __init__(self, value: any):
        self.value = value

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitLiteralExpr(self)


class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: "ExprVisitor"):
        return visitor.visitUnaryExpr(self)
