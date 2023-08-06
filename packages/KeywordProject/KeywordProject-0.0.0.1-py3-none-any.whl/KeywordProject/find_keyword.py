def find_keyword(text_list, keyword):
    '''
    :param text_list: 문자열이 리스트 형태로 모아져 있는 거
    :param keyword: 뽑아내고자 하는 문자열
    :return: 문자열과 발견된 키워드 개수가 저장된 데이터프레임 형태
    현재 디렉토리 안에 바로 csv로 저장됨
    '''
    keyword_list = []
    keyword_num = 0
    keyword_num_list = []
    keyword_df = []
    for words in text_list:
        if keyword in words:
            keyword_list.append(words)
        keyword_num = len(words.split(keyword)) - 1
        keyword_num_list.append((keyword + ',') * keyword_num)

    keyword_df = pd.concat([pd.DataFrame(keyword_list), pd.DataFrame(keyword_num_list)], axis=1)
    keyword_df.to_csv('키워드분류.csv', index=False, encoding='cp949')
    return keyword_df