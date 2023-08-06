import pandas as pd
import rhinoMorph
import numpy as np

def ex5():
    lines = []
    with open("C:/pytest/금융규제운영규정.txt", "r", encoding="CP949") as f:
        while True:
            line = f.readline()
            if not line:
                break
            # print(line.strip())
            lines.append(line)
    df = pd.DataFrame(lines)
    df.columns = ['문장']
    df_con = df[df['문장'].str.contains('금융|전자')]  # contains안에 들어가는 단어중 하나라도 있으면 출력하는 코드
    con_lst = list(df_con['문장'])
    key_n = '금융,'
    key_m = '전자,'
    n_n = []
    m_m = []
    keyward = []
    for i in range(len(con_lst)):
        n = con_lst[i].count('금융')
        m = con_lst[i].count('전자')
        keyward.append(key_n * n + key_m * m)
        # print(n, m)
    df_con['키워드'] = keyward
    print(df_con)
    df_con.to_csv('C:/pytest/금융규제운영규정_키워드금융전자.csv', encoding='CP949', index=False, header=False)
ex5()