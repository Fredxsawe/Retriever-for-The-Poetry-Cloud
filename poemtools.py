import unicode_hanzi_to_index as index

def number_to_hanzi(number):
    shuzi="〇一二三四五六七八九"
    hanzi=""
    for i in str(number):
        if i in "0123456789":
            hanzi+=shuzi[int(i)]
        else:
            hanzi+=i
    return hanzi

def hanzi_to_number(hanzi):
    num="0123456789"
    shuzi="〇一二三四五六七八九"
    number=0
    for i in str(hanzi):
        if i=='零':
            i='〇'
        if i in num:
            number=number*10+int(i)
        elif i in shuzi:
            for p in range(10):
                if i==shuzi[p]:
                    break
            number=number*10+p
        elif i in "诗云·其":
            continue
        else:
            number=-1
            break
    return number

def clear(poem0):
    punctuation=[",",".","?","!"," ","，","。","？","！","　","\n",
                 ";","；",":","：","\"","“","”","、","《","》"]
    clearpoem=[]
    for i in poem0:
        if not (i in punctuation):
            clearpoem.append(i);
    return clearpoem
    
def check_format(poem0):#检查绝句的格式，若不对则输出0
    clearpoem=clear(poem0)
    count=len(clearpoem)
    form1=0
    tip="正常"
    if count==20:
        form1=5
    elif count==28:
        form1=7
    else:
        form1=0
        tip="字数不符合要求"
    form=0
    for i in range(count-1):#检查是否全篇重复字
        if clearpoem[i+1]!=clearpoem[i]:
            form=form1
            break
    if form1!=0 and form==0:
        tip="诗云中没有所有字一样的诗"
    for i in clearpoem:#检查剩下的字是否都是汉字
        if index.to_index(i)==0:
            form=0
            tip="存在未知字符"
            break
    return form,tip
    
def calculate_title(clearpoem,form):#计算整首诗对应的编号
    title_number=0
    if form==5:#五言绝句
        a=19
    elif form==7:#七言绝句
        title_number=102016**20-102016
        a=27
    index_list=[]
    for zi in clearpoem:
        index_list.append(index.to_index(zi)-1)
    for i in index_list:
        title_number+=i*102016**a
        a-=1
    title_number-=index_list[0]#去除全篇重复字的诗的数量
    for i in range(len(index_list)-1):
        if index_list[i+1]==index_list[i]:
            continue
        elif index_list[i+1]<index_list[i]:
            title_number+=1
            break
        else:
            break
    return title_number

def cut(poem,form): #在无标点的诗中加入标点符号和换行
    i=1
    result=''
    while i<=form*4:
        result+=poem[i-1]
        if i==form or i==form*3:
            result+=',\n'
        elif i==form*2:
            result+='。\n'
        elif i==form*4:
            result+='。'
        i+=1
    return result
            

def search_poem(title1):#根据编号生成全诗
    initial_title=title=hanzi_to_number(title1)
    poem=""
    tip=""
    if title<=102016**20-102016 and title>0:
        form=5
        repeat=title//(102016**19)
    elif title>102016**20-102016 and title<=102016**20-102016+102016**28-102017:
        form=7
        repeat=(title-102016**20+102016)//(102016**27)
        title-=102016**20-102016
    else:
        tip="标题不在范围内"
        return poem,tip
    title=title+repeat
    real_index=title
    for d in [-1,0,1]:#试探
        title=real_index+d
        poem=""
        for i in range(form*4):
            poem=poem+index.to_hanzi(title//102016**(form*4-i-1)+1)
            title=title%(102016**(form*4-i-1))
        if calculate_title(poem,form)==initial_title:
            return cut(poem,form),tip
    tip="没找到"
    poem=""
    return poem,tip
