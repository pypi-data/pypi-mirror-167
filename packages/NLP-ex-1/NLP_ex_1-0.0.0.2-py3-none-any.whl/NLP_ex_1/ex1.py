# RHINO 시작
import rhinoMorph

def ex1():
    rn = rhinoMorph.startRhino()
    text = '''박윤규 과학기술정보통신부(과기정통부) 제2차관은 "국가데이터정책위는 데이터와 신산업 분야에서 13개 규제개선 과제를 발굴하는 등 
    기업의 오랜 요구에 대해 과감한 혁신으로 화답해 출범하고자 한다"고 설명했다.
    '''
    # 사용 4 : 전체형태소, 품사정보도 가져오기
    morphs, poses = rhinoMorph.wholeResult_list(rn, text)
    print('\n4. 형태소 분석 결과:')
    print('morphs:', morphs)
    print('poses:', poses)

ex1()