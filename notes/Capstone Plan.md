


# Capstone Plan #

* The general goal is to generate a set of equations about the given code that 
    - make useful fuel-usage guarantees
    - can be handled well by Rosette/SMT-solvers
* The variables in these equations will be 
    - the **fuel usage** of each subexpression
    - the value of the **credits** parameter at each subexpression

### Phase 1: Racket ###

* Add cost-limiting features to a subset of racket
    - No guarantees about actual credit usage yet
* Small set of added features:
    - A *parameter* for available `credits` with read-only reflection
    - A `(run-with limit expr)` form with arbitrary `limit` expression
    - A `CreditException`
* Most of the forms in the python implementation will now be *macros*
    - Can write a few in this phase for convenience

### Phase 2: Rosette ###

* Write a type-checker for this language
* Associate costs with various methods
* Traverse code and while making rosette *assertions*
    - Make a *symbolic* integer for available credits at every point in the code
        + Rosette must be able to verify that they are all > 0
        + Will Rosette automatically keep upper and lower bounds?
* Create macros, but type-checking happens after their expansion

### Phase 3: Synapse ###

* "Synapse is a framework for program synthesis with cost functions"
    - Didn't work. Depends on the file layout of older versions of Rosette
* Given start code, insert code to make it type-check, preserving behavior
* Possible cost functions:
    - Least possible credits used for inserted code
    - Minimize the provable cost of expressions
* Optimizations that Synapse might handle well:
    - Balancing branches of `if` expressions (only when worth it)
    - Recognizing simple loops; could run loop `credits/cost` times instead of checking available credits every loop
* Macros now represent assertions that Synapse maintains

### Possible Additional Features ###

* Objects that represent a "thread"
    - An expression, an allotment of credits, and a continuation
* Create meaningful contracts
* Constrain other resources (stack, memory)












