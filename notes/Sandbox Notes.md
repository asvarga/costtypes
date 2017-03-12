

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


### Plan ###

- figure out safety of eval in monte
- read scheme fuel stuff
- figure out fuel stuff






