class Solution:
    def is_opening(self, symbol: str) -> bool:
        return symbol in {'{', '[', '('}

    def is_closing(self, symbol: str) -> bool:
        return symbol in {'}', ']', ')'}

    def isValid(self, s: str) -> bool:
        close_to_open_parenthesis_mapping = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        stack = []

        for item in s:
            if self.is_opening(item):
                stack.append(item)
            else:
                if len(stack):
                    opening = stack.pop()
                    if self.is_closing(item) and close_to_open_parenthesis_mapping[item] == opening:
                        continue
                    else:
                        return False
                else:
                    return False
