
import re

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
    # Biểu thức hợp lệ phải chứa các ký hiệu phù hợp và dấu ngoặc phải cân bằng
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz∧∨→¬() ')
    if not all(c in valid_chars for c in expression):
        return False

    # Kiểm tra dấu ngoặc
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    # Nếu stack còn lại không rỗng thì có ngoặc không đóng
    return len(stack) == 0

# Hàm tính toán giá trị biểu thức logic
def evaluate_expression(expression, values):
    # Thay thế các biến bằng giá trị tương ứng
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    # Thay thế các toán tử logic để có thể sử dụng eval
    expression = expression.replace('∧', 'and').replace('∨', 'or').replace('¬', 'not').replace('→', '<=')
    
    # Tính giá trị biểu thức bằng eval
    try:
        return eval(expression)
    except Exception as e:
        return False

# Hàm chính xử lý biểu thức
def process_logic_expression(expression, values):
    if is_valid_expression(expression):
        result = evaluate_expression(expression, values)
        print(f"Biểu thức hợp lệ. Kết quả: {result}")
    else:
        print("Biểu thức không hợp lệ.")

# Hàm nhập biểu thức và giá trị của các biến
def input_expression_and_values():
    # Nhập biểu thức logic
    expression = input("Nhập biểu thức logic (ví dụ: (A ∧ B) → ¬C): ")

    # Nhập các giá trị của các biến logic
    values = {}
    variables = re.findall(r'[A-Za-z]+', expression)  # Tìm tất cả các biến trong biểu thức
    variables = list(set(variables))  # Lọc ra các biến duy nhất

    print("Nhập giá trị cho các biến:")
    for var in variables:
        while True:
            try:
                val = input(f"{var} (True/False): ").strip()
                # Chuyển đổi giá trị nhập thành True hoặc False
                if val.lower() == 'true':
                    values[var] = True
                    break
                elif val.lower() == 'false':
                    values[var] = False
                    break
                else:
                    print("Vui lòng nhập 'True' hoặc 'False'.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    
    # Xử lý biểu thức với giá trị vừa nhập
    process_logic_expression(expression, values)

# Gọi hàm nhập và xử lý
input_expression_and_values()