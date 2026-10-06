canget(state(middle, middle, onbox, has)).

canget(State1) :-
    move(State1, _, State2),
    canget(State2).

move(%grasp
    state(middle, middle, onbox, hasnot),
    grasp,
    state(middle, middle, onbox, has)
).

move(%climb
    state(P, P, onfloor, H),
    climb,
    state(P, P, onbox, H)
).

move(%push
    state(P1, P1, onfloor, H),
    push(P1, P2),
    state(P2, P2, onfloor, H)
).

move(%walk
    state(P1, B, onfloor, H),
    walk(P1, P2),
    state(P2, B, onfloor, H)
).
