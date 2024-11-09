from breezypythongui import EasyFrame
import math
import tkinter as tk




class TempCalc(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self, title = """Temperature Converter""")

        self.addLabel(text = "Farenheight",
                      row = 0, column = 1)
        self.farenheight = self.addFloatField(value = 32.0,
                                               row = 1,
                                               column = 1,
                                               width = 10)
        self.addLabel(text = "Celcius",
                      row = 0, column = 0)
        self.celcius = self.addFloatField(value = 0,
                                               row = 1,
                                               column = 0,
                                               width = 10)
        self.addLabel(text = "C",
                      row = 0, column = 0)
        self.celcius = self.addFloatField(value = 0,
                                               row = 1,
                                               column = 0,
                                               width = 10) 
        self.addButton(text = "<<<<<", row = 3, column = 0,
                       columnspan = 1, command = self.farToCel)
        self.addButton(text = ">>>>>", row = 3, column = 1,
                       columnspan = 1, command = self.celToFar)

    def farToCel(self):
        farenheight = self.farenheight.getNumber()
        celcius = self.celcius.getNumber()
        farConversion = (farenheight - 32) * 5/9
        self.celcius.setNumber(farConversion)
    def celToFar(self):
        farenheight = self.farenheight.getNumber()
        celcius = self.celcius.getNumber()
        farConversion = (celcius * 9/5) + 32
        self.farenheight.setNumber(farConversion)


        
        
def main():
    TempCalc().mainloop()

if __name__ == "__main__":
    main()
