total_text = input("What is the text you want to enter?\n")
print()
first = input("Now we need three letters... What's the first letter? ")
second = input("...and the 2nd? ")

third = input("...and the third? ")

print()
three_letters = [first,second,third]

print(first, "appears", str(total_text.lower().count(first)), "times.")
print(second, "appears", str(total_text.lower().count(second)), "times.")
print(third, "appears", str(total_text.lower().count(third)), "times.")

print()
print("There are",str(len(total_text.split(" "))),"words in the sentence.")

print()

print("The first letter of the text is", total_text[0], "and the last letter of the text is", total_text[-1])

print()

text_list = total_text.split(" ")

text_list.reverse()

# print(text_list)

print("In reverse, the sentence will look like this...\n" + " ".join(text_list))

print()

python_test = { True: "Python is in the text", False: "Python is not in the text"}

print("And for the finale, is the word 'python' in the text........\n",python_test[("python" or "Python") in total_text])