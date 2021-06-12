def generator(n,m):
    subjects=[]
    instructors=[]
    quizes=[]
    print("MAIN SUBJECTS")
    #n=int(input())
    print("Enter names of main subjects with their respective professors")
    for i in range(0,n):
        print("Enter the subject")
        s=input()
        subjects.append(s)
        quizes.append(s+"-QUIZ")
        print("Enter the name of it's respective professor")
        i=input()
        instructors.append(i)

    print("\n"*5)
    
    exsub=[]
    ins=[]
    print("ADDITIONAL SUBJECTS")
    #m=int(input())
    for i in range(0,m):
        print("Enter the subject")
        sub=input()
        exsub.append(sub)
        print("Enter the name of it's respective professor")
        p=input()
        ins.append(p)
    
    print("\n"*5)



    import random



    timetable={'tt':{'I':{'   ':'9:30-10:20',' ':' ','MON':random.choice(subjects),'TUES':random.choice(exsub),'WED':random.choice(subjects),'THURS':random.choice(exsub),'FRI':random.choice(subjects)},
                 'II':{'   ':'10:30-11:20',' ':' ','MON':random.choice(subjects),'TUES':random.choice(exsub),'WED':random.choice(subjects),'THURS':random.choice(subjects),'FRI':random.choice(subjects)},
                'III':{'   ':'11:30-12:20',' ':' ','MON':random.choice(subjects),'TUES':random.choice(subjects),'WED':'COA LAB','THURS':'DS LAB','FRI':random.choice(subjects)},
                'IV':{'   ':'12:30-01:20',' ':' ','MON':random.choice(subjects),'TUES':random.choice(subjects),'WED':'DSTL LAB','THURS':random.choice(subjects),'FRI':random.choice(subjects)},
                ' ':{'   ':'1:30-2:00',' ':' ','MON':'RECESS','TUES':'RECESS','WED':'RECESS','THURS':'RECESS','FRI':'RECESS'},
                'V':{'   ':'02:00-02:50',' ':' ','MON':random.choice(subjects),'TUES':random.choice(subjects),'WED':random.choice(subjects),'THURS':random.choice(exsub),'FRI':random.choice(subjects)},
                'VI':{'   ':'03:30-03:50',' ':' ','MON':random.choice(subjects),'TUES':random.choice(exsub),'WED':random.choice(subjects),'THURS':'MINI-PROJECT LAB','FRI':random.choice(subjects)},
                'VII':{'   ':'04:00-04:50',' ':' ','MON':random.choice(quizes),'TUES':random.choice(quizes),'WED':random.choice(quizes),'THURS':random.choice(quizes),'FRI':random.choice(quizes)}}}


    import pandas as pd
    df=pd.DataFrame(timetable['tt'])
    print(df)

    print("\n"*5)

    print("SUBJECT \t PROFESSOR")
    for i in range(0,n):
        print(subjects[i]+" "+" \t "+" "+instructors[i])
    
    for i in range(0,m):
        print(exsub[i]+" "+" \t "+" "+ins[i])