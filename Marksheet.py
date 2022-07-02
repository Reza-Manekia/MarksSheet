print("!________________MARKSHEET_______________!")

name = input("What is your name: ")
f_name = input("What is your father name: ")
Class = int(input("Enter your class: "))
print("___Enter your Marks____")  #marks out of 100
Maths = int(input("Maths: "))
phy = int(input("Physics: "))
Chem = int(input("Chem: "))
Eng = int(input("English: "))
Sci = int(input("Science: "))

# Calculations;

per = (Maths+phy+Chem+Eng+Sci)/5    #percentage = (obt/total)*100
print("Percentage:" + " " + str(per))

if per>90:
    print("Grade= A+")

if 90<per<=80:
    print("Grade= A")

if 80<per<=70:
    print("Grade= B+")

if 60<per<=70:
    print("Grade= B")

else:
    print("fail")