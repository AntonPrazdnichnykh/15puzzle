if __name__ == '__main__':
    from tkinter import *
    from PIL import Image
    from random import *


    def search_frame(list):
        for i in range(len(list)):
            if type(list[i]) == type(Frame()):
                return i


    def shuffler(list):
        a = []
        for j in range(randint(100, 1000)):
            z = search_frame(list)
            for i in range(len(list)):
                if (abs((i // 3) - (z // 3)) == 1) and ((i % 3) == (z % 3)) or (((i // 3) == (z // 3)) and (abs((i % 3) - (z % 3)) == 1)):
                    a.append(i)
            b = choice(a)
            t = list[b]
            list[b] = list[z]
            list[z] = t
        return list

    def do_nothing():
        pass


    def move(list, index_1):
        z = search_frame(list)
        t = list[index_1]
        list[index_1] = list[z]
        list[z] = t
        for i in range(len(list)):
            list[i].grid(row=i // 3, column=i % 3)
        if list != mem:
            z = search_frame(list)
            for i in range(len(list)):
                if i != z:
                    list[i].configure(command=lambda i=i: do_nothing())
            for i in range(len(list)):
                if (abs((i // 3) - (z // 3)) == 1) and ((i % 3) == (z % 3)) or (((i // 3) == (z // 3)) and (abs((i % 3) - (z % 3)) == 1)):
                    list[i].configure(command=lambda i=i: move(list, i))
        else:
            img = PhotoImage(file='8.gif')
            but = Button(root, width=200, height=200, image=img).grid(row=2, column=2)
            root_1 = Tk()
            root_1.geometry('700x50')
            lab = Label(root_1,  text='Congratulations!!! You are winner!!!', width=700, height=50, bg='lightgrey', fg='green', font='arial 14').pack()
            root_1.mainloop()

    for i in range(9):
        img = Image.open(str(i)+'.gif')
        newimg = img.resize((200, 200))
        newimg.save(str(i)+'.gif')
    root = Tk()
    root.geometry('620x620')
    buts = []
    imgs = [0 for i in range(9)]
    for i in range(8):
        imgs[i] = PhotoImage(file=str(i)+'.gif')

    for i in range(len(imgs)):
        if imgs[i] != 0:
            but = Button(root, width=200, height=200, image=imgs[i], command=lambda i=i: do_nothing())
            buts.append(but)
        else:
            but = Frame(root, width=28, height=13)
            buts.append(but)
    mem = buts.copy()
    shuffler(buts)
    for i in range(len(buts)):
        buts[i].grid(row=i // 3, column=i % 3)

    for i in range(len(buts)):
        z = search_frame(buts)
        if (abs((i // 3) - (z // 3)) == 1) and ((i % 3) - (z % 3) == 0) or (((i // 3) - (z // 3) == 0) and (abs((i % 3) - (z % 3)) == 1)):
            buts[i].configure(command=lambda i=i: move(buts, i))

    root.mainloop()




