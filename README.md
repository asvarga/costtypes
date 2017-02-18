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
* Hierarchy of sandboxing scales:
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
    - a cost type (currently) is
        + `n:int` // costs n to reduce
        + `(n:int, t:type)` // costs n to reduce to function of cost type `t`
    - assumes that the code passes usual type-checks
    - improvements mentioned below  
* Static: A type system for cost, in credits
    - `[@lrun limit body fail]` 
        + limits the runtime of the body 
        + type is approximately `limit`
        + if `type of body > limit`: replace whole expr with fail
    - `[@app f a b]`
        + if the type of `f` can't be known statically, becomes an `@app?` expr
* Dynamic: Inserted checks on code that can't be typed statically
    - `[@lrun limit body fail]`
        + a stack of allotted credits is maintained
        + `@lrun` adds a stack frame with `limit` credits for `body`
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

### PROBLEMS / IMPROVEMENTS ###
* "dependent types": type of function is function of types of args
    - types for variadic functions
* bounding symbol look-up cost
* other resources
* other good ideas
* allow arbitrary proofs about cost



# TODO #

* fix `frun` and `drun`
* attach type to anything


# NOTES #
* `drun` could be variadic, and the function could return a vector the size of the number of branches, that sum to <= the allotted credits
* `lrun` doesn't take responsibility for its fail-case, but `frun` does



















