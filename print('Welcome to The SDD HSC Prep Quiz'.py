print('Welcome to The SDD HSC Prep Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.ower()=='yes':
    answer=input('Question 1: At Which Stage of the Software Development cycle are the needs of the client first identified?')
    if answer.lower()=='defining and understanding':
        score += 1
        print('correct')
    else:
        print('Wrong Answer, the correct was "defining and understanding"  ')
 
 
    answer=input('Question 2:  In a complex modular system, module A calls module B. During the testing process an error message was produced indicating that module A had provided too few parameters for module B to proceed. Which Error has occured?')
    if answer.lower()=='runtime':
        score += 1
        print('correct')
    else:
        print('Wrong Answer, the correct was "runtime" :(')
 
    answer=input('Question 3: An engineer created a spreadsheet to estimate the cost of her next project.  Which software development approach was used to create the spreadsheet?')
    if answer.lower()=='end user':
        score += 1
        print('correct')
    else:
        print('rong Answer, the correct was "end user"')

    answer=input('Question 4: At which level of testing would a software developer use a driver?')
    if answer.lower()=='module':
        score += 1
        print('correct')
    else:
        print('Wrong Answer, the correct was "module"')

    answer=input('Question 5: During which process would a software developer be most likely to use a metalanguage??')
    if answer.lower()=='creating source code':
        score += 1
        print('correct')
    else:
        print('Wrong Answer, the correct was "Creating source code"(')
 
 
print(', you attempted',score,"questions correctly! I hope you learnt some software knowledge")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')