import tkinter as tk
from tkinter import ttk
import numpy as np
from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1)

class dashboardView(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Salonga Music Shop")
        
        self.set_window() 
        self.custom_styles()
        self._top_frame() 
        self._left_frame()
        self._dashboard_frame() # Main Frame
        self._top_label()
        
        self._app_icon()
        self._selection_1()
        self._selection_2()
        self._selection_3()
        self._selection_4()
        self._selection_5()

        
    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 760
        set_height = 500
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(bg='#DFDFDF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)
    
    def _top_frame(self):
        self.topFrame = ttk.Frame(self, style='TopFrame.TFrame')
        self.topFrame.place(x=446, y=24, anchor=tk.CENTER, width=628, height=48)
        Shadow(self.topFrame, color='#A1A1A1', size=1.015, offset_x=0, offset_y=1)

    def _left_frame(self):
        self.leftFrame = ttk.Frame(self, style='LeftFrame.TFrame')
        self.leftFrame.place(x=66, y=250, anchor=tk.CENTER, width=132, height=500)
        Shadow(self.leftFrame, color='#9F9F9F', size=1.015, offset_x=1, offset_y=0)

    def _dashboard_frame(self):
        self.dashboardFrame = ttk.Frame(self, style='DashboardFrame.TFrame')
        self.dashboardFrame.place(x=448, y=276, anchor=tk.CENTER, width=623, height=447)
        
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Custom.TLabel", font=('Consolas', 12, 'bold'))    # Bigger fontsize
        self.style.configure("Custom2.TLabel", font=('Consolas', 10, 'italic')) # Smaller fontsize

        self.style.configure("Custom.TButton", font=('Consolas', 12, 'bold'), foreground="#2D2D2D")  # Active Selection
        self.style.configure("Custom2.TButton", font=('Consolas', 12, 'bold'), foreground="#595959") # Inactive Selection

        self.style.configure("TopFrame.TFrame", background='#FFFFFF')
        self.style.configure("LeftFrame.TFrame", background='#EDEDED')
        self.style.configure("DashboardFrame.TFrame", background='#DFDFDF')

    def _top_label(self):
        self.topLabel = ttk.Label(self.topFrame, text='Admin', style='Custom.TLabel', background='#FFFFFF')
        self.topLabel.place(x=20, y=10)
    
    def _app_icon(self): # Icon + Name placeholder
        self.appIcon = ttk.Label(self.leftFrame, text="Icon: Name", foreground='#595959', style='Custom2.TLabel')
        self.appIcon.place(x=20, y=12)
    
    def _selection_1(self):
        self.selection1 = tk.Button(self.leftFrame, text="Dashboard", font=('Consolas', 12, 'bold'), foreground="#2D2D2D", background='#FFFFFF', relief=tk.FLAT)
        self.selection1.place(x=6, y=50, width=116, height=36)
        Shadow(self.selection1, color='#7F7F7F', size=1.1, offset_x=1, offset_y=1)
        
    def _selection_2(self):
        self.selection2 = tk.Button(self.leftFrame, text="Products", font=('Consolas', 12, 'bold'), foreground="#595959", background='#E2E2E2', relief=tk.FLAT)
        self.selection2.place(x=8, y=95, width=116, height=36)
        # Shadow(self.selection2, color='#7F7F7F', size=1.1, offset_x=1, offset_y=1)
        
    def _selection_3(self):
        self.selection3 = tk.Button(self.leftFrame, text="Reports", font=('Consolas', 12, 'bold'), foreground="#595959", background='#E2E2E2', relief=tk.FLAT)
        self.selection3.place(x=8, y=140, width=116, height=36)
        # Shadow(self.selection2, color='#7F7F7F', size=1.1, offset_x=1, offset_y=1)
        
    def _selection_4(self):
        self.selection4 = tk.Button(self.leftFrame, text="Delivery", font=('Consolas', 12, 'bold'), foreground="#595959", background='#E2E2E2', relief=tk.FLAT)
        self.selection4.place(x=8, y=185, width=116, height=36)
        # Shadow(self.selection2, color='#7F7F7F', size=1.1, offset_x=1, offset_y=1)
        
    def _selection_5(self):
        self.selection5 = tk.Button(self.leftFrame, text="Employees", font=('Consolas', 12, 'bold'), foreground="#595959", background='#E2E2E2', relief=tk.FLAT)
        self.selection5.place(x=8, y=230, width=116, height=36)
        # Shadow(self.selection2, color='#7F7F7F', size=1.1, offset_x=1, offset_y=1)





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
        self.to_rgb = tuple([int(x) for x in self.master.winfo_rgb(self.master.tk.call('ttk::style', 'lookup', self.master.winfo_class(), '-background'))]) # Updated line to account for button

        
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



    