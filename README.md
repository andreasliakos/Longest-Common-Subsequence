# Longest-Common-Subsequence

1 Introduction

Solving the maximum common subsequence problem [Bla20], [Sta98] is requested. Its resolution
problem, among others, has application in bioinformatics, and in particular in similarity analysis in
DNA sequences. DNA sequences are represented by strings formed by 4 characters
(A,G,C,T) representing the nucleotides adenine, guanine, cytosine and thymine.

2 Longest Common Subsequence (LCS=Longest Common Subsequence)

Suppose two strings X and Y are given with lengths m and n respectively. On the maximum common problem
subsequence is asked to find the longest subsequence that is found in both strings X and Y. The subsequence consists of characters that can be found in both strings in the same order from left to right. For example if X="AATCGAG" and Y="CCATCGG" then
the maximum common subsequence is "ATCGG" with length 5.

Write a simple brute force algorithm to solve the problem. Let this algorithm generate all subsequences of X (2
m in number of subsequences) and check which ones they are
the largest that also exists in Y. Then implement a dynamic programming algorithm whose pseudocode is given in Algorithm 1. Extend the algorithm so that it returns except
the length of the maximum subsequence and the maximum subsequence itself. A useful visualization of
algorithm is located at https://www.cs.usfca.edu/galles/visualization/DPLCS.html. The subproblem results memorization table for X="AATCGAG" and Y="CCATCGG" is shown
in Figure 1.

![image](https://user-images.githubusercontent.com/115406856/220791291-3e9ae909-dc28-44be-943e-a25e0d401db0.png)

![image](https://user-images.githubusercontent.com/115406856/220791395-8ec2a7b1-dce1-4a2a-98fb-80852827ec4e.png)

