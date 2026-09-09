#计算一个汉字在unicode中是第几个汉字

# 定义Unicode官方标准汉字的编码区间，共102016个
# 格式：(起始码点, 结束码点)，覆盖所有标准汉字，排除非汉字字符
HANZI_UNICODE_RANGES = [
    (0x4E00, 0x9FFF),    # CJK 基本汉字区（日常使用的99%汉字都在这里）
    (0x3400, 0x4DBF),    # CJK 扩展A区
    (0x20000, 0x2A6DF),  # CJK 扩展B区
    (0x2A700, 0x2B73F),  # CJK 扩展C区
    (0x2B740, 0x2B81F),  # CJK 扩展D区
    (0x2B820, 0x2CEAF),  # CJK 扩展E区
    (0x2CEB0, 0x2EBEF),  # CJK 扩展F区
    (0x30000, 0x3134F),  # G
    (0x31350, 0x323AF),  # H
    (0x2EBF0, 0x2EE5F),  # I
    (0x323B0, 0x3347F)   # J
]

def to_index(char: str) -> int:
    """
    核心函数：单个字符 → 汉字编号x
    :param char: 输入的单个字符
    :return: 汉字返回第x个编号，非汉字/多字符返回0
    """
    #更换顺序，使结果符合《诗云》小说原文
    if char=="一":
        char="啊"
    elif char=="丁":
        char="唉"
    elif char=="啊":
        char="一"
    elif char=="唉":
        char="丁"
        
    # 获取字符的Unicode码点（十进制数值）
    char_code = ord(char)
    total_count = 0  # 累计：前面所有区间的汉字总数量
    
    # 遍历所有汉字区间，判断并计算编号
    for start, end in HANZI_UNICODE_RANGES:
        if start <= char_code <= end:
            return total_count + (char_code - start + 1)
        total_count += end - start + 1
    
    # 不在任何汉字区间，返回0
    return 0

def to_hanzi(x: int) -> str:
    rem = x
    char=''
    for s, e in HANZI_UNICODE_RANGES:
        length = e - s + 1
        if rem > length:
            rem -= length
        else:
            char=chr(s + rem - 1)
            break
    if char=="一":
        char="啊"
    elif char=="丁":
        char="唉"
    elif char=="啊":
        char="一"
    elif char=="唉":
        char="丁"
    return char

# 调试
if __name__ == "__main__":
    print("Unicode汉字转编号")
    user_input = input("输入汉字：")
    if len(user_input)!=1:
        print("输入错误")
        exit()
    result = to_index(user_input)
    print(f"\n输入字符：{user_input}")
    print(f"Unicode汉字编号 x = {result}")
