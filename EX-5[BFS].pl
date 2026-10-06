%BFS in prolog
bfs(Start, Goal, Path) :- 
    bfs_search([[Start]], Goal, Result), 
    reverse(Result, Path). 
 
bfs_search([[Goal|Rest]|_], Goal, [Goal|Rest]). 
 
bfs_search([[Current|Rest]|Others], Goal, Path) :- 
    findall([Next,Current|Rest], 
           (edge(Current, Next), 
           \+ member(Next, [Current|Rest])), 
           NewPaths), 
    append(Others, NewPaths, Queue), 
    bfs_search(Queue, Goal, Path).
