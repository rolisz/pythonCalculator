__author__ = 'Roland'
from tokenizer import token,Tokenizer

class ExpressionError(Exception):
    pass

def indent(lines, amount, ch=' '):
    padding = amount * ch
    return padding + ('\n'+padding).join(lines.split('\n'))

class tree:

    def __init__(self,value = None,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
        self.type = 'node'

    def __str__(self):
        return "Value:" + str(self.value) +"\nChildren: \n" + indent(str(self.left),4) + "\n" + indent(str(self.right),4)

    def __eq__(self, other):
        return isinstance(other,tree) and self.value == other.value and self.left == other.left and self.right == other.right

class parseTree:

    def buildParseTree(self,tokens):
        return self.parseAssignment(tokens)

    def parseAssignment(self,tokens):
        for i in range(len(tokens)):
            if token('operator','=') == tokens[i]:
                if i == 0:
                    raise ExpressionError("Assignement is not done this way")
                return tree('=',tokens[:i][0],self.parseAssignment(tokens[i+1:]))
        return self.parseParens(tokens)

    def parseAdditive(self,tokens):
        i = 1
        while i<len(tokens):
            if tokens[i] in ['+','-']:
                return tree(tokens[i].value,self.parseMultiplicative(tokens[:i]),self.parseAdditive(tokens[i+1:]))
            i+=1
        if len(tokens) == 2 and tokens[0] in ['+','-']:
            return token(tokens[1].type,"".join([tokens[0].value,tokens[1].value]))
        return self.parseMultiplicative(tokens)

    def parseMultiplicative(self,tokens):
        i = 0
        while i< len(tokens):
            if tokens[i].value in ['*','/','%']:
                return tree(tokens[i].value,self.parsePower(tokens[:i]),self.parseMultiplicative(tokens[i+1:]))
            i+=1
        if len(tokens) > 1:
            return self.parsePower(tokens)
        if not len(tokens):
            raise ExpressionError("Addition is not done this way")
        if tokens[0].type not in ['identifier','number','node']:
            raise ExpressionError("Operator + operator? Not good")
        return tokens[0]

    def parsePower(self,tokens):
        i = 0
        while i< len(tokens):
            if tokens[i] == token('operator','^'):
                return tree(tokens[i].value,self.parseFunctions(tokens[:i]),self.parseFunctions(tokens[i+1:]))
            i+=1
        if len(tokens) > 1:
            return self.parseFunctions(tokens)
        if not len(tokens):
            raise ExpressionError("Multiplication is not done this way")
        if tokens[0].type not in ['identifier','number','node']:
            raise ExpressionError("Operator and operator? Not good")
        return tokens[0]

    def parseFunctions(self,tokens):
        i = 0
        while i < len(tokens)-1:
            if tokens[i].type == 'identifier' and tokens[i+1].type in ['node','identifier','number'] :
                return tree(tokens[i].value,tokens[i+1])
            i+=1
        if len(tokens) > 1:
            raise ExpressionError("Bad function call")
        if tokens[0].type == 'node':
            return tokens[0]
        return tokens[0].value

    def parseParens(self,tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == token('operator','('):
                openCount = 1
                start = i
                i +=1
                while i < len(tokens) and openCount:
                    if tokens[i] == token('operator','('):
                        openCount+=1
                    if tokens[i] == token('operator',')'):
                        openCount-=1
                    if openCount == 0:
                        tokens[start:i+1] = [self.parseParens(tokens[start+1:i])]
                        i = start
                    i+=1
                if openCount != 0:
                    raise ExpressionError("Parens problem")
            i +=1
        return self.parseAdditive(tokens)


