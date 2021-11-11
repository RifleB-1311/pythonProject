dtb= float(input("Nhập điểm trung bình: "))
if dtb >= 0:
    if dtb < 5:
        print("Xếp loại Yếu")
elif dtb >= 5:
    #if dtb < 7:
    print("Xếp loại Trung bình")
elif dtb >= 7:
    #if dtb < 8:
    print("Xếp loại Khá")
elif dtb >= 8:
    #if dtb < 9:
    print("Xếp loại Giỏi")
else:
    print("Xếp loại Xuất sắc")