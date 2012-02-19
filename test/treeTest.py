__author__ = 'Roland'
from tree import tree, parseTree,ExpressionError
from tokenizer import token, Tokenizer

pT = parseTree()
tok = Tokenizer()
assert(pT.buildParseTree(tok.tokenize("1+2")) == tree('+','1','2'))
assert(pT.buildParseTree(tok.tokenize("(x+(y*z+2))-3*((5+x)/2-4)")) == tree('-',tree('+','x',tree('+',tree('*','y','z'),'2')),tree('*','3',tree('-',tree('/',tree('+','5','x'),'2'),'4'))))
assert (pT.buildParseTree(tok.tokenize("sin(x)+ln(y)*3")) == tree('+',tree('sin','x'),tree('*',tree('ln','y'),'3')))
assert (pT.buildParseTree(tok.tokenize('x^y*2-3')) == tree('-',tree('*',tree('^','x','y'),'2'),'3'))
assert (pT.buildParseTree(tok.tokenize('x=y=5*3-20*sin(x+y)')) == tree('=','x',tree('=','y',tree('-',tree('*','5','3'),tree('*','20',tree('sin',tree('+','x','y')))))))
try:            # teste pentru erori
    Tree = pT.buildParseTree(tok.tokenize('x***y'))
    assert(False)
except ExpressionError:
    assert(True)
try:
    Tree = pT.buildParseTree(tok.tokenize('x===y'))
    assert(False)
except ExpressionError:
    assert(True)
try:
    Tree = pT.buildParseTree(tok.tokenize('x+++y'))
    assert(False)
except ExpressionError:
    assert(True)
try:
    Tree = pT.buildParseTree(tok.tokenize('+x*3'))
    assert(False)
except ExpressionError:
    assert(True)
assert(pT.buildParseTree(tok.tokenize('5+(-3)')) == tree('+','5','-3'))
print(pT.buildParseTree(tok.tokenize('2^(5+1)')))
print(pT.buildParseTree(tok.tokenize('(5+1)^(2+1)')))
#assert(pT.buildParseTree(tok.tokenize('2^(5+1)')) == tree('+','5','-3'))