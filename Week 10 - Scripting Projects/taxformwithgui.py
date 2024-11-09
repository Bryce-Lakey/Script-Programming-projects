from breezypythongui import EasyFrame
import math

class TaxForm(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = """Tax Form""")

        self.addLabel(text = "Gross income",
                      row = 0, column = 0)
        self.grossIncomeField = self.addIntegerField(value = 0,
                                               row = 0,
                                               column = 1,
                                               width = 20)

        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.dependentsField = self.addIntegerField(value = 0,
                                               row = 1,
                                               column = 1,
                                               width = 20)

        self.addButton(text = "Compute", row = 3, column = 0,
                       columnspan = 2, command = self.tax)


        self.addLabel(text = "Result",
                      row = 4, column = 0)
        self.resultField = self.addFloatField(value = 0.0,
                                               row = 4,
                                               column = 1,
                                               width = 20,
                                                precision = 2,
                                                state = "readonly")
    def tax(self):
        income = self.grossIncomeField.getNumber()
        dependents = self.dependentsField.getNumber()
        taxResult = income / 6.9 * dependents
        self.resultField.setNumber(taxResult)
        
    
        
        
def main():
    TaxForm().mainloop()

if __name__ == "__main__":
    main()
