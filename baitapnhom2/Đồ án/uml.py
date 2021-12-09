class Mark:
    avarage: float
    process: float
    dynamic: float
    def __init__(self,avarage,process,dynamic):
        self.avarage=avarage
        self.process=process
        self.dynamic=dynamic

    def outputMark(self):
        result= "Điểm trung bình: "+str(self.avarage) + "Điểm quá trình: "+str(self.process) + "Điểm năng động: " + str(self.dynamic)
        return result

class Lecturers:
    mark: list[Mark]
    lecturersname: str
    lecturersphone: str
    def __init__(self,lecturersname,lecturersphone):
        self.mark=[]
        self.lecturersphone=lecturersphone
        self.lecturersname=lecturersname
    def inputLecturers(self,diem:Mark):
        self.mark.append(diem)
    def outputLecturers(self):
        result="Tên giảng viên: " + self.lecturersname + "Số điện thoại: "+ self.lecturersphone
        return result

class Course:
    mark: list[Mark]
    lecturers:Lecturers
    coursename: str
    creditnumber: int
    lecturers: str
    def __init__(self,coursename,creditnumber,lecturers):
        self.mark=[]
        self.coursename=coursename
        self.creditnumber=creditnumber
        self.lecturers=lecturers
    def inputCourse(self,diem:Mark):
        self.mark.append(diem)
    def outputCourse(self):
        result= "Tên ngành học: "+self.coursename + "Số tín chỉ: "+ str(self.creditnumber) + "Tên giảng viên: "+ self.lecturers
        return result

class Tuition:
    tuitionname: str
    tuitionamount: int
    payment: str
    def __init__(self,tuitionname,tuitionamount,payment):
        self.tuitionname=tuitionname
        self.tuitionamount=tuitionamount
        self.payment=payment
    def outputTuition(self):
        result= "Tên học phí: "+self.tuitionname +"Học phí phải đóng(triệu đồng): " + str(self.tuitionamount) +"Cách thanh toán: "+ self.payment
        return result

class Payment:
    amount: float
    def __init__(self,amount):
        self.amount=amount
    def outputPayment(self):
        result="Học phí phải đóng:"+str(self.amount)

class Cash(Payment):
    cashtendered: float
    def __init__(self,amount,cashtendered):
        Payment.__init__(self,amount)
        self.cashtendered=cashtendered
    def outputCash(self):
        result= self.outputPayment() + "Tiền mặt: "+str(self.cashtendered)
        return result

class Bank(Payment):
    bankID: str
    def __init__(self,amount,bankID):
        Payment.__init__(self, amount)
        self.bankID=bankID
    def outputBank(self):
        result= self.outputPayment()+ "Số tài khoản:"+self.bankID
        return result

class Student:
    mark: list[Mark]
    course: list[Course]
    tuition: list[Tuition]
    Name: str
    Phone: str
    Email: str
    ID: str
    Address: str
    Marks: float
    Courses: str
    Tuition: int
    def __init__(self,name,phone,email,id,address,marks,courses,tuition):
        self.studentmanage=[]
        self.marks=[]
        self.courses=[]
        self.tuition=[]
        self.Name=name
        self.Phone=phone
        self.Email=email
        self.ID=id
        self.Address=address
        self.Marks=marks
        self.Courses=courses
        self.Tuition=tuition
    def addMark(self, diem : Mark) -> None:
        self.mark.append(diem)

    def addCourses(self, nganhhoc : Course) -> None:
        self.courses.append(nganhhoc)

    def addTuition(self,hocphi : Tuition) -> None:
        self.tuition.append(hocphi)

    def outputStudent(self):
        result= "Tên sinh viên:"+ self.Name + "Số điện thoại: "+self.Phone +"Email: "+self.Email+ "Mã sinh viên: " +self.ID +"Địa chỉ: "+self.Address
        for diem in self.mark:
            result+= "Các loại điểm của sinh viên: "+diem.outputMark()
            return result
        for nganhhoc in self.courses:
            result+= "Ngành học:"+nganhhoc.outputCourse()
            return  result
        for hocphi in self.tuition:
            result+= "Các loại học phí: "+hocphi.outputTuition()
            return result

class StudentManage:
    dssv: list[Student]
    insertStudentname: str
    deleteStudentname: str
    sortStudentType: str

    def __init__(self,insertStudentname,deleteStudentname,sortStudentType):
        self.dssv=[]
        self.insertStudentname=insertStudentname
        self.deleteStudentname=deleteStudentname
        self.sortStudentType=sortStudentType

    def insertStudent(self):
        result= "Tên sinh viên được thêm vào: "+self.insertStudentname
        return result

    def deleteStudent(self):
        result= "Tên sinh viên đã được xóa: "+self.deleteStudentname
        return result

    def sortStudent(self):
        result= "Cách thức sắp xếp sinh viên tăng dần hoặc giảm dần ( theo tên, theo điểm trung bình,...): "+ self.sortStudentType
        return result

def main():
    for i in range(3):
        sinhvien= Student(input("Nhập tên sinh viên "+str(i+1)+": "),input("Nhập số điện thoại:"),input("Nhập email: "),input("Nhập mã sinh viên:"),input("Nhập địa chỉ:"),input("Nhập điểm:"),input("Nhập"))
