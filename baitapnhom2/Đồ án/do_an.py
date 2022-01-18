class Tuition:
    tuitionname: str
    tuitionamount: int

    def __init__(self,tuitionname,tuitionamount) -> None:
        self.tuitionname= tuitionname
        self.tuitionamount= tuitionamount

    def displayTuitionname(self) -> str:
        return self.tuitionname

    def displayTuitionamount(self) -> int:
        return self.tuitionamount

    def outputTuition(self) ->str:
        tuition = "Tên học phí: " + self.tuitionname + " ,Số tiền phải nộp: " +str(self.tuitionamount)
        return tuition

class Cash(Tuition):
    cashtendered: float

    def __init__(self,tuitionname,tuitionamount,cashtendered) -> None:
        Tuition.__init__(self,tuitionname,tuitionamount)
        self.cashtendered = cashtendered

    def outputCash(self) -> str:
        cash= self.outputTuition() + ",Tiền mặt: "+ str(self.cashtendered)
        return cash

class Bank(Tuition):
    bankID: str

    def __init__(self,tuitionname,tuitionamount,stk):
        Tuition.__init__(self,tuitionname,tuitionamount)
        self.bankID=stk

    def outputBank(self) ->str:
        bank= self.outputTuition() +",Số tài khoản: " + self.bankID
        return bank

class Mark:
    average: float
    semester: float
    process: float

    def __init__(self,process,semester) ->None:

        self.semester = semester
        self.process = process
        self.average = round(0.3 * self.process + 0.7 * self.semester,2)
    def displayAverage(self) ->float:
        return self.average

    def displaySemester(self) ->float:
        return self.semester

    def displayProcess(self) ->float:
        return self.process

    def outputMark(self) ->str:
        mark= "Điểm quá trình: " + str(self.process) + ", Điểm thi: " + str(self.semester) + ", Điểm trung bình: " + str(self.average)
        return mark

class Lecturer:
    lecturername: str
    lecturerphone: str

    def __init__(self,lecturername,lecturerphone) -> None:
        self.lecturername= lecturername
        self.lecturerphone= lecturerphone

    def outputLecturer(self) ->str:
        lecturer = "Tên giảng viên: " + self.lecturername + ", Số điện thoại:" +self.lecturerphone
        return lecturer


class Course:
    dsdiem: list[Mark]
    lecturer:  Lecturer
    coursename: str
    creditnumber: int

    def __init__(self,coursename,creditnumber) -> None:
        self.coursename= coursename
        self.creditnumber= creditnumber
        self.dsdiem = []



    def displayDsdiem(self) -> list[Mark]:
        return self.dsdiem

    def displayLecturer(self) -> Lecturer:
        return self.lecturer

    def displayCourseName(self) ->str:
        return self.coursename

    def displayCreditNumber(self) ->int:
        return self.creditnumber

    def outputCourse(self) -> str:
        course = "Tên ngành học: " + self.coursename + ", Số tín chỉ: " + str(self.creditnumber)+"\n"
        for diem in self.dsdiem:
            course += "\t" + diem.outputMark() + "\n"
        return course

class Student:
    name: str
    phone: str
    email: str
    ID: str
    address: str
    course: list[Course]
    tuition: Tuition

    def __init__(self,name,phone,email,id,address) ->None:
        self.name = name
        self.phone = phone
        self.email = email
        self.ID= id
        self.address = address

    def outputStudent(self) ->str:
        result = "Tên sinh viên: "+self.name +", Số điện thoại: " + self.phone +", Email: " + self.email + ", ID: " + self.ID + ", Địa chỉ: " + self.address
        return result

def main():
    n = int(input("Mời nhập số sinh viên cần nhập dữ liệu:"))       #Nhập dữ liệu cho sinh viên
    arr=[] #danh sách sinh viên
    arr1=[] #danh sách điểm
    arr2=[] #danh sách môn
    for j in range(n):
        sinhvien = Student(input("Mời nhập tên sinh viên " + str(j + 1) + ":"),
                           input("Mời nhập số điện thoại sinh viên " + str(j + 1) + ":"),
                           input("Mời nhập email sinh viên " + str(j + 1) + ":"),
                           input("Mời nhập số sinh viên " + str(j + 1) + ":"),
                           input("Mời nhập địa chỉ sinh viên " + str(j + 1) + ":"))
        diem= Mark(float(input("Mời nhập điểm quá trình: ")),float(input("Mời nhập điểm thi: ")))
        mon= Course(input("Mời nhập tên môn học: "),input("Mời nhập số tín chỉ: "))
        arr.append(sinhvien)
        arr1.append(diem)
        arr2.append(mon)
    #Lưu danh sách
    import pickle
    f = open("Danh sách sinh viên.txt", "wb")
    for i in arr:
        pickle.dump(i.outputStudent(), f)
    f.close()  # Lưu trữ danh sách sinh viên
    f = open("Danh sách sinh viên.txt", "rb")
    for i in arr:
        a = pickle.load(f)
        print(a)
    f.close()

    print("\n")
    a="y"
    while a!="n" and a!="N":    # Tính năng quản lí sinh viên
        chucnang= int(input("Xin vui lòng chọn chức năng ( 0:Sắp xếp danh sách, 1: Tra cứu thông tin sinh viên, 2:Xóa sinh viên, 3: Sửa thông tin sinh viên):  "))
        if (chucnang == 0) :
            check = int(input("Mời nhập cách sắp xếp tên trong danh sách( 0: giảm dần, 1: tăng dần):"))
            if check == 0:
                for a in range(0, len(arr)-1):
                    for b in range(a + 1, len(arr)):
                        if arr[a].name < arr[b].name:       #Sắp xếp giảm dần
                            arr[a], arr[b] = arr[b], arr[a]
                arr_result = []
                for item in arr:
                    item = item.outputStudent()
                    arr_result.append(item)
                print("\nDanh sách sinh viên sau khi được sắp xếp giảm dần theo tên là:",arr_result)

            if check == 1:
                for a in range(0, len(arr) - 1):
                    for b in range(a + 1, len(arr)):  # Sắp xếp danh sách tăng dần
                        if arr[a].name > arr[b].name:
                            arr[a], arr[b] = arr[b], arr[a]
                arr_result = []
                for item in arr:
                    item = item.outputStudent()
                    arr_result.append(item)
                print("\nDanh sách sinh viên sau khi được sắp xếp tăng dần theo tên là:", arr_result)
        if chucnang ==1:
            nhapso= int(input("Bạn muốn tra cứu thông tin bằng gì ? ( 1:Tên, 2:SĐT, 3:Email, 4:ID, 5:Địa chỉ):"))
            tracuu= input("Mời nhập thông tin cụ thể cần tra cứu:")
            if nhapso==1:
                for i in range(len(arr)):
                    if tracuu == arr[i].name:
                        print("Thông tin bạn muốn tra cứu là: ",arr[i].outputStudent()+','+arr1[i].outputMark() + ","+arr2[i].outputCourse())
                        break
                else:
                    print("Ko có trong danh sách sinh viên")
            if nhapso==2:
                for i in range(len(arr)):
                    if tracuu == arr[i].phone:
                        print("Thông tin bạn muốn tra cứu là: ", arr[i].outputStudent()+','+arr1[i].outputMark() + ","+arr2[i].outputCourse())
                        break
                else:
                    print("Ko có trong danh sách sinh viên")
            if nhapso==3:
                for i in range(len(arr)):
                    if tracuu == arr[i].email:
                        print("Thông tin bạn muốn tra cứu là: ", arr[i].outputStudent()+','+arr1[i].outputMark() + ","+arr2[i].outputCourse())
                        break
                else:
                    print("Ko có trong danh sách sinh viên")
            if nhapso==4:
                for i in range(len(arr)):
                    if tracuu == arr[i].ID:
                        print("Thông tin bạn muốn tra cứu là: ", arr[i].outputStudent()+','+arr1[i].outputMark() + ","+arr2[i].outputCourse())
                        break
                else:
                    print("Ko có trong danh sách sinh viên")
            if nhapso==5:
                for i in range(len(arr)):
                    if tracuu == arr[i].address:
                        print("Thông tin bạn muốn tra cứu là: ", arr[i].outputStudent()+','+arr1[i].outputMark() + ","+arr2[i].outputCourse())
                        break
                else:
                    print("Ko có trong danh sách sinh viên")

        if chucnang ==2:
            nhap= input("Vui lòng nhập Họ và Tên sinh viên cần xóa: ")
            for i in range(len(arr)):
                if nhap == arr[i].name:
                    arr.remove(arr[i])
                    print("Đã xóa sinh viên !")

        if chucnang ==3:
            x= int(input("Mời nhập thông tin bạn muốn sửa ? (1:Tên, 2:SĐT, 3:Email, 4:ID, 5:Địa chỉ): "))
            if x==1:
                y = input("Mời nhập Họ và Tên của sinh viên bạn muốn sửa ? : ")
                sua = input("Bạn muốn sửa thành gì ? : ")
                for i in range(len(arr)):
                    if y == arr[i].name:
                        arr[i].name.replace(y,sua)
                        print("Tên đã được sửa từ ",y," sang ",sua," !")

            if x==2:
                y = input("Mời nhập SDT của sinh viên bạn muốn sửa ? : ")
                sua = input("Bạn muốn sửa thành gì ? : ")
                for i in range(len(arr)):
                    if y == arr[i].phone:
                        arr[i].phone.replace(y,sua)
                        print("SDT đã được sửa từ ",y," sang ",sua," !")
            if x==3:
                y = input("Mời nhập Email của sinh viên bạn muốn sửa ? : ")
                sua = input("Bạn muốn sửa thành gì ? : ")
                for i in range(len(arr)):
                    if y == arr[i].email:
                        arr[i].email.replace(y,sua)
                        print("Email đã được sửa từ ",y," sang ",sua," !")

            if x==4:
                y = input("Mời nhập ID của sinh viên bạn muốn sửa ? : ")
                sua = input("Bạn muốn sửa thành gì ? : ")
                for i in range(len(arr)):
                    if y == arr[i].ID:
                        arr[i].ID.replace(y,sua)
                        print("ID đã được sửa từ ",y," sang ",sua," !")

            if x==5:
                y = input("Mời nhập địa chỉ của sinh viên bạn muốn sửa ? : ")
                sua = input("Bạn muốn sửa thành gì ? : ")
                for i in range(len(arr)):
                    if y == arr[i].address:
                        arr[i].address.replace(y,sua)
                        print("Địa chỉ đã được sửa từ ",y," sang ",sua," !")

        a= input("Có tiếp tục sử dụng chức năng hay không ? (Y:Có, N:Không): ")
main()








