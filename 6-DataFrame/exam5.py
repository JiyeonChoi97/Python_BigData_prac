from pandas import ExcelFile # Excel 파일을 읽어들이기 위한 클래스

xls = ExcelFile('data/children_house.xlsx')
print(xls)
print(type(xls))
print('-'*30)

# 엑셀 파일의 sheet 이름에 대한 리스트
print(xls.sheet_names)
print('-'*30)

# 가져오고자 하는 sheet 이름을 지정하여 데이터프레임으로 변환
df = xls.parse(xls.sheet_names[0])
print(df)
print('-'*30)
print(type(df))

'''
<pandas.io.excel._base.ExcelFile object at 0x00000229456CB288>
<class 'pandas.io.excel._base.ExcelFile'>
------------------------------
['데이터', '메타정보']
------------------------------
       지역   2014   2015   2016
0   전국(계)  43742  42517  41084
1      서울   6787   6598   6368
2      부산   1957   1971   1937
3      대구   1588   1539   1483
4      인천   2308   2278   2231
5      광주   1260   1264   1238
6      대전   1698   1669   1584
7      울산    946    934    895
8      세종    160    216    250
9      경기  13259  12689  12120
10     강원   1257   1227   1180
11     충북   1229   1230   1208
12     충남   2053   1988   1974
13     전북   1654   1623   1562
14     전남   1242   1238   1251
15     경북   2212   2130   2102
16     경남   3533   3349   3158
17     제주    599    574    543
------------------------------
<class 'pandas.core.frame.DataFrame'>
'''