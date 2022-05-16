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
        self.AreaX = tk.Label(self.areaCountFrame)
        self.AreaX.configure(cursor="based_arrow_down", relief="flat", text="AreaX")
        self.AreaX.pack(side="top")
        self.entry7 = tk.Entry(self.areaCountFrame)
        self.areaW = tk.IntVar(value="")
        self.entry7.configure(font="TkDefaultFont", show="0", textvariable=self.areaW)
        self.entry7.pack(side="top")
        self.AreaY = tk.Label(self.areaCountFrame)
        self.AreaY.configure(text="AreaY")
        self.AreaY.pack(side="top")
        self.entry5 = tk.Entry(self.areaCountFrame)
        self.areaH = tk.IntVar(value="")
        self.entry5.configure(
            font="TkDefaultFont", show="0", state="normal", textvariable=self.areaH
        )
        self.entry5.pack(side="top")
        self.label5 = tk.Label(self.areaCountFrame)
        self.label5.configure(text="How Many")
        self.label5.pack(side="top")
        self.entry6 = tk.Entry(self.areaCountFrame)
        self.count = tk.IntVar(value="")
        self.entry6.configure(font="TkDefaultFont", textvariable=self.count)
        self.entry6.pack(side="top")
        self.areaCountFrame.configure(height="200", width="200")
        self.areaCountFrame.grid(column="0", row="0")
        self.pickMaterialFrame = ttk.Frame(self.inputFrame)
        self.MaterialLabel = tk.Label(self.pickMaterialFrame)
        self.MaterialLabel.configure(text="What material\nDo you want?")
        self.MaterialLabel.pack(side="top")
        self.selectPaper = tk.Radiobutton(self.pickMaterialFrame)
        self.paperchoice = tk.IntVar(value=1)
        self.selectPaper.configure(
            compound="top", offrelief="flat", text="Paper", value="1"
        )
        self.selectPaper.configure(variable=self.paperchoice)
        self.selectPaper.pack(anchor="w", side="top")
        self.selectLam = tk.Radiobutton(self.pickMaterialFrame)
        self.selectLam.configure(text="Laminated", value="2", variable=self.paperchoice)
        self.selectLam.pack(side="top")
        self.selectPVC = tk.Radiobutton(self.pickMaterialFrame)
        self.selectPVC.configure(
            cursor="boat", indicatoron="true", text="PVC", value="3"
        )
        self.selectPVC.configure(variable=self.paperchoice)
        self.selectPVC.pack(anchor="w", side="top")
        self.pickMaterialFrame.configure(height="200", width="200")
        self.pickMaterialFrame.grid(column="1", row="0")
        self.inputFrame.configure(height="200", text="Inputframe", width="200")
        self.inputFrame.pack(fill="x", side="top")
        self.CalcButton = tk.Button(self.Programframe)
        self.CalcButton.configure(
            anchor="e",
            cursor="based_arrow_down",
            relief="raised",
            text="hit to calculate",
        )
        self.CalcButton.pack(anchor="w", side="top")
        self.labelframe6 = ttk.Labelframe(self.Programframe)
        self.label6 = tk.Label(self.labelframe6)
        self.label6.configure(text="Your Poster Costs")
        self.label6.pack(side="left")
        self.PriceOutput = tk.Text(self.labelframe6)
        self.PriceOutput.configure(height="1", width="10")
        self.PriceOutput.pack(side="top")
        self.labelframe6.configure(height="200", text="Output", width="400")
        self.labelframe6.pack(expand="false", fill="x", side="top")
        self.Programframe.configure(height="400", width="800")
        self.Programframe.pack(side="top")

        # Main widget
        self.mainwindow = self.Programframe

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Pyui3App(root)
    app.run()
