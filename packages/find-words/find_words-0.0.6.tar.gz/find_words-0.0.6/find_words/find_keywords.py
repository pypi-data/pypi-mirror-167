from typing import Iterable
import pandas as pd

def find_kewords_in_txt(txt_path, keywords) :
    '''
    find_kewords_in_txt(txt_path, keywords) : .txt 파일을 \n단위로 끊어서 kewords 에 해당하는 문장을 찾아 DataFrame으로 반환
    txt_path : str
            - 텍스트 파일 경로
    keywords : str or Iterable
            - 텍스트 파일에서 찾을 키워드
            
    return : pandas.DataFrame
    '''
    
    assert isinstance(txt_path, str)
    
    keyword_list = []
    if isinstance(keywords, str) :
        keyword_list.append(keywords)
    elif isinstance(keywords, Iterable) :
        keyword_list = keywords
    else :
        raise ValueError
    
    filterd_lines = []
    with open(txt_path, "r", encoding = "cp949") as fs :
        
        while True :
            line = fs.readline()
            if not line : 
                break
            
            is_in = False
            line_info = [line.strip()]
            for keyword in keyword_list :
                keyword_count = line.count(keyword)
                line_info.append(keyword_count)
                if keyword_count :
                    is_in = True
                    
            if is_in :
                filterd_lines.append(line_info)

        df = pd.DataFrame(filterd_lines, columns=["내용"] + keyword_list)

        return df