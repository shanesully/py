'''
@shanesully
Calculator program
'''


class Calculator(object):
    '''
    Simple stack-based calculator which supports infix, Polish Prefix and 
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


    def evaluate(self):
        '''
        Evaluate the expression
        '''
        self.get_expression()
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
    a_calculator = Calculator()

    print a_calculator.evaluate()

if __name__ == '__main__':
    main()

