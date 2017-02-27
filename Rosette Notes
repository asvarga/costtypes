
Rosette Notes
-------------

- Symbolic procedures may, in the worst case, take as much time to execute as the slowest concrete procedure to which any symbolic procedure could evaluate under any solution?.
- vectors
	- A concrete vector supports constant-time access for concrete slot indices, and linear-time access for symbolic slot indices. 
	- A symbolic vector supports (worst-case) linear- and quadratic-time access for concrete and symbolic indices, respectively. 
	- Access time for symbolic vectors is given with respect to the longest possible concrete array to which any symbolic vector could evaluate under any solution?.
					conc vec 	sym vec 
		conc ind 	O(1) 		O(n)
		sym ind 	O(n) 		O(n^2)
- Rosette’s default solver is z3, although new (SMT) solvers can be added well. Rosette will work with any solver that implements the gen:solver generic interface.
- immutable transparent structures are treated as values rather than references.
- In addition to the memory and register values, the state of a Rosette program also includes the current path condition and the current assertion store. 
	- The path condition is a boolean value encoding the branch decisions taken to reach the present state
	- the assertion store is the set of boolean values (i.e., constraints) that have been asserted so far.


Questions
---------
- How is the term-cache implemented? It seems cool. (trie for s-exprs?)
	- "Rosette uses the term cache to ensure that no syntactically identical terms are created."




Capstone Ideas
-----

*** Tim: "Tell me about Synapse and what you envision using it for, then we can discuss."

ROSETTE : type-check desugared code
- Use both upper and lower bounds on cost
	- prepare examples of forms and their associated cost-types
- "path conditions": at any point in code:
	- pre-condition: can assume that there are sufficient credits available
	- guarantee: will never run code with insufficient credits
	- the available credits at each point in code should be a symbolic variable
* traverse code and make assertions about cost
	- should code ignore parent code? (information flows up)
- these programs have read access to available credits parameter (reflection)

SYNAPSE : intelligently/optimally desugar/synthesize the code
- could just use Synapse's cost computing functionality/structures (and not the synthesis)
- optimizations that Synapse might handle well
	- recognizing loops: "loop available/cost times" instead of checking each time
	- balancing if branchings
- things to optimize
	- less dynamic checks (more credits towards given code)
	- minimum provable cost (for min or max bound)


- treat cost-limiting forms like macros with associated guarantees
	- have many macros (and variants) that get desugared to a small set of forms
		- limit body expr vs limit this expr
		- exception vs no-exception
		- dependent on available cost?
- unfinished runs:
	- let program specify whether to run if it can't finish (min < creds < max)
	- throw/cc: when out of credits, pause to be resumed later
	- also allow left-over credits to be saved for later (maybe)
	- process object: continuation + available credits
- dependent types: depends on available credits
	- depending on values (like real dependent types) is obviously harder
- Use less special forms, and smarter type-checking
- Type-checking my cost-limiting language includes checking that cost-limits are guaranteed to be respected
	- use rosette to synthesize programs that type-check and are optimal in some way
	- take program as input and create new functionally equivalent program that type-checks *and is optimal*
	- either
		- just say input and output programs must always be equivalent
		- place holes in the input program to be filled
- could just verify my implementation or prove bounds on arbitrage
- a trivial cost-limiter always cost-checks for everything




