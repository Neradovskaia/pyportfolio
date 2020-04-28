import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path


class NewGame:

    def __init__(self):
        self.player = 'X'
        self.board = {}
        for p in range(1, 10):
            self.board[str(p)] = str(p)

    def make_move(self, position):
        if self.position_is_valid(position):
            self.update_board(position)
            return True
        else:
            return False

    def update_board(self, position):
        self.board[position] = self.player

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def position_is_valid(self, position):
        if self.position_is_int(self.board[position]):
            return True
        else:
            return False

    @staticmethod
    def position_is_int(position):
        try:
            int(position)
            return True
        except ValueError:
            return False

    def game_over(self):
        win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))
        for each in win_coord:
            if self.board[str(each[0])] == self.board[str(each[1])] == self.board[str(each[2])]:
                print('3 in line!')
                return True
        if self.tie():
            return True
        return False

    def tie(self):
        n_empty_spots = 0
        for p in range(1, 10):
            if self.position_is_int(self.board[str(p)]):
                n_empty_spots += 1
        if n_empty_spots == 0:
            return True
        return False


class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Tic Tac Toe')
        self.app.geometry("182x185+500+200")
        self.make_topmost()
        self.app.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.img = tk.PhotoImage(width=50, height=50)
        count = 0
        self.game = NewGame()
        self.buttons = {}
        for r in range(3):
            for c in range(3):
                count += 1
                btn = tk.Button(self.app,
                                text=str(count),
                                borderwidth=1,
                                command=lambda count=count: self.click_btn(str(count)),
                                image=self.img
                                )
                btn.grid(row=r, column=c)
                self.buttons[str(count)] = btn

    def on_exit(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?", parent=self.app):
            self.app.destroy()

    def center(self):
        """Centers this Tk window"""
        self.app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))

    def make_topmost(self):
        """Makes this window the topmost window"""
        self.app.lift()
        self.app.wm_attributes("-topmost", 1)

    def click_btn(self, count):
        if self.game.position_is_valid(count):
            self.game.update_board(count)
            self.update_btns(count)
            if self.game.game_over():
                self.on_game_end()
            else:
                self.game.change_player()
        else:
            messagebox.showinfo(title='Wrong square', message='Chose another square')

    def update_btns(self, count):
        btn = self.buttons[count]
        if self.game.player == 'X':
            filename = 'cross_image.png'
        else:
            filename = 'zero_image.png'
        imgs_folder = Path('imgs')
        file_to_open = imgs_folder / filename
        img_to_show = ImageTk.PhotoImage(Image.open(file_to_open))
        btn.configure(image=img_to_show)
        btn.image = img_to_show
        self.buttons[count] = btn

    def on_game_end(self):
        self.disable_btns()
        if self.game.tie():
            if messagebox.askyesno(title='Game over', message='Tie! Play again?', parent=self.app):
                self.reset_game()
            else:
                self.app.destroy()
        else:
            if messagebox.askyesno(title='Game over',
                                   message=f'Congratulations! {self.game.player} won! Play again?',
                                   parent=self.app):
                self.reset_game()
            else:
                self.app.destroy()

    def reset_game(self):
        self.game = NewGame()
        for p in range(1, 10):
            position = str(p)
            btn = self.buttons[position]
            btn.configure(image=self.img)
            btn.image = self.img
            btn.configure(state='normal')
            btn.state = 'normal'
            self.buttons[position] = btn

    def disable_btns(self):
        for p in range(1, 10):
            position = str(p)
            btn = self.buttons[position]
            btn.configure(state='disabled')
            btn.state = 'disabled'
            self.buttons[position] = btn


if __name__ == '__main__':
    App().app.mainloop()
