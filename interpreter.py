def mini_string_fuck_interpreter(code):
    cleaned_code = ''.join([char for char in code if char == '+' or char == '.'])
    memory_cell = 0
    return_string = ''
    for instruction in cleaned_code:
        if instruction == '+':
            if memory_cell < 255:
                memory_cell +=1
            else:
                memory_cell = 0
        else:
            return_string += chr(memory_cell)
    return return_string
