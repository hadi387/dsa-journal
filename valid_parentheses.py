def is_valid(s):
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for bracket in s:
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[bracket]:
                return False

    if len(stack) == 0:
        return True

    return False


# Test cases
print(is_valid("()"))       
print(is_valid("()[]{}"))   
print(is_valid("(]"))       
print(is_valid("([)]"))      
print(is_valid("{[]}"))      