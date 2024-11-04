import operator

# Diccionario de operadores con precedencia y función
OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.floordiv)
}

# Función para evaluar expresiones prefijas
def eval_prefix(expr):
    stack = []
    for token in reversed(expr):
        if token in OPERATORS:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(OPERATORS[token][1](op2, op1))
        else:
            stack.append(int(token))
    return stack[0]

# Función para evaluar expresiones postfijas
def eval_postfix(expr):
    stack = []
    for token in expr:
        if token in OPERATORS:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(OPERATORS[token][1](op2, op1))
        else:
            stack.append(int(token))
    return stack[0]

# Función auxiliar para manejar la precedencia y paréntesis mínimos en infijo
def format_infix(op, left, right, parent_prec):
    op_prec = OPERATORS[op][0]
    left_expr = f"({left})" if (get_precedence(left) < op_prec) and not left.isdigit() else left
    right_expr = f"({right})" if (get_precedence(right) < op_prec) and not right.isdigit() else right
    return f"{left_expr} {op} {right_expr}"

# Función para convertir a infijo considerando precedencia
def to_infix(expr, order):
    stack = []
    if order == "PRE":
        for token in reversed(expr):
            if token in OPERATORS:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(format_infix(token, op1, op2, OPERATORS[token][0]))
            else:
                stack.append(token)
    elif order == "POST":
        for token in expr:
            if token in OPERATORS:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(format_infix(token, op1, op2, OPERATORS[token][0]))
            else:
                stack.append(token)
    return stack[0]

# Función para obtener la precedencia de un operador
def get_precedence(expr):
    return OPERATORS[expr][0] if expr in OPERATORS else -1

# Función principal para ejecutar el programa
def main():
    while True:
        command = input("Ingrese una acción (EVAL/MOSTRAR/SALIR): ").strip().split()
        
        if not command:
            continue
        
        action = command[0]
        
        if action == "SALIR":
            print("Saliendo del programa.")
            break
        
        if len(command) < 3:
            print("Comando inválido.")
            continue

        order = command[1]
        expr = command[2:]
        
        if action == "EVAL":
            if order == "PRE":
                result = eval_prefix(expr)
                print("Resultado:", result)
            elif order == "POST":
                result = eval_postfix(expr)
                print("Resultado:", result)
            else:
                print("Orden inválido.")
        
        elif action == "MOSTRAR":
            if order in {"PRE", "POST"}:
                infix_expr = to_infix(expr, order)
                print("Expresión en infijo:", infix_expr)
            else:
                print("Orden inválido.")
        
        else:
            print("Acción no reconocida.")

if __name__ == "__main__":
    main()



