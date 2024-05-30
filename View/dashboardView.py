import tkinter as tk
from tkinter import ttk
import numpy as np


# class Controller():
#     pass

class dashboardView(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Salonga Music Shop")
        
        self.mainframe() # Main/Root Frame
        self.set_window() 
        self.custom_styles()
        self._top_label() # Top Bar + Heading   
        self._bottom_frame() 
        
    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 600
        set_height = 400
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(bg='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ttk.Frame(self, borderwidth=1, relief='solid')
        self.frame.place(x=300, y=200, anchor=tk.CENTER, width=420, height=280)
        Shadow(self.frame, color='#888888', size=1.015, offset_y=4)
    
    def _top_label(self):
        self.signupLabel = ttk.Label(self.frame, text="Dashboard", font=("Consolas", 14, 'bold'), 
                                    relief='solid', borderwidth=1, anchor=tk.CENTER, background='#E9E9E9')
        self.signupLabel.place(width=420, height=52, x=-1, y=-1)

    def _bottom_frame(self):
        self.bottomFrame = ttk.Frame(self.frame, borderwidth=1, relief='solid')
        self.bottomFrame.place(relx=0.5, y=257, anchor=tk.CENTER, width=420, height=44)
        
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Text.TLabel", font=('Consolas', 10), background='#F7F7F7')
        self.style.configure("Custom.TButton", font=('Consolas', 10))
        self.style.configure("CustomForm.TFrame", background='#F7F7F7', borderwidth=1, relief='solid')
    



class Shadow(tk.Tk):

    '''
    Add shadow to a widget
    
    This class adds a squared shadow to a widget. The size, the position, and
    the color of the shadow can be customized at wills. 
    Note that enough space around the widget is required for the shadow to
    correctly appear. Moreover, other widgets nearer than shadow's size will be
    covered by the shadow.
    '''
    def __init__(self, widget, color='#212121', size=5, offset_x=0, offset_y=0):
        '''
        Bind shadow to a widget.

        Parameters
        ----------
        widget : tkinter widget
            Widgets to which shadow should be binded.
        color : str, optional
            Shadow color in hex notation. The default is '#212121'.
        size : int or float, optional
            Size of the shadow. If int type, it is the size of the shadow out
            from the widget bounding box. If float type, it is a multiplier of
            the widget bounding box (e.g. if size=2. then shadow is double in
            size with respect to widget). The default is 5.
        offset_x : int, optional
            Offset by which shadow will be moved in the horizontal axis. If
            positive, shadow moves toward right direction. The default is 0.
        offset_y : int, optional
            Offset by which shadow will be moved in the vertical axis. If
            positive, shadow moves toward down direction. The default is 0.

        Returns
        -------
        None.

        '''
        # Save parameters
        self.widget = widget
        self.shadow_size = size
        self.shadow_color = color
        self.shadow_x = int(offset_x)
        self.shadow_y = int(offset_y)
        
        # Get master and master's background
        self.master = widget.master
        self.to_rgb = tuple([el//257 for el in self.master.winfo_rgb(self.master.cget('bg'))])
        
        # Start with normal view
        self.__lines = []
        self.display()
    
    def __destroy_lines(self):
        ''' Destroy previous shadow lines '''
        for ll in self.__lines:
            ll.destroy()
        self.__lines = []
    
    def display(self):
        ''' Destroy shadow according to selected configuration '''
        def _rgb2hex(rgb):
            """
            Translates an rgb tuple of int to hex color
            """
            return "#%02x%02x%02x" % rgb
    
        def _hex2rgb(h):
                """
                Translates an hex color to rgb tuple of int
                """
                h = h.strip('#')
                return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        # Destroy old lines
        self.__destroy_lines()
        
        # Get widget position and size
        self.master.update_idletasks()
        x0, y0, w, h = self.widget.winfo_x(), self.widget.winfo_y(), self.widget.winfo_width(), self.widget.winfo_height()
        x1 = x0 + w - 0
        y1 = y0 + h - 0
        
        # Get shadow size from borders
        if type(self.shadow_size) is int:
            wh_shadow_size = self.shadow_size
        else:
            wh_shadow_size = min([int(dim * (self.shadow_size - 1)) for dim in (w,h)])
        uldr_shadow_size = wh_shadow_size - self.shadow_y, wh_shadow_size - self.shadow_x, \
                    wh_shadow_size + self.shadow_y, wh_shadow_size + self.shadow_x
        uldr_shadow_size = {k:v for k,v in zip('uldr', uldr_shadow_size)}
        self.uldr_shadow_size = uldr_shadow_size
        
        # Prepare shadow color
        shadow_color = self.shadow_color
        if not shadow_color.startswith('#'):
            shadow_color = _rgb2hex(tuple([min(max(self.to_rgb) + 30, 255)] * 3))
        self.from_rgb = _hex2rgb(shadow_color)
        
        # Draw shadow lines
        max_size = max(uldr_shadow_size.values())
        diff_size = {k: max_size-ss for k,ss in uldr_shadow_size.items()}
        rs = np.linspace(self.from_rgb[0], self.to_rgb[0], max_size, dtype=int)
        gs = np.linspace(self.from_rgb[2], self.to_rgb[2], max_size, dtype=int)
        bs = np.linspace(self.from_rgb[1], self.to_rgb[1], max_size, dtype=int)
        rgbs = [_rgb2hex((r,g,b)) for r,g,b in zip(rs,gs,bs)]
        for direction, size in uldr_shadow_size.items():
            for ii, rgb in enumerate(rgbs):
                ff = tk.Frame(self.master, bg=rgb)
                self.__lines.append(ff)
                if direction=='u' or direction=='d':
                    diff_1 = diff_size['l']
                    diff_2 = diff_size['r']
                    yy = y0-ii+1+diff_size[direction] if direction == 'u' else y1+ii-diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=ii+1-diff_1, height=1)
                        ff1.place(x=x0-ii+1+diff_size['l'], y=yy)
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=ii+1-diff_2, height=1)
                        ff2.place(x=x1, y=yy)
                    if ii >= diff_size[direction]:
                        ff.configure(width=x1-x0+ii*2-diff_size['l']-diff_size['r'], height=1)
                        ff.place(x=x0-ii+1+diff_size['l'], y=yy)
                elif direction=='l' or direction=='r':
                    diff_1 = diff_size['u']
                    diff_2 = diff_size['d']
                    xx = x0-ii+1+diff_size[direction] if direction == 'l' else x1+ii-diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=1, height=ii+1-diff_1)
                        ff1.place(x=xx, y=y0-ii+1+diff_size['u'])
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=1, height=ii+1-diff_2)
                        ff2.place(x=xx, y=y1)
                    if ii >= diff_size[direction]:
                        ff.configure(width=1, height=y1-y0+ii*2-diff_size['u']-diff_size['d'])
                        ff.place(x=xx, y=y0-ii+1+diff_size['u'])


# if __name__ == "__main__":
#     controller = Controller()
#     app = dashboardView(controller)
#     app.main()
    