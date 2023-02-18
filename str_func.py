def task2(text):
    '''Делает заглавными всю строку'''
    return text.upper()

def upper_first(text):
    '''Делает заглавными первые буквы каждого слова в строке, поступившей на вход функции'''
    out_text = ""
    out_text += text[0].upper()
    for i in range(1,len(text)):
        if text[i-1] == " ":
            out_text += text[i].upper()
        else:
            out_text += text[i]
    return out_text