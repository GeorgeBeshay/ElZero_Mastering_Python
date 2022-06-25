# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input("What's Your Name ? ").strip().capitalize()
theEmail = input("What's Your Email? ").strip()

theUsername = theEmail[:theEmail.index("@")]
theDomain = theEmail[theEmail.index("@")+1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nAnd Your Domain Is {theDomain}")