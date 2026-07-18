# Pig Latin 
Pig latin according to my understanding is boggeled up text and the latin part maybe it could be a hint as to how its hard to understand.

## Problem
These was getting a string and re-writing it in the pig latin tongue

### Solution
Well here I went the long way by having to construct the words in the string from the characters.
These involved checking for markers in the string to indicate new words. These includes spaces and punctuations.
Then applying edits to conform the pig latin tongue.

Later I found the simple solution was inbuilt in python using the split method which took a string and broke it down to its composite words.
These would be the simplified code including pig latinization steps
> `def pig_it(text):`
>   `punc = {"!", "?", "."}`
>   `return " ".join(`
>       `word if word in punc else word[1:] + word[0] + "ay"`
>       `for word in text.split()`
>   `)`
