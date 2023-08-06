import pandas as pd
pd.set_option('mode.chained_assignment',  None)

def find(obj_file, dst_file, find_words):
    '''
    find: 지정 파일로부터 특정단어를 찾아 dataframe형태로 출력해주는 모듈
    obj_file: 목적 대상 파일(txt 파일 권장, 인코딩 utf-8)
    dst_file: csv로 출력해 저장할 파일의 이름(출력을 안할때는 공백("")으로 할 것)
    find_words: 찾을 단어 list 입력
    ex) find_words_from_file('input.txt', './ouput.csv', ['word1', 'word2'])

    return 값: 결과 dataframe

    ---
    dependency: pandas
    '''
    with open(obj_file) as f:
        data = f.read()
    refine_data = data.strip().replace("\n\n", "\n").replace("  ", " ")
    sentences = [i.strip() for i in refine_data.split('\n')]
    sentences_include_df = pd.DataFrame(sentences, columns=['문장'])
    for word in find_words:
        sentences_include_df[word]=""
        for n, i in enumerate(sentences):
            if(word in i):
                sentences_include_df.iloc[n:n+1,:].loc[:,word]="True"
            else:
                sentences_include_df.iloc[n:n+1,:].loc[:,word]="False"
    if dst_file != "":
        sentences_include_df.to_csv(dst_file, index=False)
    return sentences_include_df
