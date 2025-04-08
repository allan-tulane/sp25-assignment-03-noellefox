# CMPS 2200 Assignment 3
## Answers

**Name:**___Noelle Fox______


Place all written answers from `assignment-03.md` here for easier grading.

**1a.** 
Given _N_ dollars, the greedy algorithm to attain as few coins as possible that sum to _N_ would follow the structure:
  1. Start with the largest denominator that is less than or equal to _N_ (2^k <= _N_) and use as many coins of this value as you can before you exceed _N_
  2. subtract this value from the total _N_
  3. repeat this step with smaller denominators until you reach _N_ = 0

**1b.**
  1. Greedy choice property: Because the denominators are all in the format of powers of 2, every positive integer can be represented as a sum of powers of 2. This algorithm continuosly chooses the largest coin <= _N_  since choosing any smaller coin would result in needing more coins and violate the goal of minimizing the number of coins. Therefore, making the greedy choice is an optimal decision at that step.
  2. optimal substructure: Once the largest coin is chosen and subtracted the remaining _N_ is a subproblem of the original. Since this subproblem follows the same format of being split into powers of 2, the optimal solution to the total _N_ includes the optimal solution to the subproblem _N_ and demonstates optimal substructure.

**1c.**
  1. W(n) = O(log n)
  2. S(n) = (log n)



**2a.**
Assume _N_ = 6 and the coin Denominators = {1, 3, 4}
  1. Choose largest D for 6 = 4
  2. 6 - 4 = 2
  3. Choose largest D for 2 = 1
  4. Repeat and choose 1 again
  5. _This solution uses 3 coins_
The optimal choice would only use 2 coins(2 3's)

**2b.**
The best way to make change for _N_ with the least amount of coins would be:
  1. pick one coin
  2. solve what's left after that coin (the subproblem)
  3. add the solutions together
This proves the optimal substructure property because if an optimal solution is not used for the smaller, leftover pieces, the overall solution would not be optimal. Therefore, optimally solving the subproblems helps build a better overall solution.

**2c.**
  1. Build a list where each spot tells us the fewest amount of coins neede to make that amount. Start with a base case of 0 and move up one dollar at a time while trying every coin to find the optimal solution. By the time the code reached the intended number, the list tells you the minmum number of coins needed.             dynamic programming:
        def minCoins(N, denominator):
          d = [float('inf')] * (N + 1)
          d[0] = 0 
          
          for i in range(0, N):
              for coin in denominator:
                  if coin <= i:
                      d[i] = min(d[i], 1 + d[i - coin])
          
          return d[N] if d[N] != float('inf') else -1
  2. W(n) = O(n*k), S(n) = O(n) 
    