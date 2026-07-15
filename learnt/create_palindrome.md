# Create Palindrome
A palindrome is a string that can be read the same forward and backward

## The problem
I was tasked with establishing whether given a string I could construct a palindrome from it.
The rules were I could only shift each letter once forward or backwards to come up with a string that is a palindrome

## What I learnt
I used the **ord()** Method in *char* to convert the characters to their equivalent number representations
My assumption was if numbers where within a space of two *(Taking absolute value)* using the **abs()** method for *integers*.
>>These was factoring in characters before and after. With these I could modify the strings to a middle ground character by shifting either one character ahead or one character before.
Doing above would allow me to essentially shift the two characters to one characters

Of importance was the **position** of the characters in the string and I only acted on pairs at **corresponding** ends of the string
I implemented a recursive approach to delaing with all characters in the string.
These was done in a while loop.
>>It involved stripping of the characters I had checked and confirmed possibility for **Palindrome shifting** and return the unchecked characters as a string for confirmation. The loop existed with **False** if a single check failed and with **True** if all checks passed confirming *possibility* of existence of a Palindrome after performing **Shift**.

