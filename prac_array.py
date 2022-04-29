month = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(month[1]-month[0])


# 2. Find out your total expense in first quarter (first three months) of the year.
print(month[0]+month[1]+month[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print(2000 in month)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
month.append(1980)
print(month)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
month.insert(3,month[3]+200)
print(month)

#You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3,"black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]= ["doctor strange"]
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# 3 Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
user = int(input("Enter any number :-"))
lis = []
for i in range(1,user+1):
    if  i%2 != 0:
        lis.append(i)
print(lis)

# using list compherension
a = [ x for x in range(1,user+1) if x %2 != 0]
print(a)