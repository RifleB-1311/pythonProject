import pickle
class Person:
    name: str
    phone: str
    email: str

    def __init__(self, ten, sdt, mail):
        # Khởi tạo các giá trị
        self.name = ten
        self.phone = sdt
        self.email = mail


    def outputPerson(self) -> str:
        result = "Tên:" + self.name + ".Số điện thoại:" + self.phone + ".Email:" + self.email
        return result


class Student(Person):
    studentnumber: str
    avaragemark: float

    def __init__(self, ten, sdt, mail, soSV, dtb):
        Person.__init__(self, ten, sdt, mail)
        self.studentnumber = soSV
        self.avaragemark = dtb

    def outputStudent(self) -> str:
        result = self.outputPerson() + ".Số sinh viên:" + self.studentnumber + ".Điểm trung bình:" + str(
            self.avaragemark)
        return result


class Professor(Person):
    salary: float

    def __init__(self, ten, sdt, mail, luong):
        Person.__init__(self, ten, sdt, mail)
        self.salary = luong

    def outputProfessor(self) -> str:
        result = self.outputPerson() + ".Lương(triệu đồng):" + str(self.salary)
        return result


def main():
    #Tạo
    n=3
    arr= []        #Tạo 1 danh sách chứa các phần tử của cá nhân
    arr1 = []       #Danh sách chứa thông tin của sinh viên
    arr2 = []       #Danh sách chứa thông tin của giáo sư

    for i in range(n):
        arr.append(Person(input(f"Mời nhập tên người {i + 1}: "),input(f"Mời nhập số điện thoại người {i + 1}: "),input(f"Mời nhập email người {i + 1}: ")))
          # Danh sách 10 cá nhân
    print("\nCác phần tử trong danh sách cá nhân ban đầu là: ")
    for item in range(len(arr)):
        print(str(item+1)+" - ",arr[item].outputPerson())

    for a in range(len(arr)):
        for b in range(a+1,len(arr)):               #Sắp xếp danh sách giảm dần
            if arr[a].name<arr[b].name:
                arr[a],arr[b]=arr[b],arr[a]

    print("\nCác phần tử trong danh sách cá nhân sau khi được sắp xếp giảm dần theo tên là:")
    for item in range(len(arr)):
        print(str(item+1)+" - ",arr[item].outputPerson())
    print("\n")

    for j in range(n):
        sinhvien = Student(input("Mời nhập tên sinh viên " + str(j + 1) + ":"),
                        input("Mời nhập số điện thoại sinh viên " + str(j + 1) + ":"),
                        input("Mời nhập email sinh viên " + str(j + 1) + ":"),
                        input("Mời nhập số sinh viên " + str(j + 1) + ":"),
                        input("Mời nhập điểm trung bình sinh viên " + str(j + 1) + ":"))
        arr1.append(sinhvien)
         # Danh sách 10 sinh viên
    print("\nCác phần tử trong danh sách sinh viên ban đầu là: ")
    for item in range(len(arr1)):
        print(str(item+1)+" - ",arr1[item].outputStudent())
    for a in range(len(arr1)):
        for b in range(a+1,len(arr1)):               #Sắp xếp danh sách giảm dần
            if arr1[a].avaragemark<arr1[b].avaragemark:
                arr1[a],arr1[b]=arr1[b],arr1[a]

    print("\nCác phần tử trong danh sách sinh viên sau khi được sắp xếp giảm dần theo điểm trung bình là:")
    for item in range(len(arr1)):
        print(str(item+1)+" - ",arr1[item].outputStudent())
    print("\n")

    for k in range(n):
        giaosu = Professor(input("Mời nhập tên giáo sư " + str(k + 1) + ":"),
                          input("Mời nhập số điện thoại giáo sư " + str(k + 1) + ":"),
                          input("Mời nhập email giáo sư " + str(k + 1) + ":"),
                          input("Mời nhập lương giáo sư(triệu đồng) " + str(k + 1) + ":"))
        arr2.append(giaosu)
    print("\nCác phần tử trong danh sách giáo sư ban đầu là: ")
    for item in range(len(arr2)):
        print(str(item+1)+" - ",arr2[item].outputProfessor())
    for a in range(len(arr2)):
        for b in range(a+1,len(arr2)):               #Sắp xếp danh sách tăng dần
            if arr2[a].salary>arr2[b].salary:
                arr2[a],arr2[b]=arr2[b],arr2[a]

    print("\nCác phần tử trong danh sách giáo sư sau khi được sắp xếp tăng dần theo lương là:")
    for item in range(len(arr2)):
        print(str(item+1)+" - ",arr2[item].outputProfessor())

    # Lưu trữ tập tin:
    f = open("Danh sách cá nhân.txt", "wb")
    for i in arr:
        pickle.dump(i.outputPerson(), f)
    f.close()                                               #Lưu trữ danh sách cá nhân
    f = open("Danh sách cá nhân.txt", "rb")
    for i in arr:
        a=pickle.load(f)
        print(a)
    f.close()

    f = open("Danh sách sinh viên.txt", "wb")
    for i in arr1:
        pickle.dump(i.outputStudent(), f)
    f.close()                                               #Lưu trữ danh sách sinh viên
    f = open("Danh sách sinh viên.txt", "rb")
    for i in arr1:
        a=pickle.load(f)
        print(a)
    f.close()

    f = open("Danh sách giáo sư.txt", "wb")
    for i in arr2:
        pickle.dump(i.outputProfessor(), f)
    f.close()                                               #Lưu trữ danh sách giáo sư
    f = open("Danh sách giáo sư.txt", "rb")
    for i in arr2:
        a=pickle.load(f)
        print(a)
    f.close()
if __name__=="__main__""" :
    main()

