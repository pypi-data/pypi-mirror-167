import pandas as pd
import rhinoMorph
import numpy as np

def ex4():
    rn = rhinoMorph.startRhino()
    f = open('C:/pytest/금융규제운영규정.txt')
    lines = f.readlines()
    # for i in range(len(lines)):  # '\n' 가 보기 싫어 삭제하는 코드 다만 다 삭제되면 에러가 뜬다.
    #     lines.remove('\n')
    text = []

    for each_line in lines:
        if each_line.find('금융') > 0:
            # print(each_line)
            text.append(each_line)
        else:
            pass
    text = pd.DataFrame(text)
    text.to_csv('C:/pytest/금융규제운영규정_금융.csv', encoding='CP949', index=False)

    data = pd.read_csv('C:/pytest/금융규제운영규정_금융.csv', encoding='CP949')
    print(data)
ex4()