import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self):
        # ウィンドウを初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')
        self.master.configure(padx=16, pady=16)

        # TODO入力エリアを作成
        self.input_area = InputArea(self.master)
        self.input_area.pack(side='top', fill='x')
        self.input_area.click_add_btn = self.click_add_btn

        # TODOリストの表示エリアを作成
        self.list_area = ListArea(self.master)
        self.list_area.pack(side='bottom', expand=True, fill='both')

    def mainloop(self):
        # masterに処理を委譲
        self.master.mainloop()

    def click_add_btn(self):
        """
        このメソッドを追加

        入力エリアの追加ボタンが押されたら呼ばれる
        入力エリアの入力値をリストエリアに追加する
        """
        todo = self.input_area.entry.get()  # 入力値を取得
        if todo != '':
            self.input_area.entry.delete(0, 'end')  # 入力行に残ったテキストを削除
            self.list_area.listbox.insert('end', todo)  # リストにTODOを追加
        else:
            messagebox.showerror('エラー', '追加する内容が入力されていません')


class InputArea(tk.Frame):
    """
    TODOの入力エリア
    ユーザーの入力を処理する
    ユーザーが入力したTODOテキストを追加ボタンでリストに追加するのが役割
    """

    def __init__(self, master):
        super(InputArea, self).__init__(master)

        # ハンドル
        self.click_add_btn = None

        # ラベルの作成
        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left')

        # 入力行の作成
        self.entry = tk.Entry(self)
        self.entry.pack(side='left', expand=True, fill='x')

        # 追加ボタンの作成
        self.add_btn = tk.Button(self, text='追加', command=self._click_add_btn)
        self.add_btn.pack(side='left')

    def _click_add_btn(self):
        if self.click_add_btn:
            self.click_add_btn()


class ListArea(tk.Frame):
    """
    TODOアプリの表示エリア
    ユーザーが入力したTODOが表示される
    """

    def __init__(self, master):
        super(ListArea, self).__init__(master)

        # リストの作成
        self.listbox = tk.Listbox(self, height=5)
        self.listbox.pack(side='top', expand=True, fill='both')

        # 削除ボタンの作成
        self.del_btn = tk.Button(self, text='削除', command=self._click_del_btn)
        self.del_btn.pack(side='bottom', fill='x')

    def _click_del_btn(self):
        """
        選択中のTODOを削除する
        """
        sel = self.listbox.curselection()
        for i in sel[::-1]:
            self.listbox.delete(i)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
