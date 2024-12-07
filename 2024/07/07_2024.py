import itertools

def evaluate_expression(numbers, operators):
    """Evaluate an expression formed by numbers and operators left-to-right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def is_possible(test_value, numbers):
    """Check if test_value can be achieved with any combination of + and *."""
    operator_positions = len(numbers) - 1
    for operators in itertools.product(['+', '*'], repeat=operator_positions):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def calculate_total_calibration(file_path):
    """Calculate the total calibration result from the input file."""
    total_calibration_result = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            # Parse the test value and the list of numbers
            if ':' not in line:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            parts = line.strip().split(':')
            try:
                test_value = int(parts[0].strip())
                numbers = list(map(int, parts[1].strip().split()))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            # Check if the equation can be made true
            if is_possible(test_value, numbers):
                total_calibration_result += test_value

    return total_calibration_result

file_path = 'input.txt'
result = calculate_total_calibration(file_path)
print(f"The total calibration result is: {result}")

#The total calibration result is: 850435817339


#####     Part two     #####

import itertools

def evaluate_expression(numbers, operators):
    """Evaluate an expression formed by numbers and operators left-to-right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))  # Concatenate as digits
    return result

def is_possible(test_value, numbers):
    """Check if test_value can be achieved with any combination of +, *, and ||."""
    operator_positions = len(numbers) - 1
    for operators in itertools.product(['+', '*', '||'], repeat=operator_positions):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def calculate_total_calibration(file_path):
    """Calculate the total calibration result from the input file."""
    total_calibration_result = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            # Parse the test value and the list of numbers
            if ':' not in line:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            parts = line.strip().split(':')
            try:
                test_value = int(parts[0].strip())
                numbers = list(map(int, parts[1].strip().split()))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            # Check if the equation can be made true
            if is_possible(test_value, numbers):
                total_calibration_result += test_value

    return total_calibration_result


file_path = 'input.txt'
result = calculate_total_calibration(file_path)
print(f"The total calibration result is: {result}")

#The total calibration result is: 104824810233437