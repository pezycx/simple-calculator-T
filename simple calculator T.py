def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("不能除以零！")
    return x / y

def main():
    print("欢迎使用简单计算器！")
    print("支持的操作：+ (加), - (减), * (乘), / (除)")
    
    try:
        num1 = float(input("请输入第一个数字: "))
        operation = input("请输入操作符: ")
        num2 = float(input("请输入第二个数字: "))
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            raise ValueError("无效的操作符！")
        
        print(f"结果: {result}")
    except ValueError as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"意外错误: {e}")

if __name__ == "__main__":
    main()