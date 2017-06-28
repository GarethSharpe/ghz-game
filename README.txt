The GHZ game

Consider the following game, where there are three players: Alice, Bob, and Charlie. 

Step 1. The referee chooses a three bit string r s t uniformly from the set {000, 011, 101, 110}
Step 2. The referee sends r to Alice, s to Bob, and t to Charlie. 
Step 3. Depending on their bit recieved, Alice, Bob, and Charlie each send an answer back to the referee.
        Their answers must be bits: a from Alice, b from Bob, and c from Charlie.
Step 4. The referee determins if the round has been won depending on the rules outlined below.

Rules: 
They win if a ⊕ b ⊕ c = r ∨ s ∨ t and lose otherwise.
The following table lists the winning condition for each possible set of questions:

r s t | a⊕b⊕c
0 0 0 |    0
0 1 1 |    1
1 0 1 |    1
1 1 0 |    1

----------------------------
Classical Strategy
----------------------------

First consider a deterministic strategy, where each answer is a function of the question received
and no randomness is used by the players. Let us write ar, bs and ct to denote the answers that
would be given for each choice of r, s, and t. The winning conditions can be expressed by the four equations:

a0 ⊕ b0 ⊕ c0 = 0
a0 ⊕ b1 ⊕ c1 = 1
a1 ⊕ b0 ⊕ c1 = 1
a1 ⊕ b1 ⊕ c0 = 1

Adding the four equations modulo 2 gives 0 = 1; a contradiction. This means it is not possible
for a deterministic strategy to win every time, so the probability of winning can be at most 3/4
(because at least one of the four question sets will be answered incorrectly). 

It is easy to devise a strategy that wins 3/4 of the time (a0 = a1 = b0 = b1 = c0 = c1 = 1, for instance), and so the
maximum probability of winning is 3/4.

----------------------------
Quantum Strategy
----------------------------

Full Results Table
---------------------------------
x y z | x or y or z | a⊕b⊕c 
0 0 0 |   0         | 0⊕1⊕1 = 0
      |             | 1⊕0⊕1 = 0
      |             | 1⊕1⊕0 = 0
      |	            | 0⊕0⊕0 = 0
---------------------------------
1 1 0 |      1      | 1⊕1⊕1 = 1 
      |             | 1⊕0⊕0 = 1 
      |             | 0⊕1⊕0 = 1 
      |             | 0⊕0⊕1 = 1 

Condensed Results Table
---------------------------------------
x y z | x or y or z | a  b⊕c | a⊕b⊕c
0 0 0 |	     0	    | 0   0  |	 0
      |	     	    | 1   1  |	 0
---------------------------------------
1 1 0 |	     1	    | 0   1  |	 1
      |	     	    | 1   0  |	 1