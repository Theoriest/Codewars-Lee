# Multiplicative persistence
These is the number of times you must multiply the digits in num until you reach a single digit.

## Problem
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

> For example (Input --> Output):
>
>> 39 --> 3 (because 3\*9 = 27, 2\*7 = 14, 1\*4 = 4 and 4 has only one digit, there are 3 multiplications)
>> 999 --> 4 (because 9\*9\*9 = 729, 7\*2\*9 = 126, 1\*2\*6 = 12, and finally 1\*2 = 2, there are 4 multiplications)
>> 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

## What I learnt
Building up on failures I learnt while learning **recursion**, I noticed if note implemented right a *function* would not exit ***recursive*** step if condition for escaping is implemented wrongly.

These would raise the following error
> `***maximum recursion depth reached***`

The program would then exit execution.

With these in mind I also noticed a count of the number of times the function was executed was kept and an in built **condition** was implemented that if a count of  ***999*** is reached then  the program would stop execution and exit.

These (**recursion count**) I learnt was implemented in stacks and wait for it the error is as a result of ***stack overflow***. 

The stack is set at a size of **1000** by default, these can be increased by setting system settings to a different number either lower or even higher.

But  for me the key was that a count was being maintained and stored some where.

## Solution

My solution involved recursively parsing the result of multiplation of numbers constituing a digit until the product was a single digit number.
Afterward I would retrieve the stored count, but I thought to myself if these is a predefined variable. I might run into issues with passing multiple  numbers too find their respective ***Multiplicative Persistence***.

The first number might return the correct value but the second would be a sum of the first and second numbers multiplicative persistence.

So I thought I'd borrow from a past solution  <a href="./create_palindrome.md">***create_palindrome.md***</a>

> Here I implemented a helper function to help with my recursive step.
>
> Using these approach I implemented a helper function for which I manually tracked the number of its function calls ( i.e the helper function ) using a ***global count*** variable and return the count for each number passed to the function. 
>
>I would then manually reset count to **0** in the parent function  before calling helper with a new number.


