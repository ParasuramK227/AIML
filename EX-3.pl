% A* Algorithm in Prolog 
edge(a,b,1). 
edge(a,c,3). 
edge(b,d,3). 
edge(b,e,6). 
edge(c,f,5). 
edge(e,g,2). 
edge(f,g,2). 
 
heuristic(a,7). 
heuristic(b,6). 
heuristic(c,4). 
heuristic(d,5). 
heuristic(e,2). 
heuristic(f,1). 
heuristic(g,0). 
astar(Start, Goal, Path) :- 
search([[Start]], Goal, RevPath), 
reverse(RevPath, Path). 
search([[Goal|Rest]|_], Goal, [Goal|Rest]). 
search([[Node|Rest]|Others], Goal, Path) :- 
findall([Next,Node|Rest], 
edge(Node,Next,_), 
NewPaths), 
append(Others, NewPaths, Queue), 
search(Queue, Goal, Path).
