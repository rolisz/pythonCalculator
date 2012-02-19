__author__ = 'Roland'
import interpreter

print("Enter your expressions to be calculated. Enter 'Exit' to exit the calculator.")
expression = ""
tokenizer = interpreter.Tokenizer()
parser= interpreter.parseTree()
interpr = interpreter.interpreter()
while True:
    expression = input('> ')
    if expression != "Exit":
        try:
            result = interpr.evaluate(parser.buildParseTree(tokenizer.tokenize(expression)))
            print(result)
        except Exception as e:
            print(e)
    else:
        break

print("Thank you for using rolisz calculator!")