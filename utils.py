# 工具函数模块 V3

def add(a, b):
    return a + b

def multiply(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def greet(name):
    return f"Hello, {name}! V3!"
