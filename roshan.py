import pyperclip

def add_three_numbers():
    clipboard_num = float(pyperclip.paste().strip())

    num1 = 5.0
    num2 = 8.0
    num3 = 11.0

    result = "Min:", clipboard_num + num1, "AVG:", clipboard_num + num2 , "Max:", clipboard_num + num3
    pyperclip.copy(str(result))
    return result

print(add_three_numbers())