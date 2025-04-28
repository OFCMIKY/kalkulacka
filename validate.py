class ValidateInput:
    def __init__(self):
        self.input_data = None
        self.valid_operations = ["+", "-", "*", "/", "^"]
        self.valid_numbers = set(range(-1000, 1001))
        self.valid_input = False
        self.error_message = None
        self.numbers = []
        self.operation = None
    
    def validate_numbers(self, numbers):
        return_numbers = []
        for number in numbers:
            if not number.isnumeric():
                self.error_message = f"Invalid number: {number}."
                return [False, self.error_message]
            else:
                return_numbers.append(float(number))
        return [True, return_numbers]
    
    def validate_operation(self, operation):
        if operation not in self.valid_operations:
            self.error_message = f"Invalid operation: {operation}. Must be one of {self.valid_operations}."
            return [False, self.error_message]
        return [True, operation]
    

    