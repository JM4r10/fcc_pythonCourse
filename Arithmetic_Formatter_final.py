problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems, secpar = False):
    secpar = True    
    opera = list()
#Checking if there are 5 or less problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
#Creating a list of 3 elements, first operand, operator, second operand
    for prob in problems:
        set = prob.split()
        if len(set) == 3:
#Checking if the lenght of each operands is 4 or less, the operator is a '+' or a '-' sign and operands are actually integers and calculating result (also justified to the right), otherwise returns error
            for element in set:
                if len(element) > 4: return 'Error: Numbers cannot be more than four digits.'
            operator = set[1]
            if operator !='-' and operator !='+': return "Error: Operator must be '+' or '-'."
            if set[0].isdigit() == False or set[2].isdigit() == False: return 'Error: Numbers must only contain digits.'
            if operator == '+': result = int(set[0]) + int(set[2])
            else: result = int(set[0]) - int(set[2])
#Determinating which operand is the longest in order to create a couple of variables, with each with a string already justified to the right and how many dashes must go in the third line (also justified)
            longest = max(len(set[0]), len(set[2]))
            firstoperand = set[0].rjust(longest+2)
            secondoperand = set[2].rjust(longest+1)
            dashes = '-'*(longest+2)
            result = str(result).rjust(longest+2)
#For each problem the opera list receives an element consisting of a tuple of the first operand, operator, second operand, dashed line and the result
            opera.append((firstoperand, operator, secondoperand, dashes, result))
#Created a variable for each expected line, running a 'for' cycle that would organize every element of every problem in their correspondent line with 4 spaces between each
    lineone = linetwo = dashedline = linethree = ''
    for i in opera:
        lineone += f"{i[0]}    "
        linetwo += f"{i[1]}{i[2]}    "
        dashedline += f"{i[3]}    "
        linethree += f"{i[4]}    "
#Finally the arranged_problems is a string variable with the answer correctly formatted
    if secpar: arranged_problems = f"{lineone.rstrip()}\n{linetwo.rstrip()}\n{dashedline.rstrip()}\n{linethree.rstrip()}"
    else: arranged_problems =f"{lineone.rstrip()}\n{linetwo.rstrip()}\n{dashedline.rstrip()}"
    return arranged_problems

print(arithmetic_arranger(problems))