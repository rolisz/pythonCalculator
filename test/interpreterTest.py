__author__ = 'Roland'
from interpreter import interpreter
from tokenizer import Tokenizer
from tree import parseTree

pT = parseTree()
tok = Tokenizer()
interp = interpreter()
Tree = pT.buildParseTree(tok.tokenize("1+2"))
assert(interp.evaluate(Tree) == 3)
Tree = pT.buildParseTree(tok.tokenize("(5+(2*3+2))-3*((5+6)/2-4)"))
assert(interp.evaluate(Tree) == 8.5)
Tree = pT.buildParseTree(tok.tokenize("x = 2"))
assert(interp.evaluate(Tree) == 2)
Tree = pT.buildParseTree(tok.tokenize("y = 4^3"))
assert(interp.evaluate(Tree) == 64)
Tree = pT.buildParseTree(tok.tokenize("y^x*2-3"))
assert(interp.evaluate(Tree) == 8189)
Tree = pT.buildParseTree(tok.tokenize("(x+(2*y+2))-y*((5+x)/2-4)"))
assert(interp.evaluate(Tree) == 164)
Tree = pT.buildParseTree(tok.tokenize("sin(10)"))
assert(interp.evaluate(Tree) == -0.5440211108893698)
Tree = pT.buildParseTree(tok.tokenize("2^(5+1)"))
assert(interp.evaluate(Tree) == 64)
Tree = pT.buildParseTree(tok.tokenize("(2+1)^(2+1)"))
assert(interp.evaluate(Tree) == 27)