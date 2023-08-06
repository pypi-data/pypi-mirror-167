import rhinoMorph
rn = rhinoMorph.startRhino()

# 3 버전
# 파일을 쓰기 모드로 엽니다.
import pandas as pd

path = "C:/pytest_basic-20220907T003523Z-001/pytest/"
fp = open(path + "금융규제운영규정.txt", 'r')
data = []
input_N = []
find_N = []
find = False

input_N = (input('검색할 키워드를 입력하세요.').split())

for i in input_N:
    print(i)

# pandas 형식으로 저장
for line in fp.readlines():
    for check in rhinoMorph.onlyMorph_list(rn, line):
        for i in input_N:
            if i == check:
                data.append(line[:-1])
                break

fp.close()

df_data = pd.DataFrame(data)
df_data = pd.DataFrame(df_data[0].unique())
df_data

# 2번 버전
# column 2번째 사용하기
count = 0
check2 = 0
for i in input_N:
    df_data[i] = ""

for i in input_N:
    for line in df_data[0]:
        for check in rhinoMorph.onlyMorph_list(rn, line):
            if i == check:
                count = count + 1
        df_data[i][check2] = count
        check2 = check2 + 1
        count = 0
    check2 = 0

df_data.to_csv(path+"연습문제5번2.csv",index=False)
data_csv = pd.read_csv(path+"연습문제5번2.csv")
print(data_csv)

