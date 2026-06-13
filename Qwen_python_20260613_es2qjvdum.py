from src.ccid_calculator import CompositeCIDCalculator

calculator = CompositeCIDCalculator()
result = calculator.calculate_ccid('reference.png', 'generated.png')
print(result.message)