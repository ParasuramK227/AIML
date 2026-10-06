% Hill Climbing Algorithm 
value(a,1). 
value(b,3). 
value(c,5). 
value(d,7). 
value(e,9). 

next(a,b). 
next(b,c). 
next(c,d). 
next(d,e).

hill_climb(Node, Node) :- 
    \+ next(Node,_).

hill_climb(Node, Result) :- 
    next(Node, Next), 
    value(Node, V1), 
    value(Next, V2), 
    V2 > V1, 
    hill_climb(Next, Result).
