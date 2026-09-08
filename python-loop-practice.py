#!/usr/bin/env python
# coding: utf-8

# # Q1. The Dragon's Coins (For Loop)
# Story: A brave knight enters a dragon's cave where there are 100 treasure chests. Every 10th
# chest contains 10 gold coins. Others are empty.<br>
# Task: Write a program to calculate how many coins the knight collects*.<br>
# Input: Number of chests n = 100<br>
# Output: Total coins collected.

# In[3]:


spell=" "
c=0
while(spell!="success"):
    spell=input()
    c+=1
print("Number of attempts",c)


# # Q2. WAP TO print "vowels" ,if the character is vowels.

# In[48]:


ch=input()
for i in "aeiouAEIOU":
    if(i==ch):
        print("Vowels")



# # Q3. The Train Compartment Puzzle (Nested Loops)
# Story: A train has 3 compartments, each with 4 seats. The conductor wants to print a seat
# map showing seat numbers like C1-S1, C1-S2...
# Task: Display the full seat map using nested loops.<br>
# Output:<br>
# C1-S1 C1-S2 C1-S3 C1-S4<br>
# C2-S1 C2-S2 C2-S3 C2-S4<br>
# C3-S1 C3-S2 C3-S3 C3-S4

# In[1]:


for i in range(1,4):
    for j in range (1,5):
        print("C"+str(i)+"-S"+str(j),end=" ")
    print()



# # Q4. Secret Code Breaker (Loop + String)
# Story: A spy is decoding a secret message where only every 3rd character is part of the real
# message.
# Task: Write a program that extracts every 3rd character from the given string.<br>
# Input: "a1b2c3d4e5f6g7h8i9j0";<br>
# output:b3e6h9
# 

# In[50]:


a=input("Enter alpha numeric:")
result = ""
for i in range(2,len(a),3):
       result+=a[i]
print(result)



# # Q5. The Turtle Race (Loop with Conditionals)
# Story: 5 turtles are racing. Their speeds (1–10) are input. If a turtle runs at speed 5 or above,
# it finishes the race.
# Task: Count how many turtles finish the race.<br>
# Input: [3, 5, 7, 2, 10]<br>
# Output: 3 turtles finished<br>
# Hint: Use a loop with an if condition.

# In[5]:


speeds = [3, 5, 7, 2, 10]
finished_count = 0

for speed in speeds:
    if speed >= 5:
        finished_count += 1

print(f"{finished_count} turtles finished")



# # Q6 WAP to print all the triplets of pythagoras

# In[21]:


n=int(input())
for i in range(1,n+1,1):
    for j in range(i+1,n+1,1):
        for k in range(j+1,n+1,1):
            if (i**2==j**2+k**2)or(j**2==i**2+k**2) or (k**2==i**2+j**2):
                print(i,j,k)


# # Q7 WAP to check a number is prime or not

# In[12]:


n=int(input())
c=0
for i in range(2,n//2+1,1):
    if(n%i==0):
        c+=1
if(c==0):
    print("prime")
else:
    print("not prime")


# # Q8 WAP TO PRINT ALL THE TRIPLET OF PYTHAGORAS USING WHILE LOOP

# In[24]:


n=int(input("enter any number"))
i=1
while i<=n:
    j=i+1
    while j<=n:
        k=j+1
        while k<=n:
            if (i**2==j**2 + k**2) or (j**2==i**2+k**2) or (k**2==i**2+j**2):
                print(i,j,k)
            k+=1 
        j+=1
    i+=1


# # Q9 WAP to check a number the number is palindrome or not.

# In[25]:


n=int(input())
num=n
s=0
while(n!=0):
    a=n%10
    s=s*10+a
    n=n//10
if(s==num):
    print("palindrome")
else:
    print("not palindrome")


# # Q10 WAP to check the number is perfect number or not.

# In[33]:


n=int(input())
i=1
num=n
s=0
while(n/2>=i):
    if(n%i==0):
        s=s+i
    i=i+1
if s==num:
    print("Perfect number")
else:
    print("not perfect number")


# # Q11 WAP to print all the prime number between lower limit and upper limit

# In[34]:


l=int(input('Enter any number'))
u=int(input('Enter any number'))
while(l<=u):
    j=2
    c=0
    while(j<l):
        if(l%j==0):
            c+=1
        j+=1
    if(c==0):
        print(l)
    l+=1


# # Q12 WAP PROGRAM TO PRINT ALL THE PERFECT NUMBER BETWEEN LOWER LIMIT AND UPPER LIMIT

# In[35]:


l=int(input('Enter any number'))
u=int(input('Enter any number'))
while(l<=u):
    s=0
    tem=l
    j=1
    while(tem/2>=j):
        if(tem%j==0):
            s+=j
        j+=1
    if(s==l):
        print(l)
    l+=1


# # Q13 WRITE A PROGAM TO PRINT ALL THE PALINDOME NUMBER BETWEEN LOWER LIMIT AND UPPER LIMIT

# In[37]:


l=int(input('Enter the lower limit'))
u=int(input('Enter yhe upper limit'))
while(l<=u):
    lim=l
    s=0
    while(lim!=0):
        a=lim%10
        s=s*10+a
        lim=lim//10
    if(l==s):
        print(l)
    l+=1


# # Q14 WAP A PROGAM TO PRINT THE Armstrong Numbers  BETWEEN LOWER AND UPPER NUMBER.

# In[38]:


l=int(input("Enter the number"))
h=int(input("Enter the number"))
while l<=h:
    lim=l
    sum=0
    while(lim!=0):
        a=lim%10
        sum+=a**3
        lim=lim//10
    if(sum==l):
        print(l)
    l+=1


# # Q15.Find the factorial of square each digit and sum it.

# In[40]:


n=int(input("enter any number"))
fact_sum=0
while n>0:
    digit=n%10 
    sq_digit=digit**2 
    i=1
    fact=1
    while i<=sq_digit:
        fact*=i
        i+=1
    fact_sum+=fact
    n//=10
print(fact_sum)


# # Q16. WAP to find the sum of factorial of each digit 

# In[41]:


#123-->1!+2!+3!=1+2+6=9
n=int(input("enter any number"))
fact_sum=0
while n>0:
    digit=n%10 
    i=1
    fact=1
    while i<=digit:
        fact*=i
        i+=1
    fact_sum+=fact 
    n//=10
print(fact_sum)     


# In[ ]:




