f = open('C:/pytest/금융규제운영규정.txt','r')
data = f.readlines()
f.close()

anum = input('몇개를 찾으시겠습니까?(숫자만 입력해주시기 바랍니다)')
adata = input('찾을 단어를 입력해주시기 바랍니다(단어사이를 띄어주세요):')

# 사용자가 입력한 단어를 띄어쓰기를 구분으로 리스트 만들기
a1 = adata.split(' ')

# 사용자가 입력한 숫자에 맞게 빈리스트 만들기
list_ = {}
num = 0
for i in range(int(anum)):
    list_[num] = []
    num += 1

# 각 리스트에 찾은 단어가 있는 문장을 넣은 리스트 만들기
num = 0
for a in a1:
    for b in data:
        if a in b:
            list_[num].append(b)
    num += 1

# 데이터프레임 만들기
list1_ ={}
num = 0
for i in range(int(anum)):
    list1_[num] = len(list_[num])
    num += 1

# 데이터프레임 만들기
import pandas as pd
num1 = 0
df_ = pd.DataFrame(index = range(max(list1_.values())))
for i in range(len(list_.keys())):
    df_[num1] = pd.DataFrame(list_[num1])
    num1 += 1

# 저장
num2 = 0
path = 'C:/pytest/'
while int(num2) < int(anum):
    df_[num2].to_excel(path+a1[num2]+'.xlsx', index = False, header = 0)
    num2 += 1