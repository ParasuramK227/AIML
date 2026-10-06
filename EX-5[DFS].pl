% DFS in Prolog

edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(e,g).
edge(f,g).

dfs(Start, Goal, Path) :-
    dfs_search(Start, Goal, [Start], Path).

dfs_search(Goal, Goal, Visited, Path) :-
    reverse(Visited, Path).

dfs_search(Current, Goal, Visited, Path) :-
    edge(Current, Next),
    \+ member(Next, Visited),
    dfs_search(Next, Goal, [Next|Visited], Path).