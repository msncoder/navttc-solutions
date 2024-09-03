# # my_list = [
# #     {"name":"saad","math's_score":22,"eng_score":33},
# #            {"name":"saad","math's_score":55,"eng_score":43}
# #            ]

# # for i in my_list:
# #     for j,k in i.items():
# #         if j == "math's_score":
# #             print(k)





# 1.     Simple Calculator
# Problem: Create a simple calculator program that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding operation.
# Hint: Use if-elif-else statements to handle different operations.

# a = int(input("Enter a Number"))
# b = input("Enter a Operand")
# c = int(input("Enter a Number"))

# if b == "+":
#     print(a+c)
# elif b == "-":
#     print(a+c)
# elif b == "*":
#     print(a*c)
# elif b == "-":
#     print(a/c)
# else:
#     print("Invalid Error")



# 2. Vowel or Consonant Checker
# Problem: Write a program that asks the user for a single character and determines whether it's a vowel or a consonant.
# Hint: Use a list or set of vowels to check against the input character.

# vowels = "aeiouAEIOU"
# a = input("Enter a character")

# if a in vowels:
#     print("it's a vowels")
# else:
#     print("it's consonant")



# 3. Palindrome Checker
# Problem: Write a program that checks whether a given string is a palindrome. A palindrome is a word that reads the same forward and backward.
# Hint: Compare the string to its reverse using slicing.

# palindrome = input("Enter a palindrom")

# if palindrome == palindrome[::-1]:
#     print("it's a palindrome")
# else:
#     print("it's not a palindrome")



# 4. Find the Largest Number in a List
# Problem: Write a program that finds and prints the largest number in a list of numbers provided by the user.
# Hint: Use a loop to iterate through the list and keep track of the largest number found.

# li = [1,2,3,4,5]
# l = li[0]
# for i in li:
#     if i > l:
#         l = i
# print(l)



# 5. Count the Number of Words in a Sentence
# Problem: Write a program that counts the number of words in a given sentence. Assume words are separated by spaces.

# sentence = "my Name is saad"
# count = 1

# for i in sentence:
#     if i == " ":
#         count += 1
# print(count)

# 6. Unique Elements in a List
# Problem: Write a program that takes a list of numbers and returns a new list with only the unique elements (removing duplicates).

# li = [1,2,3,1,2,3]

# li1 = []

# for i in li:
#     if i in li1:
#         continue
#     else:
#         li1.append(i)
# print(li1)

# 7. Reverse a String
# Problem: Write a program that reverses a string provided by the user.
# Hint: Use slicing or a loop to reverse the string.

# sentence = "saad"
# print(sentence[::-1])

# 8. Find the Second Largest Number
# Problem: Write a program that finds the second largest number in a list of numbers.
# Hint: Sort the list or iterate through it while keeping track of the two largest numbers.

# li = [22,33,44,55]
# largest = li[0]
# second_largest = li[0]


# for i in li:
#     if i > largest:
#         second_largest = largest
#         largest = i

# print(largest)
# print(second_largest)