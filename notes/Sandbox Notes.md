

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
- give all objects a reference to their own code
    + private by default, but can (honestly) reveal their code
    + give exactly the information that they alrady have

### Plan ###

+ skim rest of E docs (especially E-Kernel)
+ read about scheme engines
- look into monte: eval, JIT, etc
- look into racket: OCap, eval, JIT, etc
- return to rosette engines
- figure out engines+OCap






