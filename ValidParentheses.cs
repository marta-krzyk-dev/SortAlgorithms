/*Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
    */
public class Solution {
    public bool IsValid(string s) {
        
        var stack = new Stack<char>();
        
        foreach(var c in s) {
            
            if (IsOpenBracket(c)) {
                stack.Push(c);
            } else {
                if (stack.Count == 0 || !IsValidPair(stack.Pop(), c))
                    return false;
            }
        }
        
        return stack.Count == 0;
        }
     
    private bool IsValidPair(char opening, char closing) {
        return (opening == '[' && closing == ']') ||
             (opening == '(' && closing == ')') ||
             (opening == '{' && closing == '}');
    }
    
    private bool IsOpenBracket(char c) {
        return c == '[' || c == '(' || c=='{';
    }
 }
