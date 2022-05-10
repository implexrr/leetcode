class Solution:
    
    """
    Solution via stack.
    
    When encountering a open bracket, toss it onto the stack. When encountering a
    close bracket, either pop corresponding open bracket from the top of the stack
    or return that a mistake has been made.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    
    # Utilize a stack to check for valid parentheses
    def isValid(self, s: str) -> bool:
        
        # Create empty xstack
        dishes = []
        open_brackets = ["{", "(", "["]

        for bracket in s:
            if (bracket in open_brackets):
                dishes.append(bracket)
            elif (not dishes):
                return False
            elif (bracket == "]"):
                if dishes[-1] == "[":
                    dishes.pop()
                else:
                    return False
            elif (bracket == ")"):
                if dishes[-1] == "(":
                    dishes.pop()
                else:
                    return False
            elif (bracket == "}"):
                if dishes[-1] == "{":
                    dishes.pop()
                else:
                    return False
                
        # The final stack must be completely empty as well, otherwise inputs like "(" are valid.
        return (not dishes) 