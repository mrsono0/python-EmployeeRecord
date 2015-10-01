__author__ = 'gunner'
file = open("record.txt", 'a')
while True:
    print "Select the Choices"
    print("0 - To Quit\n1 - To Enter Employee Records\n2 - To search the Employee detail\n3 - View All Records")
    choices = raw_input("? : ")
    if choices == '0':
        break
    elif choices == '1':
        while True:
            s = raw_input("Enter next Employee record (y/n?)")
            if(s == 'n'):
                print "You Terminated"
                running = False
                break;
            else:
                name = raw_input("Employee Name : ")
                emp_num = raw_input("Employee Number : ")
                department = raw_input("Department : ")
                salary = raw_input("Enter Salary")
                dob = raw_input("Date of Birth")
                join_date = raw_input("Joined Date" )
                file.write("%s|%s|%s|%s|%s|%s \n" % (name,emp_num,department,salary,dob,join_date,))
    elif choices == '2':
        print "Searching the file..."
        searchForValue = raw_input("which value do u want to search ?")
        file = open('record.txt', 'r')
        for line in file:
            name = line.split("|",4)
            if name[0].lower() == searchForValue.lower():
                print "Name Found!"
                print name
                break;
            else:
                print "Record Not Found!"
    elif choices == '3':
        file = open('record.txt', 'r')
        for line in file:
            print line