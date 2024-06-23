import customtkinter as ctk
import tkinter as tk
from PIL import Image

class salesView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.active_tab = 1
        self.search_query = tk.StringVar()
        self.selected_product = [] # Tracks all active selections
        self.trashIcon = ctk.CTkImage(light_image=Image.open('./assets/trash.png'), size=(15,15))
        
        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass
    
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
    
    def show_selection(self):
        self.selectionTable = ctk.CTkScrollableFrame(self.firstPageFrame, width=493, height=423, fg_color='transparent')
        self.selectionTable.place(x=0, y=120)
        
        values = [ # Insert values here
            ['Electric Guitar', 'Fendy', '₱900', '10 In Stock'],
            ['Name', 'Brand', 'Price', '5 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '5 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '5 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
            ['Name', 'Brand', 'Price', '0 In Stock'],
        ]
        
        columns = 5 
        frame_width = 83
        frame_height = 126
        x_spacing = 17
        y_spacing = 16

        self.placeholderIcon = ctk.CTkImage(light_image=Image.open('./assets/placeholder.png'), size=(66,66))
        
        for index, (name, brand, price, quantity) in enumerate(values):
            row = index // columns
            col = index % columns
            
            x = col * (frame_width + x_spacing)
            y = row * (frame_height + y_spacing)
            
            self.selectionFrame = ctk.CTkFrame(self.selectionTable,
                                        width=frame_width, height=frame_height,
                                        fg_color='transparent', bg_color='transparent')
            self.selectionFrame.grid(row=row, column=col, padx=7, pady=5)
            
            self.selectionImage = ctk.CTkButton(self.selectionFrame, image=self.placeholderIcon, text='', width=83, height=83,
                                        border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                        fg_color='#FFFFFF', bg_color='#F7F7F7',
                                        hover_color='#FFFFFF', anchor='center',
                                        command=lambda name=name, brand=brand, price=price, quantity=quantity: self.handle_selection(name, brand, price, quantity))
            self.selectionImage.grid(row=0, column=0)
                    
            self.selectionName = ctk.CTkLabel(self.selectionFrame, text=name,
                                            width=80, height=12, font=('Inter Semibold', 10), text_color='#747474')
            self.selectionName.grid(row=1, column=0)
            
            self.selectionBrand = ctk.CTkLabel(self.selectionFrame, text=brand,
                                            width=80, height=7, font=('Inter Semibold', 7), text_color='#747474')
            self.selectionBrand.grid(row=2, column=0)
            
            self.selectionPrice = ctk.CTkLabel(self.selectionFrame, text=price,
                                            width=80, height=10, font=('Inter Semibold', 8), text_color='#747474')
            self.selectionPrice.grid(row=3, column=0)
            
            quantity_value = int(quantity.split()[0]) # 'X In Stock', splits and takes X (number); gives an error if format isn't followed
            
            text_color = '#AE5050' if quantity_value == 0 else ('#E9AC07' if 1 <= quantity_value <= 5 else '#329932')

            self.selectionQuantity = ctk.CTkLabel(self.selectionFrame, text=quantity,
                                            width=80, height=9, font=('Inter Semibold', 9), 
                                            text_color=text_color)
            self.selectionQuantity.grid(row=4, column=0)
    
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
            
    def handle_selection(self, name, brand, price, quantity):
        values = {'name': name, 'brand': brand, 'price': price, 'quantity': quantity} 
        self.selected_product.append(values)  # Tracks all active selections
        
        self.refresh_order_list()
        print("Order List:")
        
        for item in self.selected_product:
            name = item['name']
            brand = item['brand']
            price = item['price']
            quantity = int(item['quantity'].split()[0]) # 'X In Stock', splits and takes X (number); gives an error if format isn't followed
            print(name, brand, price, quantity)
        print()

    def delete_row(self, index):
        if index < len(self.selected_product):
            self.selected_product.pop(index)  # Removes selection from list 'selected_product[]'
        
        self.refresh_order_list()
        print(f"Selection deleted at index: {index}") # For debugging

    def refresh_order_list(self):
        # Clears all selections
        for widget in self.orderListFrame.winfo_children():
            widget.destroy()
        
        # Places all selections after clearing
        for i, item in enumerate(self.selected_product):
            self.create_row(i, item)

    def create_row(self, index, item):
        name = item['name']
        brand = item['brand']
        price = item['price']
        quantity = item['quantity']

        quantity = int(quantity.split()[0])
        print(name, brand, price, quantity) # For debugging
        
        self.rowFrame = ctk.CTkFrame(self.orderListFrame, width=285, height=40, fg_color='transparent')
        self.rowFrame.place(x=0, y=index * 40)

        self.deleteButton = ctk.CTkButton(self.rowFrame, image=self.trashIcon, text='', width=15, height=15,
                                    border_width=0, fg_color='transparent', corner_radius=0,
                                    hover_color='#000000', anchor='center',
                                    command=lambda i=index: self.delete_row(i))
        self.deleteButton.place(x=3, y=8)

        self.rowLine = ctk.CTkFrame(self.rowFrame, width=285, height=2, fg_color='#E9E9E9')
        self.rowLine.place(x=0, y=39)
        
            
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