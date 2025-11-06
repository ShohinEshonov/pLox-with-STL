


from sys import argv, exit


class GenerateAst:
    def main(self, args):
        if len(args) != 2:
            print("Usage: generate_ast <output directory>")
            exit(64)

        outputDir = args[1]
        self.defineAst(
            outputDir,
            "Expr",
            [
                "Binary = left:Expr, operator:Token, right:Expr",
                "Grouping = expression:Expr",
                "Literal = value:Any",
                "Unary = operator:Token, right:Expr",
            ],
        )

    def defineAst(self, outputDir, baseName, types):
        path = f"{outputDir}/{baseName}.py"
        with open(path, "w", encoding="utf-8") as file:
            # Заголовок
            file.write("from abc import ABC, abstractmethod\n\n\n")

            # === Базовый класс ===
            file.write(f"class {baseName}(ABC):\n")
            file.write("    @abstractmethod\n")
            file.write(f'    def accept(self, visitor: "{baseName}Visitor"):\n')
            file.write("        pass\n\n\n")

            # === Абстрактный Visitor ===
            self.defineVisitor(file, baseName, types)

            # === Подклассы ===
            for type_ in types:
                className = type_.split("=")[0].strip()
                fields = type_.split("=")[1].strip()
                self.defineType(file, baseName, className, fields)

    def defineVisitor(self, file, baseName, types):
        file.write(f"class {baseName}Visitor(ABC):\n")
        for type_ in types:
            typeName = type_.split("=")[0].strip()
            file.write("    @abstractmethod\n")
            file.write(f'    def visit{typeName}{baseName}(self, expr: "{typeName}"):\n')
            file.write("        pass\n")
        file.write("\n\n")

    def defineType(self, file, baseName, className, fieldList):
        file.write(f"class {className}({baseName}):\n")

        # Разбор полей
        fields = [f.strip() for f in fieldList.split(",")]
        names = [f.split(":")[0] for f in fields]

        # Конструктор с type hints для полей
        params = ", ".join(fields)
        file.write(f"    def __init__(self, {params}):\n")
        for name in names:
            file.write(f"        self.{name} = {name}\n")
        file.write("\n")

        # Метод accept с forward reference
        file.write(f'    def accept(self, visitor: "{baseName}Visitor"):\n')
        file.write(f"        return visitor.visit{className}{baseName}(self)\n\n\n")


if __name__ == "__main__":
    ast = GenerateAst()
    ast.main(argv)
