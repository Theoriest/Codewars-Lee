def to_camel_case(text):
    text = text.replace("-","_")
    text_lt = text.split("_")
    return "".join(n.capitalize() for n in text_lt )

print(to_camel_case("the_stealth_warrior"))