import itertools
import re

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
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
    # Thay thế các biến trong biểu thức với giá trị tương ứng
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    # Thay thế các toán tử logic để có thể sử dụng eval
    expression = expression.replace('∧', 'and').replace('∨', 'or').replace('¬', 'not').replace('→', '<=')
    
    try:
        return eval(expression)
    except Exception as e:
        return False

# Hàm tạo bảng chân trị
def truth_table(expression):
    # Kiểm tra tính hợp lệ của biểu thức
    if not is_valid_expression(expression):
        print("Biểu thức không hợp lệ.")
        return

    # Tìm tất cả các biến trong biểu thức
    variables = list(set(re.findall(r'[A-Za-z]+', expression)))
    variables.sort()

    # Tạo tất cả các tổ hợp giá trị True/False cho các biến
    table = list(itertools.product([True, False], repeat=len(variables)))

    # In tiêu đề bảng
    header = ' '.join(variables) + ' Kết quả'
    print(header)

    # Tính toán và in kết quả cho mỗi tổ hợp giá trị
    for values in table:
        values_dict = dict(zip(variables, values))
        result = evaluate_expression(expression, values_dict)
        result_str = 'T' if result else 'F'
        print(' '.join(['T' if v else 'F' for v in values]) + ' ' + result_str)

# Hàm nhập biểu thức logic
def input_expression():
    expression = input("Nhập biểu thức logic (ví dụ: (A ∨ ¬B) ∧ C): ").strip()
    truth_table(expression)

# Gọi hàm nhập và xử lý
input_expression()
