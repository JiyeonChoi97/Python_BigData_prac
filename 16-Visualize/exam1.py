import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200424145200.xlsx')
print(df)
print('-'*30)

col_list = list(df.columns)
print(col_list)
print('-'*30)

df_traffic = df.filter(['시도별(1)', '2018. 01', '2018. 02', '2018. 03', '2018. 04', 
                        '2018. 05', '2018. 06', '2018. 07', '2018. 08', 
                        '2018. 09', '2018. 10', '2018. 11', '2018. 12'])
print(df_traffic)
print('-'*30)

df_traffic.drop(0, inplace=True)
print(df_traffic)
print('-'*30)

df_traffic = df_traffic.rename(index=df_traffic['시도별(1)']).drop('시도별(1)', axis=1)
print(df_traffic)
print('-'*30)

dic_month= {'2018. 01':'1월', '2018. 02':'2월', '2018. 03':'3월', '2018. 04':'4월', 
            '2018. 05':'5월', '2018. 06':'6월', '2018. 07':'7월', '2018. 08':'8월', 
            '2018. 09':'9월', '2018. 10':'10월', '2018. 11':'11월', '2018. 12':'12월'}

df_traffic.rename(columns=dic_month, inplace=True)
print(df_traffic)
print('-'*30)

df_traffic =df_traffic.T
print(df_traffic)
print('-'*30)

df_traffic.drop(['경기', '강원', '충북', '전북', '제주', '충남', 
                 '전남', '경북', '경남', '광주', '대전', '울산', '세종'], axis=1, inplace=True)
print(df_traffic)
print('-'*30)

'''
    시도별(1)  2018. 01 2018. 01.1  ...  2018. 12 2018. 12.1 2018. 12.2
0   시도별(1)  발생건수 (건)   사망자수 (명)  ...  발생건수 (건)   사망자수 (명)   부상자수 (명)
1       서울      3192         30  ...      3221         24       4471
2       부산       965         10  ...      1020          7       1373
3       경기      4405         61  ...      4532         65       6755
4       강원       588         13  ...       577         21        875
5       충북       621         12  ...       785         18       1293
6       충남       596         18  ...       728         31       1093
7       전북       533         20  ...       544         16        811
8       전남       668         29  ...       804         31       1268
9       경북      1023         24  ...      1119         37       1644
10      경남       859         21  ...       974         32       1408
11      제주       331         11  ...       339          7        499
12      대구      1044         11  ...      1098         13       1588
13      인천       694         14  ...       599          8        833
14      광주       562          7  ...       655          4       1013
15      대전       547         11  ...       638          6        989
16      울산       341          8  ...       320          3        467
17      세종        57          4  ...        57          0         83

[18 rows x 37 columns]
------------------------------
['시도별(1)', '2018. 01', '2018. 01.1', '2018. 01.2', '2018. 02', '2018. 02.1', '2018. 02.2', '2018. 03', '2018. 03.1', '2018. 03.2', '2018. 04', '2018. 04.1', '2018. 04.2', '2018. 05', '2018. 05.1', '2018. 05.2', '2018. 06', '2018. 06.1', '2018. 06.2', '2018. 07', '2018. 07.1', '2018. 07.2', '2018. 08', '2018. 08.1', '2018. 08.2', '2018. 09', '2018. 09.1', '2018. 09.2', '2018. 10', '2018. 10.1', '2018. 10.2', '2018. 11', '2018. 11.1', '2018. 11.2', '2018. 12', '2018. 12.1', '2018. 12.2']
------------------------------
    시도별(1)  2018. 01  2018. 02  ...  2018. 10  2018. 11  2018. 12
0   시도별(1)  발생건수 (건)  발생건수 (건)  ...  발생건수 (건)  발생건수 (건)  발생건수 (건)
1       서울      3192      2973  ...      3500      3243      3221
2       부산       965       859  ...      1029      1039      1020
3       경기      4405      4327  ...      4845      4765      4532
4       강원       588       522  ...       678       654       577
5       충북       621       692  ...       881       934       785
6       충남       596       632  ...       831       742       728
7       전북       533       489  ...       652       626       544
8       전남       668       665  ...       984       843       804
9       경북      1023       961  ...      1282      1200      1119
10      경남       859       807  ...      1091       990       974
11      제주       331       269  ...       355       402       339
12      대구      1044       908  ...      1131      1198      1098
13      인천       694       636  ...       674       611       599
14      광주       562       515  ...       666       672       655
15      대전       547       567  ...       684       709       638
16      울산       341       313  ...       390       336       320
17      세종        57        73  ...        65        65        57

[18 rows x 13 columns]
------------------------------
   시도별(1) 2018. 01 2018. 02 2018. 03  ... 2018. 09 2018. 10 2018. 11 2018. 12
1      서울     3192     2973     3072  ...     3144     3500     3243     3221
2      부산      965      859     1019  ...     1007     1029     1039     1020
3      경기     4405     4327     3932  ...     4504     4845     4765     4532
4      강원      588      522      526  ...      683      678      654      577
5      충북      621      692      763  ...      820      881      934      785
6      충남      596      632      713  ...      767      831      742      728
7      전북      533      489      549  ...      623      652      626      544
8      전남      668      665      762  ...      857      984      843      804
9      경북     1023      961     1097  ...     1223     1282     1200     1119
10     경남      859      807      952  ...      970     1091      990      974
11     제주      331      269      371  ...      338      355      402      339
12     대구     1044      908     1030  ...     1122     1131     1198     1098
13     인천      694      636      585  ...      679      674      611      599
14     광주      562      515      607  ...      643      666      672      655
15     대전      547      567      599  ...      623      684      709      638
16     울산      341      313      364  ...      318      390      336      320
17     세종       57       73       81  ...       50       65       65       57

[17 rows x 13 columns]
------------------------------
   2018. 01 2018. 02 2018. 03 2018. 04  ... 2018. 09 2018. 10 2018. 11 2018. 12
서울     3192     2973     3072     3219  ...     3144     3500     3243     3221
부산      965      859     1019      963  ...     1007     1029     1039     1020
경기     4405     4327     3932     4327  ...     4504     4845     4765     4532
강원      588      522      526      593  ...      683      678      654      577
충북      621      692      763      821  ...      820      881      934      785
충남      596      632      713      773  ...      767      831      742      728
전북      533      489      549      605  ...      623      652      626      544
전남      668      665      762      841  ...      857      984      843      804
경북     1023      961     1097     1204  ...     1223     1282     1200     1119
경남      859      807      952      958  ...      970     1091      990      974
제주      331      269      371      332  ...      338      355      402      339
대구     1044      908     1030     1105  ...     1122     1131     1198     1098
인천      694      636      585      613  ...      679      674      611      599
광주      562      515      607      598  ...      643      666      672      655
대전      547      567      599      622  ...      623      684      709      638
울산      341      313      364      330  ...      318      390      336      320
세종       57       73       81       88  ...       50       65       65       57

[17 rows x 12 columns]
------------------------------
      1월    2월    3월    4월    5월    6월    7월    8월    9월   10월   11월   12월
서울  3192  2973  3072  3219  3454  3253  3321  3203  3144  3500  3243  3221
부산   965   859  1019   963  1016   969  1030  1021  1007  1029  1039  1020
경기  4405  4327  3932  4327  4445  4397  4610  4359  4504  4845  4765  4532
강원   588   522   526   593   662   635   663   717   683   678   654   577
충북   621   692   763   821   787   818   855   841   820   881   934   785
충남   596   632   713   773   799   725   745   756   767   831   742   728
전북   533   489   549   605   599   569   555   585   623   652   626   544
전남   668   665   762   841   843   798   863   859   857   984   843   804
경북  1023   961  1097  1204  1212  1169  1240  1236  1223  1282  1200  1119
경남   859   807   952   958   968   967   996   961   970  1091   990   974
제주   331   269   371   332   351   391   383   377   338   355   402   339
대구  1044   908  1030  1105  1165  1116  1152  1130  1122  1131  1198  1098
인천   694   636   585   613   666   606   671   598   679   674   611   599
광주   562   515   607   598   645   618   639   639   643   666   672   655
대전   547   567   599   622   630   645   617   673   623   684   709   638
울산   341   313   364   330   318   337   297   328   318   390   336   320
세종    57    73    81    88    76    69    62    52    50    65    65    57
------------------------------
       서울    부산    경기   강원   충북   충남   전북  ...   제주    대구   인천   광주   대전   울산  세종
1월   3192   965  4405  588  621  596  533  ...  331  1044  694  562  547  341  57
2월   2973   859  4327  522  692  632  489  ...  269   908  636  515  567  313  73
3월   3072  1019  3932  526  763  713  549  ...  371  1030  585  607  599  364  81
4월   3219   963  4327  593  821  773  605  ...  332  1105  613  598  622  330  88
5월   3454  1016  4445  662  787  799  599  ...  351  1165  666  645  630  318  76
6월   3253   969  4397  635  818  725  569  ...  391  1116  606  618  645  337  69
7월   3321  1030  4610  663  855  745  555  ...  383  1152  671  639  617  297  62
8월   3203  1021  4359  717  841  756  585  ...  377  1130  598  639  673  328  52
9월   3144  1007  4504  683  820  767  623  ...  338  1122  679  643  623  318  50
10월  3500  1029  4845  678  881  831  652  ...  355  1131  674  666  684  390  65
11월  3243  1039  4765  654  934  742  626  ...  402  1198  611  672  709  336  65
12월  3221  1020  4532  577  785  728  544  ...  339  1098  599  655  638  320  57

[12 rows x 17 columns]
------------------------------
       서울    부산    대구   인천
1월   3192   965  1044  694
2월   2973   859   908  636
3월   3072  1019  1030  585
4월   3219   963  1105  613
5월   3454  1016  1165  666
6월   3253   969  1116  606
7월   3321  1030  1152  671
8월   3203  1021  1130  598
9월   3144  1007  1122  679
10월  3500  1029  1131  674
11월  3243  1039  1198  611
12월  3221  1020  1098  599
------------------------------
'''

