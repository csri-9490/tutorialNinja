def expand_string(input_str):
    result = ''
    current_char = ''
    current_count_str = ''
    for char in input_str:
        if char.isalpha():
            if current_count_str:
                result += current_char + chr(ord(current_char) + int(current_count_str))
                current_count_str = ''
            current_char = char
        elif char.isdigit():
            current_count_str += char
    if current_count_str:
        result += current_char + chr(ord(current_char) + int(current_count_str))
    return result
input_str = "a4k3b2"
output_str = expand_string(input_str)
print(output_str)
