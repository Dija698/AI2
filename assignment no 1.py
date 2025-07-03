                                                  #my assignment no 1
#Aprogram that conversts temperature fron celsius into fahrenheit

celsius=input("temperature")
print("temperature in fahrenheit is:",int(celsius)*float(9/5)+int(32))

#program that calculate the area of the rectangle

lenght=input("enter lenght")
breadth=input("enter breadth")
print("area of reactangle is:",int(lenght)*int(breadth))

#program that calculate the compound interest

P=input("enter principle")
R=input("enter rate")
T=input("enter time")
print("compound interest is:",int(P)*(int(1)+float(int(R)/100))*int(T)-int(P))

#program that calculate the perimeter of the rectangle

l=input("enter length")
b=input("enter breadth")
print("perimeter of rectangle is:",int(l)+int(b))

#program that input three numbers and calculate their average

N1=input("enter number")
N2=input("enter number")
N3=input("enter number")
print("average of numbers is:",(int(N1)+int(N2)+int(N3))/3)

#program that display square and cube of a number 

number=input("enter number")
print("square of number is:", int(number)*int(number))
print("cube of number is:", int(number)*int(number)*int(number))

#program that distributes candies equally in students

N=input("enter number of candies")
K=input("enter number of students")
print("distribution of candies equally:",int(N)//int(K))
print("cadies left:", int(N) % int(K))

#program to calculate profit

A=input("enter cost price")
B=input("enter selling price")
print("profit is;", int(B)-int(A))

#program that calculate marks and percentage

sub1=input("enter marks in sub1")
sub2=input("enter marks in sub2")
sub3=input("enter marks in sub3")
sub4=input("enter marks in sub4")
sub5=input("enter marks in sub5")
TM= (int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5))
print(TM)
print("percentage:",int(TM)/500*100)
print("average:",(int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5))/5)

#program that calculate age in months and days

age=input("enter your age")
print("age in monrhs:", int(age)*12)
print("age in days:", int(age)*365)

#program that converts USD into PKR

PKR=input("enter amount in pkr")
USD=int(PKR)*283.5
print(USD)

#program that calculate sum of first natural numbers

n=input("enter a number")
sum=int(n)*(int(n)+1)/2
print(sum)

#program that calculate the percentage of correct answers

t=input("enter total number of questions")
c=input("enter number of correct questions")
percentage=(int(c)/int(t))*100
print(percentage)

#program that calculate speed

S=input("enter distance")
t=input("enter time")
print("speed is:", int(S)/int(t))

#program to calculate body mass index

w=input("enter weight")
h=input("enter height")
print("BMI is:", float(w)/(float(h)*2))

#program that convert minutes into hours and minutes

M=input("enter minutes")
print("no of hours:", int(M)//60)
print("no of minutes:", int(M)%60)

#program for salary calculator

BS=input("enter basic salary")
HRA=0.20*int(BS)
DA=0.15*int(BS)
total_salary=BS+HRA+DA
print(total_salary)