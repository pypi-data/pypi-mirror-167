def ftww(path, filename):
    '''
    path = csv 파일을 저장할 경로
    filename = 사용할 텍스트 파일(.txt)

    return df_list = 찾은 텍스트와 빈도수에 대한 데이터프레임
    '''

    import os
    import pandas as pd

    f = open(path + filename, 'r')
    lines = f.readlines()

    org_lines = []

    for line in lines:
        temp = line.rstrip('\n')
        org_lines.append(temp)
    
    kwd = list(input().split())
    kwd_list = []

    for key in kwd:
        temp = []
        for line in org_lines:
            if key in line:
                temp.append(line)
        kwd_list.append(temp)

    often_list = []

    for key, line in zip(kwd, kwd_list):
        temp_list = []
        for l in line:
            temp = l.count(key)
            temp_kwd = (key + ',')*temp
            temp_list.append(temp_kwd)
        often_list.append(temp_list)

    df_list = []

    for k, key, often in zip(kwd, kwd_list, often_list):
        temp = pd.DataFrame({k : key, k+' 빈도' : often})
        df_list.append(temp)

    path_list = []

    for key, df in zip(kwd, df_list):
        df.to_csv(path + key+'_inline_multi_input.csv', index = False, encoding= 'CP949')
        path_list.append(path + key+'_inline_multi_input.csv')

    return df_list