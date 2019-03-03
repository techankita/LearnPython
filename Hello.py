# # # name,char= input("enter your name and a character: ").split(",")
# # # print(f"length of your name is: {len(name)}")
# # # print(f"{char} count is: {name.lower().count(char.replace(" ","").lower())}")

# # # stmt="I am god"
# # # print(stmt.replace(" ","*",))
# # i=1
# # # while i<=3:
# # #     user_Name,age=input("What is your Name and age : ").split(",")
# # #     age=int(age)


# # #     if (user_Name.lower()[0]=="a" or "A") and age>10:
# # #         print(f"{user_Name} you can watch coco movie")
# # #     else:
# # #         print(f"Sorry {user_Name} , you can not watch coco")

# # ############## sum of N natural numbers:###########################
# # n=0
# # # result=int(input("Enter your number: "))
# # # i=1


# # # while i<=result:
# # #     n=n+i
# # #     i= i+1
# # # print(n)



# # #############sum of digits of a number:#######################



# # # number = (input("Enter a number :"))
# # # sum=0
# # # i=0
# # # while i<len(number):
# # #     sum=sum+int(number[i])
# # #     i=i+1
# # # print(sum)


# # #print index of each latter


# # # counter=int(input("how many attempts you want? "))
# # a=1
# # # while a<=counter: 
    
# # #     print(f"attempt: {a}")
# # #     name=input("Enter a name: ")
# # #     i=0
# # #     while i<len(name):
# # #         sum=i+1
# # #         print(f"The postion of {name[i]} is:{sum}" )
# # #         i=i+1
# # #     a=a+1

# # ################count frequency of latter in string##############
# # # name=input("Enter your string:")

# # # i=0
# # # while i<len(name):
# # #  name1 =name.count(name[i])
# # #  print(f"{name[i]}: {name1}")
# # #  i=i+1

# # ###############Sum of n natural numbers using for loop#################


# # # n=0

# # # result=int(input("enter your number"))
# # # for i in range (1,result+1): 
# # #     n=n+i
    
# # # print(n)

# # #Modify Number game#
# # # win=65
# # # Guess= int(input("Enter your number: ")) 
# # # if Guess==win :
# # #      print("congrats!! you won")
# # # elif Guess>win :
# # #      print ("Too high")
# # # else:
# # #      print ("To low")

# # # import random
# # # i=0

# # # win= random.randint(1,100)
# # # guess= int(input("enter number between 1 to 100: "))
# # # while (i<=5) :
# # #      if win==guess :
# # #           print("You Win!!")
# # #      else: 
# # #           print ("You Loose :(")
               
# # #           i=i+1

# # # win=65
# # # i=1
# # # game_over= False
# # # while game_over != True :
# # #      guess= int(input("enter number between 1 to 100: "))



# # #      if win==guess :
# # #           print ("you win!!")
# # #           game_over= True
          
# # #           print(f"you win this game in {i} guesses")
# # #      else:
# # #           print("you loose!!")
# # #           print ("guess again!")
# # #           i=1+1
# # n=0


# # # i=0
# # # temp=0
# # # fab = [0,1,2,3,4,5,6,7,8,9,10]
# # # for i in range (11):
# # #      temp =temp+ fab[i]
# # #      i= i+1
# # #      print (temp)    

# # #Area of a triangle
# # # def area(a,b) :
# # #      ar= a*b/2
# # #      print (f"area of triangle= {ar}")

# # # num1= int(input("enter height: "))
# # # num2= int(input("enter width: "))
# # # area= area(num1,num2)

# # # import cmath
# # # def rootofquad(a,b,c) :

# # #      x1= (-b+ cmath.sqrt(b**2-4*a*c))/(2*a)
# # #      x2= (-b- cmath.sqrt(b**2-4*a*c))/(2*a)
# # #      print (f"x1 is {x1}")
# # #      print (f"x2 is {x2}")

# # # num1= int(input("enter a: "))
# # # num2= int(input("enter b: "))
# # # num3= int(input("enter c: "))

# # # rootofquad=rootofquad(num1,num2,num3)     


# # #swap two numbers:

# # # def swap(a,b) :
# # #      a,b=b,a
# # #      print (f"a is {a}, print b is {b}")
# # #      return a,b
     
# # a=0
# # b=1
# # while b<10 :
# #      a,b=b,a+b 
     
     
# #      print(a,b)
# #      i=i+1
# # # while True :
# # #      num1= input("enter a: ")
# # #      num2= input("enter b: ")
     
# # #      result=swap(num1,num2)
     
# numbers=[1,2,3,4]
# print (numbers)
# for number in numbers:
#     number**2
# print(numbers)
