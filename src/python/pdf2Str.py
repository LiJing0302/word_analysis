import pdfplumber


def pdfToTxt():
    with pdfplumber.open(r'./test.pdf') as pdf:
        for page in pdf.pages:
            text = page.extract_text()  # 提取当前页文本
            txt = open('./test.txt', mode='a', encoding='utf-8')
            txt.write(text+'\n')
