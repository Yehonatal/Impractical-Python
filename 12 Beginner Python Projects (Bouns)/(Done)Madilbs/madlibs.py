# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtube = "someone" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


print("Madlibs Game")
print("The Magic Computer")


noun = input("Enter a Noun: ")
plural_noun = input("Enter a Plural Noun: ")
verb_pt = input("Enter a Verb(Present Tense): ")



print(f"Today, every student has a computer small enough to fit into his {noun}. \nHe can slove any math problems by simply pushing the computers little {plural_noun}. \nComputers can add, multiply, divide, and {verb_pt}.")
