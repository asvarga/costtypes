# README #

### TODO ###

* dynamic runls
* useful example, like iterative improvement of some approximation
    - need mutable values


* !!! [app? f a b] for when f's app-cost can't be known statically
    - first just compute eval f to f_
    - then check if it has enough credit to compute a, b, and (f_ a b)
        + iff so, do it
* Do exprs need to have cost attached?
    - just some? 
    - *just closures?*
    - just lambda exprs? 
    - sometimes the cost of an expr that evals to a closure can be known before actually evaling, but sometimes it can't

* consider building off pyret project
    - pro: has type annotations
    - con: no try/catch
* there may always be cases where cost can be known statically but is hard to prove




















