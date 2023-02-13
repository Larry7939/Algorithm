total = int(input("초 입력"))
hour = total//3600
min = total//60-hour*60
sec = total%60
print(f"{hour}시 {min}분 {sec}초")
