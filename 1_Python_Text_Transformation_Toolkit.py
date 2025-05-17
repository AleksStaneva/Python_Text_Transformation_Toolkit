# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:
    # TODO: Reverse the text using slicing or a loop
    reversed_word = text[::-1]
    print(reversed_word)

elif choice == 2:
    # TODO: Convert the text to uppercase using string methods
    uppercase_wording = text.upper()
    print(uppercase_wording)

elif choice == 3:
    # TODO: Convert the text to lowercase using string methods
    lowercase_wording = text.lower()
    print(lowercase_wording)

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    title_wording = text.title()
    print(title_wording)

elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    vowel_counter = 0
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    for i in text:
        if i == vowels[0] or i == vowels[1] or i == vowels[2] or i == vowels[3] or i == vowels[4] or i == vowels[
            5] or i == vowels[6] or i == vowels[7] or i == vowels[8] or i == vowels[9]:
            vowel_counter += 1
    print(vowel_counter)

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    new_text = text.replace(' ', '')
    print(new_text)

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    vowels = "aeiouAEIOU"
    replacement = '*'
    for i in vowels:
        text = text.replace(i, replacement)
    print(text)

elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)
    converted_text = text.lower().replace(" ", "")

    text_first_half = 0
    text_second_half = len(converted_text) - 1

    is_palindrome = True

    while text_first_half < text_second_half:
        if converted_text[text_first_half] != converted_text[text_second_half]:
            is_palindrome = False
            break

        text_first_half += 1
        text_second_half -= 1

    if is_palindrome:
        print(f'The text {text} IS a palindrome.')
    else:
        print(f"The text {text} IS NOT a palindrome.")

elif choice == 9:
    # TODO: Count the frequency of each word and display the result
    text = text.split()
    text1 = []

    for i in text:
        if i not in text1:
            text1.append(i)
    for i in range(0, len(text1)):
        print('Frequency of', text1[i], 'is :', text.count(text1[i]))

else:
    print("❌ Invalid choice! Please restart the program.")