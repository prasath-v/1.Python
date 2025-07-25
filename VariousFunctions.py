class myFunctions():
    # list out the items in the list
    def Subfields():
        subfields = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print('Sub-fields in AI are:')
        for field in subfields:
            print(field)

    # checks whether the given number is Odd or Even
    def oddEven():
        num = int(input('Enter a number:'))
        if num == 0:
            print(f"Given number is Zero")
        elif num%2 == 0:
            print(f"{num} is Even Number")
        else:
            print(f"{num} is Odd Number")

    # elegibility of marriage for male and female according to their age limit
    def marriageEligibility(gender, age):
        gender = gender.lower()
        if(gender.lower() == 'male'):
            msg = 'not eligible' if(age<21) else 'eligible'
        else:
            msg = 'not eligible' if(age<18) else 'eligible'

        status = f"For {gender}, Your age is {age} and you're {msg}"
        return status

    # calculate the percentage of your marks - using enumerate
    def percentage(marks, total):
        scored = 0
        for i, mark in enumerate(marks):
            print(f"Subject{i+1}= {mark}")
            scored += mark
        percentage = (scored/total)*100
        print(f"Percenage : {percentage:.2f}")

    # calculate the percentage of your marks - using enumerate with starts with 1
    def percentage2(marks, total):
        scored = 0
        # By default, enumerate() starts at 0, but we can change that by passing a start value
        for i, mark in enumerate(marks, start=1): 
            print(f"Subject{i}= {mark}")
            scored += mark
        percentage = (scored/total)*100
        print(f"Percenage : {percentage:.2f}")

    # area of Triangle
    def area(height, base):
        return (height*base)/2

    # perimeter of Triangle
    def perimeter(side1, side2, side3):
        return side1+side2+side3