from pandas import DataFrame
from matplotlib import font_manager
import pandas

# 글꼴 폴더 확인
font_manager._rebuild()

# 목록을 리스트로 가져온다.
flist = font_manager.findSystemFonts()
print(flist)
print('-'*30)

# 리스트로 정보조회
font_list = []
for v in flist:
    fprop = font_manager.FontProperties(fname=v)
    font_list.append({'name':fprop.get_name(), 'file':fprop.get_file()})

print(font_list[:5])
print('-'*30)

# 데이터 프레임으로 생성
df = DataFrame(font_list)
print(df)
print('-'*30)

# pandas에게 콘솔창에 표시할 최대 행 수를 전체 데이터수로 설정
print(pandas.get_option('display.max_rows'))
print('-'*30)

row, col = df.shape
pandas.set_option('display.max_rows', row)
print(df.sort_values('name'))
print('-'*30)

# 데이터프레임을 파일로 출력
df.to_csv('my_font_list.csv', index=True)
df.to_excel('my_font_list.xls', index=False)

