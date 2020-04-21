from pandas import DataFrame

# 리스트를 원소로 갖는 딕셔너리
grade_dic = {
                '국어': [98, 88, 92, 63, 120],
                '영어': [None, 90, 70, 60, 50],
                '수학': [88, 62, None, 31, None],
                '과학': [64, 72, None, 70, 88]                
            }

# 딕셔너리의 키값이 컬럼의 이름으로 지정됨 
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print(df)
print(type(df))
print('-'*30)

'''
     국어    영어    수학    과학
철수   98   NaN  88.0  64.0
영희   88  90.0  62.0  72.0
민철   92  70.0   NaN   NaN
수현   63  60.0  31.0  70.0
호영  120  50.0   NaN  88.0
<class 'pandas.core.frame.DataFrame'>
------------------------------
'''