print(df)
print('-' * 30)

tmp_df = df.filter(['movieNm', 'audiCnt'])
print(tmp_df)
print('-' * 30)

daily_rand_df = tmp_df.rename(index=tmp_df['movieNm'],
                              columns={'audiCnt':'관람객'})
print(daily_rand_df)
print('-' * 30)

daily_rand_df.drop('movieNm', axis=1, inplace=True)
print(daily_rand_df)
print('-' * 30)

print(daily_rand_df['관람객'])
print('-' * 30)

daily_rand_df['관람객'] = daily_rand_df['관람객'].astype(int)
print(daily_rand_df['관람객'])
print('-' * 30)

daily_rand_df_sort = daily_rand_df.sort_values('관람객')
print(daily_rand_df_sort)
print('-' * 30)

# 그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'      # 한글 폰트 설
pyplot.rcParams['font.size']=16                   # 글자 크기 설정
pyplot.rcParams['figure.figsize']=(14,8)             # 그래프의 가로, 세로크기(inch)

daily_rand_df_sort.plot.barh(rot=45)
pyplot.title('%s 박스오피스 순위' %yesterday_str)
pyplot.grid()
pyplot.savefig('박스오피스 순위.png')
pyplot.show()


