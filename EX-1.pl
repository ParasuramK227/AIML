male(john).
male(david).

female(mary).
female(linda).

parent(john, david).
parent(mary, david).
parent(john, linda).
parent(mary, linda).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).