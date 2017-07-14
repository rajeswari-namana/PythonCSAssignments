#Library Management System
class LibraryRecord():  # class 1
    def __init__(self): #_init_ constructor
        pass

    def lib(self):
        __libName = "Krishna" # Private data member
        print("Librarian name is",__libName)

class LibraryMembership():  #class 2
    fee="$200"
    def __init__(self): #_init_ constructor
       print("Membership fee: $200")

class MebershipFee(LibraryMembership):  #inheritance( #class 3)

    def __init__(self): #_init_ constructor
        LibraryMembership.__init__(self)

    def membershipFee(self,isPaid):
        self.isPaid=isPaid
        if (self.isPaid=="true"):
            print("Membership amount of",self.fee,"has been paid")
        else:
            print("Membership amount of", self.fee, "has not been paid")

class StudentDetails(): #class 4
    def __init__(self): #_init_ constructor
        pass

    def studentInfo(self, studentName,studentID):
        self.studentName = studentName
        self.studentID = studentID
        print("Student name is",self.studentName,"and student ID is",self.studentID)

class BookDetails():    #class 5
    def __init__(self): #_init_ constructor
        pass

    def book(self,bookname,bookID,bookAuthor):
        self.bookname=bookname
        self.bookID=bookID
        self.bookAuthor=bookAuthor
        print("Book name: "+self.bookname+"/ Book ID: "+self.bookID+"/ Author: "+self.bookAuthor)

class StudentBookDetails(StudentDetails,BookDetails):   # multiple inheritance (#class 6)
    def __init__(self):     #_init_ constructor
        super().__init__()  # use of super keyword

    def bookDates(self,borrowedOn,returnDate):
        self.borrowedOn = borrowedOn
        self.returnDate = returnDate
        print("The book was borrowed on "+self.borrowedOn+" and has to be returned on "+self.returnDate)
        print("------------------------------------------------------------------------------")

#instances of classes
lib1=LibraryRecord()
lib1.lib()
student1=StudentDetails()
student1.studentInfo("Raji",16)
fee=MebershipFee()
fee.membershipFee("true")
book1=StudentBookDetails()
book1.book("python","20000","jose")
book1.bookDates("07-13-2017","07-23-2017")

lib1=LibraryRecord()
lib1.lib()
student1=StudentDetails()
student1.studentInfo("swetha",18)
fee=MebershipFee()
fee.membershipFee("false")
book1=StudentBookDetails()
book1.book("PDC","20002","Cory")
book1.bookDates("07-5-2017","07-15-2017")






