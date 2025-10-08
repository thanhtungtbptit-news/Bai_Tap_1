name=str(input("Nhập tên của bạn: "))
score=float(input("Nhập điểm của bạn: "))
if score >= 9:
    print("Xuất sắc ")
elif name.upper().startswith("A") and score >= 8:
    print("Xuất sắc ")
elif 8 <= score < 9:
    print("Giỏi ")    
elif 6 <= score < 8:
    print("Khá ")
elif 5 <= score < 6:
    print("Trung bình ")
elif 0 <= score < 5:
    print("Yếu ")
else:
    print("Điểm không hợp lệ ")