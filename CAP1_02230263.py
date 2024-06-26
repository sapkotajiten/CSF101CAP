################################
#  Jiten Sapkota
#  1 ME
#  02230263
################################
# Reference
# https://youtu.be/lE4hxs49EB8?si=s_Jf7PKvNbXDRu3M
# https://youtu.be/XnoXEUQrIM8?si=e23UjYHWmE_Qucmp
################################
# SOLUTION
# solution is 48387
# Put your number here: 3
################################


def read_input():
    file= open('CSF101CAP/input_3_cap1.txt','r')
    return file

# My solution 
def calculate_score(lines):
# Information given for this rock, paper, scissor game
    A = 1 # rock is 1
    B = 2 # paper is 2
    C = 3 # scissor is 3

    X = 0 # 0 points if we lose
    Y = 3 # 3 points if it is a draw
    Z = 6 # 6 points if we win

# Using dictionary (key : value):
    count_dict={'A X': 2, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

    total_value=0 #Initial score will be 0 

    for line in lines: #for loop

        value=line.strip() # The line is stripped 

        score=count_dict.get(value,None) #Assignment statement is used here

        if score is not None: # Conditional statement is used here
            total_value += score
    print("total score is:",total_value)

#Function calling at the end
calculate_score(read_input())