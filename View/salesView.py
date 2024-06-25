import customtkinter as ctk
import tkinter as tk
from PIL import Image
from CTkSpinbox import *
from tkinter import messagebox

class salesView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.active_tab = 1
        self.search_query = ctk.StringVar()

        self.selectionFrames = []
        self.rowFrames = [] # Stores created rows, upon item selection
        self.row_counter = 0
        
        self.trashIcon = ctk.CTkImage(light_image=Image.open('./assets/trash.png'), size=(15,15))
        
        self.custom_styles()
        self.base_frame()
        self.update_total_price()
    def custom_styles(self):
        pass
    
    def show_selection(self):
        self.selectionTable = ctk.CTkScrollableFrame(self.firstPageFrame, width=493, height=423, fg_color='transparent')
        self.selectionTable.place(x=0, y=120)

        self.products = [
            ['Electric Guitar', 'Fendy', 1000.0, 10],
            ['Xylophone', 'Yamaha', 800.0, 5],
            ['Acoustic Guitar', 'Gibson', 850.0, 3],
            ['Bass Guitar', 'JB', 730.0, 5],
            ['Ukulele', 'RJ', 920.0, 0],
            ['Drum Set', 'Pearl', 1500.0, 7],
            ['Violin', 'Stradivarius', 1200.0, 3],
            ['Trumpet', 'Bach', 900.0, 4],
            ['Saxophone', 'Yamaha', 1100.0, 6],
            ['Flute', 'Yamaha', 700.0, 5],
            ['Cello', 'Stradivarius', 2000.0, 2],
            ['Clarinet', 'Buffet', 800.0, 8],
            ['Harp', 'Lyon & Healy', 3500.0, 1],
            ['Trombone', 'Conn', 950.0, 3],
            ['Piano', 'Steinway', 5000.0, 2],
            ['Synthesizer', 'Roland', 1300.0, 5]
        ]

        columns = 5
        frame_width = 83
        frame_height = 126

        self.placeholderIcon = ctk.CTkImage(light_image=Image.open('./assets/placeholder.png'), size=(66, 66))

        valid_index = 0
        for i in range(len(self.products)):
            name, brand, price = self.products[i][0], self.products[i][1], self.products[i][2]
            try:
                quantity = self.products[i][3]
                quantity_value = int(quantity)
            except (IndexError, ValueError):
                quantity_value = 0

            if quantity_value == 0:
                continue

            row = valid_index // columns
            col = valid_index % columns

            selection_frame = ctk.CTkFrame(self.selectionTable,
                                           width=frame_width, height=frame_height,
                                           fg_color='transparent', bg_color='transparent')
            selection_frame.grid(row=row, column=col, padx=7, pady=5)

            selection_image = ctk.CTkButton(selection_frame, image=self.placeholderIcon, text='', width=83, height=83,
                                            border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                            fg_color='#FFFFFF', bg_color='#F7F7F7',
                                            hover_color='#FFFFFF', anchor='center',
                                            command=lambda idx=i: self.add_row(idx))
            selection_image.grid(row=0, column=0)

            selection_name = ctk.CTkLabel(selection_frame, text=name,
                                          width=80, height=12, font=('Inter Semibold', 10), text_color='#747474')
            selection_name.grid(row=1, column=0)

            selection_brand = ctk.CTkLabel(selection_frame, text=brand,
                                           width=80, height=7, font=('Inter Semibold', 7), text_color='#747474')
            selection_brand.grid(row=2, column=0)

            formatted_price = f'₱{price:,.2f}'

            selection_price = ctk.CTkLabel(selection_frame, text=formatted_price,
                                           width=80, height=10, font=('Inter Semibold', 8), text_color='#747474')
            selection_price.grid(row=3, column=0)

            text_color = '#AE5050' if quantity_value == 0 else ('#E9AC07' if 1 <= quantity_value <= 5 else '#329932')
            formatted_quantity = f'{quantity} In Stock'
            
            selection_quantity = ctk.CTkLabel(selection_frame, text=formatted_quantity,
                                              width=80, height=9, font=('Inter Semibold', 9),
                                              text_color=text_color)
            selection_quantity.grid(row=4, column=0)

            valid_index += 1
    
    def add_row(self, idx):
        name, brand, price, quantity = self.products[idx][0], self.products[idx][1], self.products[idx][2], self.products[idx][3]
        y_position = 0 + (self.row_counter * 40)
        rowFrame = ctk.CTkFrame(self.orderListFrame, width=285, height=40, fg_color='transparent')

        
        
        self.deleteButton = ctk.CTkButton(rowFrame, image=self.trashIcon, text='', width=15, height=15,
                                        border_width=0, fg_color='transparent', corner_radius=0,
                                        hover_color='#F7F7F7', anchor='center',
                                        command=lambda rowFrame=rowFrame: self.delete_row(rowFrame))
        self.deleteButton.place(x=3, y=8)

        self.rowLine = ctk.CTkFrame(rowFrame, width=285, height=2, fg_color='#E9E9E9')
        self.rowLine.place(x=0, y=39)

        self.productName = ctk.CTkLabel(rowFrame, text=name, width=90, height=12,
                                        font=('Inter Semibold', 11), text_color='#747474', anchor='w')
        self.productName.place(x=29, y=9)

        self.productBrand = ctk.CTkLabel(rowFrame, text=brand, width=90, height=10,
                                        font=('Inter Semibold', 9), text_color='#747474', anchor='w')
        self.productBrand.place(x=29, y=21)

        formatted_price = f'₱{price:,.2f}'
        
        self.productPrice = ctk.CTkLabel(rowFrame, text=formatted_price, width=69, height=17,
                                    font=('Inter Semibold', 10), text_color='#747474', anchor='w')
        self.productPrice.place(x=207, y=11)
        
        spinboxValue = ctk.IntVar(value=0)
        self.productQuantity = CTkSpinbox(rowFrame, start_value=0, width=64, height=20,
                                            min_value=0, max_value=quantity, variable=spinboxValue,
                                            font=('Inter Semibold', 10), text_color='#747474',
                                            fg_color='#F7F7F7',
                                            corner_radius=5, border_width=2, border_color='#CACACA',
                                            command=lambda idx=idx: self.update_price(idx))
        self.productQuantity.place(x=130, y=9)
        
        rowFrame.place(x=0, y=y_position)
        self.rowFrames.append((rowFrame, spinboxValue, idx))
        self.row_counter += 1
        self.update_total_price()
        
    def update_price(self, idx):
        for rowFrame, spinboxValue, product_idx in self.rowFrames:
            if rowFrame.winfo_ismapped(): # Check if row is visible
                quantity = spinboxValue.get()
                price = quantity * self.products[product_idx][2] # Calculates price before configuring
                for widget in rowFrame.winfo_children():
                    if isinstance(widget, ctk.CTkLabel) and "₱" in widget.cget("text"):
                        widget.configure(text=f'₱{price:,.2f}')
        self.update_total_price()
            
    def update_total_price(self):
        total = sum(spinboxValue.get() * self.products[product_idx][2] for rowFrame, spinboxValue, product_idx in self.rowFrames if rowFrame.winfo_ismapped())
        formatted_total = f'₱{total:,.2f}'
        self.revenueLabel.configure(text=formatted_total)

    def delete_row(self, row_frame):
        for item in self.rowFrames:
            if item[0] == row_frame:
                self.rowFrames.remove(item)
                break
        
        row_frame.destroy()
        
        for idx, (frame, _, _) in enumerate(self.rowFrames):
            y_position = 0 + (idx * 40)
            frame.place(x=0, y=y_position)
        
        self.row_counter -= 1
        
        self.update_total_price()

        

        
            
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        orderID = 1 # ID Counter, increments on click (save button)
        
        self.orderIDLabel = ctk.CTkLabel(self.orderFrame, text=f"Order #{orderID:04}", width=121, height=23, # Pads zeroes (length of 4), e.g. 0001
                                         font=('Inter', 15, 'bold'), text_color='#2E2E2E') 
        self.orderIDLabel.place(x=82, y=12)
        
        self.orderColumnFrame = ctk.CTkFrame(self.orderFrame, width=285, height=24, corner_radius=0, fg_color='#E9E9E9')
        self.orderColumnFrame.place(x=0, y=48)
        
        self.orderProduct = ctk.CTkLabel(self.orderColumnFrame, text='Product', width=106, height=22,
                                         font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='w')
        self.orderProduct.place(x=10, y=1)
        
        self.orderQuantity = ctk.CTkLabel(self.orderColumnFrame, text='Qty', width=28, height=22,
                                         font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='center')
        self.orderQuantity.place(x=148, y=1)
        
        self.orderPrice = ctk.CTkLabel(self.orderColumnFrame, text='Price', width=63, height=22,
                                         font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='w')
        self.orderPrice.place(x=207, y=1)    

        self.orderListFrame = ctk.CTkFrame(self.orderFrame, width=285, height=354, fg_color='transparent')
        self.orderListFrame.place(x=0, y=72)
        
        self.buyerInfoFrame = ctk.CTkFrame(self.orderFrame, width=285, height=64, fg_color='#F1F1F1')
        self.buyerInfoFrame.place(x=0, y=426)
        
        self.buyerNameLabel = ctk.CTkLabel(self.buyerInfoFrame, width=98, height=16,
                                           text="Buyer's Name: ", anchor='w', font=('Inter Bold', 12), text_color='#747474')
        self.buyerNameLabel.place(x=17, y=10)
        
        self.buyerNameEntry = ctk.CTkEntry(self.buyerInfoFrame, width=113, height=22, fg_color='#FFFFFF', 
                                           border_width=2, border_color='#CACACA', 
                                           font=('Inter Medium', 11), text_color='#747474')
        self.buyerNameEntry.place(x=118, y=7)
        
        self.buyerContactLabel = ctk.CTkLabel(self.buyerInfoFrame, width=98, height=16,
                                           text="Phone #: ", anchor='w', font=('Inter Bold', 12), text_color='#747474')
        self.buyerContactLabel.place(x=17, y=37)
        
        self.buyerContactEntry = ctk.CTkEntry(self.buyerInfoFrame, width=113, height=22, fg_color='#FFFFFF', 
                                           border_width=2, border_color='#CACACA', 
                                           font=('Inter Medium', 11), text_color='#747474')
        self.buyerContactEntry.place(x=118, y=34)
        
        self.line = ctk.CTkFrame(self.buyerInfoFrame, width=285, height=2, fg_color='#CDCDCD')
        self.line.place(x=0, y=63)
        
        self.revenueFrame = ctk.CTkFrame(self.orderFrame, width=285, height=36, fg_color='#F1F1F1')
        self.revenueFrame.place(x=0, y=490)
        
        self.revenueTitle = ctk.CTkLabel(self.revenueFrame, text='Revenue', width=66, height=25, anchor='center',
                                         font=('Inter Bold', 14), text_color='#747474')
        self.revenueTitle.place(x=14, y=5)
                
        self.revenueLabel = ctk.CTkLabel(self.revenueFrame, width=98, height=25, text='₱0.00', 
                                         font=('Inter Bold', 14), text_color='#57AF20')
        self.revenueLabel.place(x=181, y=5)
        
        self.buttonFrame = ctk.CTkFrame(self.orderFrame, width=252, height=30, fg_color='transparent')
        self.buttonFrame.place(x=17, y=539)
        
        self.clearButton = ctk.CTkButton(self.buttonFrame, width=115, height=30, bg_color='transparent', 
                                         fg_color='#E2E2E2', hover_color='#D5D5D5', corner_radius=8,
                                         text='Clear', font=('Consolas', 14), text_color='#595959', 
                                         command=self.clear_form)
        self.clearButton.place(x=0, y=0)
        
        self.saveButton = ctk.CTkButton(self.buttonFrame, width=115, height=30,  bg_color='transparent',
                                        fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=8,
                                        text='Save', font=('Consolas', 14), text_color='#F7F7F7', 
                                        command=self.save_button_clicked)
        self.saveButton.place(x=138, y=0)
        
    def show_firstPage(self):
        self.firstPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.firstPageFrame.place(x=12, y=15)
                
        self.tabFrame = ctk.CTkFrame(self.firstPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=3, y=0)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=133, y=0)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=19, y=33)
        
        self.dividerLine = ctk.CTkFrame(self.firstPageFrame, width=522, height=2, fg_color='#DDDDDD')
        self.dividerLine.place(x=0, y=51)
        
        self.filterFrame = ctk.CTkFrame(self.firstPageFrame, fg_color='transparent', width=336, height=56)
        self.filterFrame.place(x=14, y=59)    

        self.brandFrame = ctk.CTkFrame(self.filterFrame, width=160, height=56, fg_color='transparent')
        self.brandFrame.place(x=0, y=0)
        
        self.brandLabel = ctk.CTkLabel(self.brandFrame, width=106, height=26, text='Brand',
                                    font=('Inter Medium', 12), text_color='#595959', anchor='w')
        self.brandLabel.place(x=4, y=0)
        
        self.brandDropdown = ctk.CTkComboBox(self.brandFrame, 
                                            values=['All', 'Fender', 'Yamaha'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA',)
        self.brandDropdown.set('All')
        self.brandDropdown.place(x=0, y=26)
        
        self.typeFrame = ctk.CTkFrame(self.filterFrame, width=160, height=56, fg_color='transparent')
        self.typeFrame.place(x=176, y=0)

        self.typeLabel = ctk.CTkLabel(self.typeFrame, width=106, height=26, text='Type',
                                    font=('Inter Medium', 12), text_color='#595959', anchor='w')
        self.typeLabel.place(x=4, y=0)
        
        self.typeDropdown = ctk.CTkComboBox(self.typeFrame, 
                                            values=['All', 'Guitar', 'Violin'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA',)
        self.typeDropdown.set('All')
        self.typeDropdown.place(x=0, y=26)
    
    def base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place salesView Frame, do not change this
        
        self.show_firstPage()
        self.show_selection()
        self.show_orderFrame()
        self.search_bar()
        
        self.baseFrame.bind('<Button-1>', lambda event: self.baseFrame.focus_set())
        self.firstPageFrame.bind('<Button-1>', lambda event: self.firstPageFrame.focus_set())
        self.filterFrame.bind('<Button-1>', lambda event: self.filterFrame.focus_set())
        self.selectionTable.bind('<Button-1>', lambda event: self.selectionTable.focus_set())
        self.orderFrame.bind('<Button-1>', lambda event: self.orderFrame.focus_set())

    def clear_form(self):
        self.buyerContactEntry.delete(0, 'end')
        self.buyerNameEntry.delete(0, 'end')
        
        self.selected_products = []
        for frame in self.rowFrames:
            frame.place_forget()
        self.rowFrames = []

    def save_button_clicked(self):
        pass
     
    def search_bar(self):
        self.searchFrame = ctk.CTkFrame(self.firstPageFrame, width=160, height=22, fg_color='transparent')
        self.searchFrame.place(x=349, y=14) 
        
        self.search_query.set('Search')
        
        self.searchEntry = ctk.CTkEntry(self.searchFrame, width=160, height=22,
                                        fg_color='#FAFAFA', border_color='#BCBCBC', 
                                        border_width=2, corner_radius=10, font=('Inter Medium', 11), 
                                        text_color='#959595', textvariable=self.search_query)
        self.searchEntry.place(x=0, y=0) 
        
        def on_entry_click(event):
            if self.searchEntry.get() == 'Search':
                self.searchEntry.delete(0, tk.END)  # Delete all the text in the entry

        def on_focus_out(event):
            if self.searchEntry.get() == '':
                self.search_query.set('Search')

        self.searchEntry.bind('<FocusIn>', on_entry_click)
        self.searchEntry.bind('<FocusOut>', on_focus_out)    
        
        def perform_search():
            query = self.search_query.get()
            if query.strip() != '':
                query = self.search_query.get()
                
                """Insert model/controller here"""
                
                print(f"Performing search for: {query}")
            
        self.searchEntry.bind('<Return>', lambda event: perform_search())
    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
    
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sales Page (Test)")

        self.sales_view = salesView(self.root, None)
        self.sales_view.pack(fill=ctk.BOTH, expand=True)

        self.root.update()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()