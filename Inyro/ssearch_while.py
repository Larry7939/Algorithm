id = input("Enter ID: ")
input_password = input("Enter Password: ")
if(len(id)<10):
    if(len(input_password)<10):
        print("회원가입완료")
    else:
        print("비밀번호가 10자 이상")
else:
    print("ID가 10자 이상")
