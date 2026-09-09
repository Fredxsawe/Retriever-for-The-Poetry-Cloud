from poemtools import *
from unicode_hanzi_to_index import *
import tkinter as tk

window=tk.Tk()
window.title("诗云检索器")
window.geometry("500x600")
mode=tk.IntVar(value=0)
output=''
l1=tk.Label(window,
            bg='yellow',
            text='当前模式：正文->标题',
            font=('',18),
            width=20,height=1)
l1.pack(anchor='nw',padx=10,pady=10)
tk.Label(window,
            text='选择模式：',
            font=('',15)).pack(anchor='nw',padx=10)
frame0=tk.Frame(window)
frame0.pack(anchor='nw',side='top',padx=10)

frame2=tk.Frame(window, #输出框
                width=41,
                height=6,
                padx=10,pady=10)
scroll_bar2=tk.Scrollbar(frame2)
text_box2 = tk.Text(frame2,
                    width=40,
                    height=9,
                    font=('',15),
                    fg='black',
                    yscrollcommand=scroll_bar2.set,
                    state=tk.DISABLED)

def number():
    global output
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    output=str(hanzi_to_number(output))
    text_box2.insert(tk.END,output)
    text_box2.config(state=tk.DISABLED)
def hanzi():
    global output
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    output=number_to_hanzi(output)
    if output[0:4]!="诗云·其":
        output="诗云·其"+output
    text_box2.insert(tk.END,output)
    text_box2.config(state=tk.DISABLED)

frame4=tk.Frame(window)
number_button=tk.Button(frame4, #正文->标题模式输出结果转为阿拉伯数字
                        text="转为数字",
                        font=('',15),
                        command=number)
hanzi_button=tk.Button(frame4, #正文->标题模式输出结果转为汉字数字
                       text="转为汉字",
                       font=('',15),
                       command=hanzi)

def switch0():
    l1.config(text='当前模式：正文->标题')
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    text_box2.config(state=tk.DISABLED)
    number_button.pack(side='left')
    hanzi_button.pack(side='left',padx=20)
def switch1():
    l1.config(text='当前模式：标题->正文')
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    text_box2.config(state=tk.DISABLED)
    number_button.pack_forget()
    hanzi_button.pack_forget()
mode_choose0=tk.Radiobutton(frame0,
                            text='正文->标题',
                            font=('',15),
                            variable=mode,
                            value=0,
                            command=switch0)
mode_choose0.pack(anchor='nw',side='left')
mode_choose1=tk.Radiobutton(frame0,
                            text='标题->正文',
                            font=('',15),
                            variable=mode,
                            value=1,
                            command=switch1)
mode_choose1.pack(anchor='nw',side='left',padx=20)

tk.Label(window,
         text='输入：',
         font=('',15)).pack(anchor='nw',padx=10)

frame1=tk.Frame(window, #输入框
                width=41,
                height=6,
                padx=10)
frame1.pack(anchor='nw',side='top')
scroll_bar1=tk.Scrollbar(frame1)
scroll_bar1.pack(side=tk.RIGHT, fill=tk.Y)
text_box1 = tk.Text(frame1,
                    width=40,
                    height=6,
                    font=('',15),
                    yscrollcommand=scroll_bar1.set)
text_box1.pack(anchor='nw')
scroll_bar1.config(command=text_box1.yview)

def generate():
    global output,textcolor
    content = text_box1.get("1.0", tk.END).strip()
    if mode.get()==0:
        poem=clear(content)
        poem_format,tip=check_format(poem)
        if poem_format==0: #格式错误，返回报错
            output=tip
            text_box2.config(fg='red')
        else:
            title=calculate_title(poem,poem_format)
            output="诗云·其"+number_to_hanzi(title)
            text_box2.config(fg='black')
    elif mode.get()==1:
        title=content
        poem,tip=search_poem(title)
        if tip!='': #格式错误，返回报错
            text_box2.config(fg='red')
            output=tip
        else:
            output=poem
            text_box2.config(fg='black')
    text_box2.config(state=tk.NORMAL,)
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END,output)
    text_box2.config(state=tk.DISABLED)

def inform():
    text_box2.config(state=tk.NORMAL,fg='blue')
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END,"正文->标题模式：只能输入五言绝句或七言绝句；只输入正文，不能附带标题；"
                     "可以带换行和标点符号。\n标题->正文模式：可直接输入阿拉伯数字或汉字数字，但输入"
                     "汉字数字时不能带单位（如十、百、千、万等）；可带有“诗云·其”前缀。\n"
                     "关注作者谢谢喵：https://space.bilibili.com/671390377")
    text_box2.config(state=tk.DISABLED)

frame3=tk.Frame(window)
frame3.pack(anchor='nw',padx=10,pady=10)
search_button=tk.Button(frame3,
                        text=" 查询 ",
                        font=('',15),
                        command=generate)
search_button.pack(side='left')
inform_button=tk.Button(frame3,
                        text="查看规则",
                        font=('',15),
                        command=inform)
inform_button.pack(side='left',padx=20)

tk.Label(window,
         text='结果：',
         font=('',15)).pack(anchor='nw',padx=10)

frame2.pack(anchor='nw',side='top')
scroll_bar2.pack(side=tk.RIGHT, fill=tk.Y)
text_box2.pack(anchor='nw')
scroll_bar2.config(command=text_box2.yview)

frame4.pack(anchor='nw',padx=10,pady=10)
number_button.pack(side='left')
hanzi_button.pack(side='left',padx=20)

window.mainloop()
