Pick Largest Number
===

Description
---

Simulation of the open problem presented in the book "Open Problems in Communication and Computation".

Player 1 writes down any two distinct numbers on separate slips of paper. Player 2 randomly chooses one of these slips of paper and looks at the number. Player 2 must decide whether the number in his hand is the larger of the two numbers. He can be right with probability one-half. It seems absurd that he can do better.

As wierd as it is, the proposed method (referred to as 'advanced strategy' in the sumulation) just works. To me, it looks like entanglment effect in pure math world.
I wonder how it could be used ;)

Running
---

Before running first time, make sure to install the requirements by running *pip3 install -r requirements.txt*. 
Then just run as follows:


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
- Cover T.M. (1987) Pick the Largest Number. In: Cover T.M., Gopinath B. (eds) Open Problems in Communication and Computation. Springer, New York, NY