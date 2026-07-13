"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.

"""


def likes(names):
    number_likes = len(names)
    if number_likes == 0:
        return "no one likes this"
    elif number_likes == 1:
        return names[0] +" likes this"
    elif number_likes == 2:
        return " and ".join(names) + " like this"
    elif number_likes == 3:
        last = names.pop()
        return ", ".join(names) + " and " + last + " like this"
    else:
        names_list = names[0:2]
        len_list = names[2:]
        return ", ".join(names_list) + " and " + str(len(len_list)) + " others like this"
    