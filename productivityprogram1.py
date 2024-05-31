print("Please insert your to-do tasks:")
vieccanlam = input()

print("Please insert your KPI goals:")
KPIgoal = input()

completed = False

while completed == False:
    print ('Please finish it!')
    print ('Please double check your results!')
    print ('Are you satisfied withh your work now? Answer Yes / No')
    response2 = input()
    while response2 != "Yes" and response2 != "yes":
        print ('Check 1st (There are 6 checks totally): Please revise it!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response2 = input()
    print ('Check 2nd: Are you sure now? Answer Yes / No')
    response3 = input()
    while response3 == "No" or response3 == "no":
        print ('Check 2nd: Please review it again!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response3 = input()
    print('Check 3rd: Are you sure now? Answer Yes / No')
    response4 = input()
    while response4 == "No" or response4 == "no":
        print('Check 3rd: Please review it again!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response4 = input()
    print('Check 4th: Are you sure now? Answer Yes / No')
    response5 = input()
    while response5 == "No" or response5 == "no":
        print ('Check 4th: Please review it again!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response5 = input()
    print ('Check 5th: Are you sure now? Answer Yes / No')
    response6 = input()
    while response6 == "No" or response6 == "no":
        print ('Check 5th: Please review it again!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response6 = input()
    print ('Check 6th: Are you sure now? Answer Yes / No')
    response7 = input()
    while response7 == "No" or response7 == "no":
        print ('Check 6th: Please review it again!')
        print(" ")
        print ('Are you satisfied withh your work now? Answer Yes / No')
        response7 = input()
    print("Have you finished the work? Enter Yes or No’")
    response8 = input()
    while response8 == "No" or response8 == "no":
        print ('Please finish it!')
        print(" ")
        print ('Have you really finished the work? Enter Yes or No')
        response8 = input()
    print ('Congratulations!')
    print('Now please communicate the results to the necessary stakeholders!')
    completed = True

print('The program will end now. If you want to start a new loop, please start it again')
    
    
    
    