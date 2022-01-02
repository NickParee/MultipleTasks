#Author: Nick Paree
#MUID: 901891852
#Major: Computer Science

#Question 1
#Take input from the user
masterList = []
marksList = []
for i in range(3):
    student_id = input('Please enter the student number from 1-3: ')
    name = input('Please enter the students name: ')
    marks = int(input('Please enter the number of marks: '))
    masterList.append(student_id)
    masterList.append(name)
    masterList.append(marks)
    marksList.append(marks)
#Print students names and score
print(masterList[1], ' scored ', masterList[2], ' in the first exam.')
print(masterList[4], ' scored ', masterList[5], ' in the first exam.')
print(masterList[7], ' scored ', masterList[8], ' in the first exam.')

#calculate the average marks
average = sum(marksList) / 3
print('The average score of the class is ', average, '%')

#Print highest and lowest marks
print('The highest mark obtained is ', max(marksList))
print('The lowest mark obtained is ', min(marksList))


'''Test Run of Question 1
Please enter the student number from 1-3: 1
Please enter the students name: Nick
Please enter the number of marks: 90
Please enter the student number from 1-3: 2
Please enter the students name: Joe
Please enter the number of marks: 85
Please enter the student number from 1-3: 3
Please enter the students name: Mike
Please enter the number of marks: 66
Nick  scored  90  in the first exam.
Joe  scored  85  in the first exam.
Mike  scored  66  in the first exam.
The average score of the class is  80.33333333333333 %
The highest mark obtained is  90
The lowest mark obtained is  66
'''

#Question 2
done = True
while done:
    phoneNum = input('Enter a 10 digit phone number: ')
    #Make sure phoneNum is 10 digits
    if len(phoneNum) == 10:
        print('The formatted number is: ', '(',phoneNum[0:3],')', phoneNum[3:6], '-', phoneNum[6:10])
    else:
        print('Has to be a ten digit number!')
        done = False 

'''Test Run of Question 2
Enter a 10 digit phone number: 3049754695
The formatted number is:  ( 304 ) 975 4695
Enter a 10 digit phone number: 3042336597
The formatted number is:  ( 304 ) 233 6597
Enter a 10 digit phone number: 326
Has to be a ten digit number!
'''

