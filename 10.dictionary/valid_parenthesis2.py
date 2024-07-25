user_input = "[][()]"

symbol_table={
    "<":">",
    "[":"]",
    "(":")",
    "{":"}"
    }

symbol_stack = []
top = -1
is_valid = True

for symbol in user_input:
    
    if symbol in symbol_table:
        
        top += 1
        symbol_stack.append(symbol)
        
    else:
        if len(symbol_stack) < 1:
            is_valid = False
            break
        
        current_symbol = symbol_stack[top]
        current_symbol_closing = symbol_table[current_symbol]
        
        if symbol == current_symbol_closing:
            
            top -= 1 
            symbol_stack.pop()
            
        else:
            
            is_valid = False
            break
        

if is_valid and symbol_stack == []:
    print("valid")
else:
    print("invalid")