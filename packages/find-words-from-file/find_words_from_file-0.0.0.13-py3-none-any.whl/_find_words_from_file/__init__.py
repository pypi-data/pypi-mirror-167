from .find_words_from_file import find

__doc__='''
    find(): 지정 파일로부터 특정단어를 찾아 dataframe형태로 출력해주는 모듈
    obj_file: 목적 대상 파일(txt 파일 권장, 인코딩 utf-8)
    dst_file: csv로 출력해 저장할 파일의 이름(출력을 안할때는 공백("")으로 할 것)
    find_words: 찾을 단어 list 입력
    ex) find_words_from_file('input.txt', './ouput.csv', ['word1', 'word2'])

    return 값: 결과 dataframe

    ---
    dependency: pandas
'''