class Solution:
    def isValid(self, s: str) -> bool:
        closing = [')','}',']']
        pop_dict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for element in s:
            if element in closing:
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if e == pop_dict[element]:
                    continue
                else:
                    return False
            else:
                stack.append(element)
            print(stack)
        if len(stack) > 0:
            return False
        else:
            return True



        