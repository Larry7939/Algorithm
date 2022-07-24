input_data = input()
row = int(input_data[1])
colum = ord(input_data[0])-ord('a')+1
steps = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]#나이트의 이동 가능한 경우 정리 (행,열)

count =0

for i in steps:
    if (1<=row+i[0]<=8) and (1<=colum+i[1]<=8):
       count+=1
print(count)