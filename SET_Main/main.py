# created by Vincent Li on 2022/03/31

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random

ansArr = []
now_page = 0

def run_algorithm():
    isOKToAdd = True
    lenOfAnsArr = 0

    mainArr = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
    numArr = []
    colorArr = []
    shapeArr = []
    shadingArr = []
    cardArr = []
    setArr = []
    tempArr = []

    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                for l in range(0, 9):

                    for num in range(0, 3):
                        numArr.append(mainArr[i][num])

                    for color in range(0, 3):
                        colorArr.append(mainArr[j][color])

                    for shape in range(0, 3):
                        shapeArr.append(mainArr[k][shape])

                    for shading in range(0, 3):
                        shadingArr.append(mainArr[l][shading])

    for i in range(0, 19683):
        temp = numArr[i] * 1000 + colorArr[i] * 100 + shapeArr[i] * 10 + shadingArr[i]
        cardArr.append(temp)

    for i in range(0, 19683, 3):

        for j in range(0, 3):
            tempArr.append(cardArr[i + j])

        setArr.append(tempArr)
        tempArr = []



    for i in range(0, 6561):
        tempSet = set(setArr[i])
        tempArr = list(tempSet.intersection(set(card_set_list)))

        if len(tempArr) == 3:

            for i in range(0, lenOfAnsArr):


                if sorted(tempArr) == sorted(ansArr[i]) or len(set(tempArr).intersection(set(ansArr[i]))) == 3:
                    isOKToAdd = False

            if isOKToAdd:
                ansArr.append(sorted(tempArr))
                lenOfAnsArr += 1

            isOKToAdd = True

    print("ansArr = ", ansArr)






# 基礎變數、陣列和字典設定
display_indexes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
display_unmarked_imgs = []
display_marked_imgs = []
selected_index = -1
id_to_index_dict = {}
card_set_dict = {}
card_set_list = []
hint_id = 0  #hint_id是進入hint頁面要顯示的卡牌id

# 設定背景顏色
bg_gray = '#eaeaea'


# tkinter函式定義
def all_imgs_unmarked():
    for i, j in zip(buttons, range(len(buttons))):
        i.config(image=display_unmarked_imgs[display_indexes[j]])


def id_to_index(id):
    return id_to_index_dict[id]


def button_pressed(index):
    global selected_index
    selected_index = index
    all_imgs_unmarked()
    buttons[index].config(image=display_marked_imgs[display_indexes[index]])


def button_ok_pressed():
    global selected_index
    global display_indexes
    if selected_index != -1 and number_combo.get() != "" and color_combo.get() != "" and shape_combo.get() != "" and shading_combo.get() != "":

        card_id = 0000
        if number_combo.get() == "1個":
            card_id += 1000
        elif number_combo.get() == "2個":
            card_id += 2000
        elif number_combo.get() == "3個":
            card_id += 3000

        if color_combo.get() == "紅色":
            card_id += 100
        elif color_combo.get() == "綠色":
            card_id += 200
        elif color_combo.get() == "紫色":
            card_id += 300

        if shape_combo.get() == "菱形":
            card_id += 10
        elif shape_combo.get() == "圓角矩形":
            card_id += 20
        elif shape_combo.get() == "波浪形":
            card_id += 30

        if shading_combo.get() == "實心":
            card_id += 1
        elif shading_combo.get() == "線條":
            card_id += 2
        elif shading_combo.get() == "空心":
            card_id += 3

        card_set_dict[selected_index] = card_id
        display_indexes[selected_index] = id_to_index_dict[str(card_id)]
        all_imgs_unmarked()
        buttons[selected_index].config(image=display_marked_imgs[id_to_index_dict[str(card_id)]])



def button_go_pressed():
    card_set_list.clear()
    ansArr.clear()
    if len(card_set_dict) == 9:

        for i in range(9):
            card_set_list.append(card_set_dict[i])

    else:
        print("Input isn't complete! Please check again!")
        return
    print(card_set_list)
    run_algorithm()
    created_new_win()

def game_mode_pressed():
    card_set_list.clear()
    ansArr.clear()
    card_set_dict.clear()
    all_imgs_unmarked()
    index = 0  #控制字典的key
    dict_value = []  #為了可以使用in函式所以設的list


    while len(ansArr) < 3:
        card_set_list.clear()
        ansArr.clear()
        card_set_dict.clear()
        all_imgs_unmarked()
        index = 0  # 控制字典的key
        dict_value = []  # 為了可以使用in函式所以設的list

        while len(card_set_dict) != 9:
            temp_id = random.randint(1, 3) * 1000 + random.randint(1, 3) * 100 + random.randint(1,3) * 10 + random.randint(1, 3)

            if temp_id not in dict_value:
                card_set_dict[index] = temp_id
                dict_value.append(temp_id)
                index += 1

        for i in range(9):
            card_set_list.append(card_set_dict[i])

        run_algorithm()


    for i in range(9):
        display_indexes[i] = id_to_index_dict[str(card_set_dict[i])]
        buttons[i].config(image=display_unmarked_imgs[id_to_index_dict[str(card_set_dict[i])]])

def hint_pressed():
    global hint_id
    card_set_list.clear()
    ansArr.clear()
    if len(card_set_dict) == 9:

        for i in range(9):
            card_set_list.append(card_set_dict[i])

    else:
        print("Input isn't complete! Please check again!")
        return
    print(card_set_list)
    run_algorithm()

    if len(ansArr) != 0:
        temp_list = random.sample(ansArr, 1)
        random_index = random.randint(0, 2)
        hint_id = temp_list[0][random_index]  #hint_id是進入hint頁面要顯示的卡牌id
        print("hint_id", hint_id)
        created_new_win(hint_id)
    else:
        created_new_win()







def created_new_win(id=0):
    global ansArr
    global now_page
    global hint_id
    now_page = 0

    win.attributes("-topmost", False)
    result_win = tk.Toplevel(win)
    if id == 0:
        result_win.title("SET!")
    else:
        result_win.title("來點提示")
    result_win.geometry("1200x970+58+0")
    result_win.resizable(False, False)
    result_win.config(background=bg_gray)
    result_win.attributes("-alpha", 0.9)
    result_win.attributes("-topmost", True)

    position_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    images = []


    def show_ans():
        global now_page
        print("now_page = ", now_page)
        for i in range(9):
            if id == 0:
                if len(ansArr) != 0:
                    if card_set_dict[i] in ansArr[now_page]:
                        new_img = tk.Label(result_win,image=display_marked_imgs[id_to_index_dict[str(card_set_dict[i])]])
                    else:
                        new_img = tk.Label(result_win,image=display_unmarked_imgs[id_to_index_dict[str(card_set_dict[i])]])

                else:
                    new_img = tk.Label(result_win,image=display_unmarked_imgs[id_to_index_dict[str(card_set_dict[i])]])

            else:
                if card_set_dict[i] == hint_id:
                    new_img = tk.Label(result_win, image=display_marked_imgs[id_to_index_dict[str(card_set_dict[i])]])
                else:
                    new_img = tk.Label(result_win,image=display_unmarked_imgs[id_to_index_dict[str(card_set_dict[i])]])

            new_img.grid(row=position_list[i][0], column=position_list[i][1])
            images.append(new_img)
    show_ans()

    def change_page(index):
        global now_page
        if index == -1 and now_page != 0 or index == 1 and now_page != len(ansArr) - 1:
            now_page += index
            ans_counter_img['text'] = str(now_page + 1) + "/" + str(len(ansArr))

            show_ans()


    if id == 0:
        btn_pgup = tk.Button(result_win, image=UIimage_left, command=lambda idk=-1: change_page(idk), background="red")
        btn_pgup.place(x=70,y=890,anchor=tk.CENTER)

        btn_pgdn = tk.Button(result_win, image=UIimage_right, command=lambda idk=1: change_page(idk))
        btn_pgdn.place(x=450,y=890,anchor=tk.CENTER)

        ans_counter_img = tk.Label(result_win, text=str(now_page + 1) + "/" + str(len(ansArr)), font=("System", 40))
        ans_counter_img.place(x=260, y=890, anchor=tk.CENTER)
    else:
        ans_counter_img = tk.Label(result_win, text="總共有" + str(len(ansArr)) + "組SET！", font=("System", 40))
        ans_counter_img.place(x=260, y=890, anchor=tk.CENTER)







# window init
win = tk.Tk()
win.title("SET桌遊")
win.geometry("1200x970+58+0")
win.resizable(False, False)
win.config(background=bg_gray)
win.attributes("-alpha", 0.9)
win.attributes("-topmost", True)

# 0000.jpg 和 0000M.jpg初始化
image = Image.open("SET_icons/0000.jpg")
image = image.resize((173, 266))
image1 = ImageTk.PhotoImage(image)

image = Image.open("SET_icons/0000M.jpg")
image = image.resize((173, 266))
image2 = ImageTk.PhotoImage(image)

# 新增圖片List
image = Image.open("SET_icons/0000.jpg")
image = image.resize((173, 266))
display_unmarked_imgs.append(ImageTk.PhotoImage(image))
n = 1
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                file_path = "SET_icons/" + str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1) + ".jpg"
                image = Image.open(file_path)
                image = image.resize((173, 266))
                display_unmarked_imgs.append(ImageTk.PhotoImage(image))

                id_to_index_dict[str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1)] = n
                n += 1

image = Image.open("SET_icons/0000M.jpg")
image = image.resize((173, 266))
display_marked_imgs.append(ImageTk.PhotoImage(image))
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                file_path = "SET_icons/" + str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1) + "M.jpg"
                image = Image.open(file_path)
                image = image.resize((173, 266))
                display_marked_imgs.append(ImageTk.PhotoImage(image))

image = Image.open("UI_icons/left.png")
UIimage_left = ImageTk.PhotoImage(image.resize((100, 100)))

image = Image.open("UI_icons/right.png")
UIimage_right = ImageTk.PhotoImage(image.resize((100, 100)))

# 創建按鈕
position_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
buttons = []

for i in range(9):
    new_btn = tk.Button(image=image1, command = lambda index = i: button_pressed(index), width=173, height=266, borderwidth=0)
    new_btn.grid(row=position_list[i][0], column=position_list[i][1])
    buttons.append(new_btn)



image = Image.open("UI_icons/ok.png")
UIimage_ok = ImageTk.PhotoImage(image.resize((450, 105)))
btn_ok = tk.Button(win, image=UIimage_ok, command=button_ok_pressed, borderwidth=0)
btn_ok.place(x=800, y=397, anchor=tk.CENTER)

image = Image.open("UI_icons/game.png")
UIimage_game = ImageTk.PhotoImage(image.resize((450, 105)))
btn_game_mode = tk.Button(win, image=UIimage_game, command=game_mode_pressed)
btn_game_mode.place(x=800, y=517, anchor=tk.CENTER)

image = Image.open("UI_icons/hint.png")
UIimage_hint = ImageTk.PhotoImage(image.resize((450, 105)))
btn_hint = tk.Button(win, image=UIimage_hint, command=hint_pressed)
btn_hint.place(x=800, y=637, anchor=tk.CENTER)

image = Image.open("UI_icons/set.png")
UIimage_set = ImageTk.PhotoImage(image.resize((450, 105)))
btn_go = tk.Button(win, image=UIimage_set,command=button_go_pressed)
btn_go.place(x=800, y=757, anchor=tk.CENTER)

#創建labels
image = Image.open("UI_icons/數量.png")
UIimage_num = ImageTk.PhotoImage(image.resize((151, 50)))
lb_num = tk.Label(win, image=UIimage_num)
lb_num.place(x=649, y=50, anchor=tk.CENTER)

image = Image.open("UI_icons/顏色.png")
UIimage_color = ImageTk.PhotoImage(image.resize((151, 50)))
lb_color = tk.Label(win, image=UIimage_color)
lb_color.place(x=869, y=50, anchor=tk.CENTER)

image = Image.open("UI_icons/形狀.png")
UIimage_shape = ImageTk.PhotoImage(image.resize((151, 50)))
lb_shape = tk.Label(win, image=UIimage_shape)
lb_shape.place(x=649, y=200, anchor=tk.CENTER)
#
image = Image.open("UI_icons/紋路.png")
UIimage_shading = ImageTk.PhotoImage(image.resize((151, 50)))
lb_shading = tk.Label(win, image=UIimage_shading)
lb_shading.place(x=869, y=200, anchor=tk.CENTER)

# 創建下拉式選單
number_combo = ttk.Combobox(win, values=["1個", "2個", "3個"], state='readonly', width=15)
number_combo.place(x=570, y=80)

color_combo = ttk.Combobox(win, values=["紅色", "綠色", "紫色"], state='readonly', width=15)
color_combo.place(x=790, y=80)

shape_combo = ttk.Combobox(win, values=["菱形", "圓角矩形", "波浪形"], state='readonly', width=15)
shape_combo.place(x=570, y=230)

shading_combo = ttk.Combobox(win, values=["實心", "線條", "空心"], state='readonly', width=15)
shading_combo.place(x=790, y=230)

win.mainloop()
