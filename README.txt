The GHZ game

In this game, Alice, Bob and Charlie receive input bits r, s and t, with the promise that
r ⊕ s ⊕ t = 0. Their goal is to output bits a, b and c, respectively, such that
a ⊕ b ⊕ c = r ∨ s ∨ t.

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

Clearly we can achieve 75% winning probability by setting a ≡ b ≡ c ≡ 1, and so the
maximum probability of winning is 3/4.

----------------------------
Quantum Strategy
----------------------------

There exists a quantum winning strategy in which Alice, Bob and Charlie share a GHZ state, |Ψ>abc = 1/√2(|000>abc + |111>abc).

              ┌───┐                                       ┌───┐
|0> ----------│ H │-----●---------------------------------│ M │-----> |a>    
              └───┘     |                                 └───┘  
                        |                                 ┌───┐
|0> -------------------(+)----●---------------------------│ M │-----> |b>
                              |                           └───┘
                              |                           ┌───┐
|0> -------------------------(+)--------------------------│ M │-----> |c>
                                                          └───┘

We consider the following strategy, which is performed by each of the players: On receiving input 0,
the player measures in the σx-basis and on receiving input 1, the player measures in the σy-basis.
For example, the circuit for the given values of r, s, t = 0, 1, 1 would be:

              ┌───┐                      ┌───┐            ┌───┐
|0> ----------│ H │-----●----------------│ H │------------│ M │-----> |a>    
              └───┘     |                └───┘            └───┘
                        |                ┌───┐  ┌───┐     ┌───┐
|0> -------------------(+)----●----------│Sdg│--│ H │-----│ M │-----> |b>
                              |          └───┘  └───┘     └───┘
                              |          ┌───┐  ┌───┐     ┌───┐
|0> -------------------------(+)---------│Sdg│--│ H │-----│ M │-----> |c>
                                         └───┘  └───┘     └───┘
                                         
Note:   σx-basis = H
        σy-basis = S† ⊗ H

Note that at least one of the players will receive a zero input bit. Without loss of generality, we can take this to be Alice,
i.e. a = 0. The following tables display all possible post-measurement results based on the inputs r s t.

Full Results Table
---------------------------------
r s t | r or s or t | a⊕b⊕c 
0 0 0 |      0      | 0⊕1⊕1 = 0
      |             | 1⊕0⊕1 = 0
      |             | 1⊕1⊕0 = 0
      |	            | 0⊕0⊕0 = 0
---------------------------------
0 1 1 |      1      | 1⊕1⊕1 = 1 
      |             | 1⊕0⊕0 = 1 
      |             | 0⊕1⊕0 = 1 
      |             | 0⊕0⊕1 = 1 

Condensed Results Table
---------------------------------------
r s t | r or s or t | a  b⊕c | a⊕b⊕c
0 0 0 |	     0	    | 0   0  |	 0
      |	     	    | 1   1  |	 0
---------------------------------------
0 1 1 |	     1	    | 0   1  |	 1
      |	     	    | 1   0  |	 1
      
As the tables communicate, the players win the game with 100% success.

----------------------------
Results: Classical Strategy
----------------------------
n = 100
μ = 0.73

----------------------------
Results: Quantum Strategy
----------------------------
n = 100
μ = 0.81

----------------------------
Statistical Analysis
----------------------------

Comparing computed Quantum Strategy against ideal Classical strategy:

Hₒ: μ = 0.75
Hₐ: μ > 0.75

n = 100
df = 100 - 1 = 99
σ = 0.39428

t = (x̄ - μₒ) / (σ / √n)
  = (0.81 - 0.75) / (0.39428 / √100)
  = 1.5217

p-value = 0.065636
∴ The result is significant at p < 0.10
∴ The result is not significant at p < 0.05

Comparing computed Quantum Strategy against computed Classical strategy:

Hₒ: μ = 0.73
Hₐ: μ > 0.73

n = 100
df = 100 - 1 = 99
σ = 0.39428

t = (x̄ - μₒ) / (σ / √n)
  = (0.81 - 0.73) / (0.39428 / √100)
  = 2.0290

p-value = 0.022571
∴ The result is significant at p < 0.10
∴ The result is significant at p < 0.05


