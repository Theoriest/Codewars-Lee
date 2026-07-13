"""
def pig_it(text):
    l_str = ""
    w_list = []
    pl_list = []
    punc = ["!","?","."]
    for ch in text:
        if ch == " ":
            w_list.append(l_str.replace(" ",""))
            l_str = ""
        l_str += ch 
        
    if l_str:
        w_list.append(l_str.replace(" ",""))
    for word in w_list:
        if word in punc:
            pl_list.append(word)
        else:
            pl_str = word[1:] + word[0] + "ay"
            pl_list.append(pl_str)
    
    return " ".join(pl_list)

"""
def pig_it(text):
    punc = {"!", "?", "."}
    return " ".join(
        word if word in punc else word[1:] + word[0] + "ay"
        for word in text.split()
    )
print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))    # elloHay orldway !
