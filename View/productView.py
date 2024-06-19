import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

class productView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.importIcon = ctk.CTkImage(light_image=Image.open('./assets/import.png'), size=(80,73))

        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):
        self.productFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.productFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this
        
        self.show_productReg()
        self.show_productGraph()
        self.show_reports()
        self.show_productTable()
        
    def show_productReg(self):
        self.icon = ctk.CTkImage(light_image=Image.open('./assets/plus.png'), size=(15,15)) # Icon implementation
        
        self.productRegFrame = ctk.CTkFrame(self.productFrame, width=209, height=594, fg_color='#F7F7F7', corner_radius=7)
        self.productRegFrame.place(x=12, y=10)
        
        self.imageFrame = ctk.CTkFrame(self.productRegFrame, width=128, height=128, fg_color='transparent')
        self.imageFrame.place(x=40, y=44)
        
        self.imageButton = ctk.CTkButton(self.imageFrame, image=self.importIcon, text='', width=128, height=128,
                                         border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                         fg_color='#FFFFFF', bg_color='#F7F7F7',
                                         hover_color='#FFFFFF', command=self.select_image,
                                         anchor='center')
        self.imageButton.place(x=0, y=0)
        
        self.nameFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.nameFrame.place(x=24, y=186)
        
        self.nameLabel = ctk.CTkLabel(self.nameFrame, text='Product Name', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.nameLabel.place(x=5, y=0)
        
        self.nameEntry = ctk.CTkEntry(self.nameFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959')
        self.nameEntry.place(x=0, y=26)
    
        self.brandFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.brandFrame.place(x=24, y=250)
        
        self.brandButton = ctk.CTkButton(self.brandFrame, image=self.icon, text='', width=15, height=15, 
                                        fg_color='transparent', hover_color='#F7F7F7', anchor='center')
        self.brandButton.place(x=36, y=1)
        
        self.brandLabel = ctk.CTkLabel(self.brandFrame, text='Brand', font=('Inter Medium', 12), text_color='#595959',
                                          width=34, height=26, bg_color='transparent', anchor='w')
        self.brandLabel.place(x=5, y=0)
        
        self.brandDropdown = ctk.CTkComboBox(self.brandFrame, 
                                            values=['Placeholder', 'Placeholder'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA')
        self.brandDropdown.set('Select')
        self.brandDropdown.place(x=0, y=26)
        
        self.typeFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.typeFrame.place(x=24, y=314)
                
        self.typeButton = ctk.CTkButton(self.typeFrame, image=self.icon, text='', width=15, height=15, 
                                        fg_color='transparent', hover_color='#F7F7F7', anchor='center')
        self.typeButton.place(x=80, y=1)
        
        self.typeLabel = ctk.CTkLabel(self.typeFrame, text='Product Type', font=('Inter Medium', 12), text_color='#595959',
                                          width=80, height=26, bg_color='transparent', anchor='w')
        self.typeLabel.place(x=5, y=0)
        
        self.typeDropdown = ctk.CTkComboBox(self.typeFrame, 
                                            values=['Placeholder', 'Placeholder'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA')
        self.typeDropdown.set('Select')
        self.typeDropdown.place(x=0, y=26)
        
        self.quantityFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.quantityFrame.place(x=24, y=378)
        
        self.quantityLabel = ctk.CTkLabel(self.quantityFrame, text='Initial Quantity', font=('Inter Medium', 12), text_color='#595959',
                                          width=106, height=26, bg_color='transparent', anchor='w')
        self.quantityLabel.place(x=5, y=0)
        
        self.quantityEntry = ctk.CTkEntry(self.quantityFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959')
        self.quantityEntry.place(x=0, y=26)
        
        self.priceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.priceFrame.place(x=24, y=442)
        
        self.priceLabel = ctk.CTkLabel(self.priceFrame, text='Price', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.priceLabel.place(x=5, y=0)
        
        self.priceEntry = ctk.CTkEntry(self.priceFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959')
        self.priceEntry.place(x=0, y=26)
        
        self.buttonFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=26, bg_color='transparent', fg_color='transparent')
        self.buttonFrame.place(x=24, y=532)    
        
        self.clearButton = ctk.CTkButton(self.buttonFrame, width=72, height=26, bg_color='transparent', 
                                         fg_color='#E2E2E2', hover_color='#D5D5D5', corner_radius=7,
                                         text='Clear', font=('Consolas', 12), text_color='#595959', 
                                         command=self.clear_form)
        self.clearButton.place(x=0, y=0)
        
        self.saveButton = ctk.CTkButton(self.buttonFrame, width=72, height=26,  bg_color='transparent',
                                        fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=7,
                                        text='Save', font=('Consolas', 12), text_color='#F7F7F7',
                                        )
        self.saveButton.place(x=88, y=0)
        
        self.label = ctk.CTkLabel(self.productRegFrame, text="Add Products", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
        
    def show_productGraph(self):
        self.productGraphFrame = ctk.CTkFrame(self.productFrame, width=382, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.productGraphFrame.place(x=231, y=10)
        
        self.label = ctk.CTkLabel(self.productGraphFrame, text="Stock Graph", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.productFrame, width=207, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=622, y=10)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def show_productTable(self):
        self.productTableFrame = ctk.CTkFrame(self.productFrame, width=598, height=352, fg_color='#F7F7F7', corner_radius=7)
        self.productTableFrame.place(x=231, y=252)
        
        self.label = ctk.CTkLabel(self.productTableFrame, text="Stock Levels", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        
        if file_path:
            selected_image = Image.open(file_path)
            img_width, img_height = 110, 110
            aspect_ratio = selected_image.width / selected_image.height
            
            if aspect_ratio > 1:
                # If width > height
                new_width = img_width
                new_height = int(img_width / aspect_ratio)
            else:
                # If width < height
                new_height = img_height
                new_width = int(img_height * aspect_ratio)
            
            resized_image = selected_image.resize((new_width, new_height))
            print(f"New image size: {new_width}x{new_height}")
            new_image = ctk.CTkImage(light_image=resized_image, size=(new_width, new_height))
            
            self.imageButton.configure(image=new_image)
        else: 
            # Defaults to import icon if none is selected
            self.imageButton.configure(image=self.importIcon)
    
    def clear_form(self):
        self.imageButton.configure(image=self.importIcon)
        self.nameEntry.delete(0, 'end')
        self.brandDropdown.set('Select')
        self.typeDropdown.set('Select')
        self.quantityEntry.delete(0, 'end')
        self.priceEntry.delete(0, 'end')
      
        
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Products Page (Test)")
        
        self.product_view = productView(self.root, None)
        self.product_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()