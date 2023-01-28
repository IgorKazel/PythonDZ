example = '( 12 - 4 ) * 2'

def calc(example):

    operator = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

    example_list = example.split()
    number_stack = []
    symbol_stack = []

    for i in example_list:
        if i.isdigit():
            number_stack.append(int(i))
        elif i in operator:
            if len(symbol_stack) == 0:
                symbol_stack.append(i)
                continue
            if symbol_stack[-1] == '(':
                symbol_stack.append(i)
                continue

            while symbol_stack:
                if operator.get(i)[0] <= operator.get(symbol_stack[-1])[0]:
                    y, x = number_stack.pop(), number_stack.pop()
                    number_stack.append(operator[symbol_stack[-1]][1](x, y))
                    symbol_stack.pop()
                symbol_stack.append(i)
                break

        elif i == ')':
            while symbol_stack[-1] != '(':
                y, x = number_stack.pop(), number_stack.pop()
                number_stack.append(operator[symbol_stack[-1]][1](x, y))
                symbol_stack.pop()
            if symbol_stack[-1] == '(':
                symbol_stack.pop()
        else:
            symbol_stack.append(i)

    while len(symbol_stack) > 0:
        y, x = number_stack.pop(), number_stack.pop()
        number_stack.append(operator[symbol_stack[-1]][1](x, y))
        symbol_stack.pop()

    return number_stack.pop()

result = calc(example)
print(example,'=',result)
