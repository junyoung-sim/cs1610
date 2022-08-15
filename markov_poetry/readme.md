I focused on refining the markov model to generate coherent phrases by considering how each state (a word in this case) must be correlated by N number of preceding words.

For instance, let’s say that A transitioned to B and B transitioned to C through biased randomness. After doing so, my model checks if it is likely for state C to occur 2 steps after the occurrence of A. If it is indeed likely for the transition from B to C to occur after the occurrence of A, we move on. If it isn’t coherent, we recompute and hope for something better to be outputted.
