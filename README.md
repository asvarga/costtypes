# README #

### TODO ###

* !!! consider building off pyret project
    - pro: has type annotations
    - con: no try/catch
* write getCost with knowledge that it might have INF cost
    - assume code is typable
    - !!! there may always be cases where cost can be known statically but is hard to prove
* costs for functions
    - cost to eval expr (to function)
    - cost to apply function / eval body (to function)
    - cost to apply result (etc)
    - need to use inputs to functions too?
        + need general function-cost type?
    - Maybe this is all wrong because functions passed in have unknown cost so must be dynamically checked. 
        + Some functions in scope will be known ahead of time though, like ops in BASE, "let" clauses, etc.
* !!! Do exprs need to have cost attached?
    - just some? 
    - *just closures?*
    - just lambda exprs? 
    - sometimes the cost of an expr that evals to a closure can be known before actually evaling, but sometimes it can't
    - !!! [@app? f a b] for when f's app-cost can't be known statically
        + first just compute eval f to f_
        + then check if it has enough credit to compute a, b, and (f_ a b)
            * iff so, do it

* distinguish between types of exprs, reduced values (applicable vs not)
    - ops produce values but closures produce exprs?
        + no, because ops still need an associated cost?





value: cost 0, reduce to self
expr: cost ?, reduce to ?
func: cost 0, reduce to self, appCost ?, returns ?











