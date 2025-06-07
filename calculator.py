

def calculate_expression(expr):
    # Remove spaces
    expr = expr.replace(" ", "")

    # Convert the string to a list of tokens
    def tokenize(expr):
        tokens = []
        num = ''
        for char in expr:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    tokens.append(float(num))
                    num = ''
                tokens.append(char)
        if num:
            tokens.append(float(num))
        return tokens

    # Perform multiplication, division, and modulus first
    def handle_mul_div(tokens):
        new_tokens = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '*':
                result = new_tokens.pop() * tokens[i + 1]
                new_tokens.append(result)
                i += 2
            elif tokens[i] == '/':
                if tokens[i + 1] == 0:
                    return "Error: Division by zero"
                result = new_tokens.pop() / tokens[i + 1]
                new_tokens.append(result)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        return new_tokens

    # Perform addition and subtraction
    def handle_add_sub(tokens):
        result = tokens[0]
        i = 1
        while i < len(tokens):
            op = tokens[i]
            val = tokens[i + 1]
            if op == '+':
                result += val
            elif op == '-':
                result -= val
            i += 2
        return result

    try:
        tokens = tokenize(expr)
        tokens = handle_mul_div(tokens)
        if isinstance(tokens, str):  # Error message
            return tokens
        result = handle_add_sub(tokens)
        return result
    except Exception as e:
        return f"Error: {e}"

def calculator():

    print("Enter expressions like: 2 + 3 * 4")
    print("Type 'exit' to quit\n")

    while True:
        expr = input(">> ")
        if expr.lower() == 'exit':
            print("👋 Goodbye!")
            break
        result = calculate_expression(expr)
        print("= ", result)

calculator()


