def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
      raise ZeroDivisionError("Деление на ноль!")
  return a / b

def power(a, b):
  return a ** b

def validate_operation(op):
  allowed = ("1", "2", "3", "4", "5", "q")
  if op not in allowed:
      raise ValueError("Неизвестная операция!")
  return op

def get_number(value):
  try:
      return float(value)
  except ValueError:
      raise ValueError("Нужно вводить число!")
