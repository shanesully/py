# shanesully
# Kinda bad gui version of the calculator
 
from Tkinter import *
from ttk import Frame, Button, Style
 
class CalculatorGUI(Frame):
    '''
    Simple tkinter gui wrapper for calculator objects
    '''
 
    def __init__(self, parent):
        Frame.__init__(self, parent)
 
        self.parent = parent
 
        # GUI instance's calculator
        self.calculator = Calculator()
 
        # Static label
        self.parent.title("Calculator")
        self.centerWindow()
 
        self.style = Style()
        self.style.theme_use("default")
 
        # Static label
        self.greet = Label(parent, text="Equation:")
        self.greet.grid(row=0, column=0)
 
        # Equation field
        self.equationField = Entry(parent)
        self.equationField.grid(row=0, column=1)
 
        # Calculator enter button
        self.evalButton = Button(parent, text="Calculate", command=self.eval_entry)
        self.evalButton.grid(row=1, column=1)
 
        # Static label 
        self.result_label = Label(parent, text="Result: ")
        self.result_label.grid(row=2, column=0)
 
        # Dynamic label 
        self.result_value = Label(parent)
        self.result_value.grid(row=2, column=1)
 
        # Clear button
        self.clearButton = Button(parent, text="Clear", command=self.clear)
        self.clearButton.grid(row=3, column=1)
         
    def centerWindow(self):
        '''
        Center the GUI window on screen
        '''
 
        # Positional coordinates
        w = 290
        h = 150
 
        # Screen size properties
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
 
        # Calculated coordinates
        x = (sw - w)/2
        y = (sh - h)/2
 
        # Update actual coordinates
        self.parent.geometry("{}x{}+{}+{}".format(w, h, x, y))
         
    def clear(self):
        '''
        Clear all UI I/O elements
        '''
         
        # Clear equation field
        self.equationField.delete(0, 'end')
 
        # Clear result 
        self.result_value.configure(text="")
 
 
    def eval_entry(self):
        '''
        Evaluate a given equation
        '''
 
        try:
            # Get and evaluate an equation
            if self.calculator.evaluate(self.equationField.get()):
                result = self.calculator.evaluate(self.equationField.get())
 
                # Show the result
                self.result_value.configure(text = result)
            else:
                pass
        except:
            # Harmless empty expression
            pass
 
 
class tokenized_expression():
    '''
    Tokenized equation stack object
    '''
 
    def __init__(self):
         
        self.operator_stack = []
        self.operand_stack = []
 
 
def parse_expression(expression):
        '''
        Parse a given expression to populate operator and
        operand stacks
        '''
 
        parsed_expression = tokenized_expression()
 
        # Python's supported operators
        legal_operators = ['+', '-', '*', '/', '%', '**', '//']
 
        try:
            # Populate stacks
            for x in expression:
                if x in legal_operators:
                    parsed_expression.operator_stack.append(x)
                elif x.isdigit():
                    parsed_expression.operand_stack.append(x)
                else:
                    # Probably not number
                    pass              
        except:
            raise StandardError
 
 
class Calculator(object):
    '''
    Simple stack-based calculator with support  for Polish Prefix and 
    Reverse Polish notations
     
    Calculator objects hold the all information for a single expression
    '''
 
 
    def __init__(self):
 
        self.operator_stack = []
        self.operand_stack = []
     
 
    def get_expression(self):
        # Get an expression from the user and format it for our LIFO parser
        self.expression = reversed([ x for x in raw_input("Enter expression: ").split(' ') ])
 
 
    def parse(self):
        '''
        Parse incoming expression to populate operator and
        operand stacks
        '''
 
        # Python's supported operators
        legal_operators = ['+', '-', '*', '/', '%', '**', '//']
 
        try:
            # Populate stacks
            for x in self.expression:
                if x in legal_operators:
                    self.operator_stack.append(x)
                elif x.isdigit():
                    self.operand_stack.append(x)
                else:
                    # Probably not number
                    pass              
        except:
            raise StandardError
 
 
    def evaluate(self, expression):
        '''
        Evaluate the expression
        '''
        # self.get_expression()
        self.expression = reversed([ x for x in expression.split(' ') ])
 
        self.parse()
 
        try:
            # Initialize the result using the first operand on the stack
            self.result = self.operand_stack.pop()
             
            while self.operand_stack:
                operator = self.operator_stack.pop()
                operand = self.operand_stack.pop()
 
                # self.result must be cast to str as eval itself returns int
                self.result = eval(str(self.result) + operator + operand)
 
            return self.result
        except:
            # Probably an invalid expression
            raise StandardError
         
 
    def debug(self):
        '''
        Display object state
        '''
 
        print "Operators: {}\nOperands: {}\n".format(self.operator_stack, self.operand_stack)
 
 
def main():
 
    root = Tk()
    root.geometry("250x150+300+300")
    app = CalculatorGUI(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
