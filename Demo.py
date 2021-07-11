from tkinter import *
from tkinter import font
from tkinter import messagebox
from os import path
from os import remove
import tkinter as tk
from tkinter import TOP, ttk, messagebox
import tkinter.font as tkFont
import tkinter.messagebox as msgbox


class StartPage:
    def __init__(self):
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('酒店信息管理系统')
        self.window.geometry('300x320')
        label = tk.Label(self.window, text="酒店信息管理系统", font=tkFont.Font(size=20))
        label.pack(pady=70)
        self.b1 = tk.Button(self.window, text="管理员登录", font=tkFont.Font(size=14),
                            command=lambda: DengLv(),
                            width=20, fg='white', bg='gray', activebackground='black',
                            activeforeground='white').pack()

        self.b2 = tk.Button(self.window, text='退出系统', font=tkFont.Font(size=14), command=self.window.destroy,
                            width=20, fg='white', bg='gray', activebackground='black',
                            activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环


# 登录界面
class DengLv:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("酒店管理系统")
        # self.conn = sqlite3.connect('guest.db')
        self.window.geometry("400x350+%d+%d" % (300, 400))
        # 创建用户名标签
        l1 = tk.Label(self.window, text='管理员：', font=tkFont.Font(size=14)).pack(pady=20)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()
        l2 = tk.Label(self.window, text='密码：', font=tkFont.Font(size=14)).pack(pady=20)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()
        self.buttonb1 = tk.Button(self.window, text='登录', font=tkFont.Font(size=11), command=self.login)
        self.buttonb2 = tk.Button(self.window, text='重置', font=tkFont.Font(size=11), command=self.reset)
        self.buttonb2.place(x=180, y=300, width=70, height=30)
        self.buttonb1.place(x=60, y=300, width=70, height=30)
        self.window.protocol("WM_DELETE_WINDOW", self.reset)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环


    def reset(self):
        self.window.destroy()  # 显示主窗口 销毁本窗口
        StartPage()

    def login(self):

        if self.admin_username.get() == "007" and self.admin_pass.get() == "123":
            app=Start()
            app.start()
            self.window.destroy()
        else:
            msgbox.showinfo("提示", "用户名或密码错误！")
            self.window.destroy()


# 添加、编辑联系人弹出框类
class PopupWindow(object):
    # 初始化构造及添加组件到弹出框
    def __init__(self, master, main_window, title, contact=None):
        self.main_window = main_window
        top = self.top = Toplevel(master)
        top.title(title)
        top.resizable(False, False)
        w = 280
        h = 320
        top.geometry('%dx%d+%d+%d' % (w, h, (ws - w) / 2, (hs - h) / 2))
        top.bind('<Escape>', lambda event: top.destroy())

        m_font = font.Font(size=16)
        l = Label(top, text="姓名：", font=m_font)
        l.pack(side=TOP, pady=5)
        self.e1 = Entry(top)
        self.e1.pack(side=TOP, padx=16, ipady=3, fill=X)
        self.e1.focus()
        if contact is not None:
            self.e1.insert(0, contact.name)

        l2 = Label(top, text="证件号码：", font=m_font)
        l2.pack(side=TOP, pady=5)
        self.e2 = Entry(top)
        self.e2.pack(side=TOP, padx=16, ipady=3, fill=X)
        if contact is not None:
            self.e2.insert(0, contact.phone_number)

        l2 = Label(top, text="房间号：", font=m_font)
        l2.pack(side=TOP, pady=5)
        self.e3 = Entry(top)
        self.e3.pack(side=TOP, padx=16, ipady=3, fill=X)
        if contact is not None:
            self.e3.insert(0, contact.work_place)

        l2 = Label(top, text="入住时间：", font=m_font)
        l2.pack(side=TOP, pady=5)
        self.e4 = Entry(top)
        self.e4.pack(side=TOP, padx=16, ipady=3, fill=X)
        if contact is not None:
            self.e4.insert(0, contact.e_mail)

        if contact is None:
            b2 = Button(top, text='添加', width=12, command=lambda: self.add_click(None))
            self.e4.bind('<Return>', self.add_click)
        else:
            b2 = Button(top, text='编辑', width=12, command=lambda: self.edit_click(None))
            self.e4.bind('<Return>', self.edit_click)
        b2.pack(side=LEFT, pady=10, padx=20)
        b3 = Button(top, text='取消', width=12, command=lambda: top.destroy())
        b3.pack(side=RIGHT, pady=10, padx=20)

        top.grab_set()

    # 点击编辑联系人按钮
    def edit_click(self, event):
        e1_name = self.e1.get()
        if not e1_name:
            messagebox.showinfo("出错了", '名字不能为空！')
            return
        e2_name = self.e2.get()
        if not e2_name:
            messagebox.showinfo("出错了", '证件号码不能为空！')
            return
        e3_name = self.e3.get()
        e4_name = self.e4.get()
        self.main_window.edit_value(e1_name, e2_name, e3_name, e4_name)
        self.top.destroy()

    # 点击添加联系人按钮
    def add_click(self, event):
        e1_name = self.e1.get()
        if not e1_name:
            messagebox.showinfo("出错了", '名字不能为空！')
            return
        e2_name = self.e2.get()
        if not e2_name:
            messagebox.showinfo("出错了", '证件号码不能为空！')
            return
        e3_name = self.e3.get()
        e4_name = self.e4.get()
        self.main_window.add_value(e1_name, e2_name, e3_name, e4_name)
        self.top.destroy()


# 主界面类
class MainWindow(object):
    # 默认初始化构造
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.add_btn_widget()
        self.add_search_widget()
        self.add_listbox_widget()
        self.add_statusbar_widget()
        self.read_save_contacts()
        self.sel_item = 0

    # 添加操作按钮
    def add_btn_widget(self):
        frame = Frame(self.root)
        frame.pack(pady=8)
        self.addBtn = Button(frame, text='添加客人', width=15, fg='white', bg='gray', command=lambda: self.popup("添加客人"))
        self.addBtn.pack(padx=5, fill=X, side=LEFT)
        self.delAllBtn = Button(frame, text='删除客人', width=15, fg='white', bg='gray', command=self.del_all_contacts)
        self.delAllBtn.pack(padx=5, fill=X, side=LEFT)
        self.saveAllBtn = Button(frame, text='保存客人', width=15, fg='white', bg='gray', command=self.save_all_contacts)
        self.saveAllBtn.pack(padx=5, fill=X, side=LEFT)

    # 添加搜索框
    def add_search_widget(self):
        frame = Frame(self.root)
        frame.pack(pady=8)
        entry1 = self.input_view = Entry(frame, width=34)
        entry1.insert(0, '输入部分姓名或证件号码按回车查询')
        entry1.bind("<Button-1>", self.click_input)
        entry1.bind("<FocusOut>", self.focusout_input)
        entry1.bind('<Return>', self.search_contact)
        entry1.bind('<Escape>', self.cancel_search)
        entry1.pack(ipady=3, padx=5, side=LEFT)
        entry1.selection_range(0, len(entry1.get()))
        entry1.focus()
        command4 = self.search_btn = Button(frame, text='清空输入', width=15, command=lambda: self.cancel_search(None))
        command4["state"] = "disabled"
        command4.pack(padx=5, side=LEFT)

    # 点击输入框清空内容
    def click_input(self, event):
        if self.input_view.get() == '输入部分姓名或证件号码按回车查询':
            self.input_view.delete(0, END)

    # 输入框失去焦点时
    def focusout_input(self, event):
        if len(self.input_view.get()) == 0:
            self.input_view.insert(0, '输入部分姓名或证件号码按回车查询')

    # 添加列表及滚动条
    def add_listbox_widget(self):
        frame = Frame(self.root)
        frame.pack(pady=8)
        bolded = font.Font(size=20)
        self.lb = Listbox(frame, font=bolded, height=14, width=25, borderwidth=0)
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        scrollbar.config(command=self.lb.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lb.config(yscrollcommand=scrollbar.set, activestyle='none')
        scrollbar2 = Scrollbar(frame, orient=HORIZONTAL)
        scrollbar2.config(command=self.lb.xview)
        scrollbar2.pack(side=BOTTOM, fill=X)
        self.lb.config(xscrollcommand=scrollbar2.set, activestyle='none')
        self.lb.pack(fill=BOTH)
        self.lb.bind('<Double-1>', self.dbclick)
        self.lb.bind('<Button-3>', self.rclick_popup)

    # 添加界面底部联系人数
    def add_statusbar_widget(self):
        frame = Frame(self.root)
        frame.pack(pady=8, side=LEFT)
        self.label = Label(frame, text='>系统现有 0 位客人<')
        self.label.pack()

    # 右键菜单
    def rclick_popup(self, event):
        a_menu = Menu(self.root, tearoff=0)
        a_menu.add_command(label='编辑选中的客人', command=self.edit_contact)
        a_menu.add_command(label='删除选中的客人', command=self.del_contact)
        a_menu.post(event.x_root, event.y_root)

    # 右键编辑选中的联系人
    def edit_contact(self):
        selection = self.lb.curselection()
        if len(selection) == 0:
            messagebox.showerror("出错了", '请先左键选中待操作的客人！')
            return
        self.sel_item = selection[0]
        self.right_clidk_reset()
        contact = self.contacts[self.sel_item]
        self.popup("编辑客人", contact=contact)

    # 右键删除选中的联系人
    def del_contact(self):
        selection = self.lb.curselection()
        if len(selection) == 0:
            messagebox.showerror("出错了", '请先左键选中待操作的客人！')
            return
        self.right_clidk_reset()
        answer = messagebox.askyesno("提示", "您确定要删除此客人吗？")
        if answer:
            self.lb.delete(self.sel_item, self.sel_item)
            self.contacts.pop(self.sel_item)
            self.label.config(text='系统现有 %d 位客人' % len(self.contacts))
            messagebox.showinfo('提示', '客人从系统删除成功！\n若需要保存操作结果，请点击“保存所有客人”')

    # 若是搜索后右键，则操作重置列表
    def right_clidk_reset(self, is_dbclick=False):
        b_text = self.search_btn["state"]
        if b_text == "normal":
            ic = -1
            item = self.lb.selection_get()
            if not is_dbclick:
                self.cancel_search(None)
            for ct in self.contacts:
                ic += 1
                if (ct.name in item) and (ct.phone_number in item):
                    break
            self.sel_item = ic
            self.lb.selection_set(ic, ic)

    # 双击联系人条目
    def dbclick(self, event):
        selection = self.lb.curselection()
        self.sel_item = selection[0]
        self.right_clidk_reset(is_dbclick=True)
        contact = self.contacts[self.sel_item]
        wp = contact.work_place if len(contact.work_place) != 0 else '空'
        em = contact.e_mail if len(contact.e_mail) != 0 else '空'
        msg = '姓名：%s\n证件：%s\n房间号：%s\n入住时间：%s' % (contact.name, contact.number, room, time)
        messagebox.showinfo("详细信息", msg)

    # 添加、编辑联系人弹窗
    def popup(self, title, contact=None):
        self.cancel_search(None)
        self.w = PopupWindow(self.root, self, title, contact)
        self.addBtn["state"] = "disabled"
        self.root.wait_window(self.w.top)
        self.addBtn["state"] = "normal"

    # 删除所有联系人
    def del_all_contacts(self):
        self.cancel_search(None)
        answer = messagebox.askyesno("提示", "您确定要删除所有客人吗？")
        if answer:
            self.contacts.clear()
            self.lb.delete(0, END)
            remove("contacts.csv")
            self.label.config(text='系统现有 %d 位客人' % len(self.contacts))

    # 保存联系人到文件
    def save_all_contacts(self):
        self.cancel_search(None)
        f = open("contacts.csv", "w", encoding='utf-8')
        for contact in self.contacts:
            str = '%s,%s,%s,%s\n' % (contact.name, contact.phone_number, contact.work_place, contact.e_mail)
            f.write(str)
        f.close()
        messagebox.showinfo('提示', '保存 %d 位客人到文件成功！' % len(self.contacts))

    # 读取保存在文件的联系人
    def read_save_contacts(self):
        if not path.exists('contacts.csv'):
            return
        f = open("contacts.csv", "r", encoding='utf-8')
        for line in f:
            array = line.strip().split(',')
            contact = Contact(array[0], array[1], array[2], array[3])
            self.contacts.append(contact)
            self.lb.insert(END, '%s Tel:%s' % (contact.name, contact.phone_number))
        self.label.config(text='系统现有 %d 位客人' % len(self.contacts))
        f.close()

    # 添加联系人回调
    def add_value(self, name, phone_number, work_place, e_mail):
        contact = Contact(name, phone_number, work_place, e_mail)
        self.contacts.append(contact)
        self.lb.insert(END, '%s Tel:%s' % (name, phone_number))
        self.label.config(text='系统现有 %d 位客人' % len(self.contacts))

    # 编辑联系回调
    def edit_value(self, name, phone_number, work_place, e_mail):
        contact = self.contacts[self.sel_item]
        contact.name = name
        contact.phone_number = phone_number
        contact.work_place = work_place
        contact.e_mail = e_mail
        self.lb.delete(0, END)
        for contact in self.contacts:
            self.lb.insert(END, '%s Tel:%s' % (contact.name, contact.phone_number))
        self.label.config(text='系统现有 %d 位客人' % len(self.contacts))

    # 搜索联系人方法
    def search_contact(self, event):
        self.search_btn["state"] = "normal"
        self.lb.delete(0, END)
        key = self.input_view.get().strip()
        ci = 0
        for contact in self.contacts:
            if (key in contact.name) or (key in contact.phone_number):
                self.lb.insert(END, '%s Tel:%s' % (contact.name, contact.phone_number))
                ci += 1
        self.label.config(text='查询到 %d 位客人' % ci)

    # 取消搜索
    def cancel_search(self, event):
        b_state = self.search_btn["state"]
        if b_state == "normal":
            self.search_btn["state"] = "disabled"
            self.lb.delete(0, END)
            self.input_view.delete(0, END)
            self.input_view.insert(0, '输入部分姓名或证件号码按回车查询')
            for contact in self.contacts:
                self.lb.insert(END, '%s Tel:%s' % (contact.name, contact.phone_number))
            self.label.config(text='系统现有 %d 位客人' % len(self.contacts))
            self.input_view.selection_range(0, len(self.input_view.get()))


# 联系人类对象
class Contact:
    def __init__(self, name, phone_number, work_place, e_mail):
        self.name = name
        self.phone_number = phone_number
        self.work_place = work_place
        self.e_mail = e_mail


# 程序启动入口

class Start:

    def start(self):
        root = Tk()
        root.wm_resizable(False, False)
        root.title('酒店管理系统')
        w = 380
        h = 560
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (w, h, (ws - w) / 2, (hs - h) / 2))
        m = MainWindow(root)
        root.mainloop()


if __name__ == '__main__':
    s = StartPage()
