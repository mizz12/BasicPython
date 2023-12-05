text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

text = list(map(len,["How","I", "want", "a", "drink" ,"alcoholic" ,"of", "course" ,"after", "the", "heavy", "chapters", "involving",
    "quantum", "mechanics", "All", "of", "thy", "geometry", "Herr", "Planck", "is", "fairly", "hard"]))
text_str = []

for i in text :
    text_str.append(str(i))

numbers_str = "".join(text_str)
print(numbers_str)
