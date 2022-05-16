#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


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
            exportselection="true", font="TkMenuFont", textvariable=self.count
        )
        self.entry6.pack(side="top")
        self.AreaX = tk.Label(self.areaCountFrame)
        self.AreaX.configure(cursor="based_arrow_down", relief="flat", text="AreaX")
        self.AreaX.pack(side="top")
        self.width = tk.Entry(self.areaCountFrame)
        self.areaW = tk.IntVar(value="")
        self.width.configure(font="TkDefaultFont", textvariable=self.areaW)
        self.width.pack(side="top")
        self.AreaY = tk.Label(self.areaCountFrame)
        self.AreaY.configure(text="AreaY")
        self.AreaY.pack(side="top")
        self.height = tk.Entry(self.areaCountFrame)
        self.areaH = tk.IntVar(value="")
        self.height.configure(
            exportselection="false",
            font="TkDefaultFont",
            show="0",
            textvariable=self.areaH,
        )
        self.height.pack(side="top")
        self.areaCountFrame.configure(height="200", width="200")
        self.areaCountFrame.grid(column="0", row="0")
        self.pickMaterialFrame = ttk.Frame(self.inputFrame)
        self.materialLabel = tk.Label(self.pickMaterialFrame)
        self.materialLabel.configure(text="What material\nDo you want?")
        self.materialLabel.pack(side="top")
        self.selectPaper = tk.Radiobutton(self.pickMaterialFrame)
        self.paperPrice = tk.IntVar(value=1)
        self.selectPaper.configure(
            compound="top", offrelief="flat", text="Paper", value="1"
        )
        self.selectPaper.configure(variable=self.paperPrice)
        self.selectPaper.pack(anchor="w", side="top")
        self.selectLam = tk.Radiobutton(self.pickMaterialFrame)
        self.selectLam.configure(text="Laminated", value="3", variable=self.paperPrice)
        self.selectLam.pack(side="top")
        self.selectPVC = tk.Radiobutton(self.pickMaterialFrame)
        self.selectPVC.configure(
            cursor="boat", indicatoron="true", text="PVC", value="35"
        )
        self.selectPVC.configure(variable=self.paperPrice)
        self.selectPVC.pack(anchor="w", side="top")
        self.pickMaterialFrame.configure(height="200", width="200")
        self.pickMaterialFrame.grid(column="1", row="0")
        self.inputFrame.configure(height="200", text="Inputframe", width="200")
        self.inputFrame.pack(fill="x", side="top")
        self.calcButton = tk.Button(self.Programframe)
        self.calcButton.configure(
            anchor="e", cursor="based_arrow_down", default="normal", state="normal"
        )
        self.calcButton.configure(text="hit to calculate")
        self.calcButton.pack(anchor="w", side="top")
        self.calcButton.configure(command=self.calculate)
        self.labelframe6 = ttk.Labelframe(self.Programframe)
        self.label6 = tk.Label(self.labelframe6)
        self.label6.configure(text="Your Poster Costs")
        self.label6.pack(side="left")
        self.priceOutput = tk.Text(self.labelframe6)
        self.priceOutput.configure(height="1", width="10")
        self.priceOutput.pack(side="top")
        self.labelframe6.configure(height="200", text="Output", width="400")
        self.labelframe6.pack(expand="false", fill="x", side="top")
        self.Programframe.configure(height="400", width="800")
        self.Programframe.pack(side="top")

        # Main widget
        self.mainwindow = self.Programframe

    def run(self):
        self.mainwindow.mainloop()

    def calculate(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Pyui3App(root)
    app.run()
