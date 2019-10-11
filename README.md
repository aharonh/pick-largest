Pick Largest Number
===

TLDR;
---

Simulation of the (previously?) open problem presented in the book "Open Problems in Communication and Computation", back in 1987.

The problem
---

The above paper is the oldest problem forumulation I found so far by a quck search on google, 
but according to the referenced [2] paper - 
*"... A variant of the first puzzle goes back to the mathematician Littlewood, 
who attributed it to the physicist Schrodinger."*

Below is the formulation as layed out in referenced [1] paper:

    "
    Player 1 writes down any two distinct numbers on separate slips of paper. 
    Player 2 randomly chooses one of these slips of paper and looks at the number. 
    Player 2 must decide whether the number in his hand is the larger of the two numbers. 
    He can be right with probability one-half. It seems absurd that he can do better."

    We argue that Player 2 has a strategy by which he can correctly state
    whether or not the other number is larger or smaller than the number in
    his hand with probability strictly greater than one-half.

    Solution: The idea is to pick a random splilting number T according to a
    density fit) , f{t) > 0 • for t e (-inf, inf). If the number in hand is less
    than T, decide that it is the smaller; if greater than T, decide that it is
    the larger.

    Problem: Does this result generalize? Does it apply to the secretary problem? 
    "

The solution?
---

In the reference [2] there is a proof of a theorem that shed some light on this mystery.

    "
    RANKING BY ONE OBSERVATION. Let X = (X1,..., Xn) be a vector of n
    real-valued random variables on some sample space. Denote by W the set of weak
    orders over {1,..., n}.
    1 The ranking of X is a random variable r(X) with values in W.
    For W in W, r(X) = W whenever, for all i and j in {1,..., n}, Xi ≥ X j if and only
    if iWj.

    Proposition 1. If the random variables Xi and r(X) are independent for each i, then
    r(X) is constant almost surely
    "

The problem is re-formulated as follows:

    "
    Guessing which is larger. It is helpful to present this puzzle as a two-person, 
    zerosum, win-lose game. The first player C chooses the numbers, while the second
    player G makes the guess after observing the number on one of the slips that was
    chosen at random. Player G wins if and only if she guesses correctly
    "

And the winning strategy is called the threshold strategy:

    "
    The pure strategies of C are pairs (x 1 , x 2 ) of distinct real numbers. A mixed strategy
    of C is a pair of random variables (X 1 , X 2 ) such that P(X 1 != X 2 ) = 1. We restrict
    G’s pure strategies to threshold strategies. Each t in R represents the threshold strategy
    at which the player guesses that the observed number x is the larger if x ≥ t and is the
    smaller otherwise, independently of which slip she observes.    
    "

Using the proof above and several additional statements, it is shown that: 

**Claim 1.** If G plays an arbitrary threshold strategy t against any pure strategy (x 1 , x 2 )
of C, then she

- wins with probability 1/2 when either x , x < t or x , x ≥ t;
- wins for sure when either x < t ≤ x or x < t ≤ x .

**Claim 2.** The strategy Q guarantees that player G wins with probability higher than
1/2 against any pure strategy of C.

**Claim 3.** There is no mixed strategy (X 1 , X 2 ) of C such that
- P(X 1 > X 2 ) = P(X 2 > X 1 ) = 1/2;
- each of X 1 and X 2 is independent of the events X 1 > X 2 and X 2 > X 1 .


The mystery
---

As wierd as it is, the proposed method referred to as 'strategy 2' in the sumulation code - just works. 
To me, it looks like the quantum entanglment effect in pure math world. No wander Schrodinger noticed something about it.

I might need to look into the proof further but having read it several times, it still leaves me surprised
that observing additional random value can help raise probability of choosing correct.

Now, I wonder how it could be used! Could we somehow use it to improve prediction models?

Running the Simulation
---

To get the code locally and install prerequisits:
```bash
git clone https://github.com/aharonh/pick-largest.git
cd pick-largest
pip3 install -r requirements.txt
```
To run, type the following:
```bash
pip3 install -r requirements.txt
```
Below is the sample output:


            aharon@dev:~/src/pick-largest$ python3 pick-largest.py 
            a: None, seed: 214667614969873294037158049849036284346
            b: None, seed: 177628893271350433001914924087395775510
            c: None, seed: 165376741336436202064312211207888782726
            last_guess: 0, seed: 55926123255498183901204009447556191946
            money: 9874, wins: 4937, losses: 5063
            performance:
            10050 +-----------------------------------------------+
                    |***                                            |
                    |****  **                                       |
            10000 |* ********                                     |
                    |   *********                                   |
                    |    **  *******                                |
            9950 |           *****                               |
                    |            * ** **                            |
                    |               ****                            |
                    |                * *                            |
            9900 |                  ****                     *   |
                    |                   ***       *    *****   *****|
                    |                   *****  **************  *  **|
            9850 |                      ************     ****    |
                    |                       ***     **       ***    |
                    |                                               |
            9800 +-----------------------------------------------+
                    0        2000     4000      6000     8000     10000
            a: None, seed: 214667614969873294037158049849036284346
            b: None, seed: 177628893271350433001914924087395775510
            c: None, seed: 165376741336436202064312211207888782726
            last_guess: 0, seed: 55926123255498183901204009447556191946
            money: 13282, wins: 6641, losses: 3359
            performance:
            13500 +-----------------------------------------------+
                    |                                             **|
            13000 |                                          **** |
                    |                                       ****    |
                    |                                   *****       |
            12500 |                                ****           |
                    |                             ****              |
            12000 |                         *****                 |
                    |                       ****                    |
            11500 |                   *****                       |
                    |                ****                           |
            11000 |             ****                              |
                    |          *****                                |
                    |       ****                                    |
            10500 |   *****                                       |
                    |*****                                          |
            10000 +-----------------------------------------------+
                    0        2000     4000      6000     8000     10000


References
---
- [1] Cover T.M. (1987) Pick the Largest Number. In: Cover T.M., Gopinath B. (eds) Open Problems in Communication and Computation. Springer, New York, NY https://doi.org/10.1007/978-1-4612-4808-8_43 
- [2] Samet, D., Samet, I., & Schmeidler, D. (2004). One Observation behind Two-Envelope Puzzles. The American Mathematical Monthly, 111(4), 347–351. https://doi.org/10.1080/00029890.2004.11920083
- [3] Wikipedia - Secretary problem https://en.wikipedia.org/wiki/Secretary_problem