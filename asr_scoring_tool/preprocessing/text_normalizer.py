import re
import string
import opencc  # 繁简体转换库

# 初始化繁转简转换器
converter = opencc.OpenCC('t2s.json')  # Traditional to Simplified

def normalize_text(text: str, lang: str ) -> str:
    """
    文本标准化：统一大小写、去除标点、数字标准化、繁简体转换
    :param text: 原始文本
    :param lang: 语言类型 ("en" 或 "zh")
    :return: 标准化后的文本
    """
    # 统一小写（英文）
    if lang == "en":
        text = text.lower()

    # 去除标点
    text = text.translate(str.maketrans("", "", string.punctuation))

    if lang == "zh":
        # 繁体转简体
        text = converter.convert(text)
        text = text.replace(" ", "").replace("\u3000", "")
        # 数字标准化：阿拉伯数字转中文数字
        # 如果你希望保留阿拉伯数字，这部分可以跳过
        text = normalize_chinese_numbers(text)

    else:  # 英文或其他
        # 数字标准化：用 "number" 替换数字
        text = re.sub(r"\d+", "number", text)

    return text.strip()


def normalize_chinese_numbers(text: str) -> str:
    """
    将文本中的阿拉伯数字转换为中文数字
    """
    digits = {
        '0': '零', '1': '一', '2': '二', '3': '三', '4': '四',
        '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'
    }
    for d, ch in digits.items():
        text = text.replace(d, ch)
    return text