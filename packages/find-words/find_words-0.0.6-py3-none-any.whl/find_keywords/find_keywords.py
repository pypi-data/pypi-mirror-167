from typing import Iterable
import pandas as pd

def find_kewords_in_txt(txt_path, keywords) :
    '''
    find_kewords_in_txt(txt_path, keywords) : .txt 파일을 \n단위로 끊어서 kewords 에 해당하는 문장을 찾아 DataFrame으로 반환
    txt_path : str
            - 텍스트 파일 경로
    keywords : str or Iterable
            - 텍스트 파일에서 찾을 키워드
    '''
    lines = []
    with open(txt_path, "r", encoding = "cp949") as fs :
        line = fs.read()
        lines = line.split("\n")

    keyword_list = []
    if isinstance(keywords, str) :
        keyword_list.append(keywords)
    elif isinstance(keywords, Iterable) :
        keyword_list = keywords
    print(keyword_list)
    filterd_lines = []
    for l in lines :
        l = l.strip()
        
        line_info = [l]
        is_in = False
        for keyword in keyword_list :
            keyword_count = l.count(keyword)
            line_info.append(keyword_count)
            if keyword_count :
                is_in = True
        
        if is_in :
            filterd_lines.append(line_info)

    df = pd.DataFrame(filterd_lines, columns=["내용"] + keyword_list)

    return df