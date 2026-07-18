# Odd frequency
Frequecy is the number of times an item appears in a collection, these could be a list set or even an array

## Problem
Receive a list of numbers with duplicates and return a list of numbers with ***odd*** frequecy appearance in the list.

### Solution
I received the list coverted it to a **set**
I did these to reduce the iterations over the list.
I had a set of all **unique** numbers in the list and with these I could use the count method in list to get the frequency for each unigque number.
> These included an additional step to covert the set of unique numbers to a list as a set is not ***mutable***
>
> The results would then be stored as a dictionary of a number as a key and its frequency as its corressponding value.
> Afterwards  would iterate over the dictionary to find unique numbers with odd frequecy by using the **modulus** operator. `\%`.