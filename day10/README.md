*Preface: I am not, in any way, an expert on Dynamic Programming. These opinions are my own and may be wrong*

**Advent of Code Day 10, part 2**

At face value it is obvious that this problem is asking for a combination of permutations of the 'adapters' to create a valid chain from jolt value of 0 to the device. The difficulty comes into how you can compute the permutations without spending significant mental resources to program the software but also significant computational resources to calculate the results. I'm sure some implementation of recursion is possible...but my head can't figure it out.

Enter [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming). Dynamic programming is a means to solve a problem by breaking it down into smaller parts and memoizing the previous solutions to calculate for the next.

For the problem, we will look at the following example:
