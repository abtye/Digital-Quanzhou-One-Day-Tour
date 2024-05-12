import tkinter as tk
# 这个文件里只有base64格式的数据，非常大，不要打开
import assets_base64
# 剧情
book = ["（2030年的暑假到了，小鹿到表哥小猴子的家乡——泉州做客） ", "小鹿：哇，这是什么？ "]
book += ["小猴子：这是浮粿，尝一尝吧 ","小鹿：可是我上火了"]
book += ["小猴子：没关系，现在有虚拟食物，可以只尝味道"]
book += ["小鹿：表哥，我想去清源山玩，可是暑假人会不会很多啊"]
book += ["小猴子：不用担心，现在可以VR旅游了！", "小鹿：哇！清源山真美！"]
book += ["小猴子：看，这是老君岩，它是中国最大的道教石雕", "（下午）"]
book += ["小猴子：今天我们去参观开元寺吧", "小鹿：我是个路痴……会不会迷路啊？"]
book += ["小猴子：不用担心，现在有AR导航", " "]

print("\033[31m报错是因为按钮点太快了\033[0m")

# 创建窗口
window = tk.Tk()
window.title("数字泉州一日游")
# 配置窗口，默认最大化，最小2/3
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("{}x{}".format(screen_width, screen_height))
window.minsize(screen_width*2//3, screen_height*2//3)
window.config(bg="#333333")

background_image = tk.PhotoImage(data=assets_base64.city)
# 创建标签，并设置背景图片
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0)

# 侧边对话
sidebar = tk.Label(window, bg="#333333", fg="white")
sidebar.config(width=20, font=(None, 20), anchor="nw")
sidebar.pack(side=tk.RIGHT, fill="y")

# 自动换行
width1 = sidebar.winfo_reqwidth()
sidebar.config(wraplength=width1)

page = 0
# 更新文字的函数
def talk():
    global text, count, sidebar, book, page

    story = book[page]
    sidebar.config(text="")
    text += story[count]
    sidebar.config(text=text)

    # 更新计数器
    count += 1
    if count < len(story):  # 设置循环次数
        window.after(50, talk)  # 设置每隔一秒执行一次talk函数
    return


# 初始化文字和计数器
text = ""
count = 0
talk()
fire_cake_label = None

def task1():
    global fire_cake_label
    fire_cake_img =  tk.PhotoImage(data=assets_base64.fire_cake)
    fire_cake_label = tk.Label(window, image=fire_cake_img)
    fire_cake_label.place(x=500, y=0)
    window.mainloop()
    return

def task2():
    global fire_cake_label

    fire_cake_label.destroy()
    window.mainloop()

def task3():
    global deer_label, background_image, background_label, monkey_label
    deer_vr_img = tk.PhotoImage(data=assets_base64.deer_vr)
    deer_label.config(image=deer_vr_img)
    deer_label.place(x=20, y=250)
    # 加载图片
    background_image = tk.PhotoImage(data=assets_base64.mount)
    # 创建标签，并设置背景图片
    background_label.config(image=background_image)
    monkey_label.destroy()

    window.mainloop()
    return

def task4():
    global background_label, deer_label
    deer_img = tk.PhotoImage(data=assets_base64.deer)
    deer_label.config(image=deer_img)
    monkey_img = tk.PhotoImage(data=assets_base64.monkey)
    monkey_label = tk.Label(window, image=monkey_img)
    monkey_label.place(x=400, y=250)
    background_image = tk.PhotoImage(data=assets_base64.city)
    # 创建标签，并设置背景图片
    background_label.config(image=background_image)
    window.mainloop()

def task5():
    global window
    for widget in window.winfo_children():
        widget.destroy()
    ar()

task = ["None", "task1()", "None", "None", "None", "task2()", "None","task3()"]
task += ["None", "task4()", "None", "None", "None", "task5()"]

def nextPart():
    global page, story, text, count, book, task, button
    count = 0
    if page == len(book) - 1:
        return
    else:
        page += 1
        story = book[page]
        text = ""
        talk()
        try:
            eval(task[page])
        finally:
            pass


def ar():
    global count,window,deer_label, header
    background_image = tk.PhotoImage(data=assets_base64.road)
    # 创建标签，并设置背景图片
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0)

    header = tk.Label(window, text="跟随AR导航至开元寺")
    header.config(font=(None, 20))
    header.config(height=1, fg="white", bg="#222222")
    header.pack(fill="x", anchor="nw")

    deer_img = tk.PhotoImage(data=assets_base64.mini_deer)
    deer_label = tk.Label(window, image=deer_img)
    deer_label.place(x=970, y=140, anchor="nw")
    count = 0
    a()
    window.mainloop()

def d():
    global count, deer_label, header, window
    count += 1
    if count <= 100:
        deer_label.place(y=420-count*2.8)
        window.after(20, d)
    else:
        header.config(text="完成！")
        button1 = tk.Button(window, text="退出")
        button1.config(font=(None, 20), command=lambda: window.destroy())
        button1.config(bg="#3d70df", fg="white")
        button1.config(padx=10, pady=10)
        button1.place(x=500, y=500)

def c():
    global count, deer_label
    count += 1
    if count <= 100:
        deer_label.place(x=720+count*2.5, y=580-count*1.6)
        window.after(20, c)
    else:
        count = 0
        d()

def b():
    global count, deer_label
    count += 1
    if count <= 80:
        deer_label.place(x=576+count*1.8, y=300+count*3.5)
        window.after(20, b)
    else:
        count = 0
        c()

def a():
    global count, deer_label
    count += 1
    if count <= 120:
        deer_label.place(x=count*4.8, y=600-count*2.5)
        window.after(20, a)
    else:
        count = 0
        b()


button = tk.Button(window, text="继续",command=nextPart, font=(None, 26))
button.config(bg="#3d70df", fg="white", width=5, height=1)
# 将按钮相对定位于右下角
button.place(relx=0.6, rely=0.8)

deer_img = tk.PhotoImage(data=assets_base64.deer)
deer_label = tk.Label(window, image=deer_img)
deer_label.place(x=20, y=250)

monkey_img = tk.PhotoImage(data=assets_base64.monkey)
monkey_label = tk.Label(window, image=monkey_img)
monkey_label.place(x=400, y=250)

window.mainloop()
