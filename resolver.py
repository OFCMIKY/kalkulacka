class Resolver:
    def __init__(self):
        self.numbers = []
        self.operation = None
 
    def calculate(self, numbers, operation):
        self.numbers = numbers
        print(self.numbers)
        self.procese_opration(operation)

    def procese_opration(self, operation):
        if (operation == "+"):
            self.operation = 'add'
        elif (operation == "-"):    
            self.operation = 'subtract'
        elif (operation == "*"):
            self.operation = 'multiply'
        elif (operation == "/"):
            self.operation = 'divide'
        elif(operation == "^"):
            self.operation = 'power'
        else:
            raise ValueError("Invalid operation")


    # The constructor initializes the numbers and operation attributes.
    def resolve(self):
        if self.operation == 'add':
            return sum(self.numbers)
        elif self.operation == 'subtract':
            return self.numbers[0] - sum(self.numbers[1:])
        elif self.operation == 'multiply':
            result = 1
            for number in self.numbers:
                result *= number
            return result
        elif self.operation == 'divide':
            result = self.numbers[0]
            for number in self.numbers[1:]:
                result /= number
            return result
        elif self.operation == 'power':
            result = self.numbers[0]
            for number in self.numbers[1:]:
                result **= number
            return result
        else:
            raise ValueError("Invalid operation")

