#!/usr/bin/env python
# coding: utf-8

# # 1. Equality Check 
# Write a Python code to accept two integers and check whether they are equal 
# or not. <br>
# Test Data : 15 15 <br>
# Expected Output : <br>
# Number1 and Number2 are equal 

# In[5]:


a=int(input())
b=int(input())
if a==b:
    print("Number1 and Number2 are equal")
else:
    print("Number1 and Number2 not equal")


# # 2. Even or Odd Check 
# Write a Python code to check whether a given number is even or odd. <br>
# Test Data : 15 <br>
# Expected Output : <br>
# 15 is an odd integer

# In[6]:


n=int(input())
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")


# # 3. Positive or Negative Check 
# Write a Python code to check whether a given number is positive or negative. <br>
# Test Data : 15 <br>
# Expected Output : <br>
# 15 is a positive number 

# In[7]:


n=int(input())
if n>0:
    print(n,"is a positive")
else:
    print(n,"is a negative")



# # 4. Voting Eligibility 
# Write a Python code to read the age of a candidate and determine whether he 
# is eligible to cast his/her own vote. <br>
# Test Data : 21 <br>
# Expected Output : <br>
# Congratulation! You are eligible for casting your vote. 

# In[8]:


age=int(input())
if age>=18:
    print("Congratulation! You are eligible for casting your vote.")
else:
    print("Sorry! ,you are not eligible for casting your vote.")



# # 5. Largest of Three Numbers 
# Write a Python code to find the largest of three numbers. <br>
# Test Data : 12 25 52 <br>
# Expected Output : <br>
# 1st Number = 12  
# 2nd Number = 25<br> 
# 3rd Number = 52 <br>
# The 3rd Number is the greatest among three<br> 
# 

# In[9]:


a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("The 1st Number is the greatest among three")
if b>a and b>c:
    print("The 2nd Number is the greatest among three")
if c>a and c>b:
    print("The 3rd Number is the greatest among three")


# # 6. Coordinate Quadrant Identification 
# Write a Python code to accept a coordinate point in an XY coordinate system 
# and determine in which quadrant the coordinate point lies. <br>
# Test Data : 7 9 <br>
# Expected Output : <br>
# The coordinate point (7,9) lies in the First quadrant.

# In[10]:


x=int(input())
y=int(input())
if x>0 and y>0:
    print("The coordinate point",(x,y), "lies in the First quadrant.")
elif x<0 and y>0:
     print("The coordinate point",(x,y), "lies in the Second quadrant.")
elif x<0 and y<0:
     print("The coordinate point",(x,y), "lies in the Third quadrant.")
elif x>0 and y<0:
     print("The coordinate point",(x,y), "lies in the fourth quadrant.")
else:
     print("The coordinate point",(x,y), "lies at the origin .")


# # 7. Admission Eligibility Check 
# Write a Python code to determine eligibility for admission to a professional 
# course based on the following criteria: 
# Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in 
# Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140---- <br> Input the marks obtained in Physics :65 <br>
# Input the marks obtained in Chemistry :51 <br>Input the marks obtained in 
# Mathematics :72 <br>Total marks of Maths, Physics and Chemistry : 188 <br>Total 
# marks of Maths and Physics : 137 <br>The candidate is not eligible. <br>
# Expected Output : 
# The candidate is  eligible for admission.

# In[12]:


py=int(input("Enter the marks obtained in the physics"))
ch=int(input("Enter the marks obtained in the chemistry"))
mt=int(input("Enter the marks obtained in the maths"))
total_marks=py+ch+mt
total_math_Py=mt+py
if mt>=65 and py>=55 and ch>=50:
    print(" The candidate is  eligible for admission.")
elif total_math_Py>=140:
    print(" The candidate is  eligible for admission.")
else:
    print(" The candidate is not eligible for admission.")



# # 8. Leap Year Determination 
# Write a Python code to find whether a given year is a leap year or not. <br>
# Test Data : 2016 <br>
# Expected Output : <br>
# 2016 is a leap year

# In[4]:


year=int(input())
if year%400==0:
    print(year,"is a leap year")
elif year%100==0:
    print(year,"is not leap year")
elif year%4==0:
    print(year,"is a leap year")
else:
      print(year,"is not leap year")



# # 9. Quadratic Equation Roots 
# Write a Python code to calculate the root of a quadratic equation.<br> 
# Test Data : 1 5 7 <br>
# Expected Output :<br> 
# Root are imaginary; <br>
# No solution. 

# In[15]:


a=float(input())
b=float(input())
c=float(input())


d=b**2-4*a*c
if d>0:
    root1=(-b+d**0.5)/(2*a)
    root2=(-b-d**0.5)/(2*a)
    print("Root1",root1,"Root2",root2)
elif d==0:
    root=-b/(2*a)
    print("both roots are equal:",root)
else:
    print("Root are imaginary")
    print("no solution")




# # 10. Student Marks and Division Calculation 
# Write a Python code to read the roll no, name and marks of three subjects and 
# calculate the total, percentage and division. 
# Test Data : <br>
# Input the Roll Number of the student :784 <br>
# Input the Name of the Student :James <br>
# Input the marks of Physics, Chemistry and Computer Application : 70 80 90 <br>
# Expected Output : <br>
# Roll No : 784 <br>
# Name of Student : James <br>
# Marks in Physics : 70 <br>
# Marks in Chemistry : 80 <br>
# Marks in Computer Application : 90 <br>
# Total Marks = 240 <br>
# Percentage = 80.00 <br>
# Division = First

# In[19]:


rol_nu=input("enter the roo number")
name=input("Enter the name")
py=int(input("enter the physics's marks"))
ch=int(input("Enter the marks of chemistry"))
cs=int(input("Enter the marksof computer science"))
total_marks=py+ch+cs
per=total_marks/3
if per>60:
    div="First"
elif per>50:
    div="second"
elif per>400:
    div="third"
else:
    div="fail"
print("Roll no",rol_nu)
print("name",name)
print("total_marks",total_marks)
print("Percentage=",per)
print("Division",div)



# In[ ]:




