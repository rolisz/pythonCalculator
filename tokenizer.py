import re

__author__ = 'Roland'

class TokenizerError(Exception):
    pass

class token:

    def __init__(self,type,value = None):
        self.type = type
        self.value = value

    def __str__(self):
        return self.type + " " + self.value

    def __eq__(self, other):
        if isinstance(other,token):
            return self.type == other.type and self.value == other.value
        elif isinstance(other,str):
            return str(self.value) == other
        else:
            return False

class Tokenizer:

    def tokenize(self,string):
        self.string = string
        self.tokens = []

        self.index = 0
        match = False
        while self.index < len(self.string):
            token = self.operator()
            if token:
                self.tokens.append(token)
                match = True

            token = self.identifier()
            if token:
                self.tokens.append(token)
                match = True

            token = self.number()
            if token:
                self.tokens.append(token)
                match = True


            if self.skipWhite():
                match = True

            if not match:
                raise TokenizerError('Invalid simbol found:'+self.string[self.index])
            match = False
        return self.tokens

    def operator(self):
        if self.index < len(self.string) and self.string[self.index] in '+-/*()%^=':
            t = token('operator',self.string[self.index])
            self.index +=1
            return t
        else:
            return None

    def identifier(self):
        pattern = '^[a-zA-Z][a-zA-Z0-9_]*'
        match = re.match(pattern,self.string[self.index:])
        if match:
            t = token('identifier',match.group())
            self.index = self.index + match.end()
            return t
        return None

    def number(self):
        pattern = "^[0-9]+\\.?[0-9]*"
        match = re.match(pattern,self.string[self.index:])
        if match:
            t = token('number',match.group())
            self.index = self.index + match.end()
            return t
        return None

    def skipWhite(self):
        match = False
        while self.index < len(self.string) and self.string[self.index] == " ":
            self.index+=1
            match = True
        return match

