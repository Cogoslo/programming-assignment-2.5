#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import decimal
import re


class Pyui3App:
    def __init__(self, master=None):
        # build ui
        self.Programframe = ttk.Frame(master)
        self.Label = tk.Label(self.Programframe)
        self.Label.configure(compound="bottom", text="Calc Program")
        self.Label.pack(side="top")
        self.inputFrame = ttk.Labelframe(self.Programframe)
        self.areaCountFrame = ttk.Frame(self.inputFrame)
        self.label5 = tk.Label(self.areaCountFrame)
        self.label5.configure(text="How Many")
        self.label5.pack(side="top")
        self.entry6 = tk.Entry(self.areaCountFrame)
        self.count = tk.IntVar(value="")
        self.entry6.configure(
            font="TkMenuFont", textvariable=self.count, validate="all"
        )
        self.entry6.pack(side="top")
        _validatecmd = (self.entry6.register(self.vcmd), "%p_entry_value")
        self.entry6.configure(validatecommand=_validatecmd)
        self.AreaX = tk.Label(self.areaCountFrame)
        self.AreaX.configure(relief="flat", text="Height")
        self.AreaX.pack(side="top")
        self.width = tk.Entry(self.areaCountFrame)
        self.areaW = tk.IntVar(value="")
        self.width.configure(
            font="TkDefaultFont", textvariable=self.areaW, validate="all"
        )
        self.width.pack(side="top")
        _validatecmd = (self.width.register(self.vcmd), "%p_entry_value")
        self.width.configure(validatecommand=_validatecmd)
        self.AreaY = tk.Label(self.areaCountFrame)
        self.AreaY.configure(text="Width")
        self.AreaY.pack(side="top")
        self.height = tk.Entry(self.areaCountFrame)
        self.areaH = tk.IntVar(value="")
        self.height.configure(
            font="TkDefaultFont", textvariable=self.areaH, validate="all"
        )
        self.height.pack(side="top")
        _validatecmd = (self.height.register(self.vcmd), "%p_entry_value")
        self.height.configure(validatecommand=_validatecmd)
        self.areaCountFrame.configure(height="200", width="200")
        self.areaCountFrame.grid(column="0", row="0")
        self.pickMaterialFrame = ttk.Frame(self.inputFrame)
        self.materialLabel = tk.Label(self.pickMaterialFrame)
        self.materialLabel.configure(text="What material\nDo you want?")
        self.materialLabel.pack(side="top")
        self.selectPaper = tk.Radiobutton(self.pickMaterialFrame)
        self.paperPrice = tk.DoubleVar(value=1)
        self.selectPaper.configure(text="Paper", value="1", variable=self.paperPrice)
        self.selectPaper.pack(anchor="w", side="top")
        self.selectLam = tk.Radiobutton(self.pickMaterialFrame)
        self.selectLam.configure(text="Laminated", value="5", variable=self.paperPrice)
        self.selectLam.pack(side="top")
        self.selectPVC = tk.Radiobutton(self.pickMaterialFrame)
        self.selectPVC.configure(text="PVC", value="35", variable=self.paperPrice)
        self.selectPVC.pack(anchor="w", side="top")
        self.pickMaterialFrame.configure(height="200", width="200")
        self.pickMaterialFrame.grid(column="1", row="0")
        self.inputFrame.configure(height="200", text="Inputframe", width="200")
        self.inputFrame.pack(fill="x", side="top")
        self.calcButton = tk.Button(self.Programframe)
        self.calcButton.configure(anchor="e", text="hit to calculate")
        self.calcButton.pack(anchor="w", side="top")
        self.calcButton.configure(command=self.calculate)
        self.labelframe6 = ttk.Labelframe(self.Programframe)
        self.label6 = tk.Label(self.labelframe6)
        self.label6.configure(text="Your Poster Costs")
        self.label6.pack(side="left")
        self.priceOutput = tk.Text(self.labelframe6)
        self.priceOutput.configure(font="TkFixedFont", height="2", width="10")
        self.priceOutput.pack(side="top")
        self.labelframe6.configure(height="200", text="Output", width="400")
        self.labelframe6.pack(expand="false", fill="x", side="top")
        self.frame1 = ttk.Frame(self.Programframe)
        self.InputFrame = ttk.Labelframe(self.frame1)
        self.HonInputLabel = ttk.Label(self.InputFrame)
        self.HonInputLabel.configure(text="Title")
        self.HonInputLabel.pack(side="top")
        self.titleCombo = ttk.Combobox(self.InputFrame)
        self.titleCombo.configure(values="Mr  Mrs Miss Dr Sit Mx")
        self.titleCombo.pack(side="top")
        self.label9 = ttk.Label(self.InputFrame)
        self.label9.configure(text="First Name")
        self.label9.pack(side="top")
        self.nameEntry = ttk.Entry(self.InputFrame)
        self.nameEntry.pack(side="top")
        self.label10 = ttk.Label(self.InputFrame)
        self.label10.configure(text="Surname")
        self.label10.pack(side="top")
        self.surnameEntry = ttk.Entry(self.InputFrame)
        self.surnameEntry.pack(side="top")
        self.label11 = ttk.Label(self.InputFrame)
        self.label11.configure(text="Address Line 1")
        self.label11.pack(side="top")
        self.addr1Entry = ttk.Entry(self.InputFrame)
        self.addr1Entry.pack(side="top")
        self.label12 = ttk.Label(self.InputFrame)
        self.label12.configure(text="Address Line 2")
        self.label12.pack(side="top")
        self.addr2Entry = ttk.Entry(self.InputFrame)
        self.addr2Entry.pack(side="top")
        self.label13 = ttk.Label(self.InputFrame)
        self.label13.configure(text="Phone Number")
        self.label13.pack(side="top")
        self.phone = ttk.Entry(self.InputFrame)
        self.phone.configure(validate="all")
        self.phone.pack(side="top")
        _validatecmd = (self.phone.register(self.vcmd), "%p_entry_value")
        self.phone.configure(validatecommand=_validatecmd)
        self.InputFrame.configure(height="200", text="User Input Frame", width="200")
        self.InputFrame.grid(column="0", row="0")
        self.Userinfooutputframe = ttk.Labelframe(self.frame1)
        self.Userinfooutputlabel = ttk.Label(self.Userinfooutputframe)
        self.Userinfooutputlabel.configure(text="User Info Output")
        self.Userinfooutputlabel.pack(side="top")
        self.InfoOutput = tk.Text(self.Userinfooutputframe)
        self.InfoOutput.configure(height="10", width="20", state='normal')
        self.InfoOutput.pack(side="top")
        self.Userinfooutputframe.configure(height="200", width="200")
        self.Userinfooutputframe.grid(column="1", row="0")
        self.frame1.configure(height="200", width="200")
        self.frame1.pack(anchor="e", side="left")
        self.Programframe.configure(height="400", width="800")
        self.Programframe.pack(side="top")

        # Main widget
        self.mainwindow = self.Programframe

    def run(self):
        self.mainwindow.mainloop()

    def calculate(self):
        self.InfoOutput.delete('1.0',tk.END)
        Title =  self.titleCombo.get()
        FirstName =  self.nameEntry.get()
        Surname = self.surnameEntry.get()
        Addr1 = self.addr1Entry.get()
        Addr2 = self.addr2Entry.get()
        Phone = self.phone.get()
        TotalUser= (Title + FirstName + Surname + "\n" + Addr1 + "\n" + Addr2 + "\n" + Phone )
        if self.titleCombo.get() and self.nameEntry.get() and self.surnameEntry.get() and self.addr1Entry.get() and self.addr2Entry.get() and self.phone.get().isdigit:
            self.InfoOutput.insert('1.0', TotalUser)
        else:
            self.InfoOutput.insert('1.0', 'User Info Missing\nOr Formatted Wrong')



        self.priceOutput.delete('1.0',tk.END)
        if not self.entry6.get().isdigit() or not self.width.get().isdigit() or not self.width.get().isdigit():
            self.priceOutput.insert('1.0', 'bad input')
        Xarea=int(self.width.get())
        Yarea=int(self.height.get())
        iterationcount=1
        count=int(self.entry6.get())
        materialprice=decimal
        materialprice=(self.paperPrice.get())
        price=decimal
        price=0
        priceoutput=float
        while iterationcount < count:

            while iterationcount <= 10:
                price = price + (((Xarea+Yarea)*0.03)+materialprice)
                iterationcount += 1
            if count > 10:
                price = price + (((Xarea+Yarea)*0.0075)+materialprice)
                iterationcount += 1
        priceoutput=round(price, 2)
        self.priceOutput.insert('1.0', priceoutput)
        if count < 10:
            self.priceOutput.insert('1.0', 'Count < 10')


    def vcmd(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Pyui3App(root)
    app.run()
