import pandas as pd
import rhinoMorph
import numpy as np

def ex3():
    rn = rhinoMorph.startRhino()
    f = open('C:/pytest/금융규제운영규정.txt')
    lines = f.readlines()
    # for i in range(len(lines)):  # '\n' 가 보기 싫어 삭제하는 코드 다만 다 삭제되면 에러가 뜬다.
    #     lines.remove('\n')
    # 명사 빈 리스트로 만들고 lines의 각 원소별로 명사만 추출후 noun에 추가
    noun = []
    for i in range(len(lines)):
        text_analyzed = rhinoMorph.onlyMorph_list(rn, lines[i], pos=['NNG', 'NNP''NNB', 'NP'])
        for j in range(len(text_analyzed)):
            noun.append(text_analyzed[j])
        print('\n2. 형태소 분석 결과:', text_analyzed)
    noun = pd.DataFrame(noun)  # 데이터프레임으로 만들기 csv로 저장하기위한 전처리
    noun.columns = ['명사']
    verb = []
    for i in range(len(lines)):
        text_analyzed = rhinoMorph.onlyMorph_list(rn, lines[i], pos=['VV', 'VX', 'VCP', 'VCN', 'VA'])
        for j in range(len(text_analyzed)):
            verb.append(text_analyzed[j])
        print('\n2. 형태소 분석 결과:', text_analyzed)
    verb = pd.DataFrame(verb)
    verb.columns = ['동사']
    verb.to_csv('C:/pytest/금융규제운영규정_동사.csv', encoding='CP949',
                index=False)  # encoding 지정안하면 한글 깨짐으로 지정, index=False 지정하는 이유 인덱스도 넘어가는걸 막기위함
    noun.to_csv('금융규제운영규정_명사.csv', encoding='CP949', index=False)
    verb_df = pd.read_csv('C:/pytest/금융규제운영규정_동사.csv', encoding='CP949')
    verb_df.sort_values('동사')
    verb_df_drop_dup = verb_df.drop_duplicates()
    print('동사 정렬 후 중복제거')
    print(verb_df_drop_dup)

    noun_df = pd.read_csv('C:/pytest/금융규제운영규정_명사.csv', encoding='CP949')
    noun_df.sort_values('명사')
    noun_df_drop_dup = noun_df.drop_duplicates()
    print('명사 정렬 후 중복제거')
    print(noun_df_drop_dup)
ex3()