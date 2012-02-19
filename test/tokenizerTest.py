import tokenizer

__author__ = 'Roland'

t = tokenizer.Tokenizer()
t.tokenize("1+2")
assert (t.tokenize("1+2") == [tokenizer.token('number','1'),tokenizer.token('operator','+'),tokenizer.token('number','2')])
assert (t.tokenize("1+2") == ['1',"+",'2'])
assert (t.tokenize("(x+y)*2/4") == [tokenizer.token('operator','('),tokenizer.token('identifier','x'),tokenizer.token('operator','+'),tokenizer.token('identifier','y'),
                                   tokenizer.token('operator',')'),tokenizer.token('operator','*'),tokenizer.token('number','2'),tokenizer.token('operator','/'),
                                   tokenizer.token('number','4')])
assert(t.tokenize("(x+(y*z+2))-3*((5+x)/2-4)") == [tokenizer.token('operator','('),
                                                   tokenizer.token('identifier','x'),
                                                   tokenizer.token('operator','+'),
                                                   tokenizer.token('operator','('),
                                                   tokenizer.token('identifier','y'),
                                                   tokenizer.token('operator','*'),
                                                   tokenizer.token('identifier','z'),
                                                   tokenizer.token('operator','+'),
                                                   tokenizer.token('number','2'),
                                                   tokenizer.token('operator',')'),
                                                   tokenizer.token('operator',')'),
                                                   tokenizer.token('operator','-'),
                                                   tokenizer.token('number','3'),
                                                   tokenizer.token('operator','*'),
                                                   tokenizer.token('operator','('),
                                                   tokenizer.token('operator','('),
                                                   tokenizer.token('number','5'),
                                                   tokenizer.token('operator','+'),
                                                   tokenizer.token('identifier','x'),
                                                   tokenizer.token('operator',')'),
                                                   tokenizer.token('operator','/'),
                                                   tokenizer.token('number','2'),
                                                   tokenizer.token('operator','-'),
                                                   tokenizer.token('number','4'),
                                                   tokenizer.token('operator',')'),
                                                   ])

assert (t.tokenize("1+2") == ['1',"+",'2'])
assert (t.tokenize("(x+y)*2/4") == ["(","x","+","y",")","*","2","/","4"])
assert(t.tokenize("(x+(y*z+2))-3*((5+x)/2-4)") == ["(","x","+","(","y","*","z","+","2",")",")","-","3","*","(","(","5","+","x",")","/","2","-","4",")" ])
try:
    t.tokenize("_&x+y")
    assert(False)
except tokenizer.TokenizerError:
    assert(True)
assert(t.tokenize(" x+y") == ['x','+','y'])
assert(t.tokenize(" x + y ") == ['x','+','y'])