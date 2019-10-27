#1.Using for loop, create nested list from dictionary
fruits = {'banana':3,'apple':2, 'mango':1, 'kiwi':5}
fruits_list = []
for key,value in fruits.items():
    t=[]
    t.append(key)
    fruits_list.append(t*value)
print(fruits_list)

#2.Select the shortest element from the list
# fruits = ['banana','apple', 'mango', 'kiwi']
#shortest_fruit = 'kiwi'

fruits = ['banana','apple', 'mango', 'kiwi']
shortest_fruit = min(fruits,key=len)
print(shortest_fruit)

#3.
text='''What a to do to die today at a 1/4 or 2 to 2. 
A terrible difficult thing to say but a harder thing still to do. 
The dragon will come at the beat of the drum with a rat-tat-tat-tat-tat-tattoo 
at a 1/4 or 2 to 2 today, at a 1/4 or 2 to 2.'''
#Number occurence: 12
#letter occurence: 158
#Other symbols: 66
total_numbers = 0
total_alphas = 0
total_else = 0
for letter in text:
    if  letter.isnumeric()==True:
        total_numbers +=1
    elif letter.isalpha()==True:
        total_alphas += 1
    else:
        total_else += 1
print(total_numbers)
print(total_alphas)
print(total_else)

#5.Count the number of even and odd numbers from a series of numbers.
seq = [1,44,30,15,2,18]
Even_Numbers=len([x for x in seq if x % 2 == 0])
Odd_Numbers=len([y for y in seq if y % 2 == 1])
print("Odd numbers: {0} Even numbers: {1}".format(Odd_Numbers,Even_Numbers))

#6.Using loops, print following pattern

for  x in range(4):
    print ("*"*(x +1))

#7.Using list comprehensions, transform all vowels within the string to upper case

word="python"

upper_cased="".join([letter.upper()if letter in "aeiouy" else letter for  letter in word])
print(upper_cased)

#8.Print position number of the letter
#Ask user to type letter (just one)
#Print position of the letter in the alphabet

letter=input("Type  letter: ")
if len(letter) !=1  :
    letter=input("Please type only one letter: ")
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Letter", letter ,"position is", alphabet.index(letter)+1)

#9.Find the median of three values (do not use median function)
#Ask user to input 3 values
numbers=[]
for n in range(3):
    t = int(input("Type number: "))
    numbers.append(t)
numbers.sort()
print("Median value is {0}".format(numbers[1]))

#10.Ask user for their favourite number
#If user chose number 13, ask user for another number
#Else print numbers from 0 to favourite number, but do not print number 13
#Finish printing after user's favourite number

f_number = int(input("Please type your favourite number: "))
while f_number==13:
    f_number = int(input("Please choose another number: "))

for n in range(100): 
    if n==13:
        continue
    if n==f_number+1:
        break
    print(n)

#Bonus:
for n in range(7):
    if n in (1,2,4,5,6):
        print(str(" "*3).center(5,"*"))
    elif n==3:
        print("*"*5)
    else:
        print(str("*"*3).center(5," "))