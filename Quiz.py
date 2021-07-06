print("Welcome To Quiz in Computer Science!! :)")
print("   ")

print("Are you Intreseted in playing Quiz ?")
print('     Type "Yes" or "No"')
play = input("--> ")
print(" ")
if play.lower() == "yes":
    print("Let's begin...")
    score = 0
elif play.lower() == "no":
    print("Thank You!! Have a Nice Day :)..")
    quit()
else:
    exit()

print("Pick your option as your Answer")
print("  ")
print("1) What is format specifier of int in C programming ? ")
print(" A. %d  B. %f  C. %ld  D. %s")

question = input("--> ")
if question.lower() == "a":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("2) In the following which one is the 'NOT' datatype ?  ")
print(" A. Int  B. Array  C. Boolean  D. Float")

question = input("--> ")
if question.lower() == "b":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("3) How are lists declared in Python ?  ")
print(" A. ()  B. []  C. {}  D. Non of These")

question = input("--> ")
if question.lower() == "b":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("4) In HTML style attribute classes are declared by ?  ")
print(" A. >classname  B. :classname  C. #classname  D. .classname")

question = input("--> ")
if question.lower() == "d":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("5) In HTML style attribute an 'id' is declared by ?  ")
print(" A. >idname  B. :idname  C. #idname  D. .idname")

question = input("--> ")
if question.lower() == "c":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("6) In the following which one is correct form of post increment operator ?  ")
print(" A. ++a  B. a++  C. a+  D. a--")

question = input("--> ")
if question.lower() == "b":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("7) Which one is 'NOT' a access modifier in JAVA ?  ")
print(" A. personal  B. void  C. public  D. private")

question = input("--> ")
if question.lower() == "b":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("8) Which one is not a Cloud platform in these ?  ")
print(" A. BYJU  B. AWS  C. Azure  D. Google Cloud")

question = input("--> ")
if question.lower() == "a":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("9) Who is Current CEO of Amazon ?  ")
print(" A. Werner Vogles  B. Andy Jassy  C. Bill Gates  D. Jeff Bezos")

question = input("--> ")
if question.lower() == "d":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("10) Which is the oldest andriod version in the following ?  ")
print(" A. kikat  B. gingerbread  C. cupcake  D. jellybean")

question = input("--> ")
if question.lower() == "c":
    print("   Correct Answer :)")
    score += 1
else:
    print("   Wrong Answer :(")

print(" ")
print("Your Score is " + str(score) + " out of 10 questons")
print(" ")
print("Your percentage is " + str((score/10)*100))
print(" ")
print("Thank You!! for taking this Quiz :)")
print(" ")

print("Hope you Enjoyed :) The Quiz :)..")
