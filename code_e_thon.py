n = int(input("enter no of attempts"))                                                              #taking input from user
a = ["1.Aptitude","2.English","3.Math","4.Gk","5.Exit"]                                             #list of menu

#attempt process
if n==1:
	print(a)
elif n>1:
	print("You are not eligible for test")
else:
	print("Enter correct attempt");

#selecting appropreate menu
sub = int(input("select one option"))
s = str(input("Enter START to proceed"))

if sub==1:
	print("Thank you for selecting aptitude")
	print(s)
elif sub==2:
	print("Thank you for selecting English")
	print(s)	
elif sub==3:
	print("Thank you for selecting Math")	
	print(s)
elif sub==4:
	print("Thank you for selecting Gk")	
	print(s)
else:
	print("Exit");	

apti_questions = "Aptitude questions"
eng_questions = "English questions"
math_questions = "Math questions"
gk_questions = "Gk questions"

questions=[apti_questions, eng_questions, math_questions, gk_questions]                         #storing subjects in questions variable

que = {apti_questions:[("2+3=6 is it true", False), ("91 is a prime number?", True)]}           #apti question varialble

result = {"correct Answer": 0, "Incorrect Answer": 0}                                           #show result

def get_que_choice():                                                                           #while loop
    while True:
        try:
            que_number = int(input("choose the questions you like\n1 for {}\n2:").format(apti_questions))   #select questions
        except ValueError:
            print("This is not a number")                                                       #if seleced number is wrong
        else:
            if 0>que_number or que_number.len(que):
                print("Please enter correct value")
            else:
                return que_number
def get_answer(questions,correct_answer):                                                       #while loop for answers
    while True:
        try:
            print("q: {}").format(questions)
            answer = int(input("1 for True\0 for False:"))                                      #user have to select any one options for true and false 
        except ValueError:
            print("This is not a number")
        else:
            if answer is not 0 and answeer is not 1:                                            #if number is wrong
                print("Please try again")
            elif answer is correct_answer:                                                      #if number is right
                result["correct answers:"] +=1
                return True
            else:
                result["incrrect:"] +=1                                                         #it shows the result
                return False
choice = get_que_choice()
que_name = questions[choice-1]
print("you select the").format(que_name)
