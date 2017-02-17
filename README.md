# README #

### MOTIVATION ###
* Safely run untrusted code
* Just limiting run-time
    - Meaningful platform-independent concept of "time": credits
* Lightweight

### RELATION TO SANDBOXING ###
* Only focused on the resource of computation itself
* Heirarchy of sandboxing scales:
    - different hardware: multiple computers
    - different process: OS level
    - same process, different thread: sandboxing, MrEd
    - same thread: this!

### DISCLAIMER ###
* Probably wrong!

### BASE LANGUAGE ###
- @xxx // constants
- [@xxx y z] // special form
- (f a b) // syntactic sugar for [@app f a b]

### IMPLEMENTATION ###
* Static: A type system for cost, in credits
    - a cost type (currently) is
        + n:int // costs n to reduce
        + (n:int, t:type) // costs n to reduce to function of cost type t
    - improvements mentinoed below  
* Dynamic: Inserted checks on code that can't be typed statically
    - turns "@app" into "@app?"
    - wraps

### TODO ###

* dynamic runls
    - use credits that is function of available (ex: half)























