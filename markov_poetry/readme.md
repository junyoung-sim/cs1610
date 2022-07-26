I focused on refining the markov model to generate coherent phrases by considering how each state (a word in this case) must be correlated by N number of preceding words.

For instance, let’s say that A transitioned to B and B transitioned to C through biased randomness. After doing so, my model checks if it is likely for state C to occur 2 steps after the occurrence of A. If it is indeed likely for the transition from B to C to occur after the occurrence of A, we move on. If it isn’t coherent, we recompute and hope for something better to be outputted.

Notation wise, we would be transitioning to each state based on P(S_t | S_t-1, S_t-2) with t being time.

I implemented this refinement in Python and applied it to replicate a songwriter called Harry Styles and my code is a bit buggy so prevented me from generating a full poem but my algorithm was still able to output several coherent and nice phrases, such as:

1. seemed especially alarming til now
2. things haven’t been here but you
3. help you through the last line
4. share the last line then we drink
5. endings is so overrated
6. matilda you missed me too much
7. choose your way that you know that you never know (nice!!)
