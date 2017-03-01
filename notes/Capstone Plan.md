


# Capstone Plan #

### Phase 1: Racket ###

* Add cost-limiting features to a subset of racket
    - No guarantees about actual credit usage
* Small set of added features:
    - A *parameter* for available `credits` with read-only reflection
    - A `(run-with limit expr)` form with arbitrary `limit` expression
        + A variant with an `exception` expr
* Most of the forms in the python implementation will now be macros
    - Can write a couple in this phase for convenience

### Phase 2: Rosette ###

* Write a type-checker for this language
* Associate costs with various methods
* Traverse code and while making rosette assertions
    - Make a symbolic integer for available credits at every point in the code
        + Rosette must be able to verify that they are all > 0
        + Will Rosette automatically keep upper and lower bounds?
* Create macros, but type-checking happens after their expansion

### Phase 3: Synapse ###

* "Synapse is a framework for program synthesis with cost functions"
    - It synthesizes optimized code with respect to some cost function
* Given start code, insert code to make it type-check
* Possible cost functions:
    - Least possible credits used for inserted code
    - Minimize the provable cost of expressions
* Optimizations that Synapse might handle well:
    - Balancing branches of `if` expressions (only when worth it)
    - Recognizing simple loops; could run loop `credits/cost` times instead of checking available credits every loop
* Macros now represent assertions that Synapse maintains

### Possible Features ###

* Objects that represent a "thread"
    * an expression, an allotment of credits, and a continuation







