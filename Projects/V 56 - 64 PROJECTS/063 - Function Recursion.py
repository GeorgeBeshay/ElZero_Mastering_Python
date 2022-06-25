# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need First To Understand Recursion --
# ---------------------------------------------------------------------

# Test word [ WWWoooorrrldd ] # print(x[1:])

def cleanword(word):
    if len(word) == 1:
        return word
    print(f"Print Start Function {word}")
    if word[0] == word[1]: 
        print(f"Print Before Condition {word}")
        return cleanword(word[1:])
    print(f"Print Before Return {word}")
    return word[0] + cleanword(word[1: ])
    # Stash [ World]
print(cleanword("WWWoooorrrldd"))
