

## Sandbox Notes ##

- OCap/sandboxing takes care of most guarantees one would want to make about untrusted code
    + except for fuel concerns!
- hardware ownership -> software ownership
    + both server and client can read all local code
- **Server**
    + trusted by all
    + can analyze local code for safety (mostly fuel-related)
        * send code to clients with unforgeable promises/proofs attached
    + can prevent different clients from reading eachother's code locally
- **Clients** 
    + can also analyze any code on their hardware
    + but no-one should trust their conclusions
- transparent code could be useful for markets, elections, etc
    + easier than having proofs of object behaviors

- Code-Carrying Objects
    + attach AST to the compiled objects appropriately, so it can be recovered after compilation
        * shouldn't actually give more information than having original AST
    + allows for both performance and inspectibility
        * asymptotic speed-up from constant-time look-ups?
    + access to this syntax is a capability
    + whenever actor A creates B from syntax, A gets access to B's syntax
        * this right propagates transitively
        * treat every separate hardware entity as an actor
    + These ASTs should be closures (have env attached)
        * interacting with a closure object 

- The right to *run*/*continue* is the only ambient authority that OCap doesn't handle
    + it can be split into *run-time*, *stack-usage*, and *memory-usage*
    + these both must be limited with methods like cost-type-checking


### Plan ###

+ skim rest of E docs (especially E-Kernel)
+ read about scheme engines
+ look into monte: eval, JIT, etc
+ try to implement Code-Carrying Objects in E/Monte
    * They've thought about this ("OpenSource pattern")
? look into racket: OCap, eval, JIT, etc
- return to rosette engines, but in python
- figure out engines+OCap






