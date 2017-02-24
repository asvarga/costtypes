# README #

### MOTIVATION ###
* Safely run untrusted code
* Just limiting run-time
    - Meaningful platform-independent concept of "time": credits
* Lightweight
* Uses
    - scriptable user interfaces, games, smart-things
    - programming education
    - genetic programming

### RELATION TO SANDBOXING ###
* This is only focused on the resource of computation itself
* Hierarchy of sandboxing scales: foreign program runs in
    - different hardware: multiple computers
    - different process: OS level
    - same process, different thread: sandboxing, MrEd
    - same thread: this!

### DISCLAIMER ###
* Simple prototype
* Probably wrong!

### BASE LANGUAGE ###
* `@xxx` // constants
* `[@xxx y z]` // special form
* `(f a b)` // syntactic sugar for `[@app f a b]`

### IMPLEMENTATION ###
* A type system for cost, in credits
    - cost type describes *miminum* necessary cost to run (*not max*)
    - a cost type (currently) is
        + `n:int` // costs n to reduce
        + `(n:int, t:type)` // costs n to reduce to function of cost type `t`
        + `. = (infinity, .)`
    - *assumes that the code passes usual type-checks*
* Static: Type check and modify
    - `[@lrun limit body fail]` 
        + limits the runtime of the body 
        + *cost type is just parts that will certainly be run*
        + if `type of body > limit`: replace whole expr with `fail`
    - `[@app f a b]`
        + if the type of `f` can't be known statically, becomes an `@app?` expr
* Dynamic: Inserted checks on code that can't be typed statically
    - `[@lrun limit body fail]`
        + a stack of allotted credits is maintained
        + `@lrun` takes `limit` credits from the top of the stack, and adds a new top frame with `limit` credits for `body`
            * ex: `[ 100 | 100 | 100 ]` -> `[ 30 | 70 | 100 | 100 ]`
        + if `body` runs out of credits during run-time, an exception is raised and caught here, and `fail` is run
    - `[@app? f a b]`
        + evaluates `f`
        + checks if it can afford to apply `f` now that its type is known
        + either applies `f` or raises exception accordingly

### TYPE SYSTEM METRICS ###
* No free lunch!
* Minimize "arbitrage": 
    - `(Max time to run X)/(Min time to run X)`
* meta-circular alignment?

### PROBLEMS ###
* symbol lookup cost is unbounded
* variadic functions are unbounded

### IMPROVEMENTS ###
* "dependent types": type of function is function of types of args
* allow arbitrary proofs about cost
* constrain other resources
    - stack depth
    - memory usage




# TODO #
* **try to avoid mutating credit stack**
    - `run` might need to accept failure "continuation"
        + wouldn't use python's error handling
        + requires tco, or manual expansion to a big loop
    - rosette/racket might have a better way to do this
* **implement `@run?`**: like `@frun` with no `fail` case
    - just checks if it has enough credits, and then runs w/o own try/catch
    - wraps an expr, not a closure
* fix imbalanced `@if`s by wrapping bigger branch or both in `@run?`s
* implement in Rosette?
* variadic `@drun*` for many branches?
* form that runs code for min possible (like `@frun`'s `fail` case)
* do more of lamb construction while typing? (just attach nv at run-time)

# NOTES #    
* consider all combinations of (env, name, args, expr)
    - interacting with a closure is quite different than with an expr
        + consider "getting" the body of a function in a closure 
            * this should return a closure with an extended env that maps the function's args to symbolic values
            * forbid other operations
    - also consider qhat a quote is












