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
* *`@`xxx* // constants
* [*`@`xxx* y z] // special form
* (f a b) // syntactic sugar for [*`@`app* f a b]

### IMPLEMENTATION ###
* Static: A type system for cost, in credits
    - a cost type (currently) is
        + n:int // costs n to reduce
        + (n:int, t:type) // costs n to reduce to function of cost type t
    - assumes that the code passes usual type-checks
    - improvements mentioned below  
* Dynamic: Inserted checks on code that can't be typed statically
    - [*`@`lrun* limit body fail] limits the runtime of the body
        + a stack of alloted credits is maintained
        + *`@`lrun* takes limit credits out of its allotment and adds a layer for body to run with
        + if body runs out of credits during run-time an error is raised and caught here, and fail is run
    - turns *`@`app* into *`@`app*?
        + evaluates f
        + checks if it can afford to apply f now that its type is known
        + either applies it or raises error accordingly

### TYPE SYSTEM METRICS ###
* No free lunch!
* Minimize "arbitrage": 
    - (Max time to run type x)/(Min time to run type x)/x

### POSSIBLE IMPROVEMENTS ###
* "dependent types": type of function is function of types of args
    - types for variadic functions
* other good ideas
* allow arbitrary proofs about cost



# TODO #

* dynamic runls
    - use credits that is function of available (ex: half)























