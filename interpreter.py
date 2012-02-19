__author__ = 'Roland'
from tokenizer import token,Tokenizer
from tree import tree,parseTree
import math
class InterpretError(Exception):
    pass

class interpreter:

    functions = { 'sin':math.sin,'cos':math.cos,'ln':math.log,'erfc':math.erfc,'lgamma':math.lgamma,
                  '+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:a/b,'%':lambda a,b:a%b,'^':lambda a,b:a**b,}

    def __init__(self):
        self.vars = { }

    def evaluate(self,expression):
        if isinstance(expression,tree):
            if expression.value == '=':
                return self.assign(expression)
            left = self.getValue(expression.left)
            right = self.getValue(expression.right)
            if type(expression.value) == str and expression.value in self.functions:
                if right!=None:
                    return self.functions[expression.value](left,right)
                else:
                    return self.functions[expression.value](float(left))
        raise InterpretError("Should be a tree here")

    def assign(self,expression):
        if not self.type(expression.left,'identifier'):
            raise InterpretError("Assignments must be done to a variable!")
        self.vars[expression.left.value] = self.getValue(expression.right)
        return self.vars[expression.left.value]

    def type(self,element,expected):
        return element != None and type(element) != int and type(element) != float and type(element) != str and element.type == expected

    def getValue(self,element):
        if self.type(element,'node'):
            element = self.evaluate(element)
        if self.type(element,'number'):
            element = int(element.value)
        if self.type(element,'identifier'):
            if element.value in self.vars:
                element = self.vars[element.value]
            else:
                raise InterpretError("No such variable "+element.value)
        if type(element) == str:
            if element in self.vars:
                return self.vars[element]
            else:
                try:
                    element = int(element)
                except ValueError:
                    raise InterpretError("Variable "+element+" doesn't exist")
        return element

