

### SMT Notes ###

- Start with a strongly typed implementation
    + vars about functions will be function-vars of similar signature
    + actually type-check the language
- types can be represeted as recursive datatypes in z3


- variables
    + actual (V)alues of (int) lang-variables
    + (C)ost of reducing each expression (int)
    + cost and values of (A)pplying result of each expression
        * (function of values of sub-exprs)

Things we can say (variables) about expr x:
V(x), V(A(x)), V(A(A(x))), ...      // 0 or 1 of these (just ints)
C(x), C(A(x)), C(A(A(x))), ...      // any number of these
v: V(w) | C(w)
w: expr | A(expr)










