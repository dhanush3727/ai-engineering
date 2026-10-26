# String
name = "Dhanush"
print(name) # Dhanush
print(name[0]) # D
print(name[4]) # u
print(name[-4]) # n
print(name[-7]) # D

# String slicing [start:end]
print(name[0:3]) # Dha
print(name[:3]) # Dha
print(name[3:]) # nush
# It takes every 2 character [start:end:step]
print(name[::2]) # Dauh
# Reverse a string
print(name[::-1]) # hsunahD
print(name[1:5:2]) # hn

# String modify
name = "C" + name[1:]
print(name)# Chanush

# small exercise
text = "Artificial Intelligence"
print(f"The first character is {text[0]}")
print(f"The last character is {text[-1]}")
print(f"The first 10 character {text[:10]}")
print(f"Everythin after the first 11 characters {text[11:]}")
print(f"The string reversed {text[::-1]}")

# String methods
user_input = "   Artificial Intelligence   "
words = ["Python", "is", "useful"]
languages = ["Python", "JavaScript", "TypeScript"]
print(user_input.upper())
print(user_input.lower())
print(user_input.lstrip())
print(user_input.rstrip())
print(user_input.strip())
print(user_input.replace("Intelligence", "Super Intelligence"))
print(user_input.replace(" ", "-"))
print(user_input.split())
print(" ".join(words))
print(",".join(languages))
print(text.startswith("Art"))
print(text.endswith("ce"))

# Small exercise
text = "   Python is powerful for AI Engineering   "
cleaned_text = text.strip()
print(cleaned_text)

lowercase_text = cleaned_text.lower()
print(lowercase_text)

replaced_text = lowercase_text.replace("python", "javascript")
print(replaced_text)

words = replaced_text.split()
print(words)

final_text = " - ".join(words)
print(final_text)

print(final_text.startswith("javascript"))
print(final_text.endswith("engineering"))

# Another exercise
user_message = "   I want to LEARN Python for AI engineering!!!   "
cleaned_msg = user_message.strip()
print(cleaned_msg)

lowercase_msg = cleaned_msg.lower()
print(lowercase_msg)

remove_suffix = lowercase_msg.replace("!","")
print(remove_suffix)

words = remove_suffix.split()
print(words)

print(len(words))

message = " ".join(words).capitalize()
print(message)