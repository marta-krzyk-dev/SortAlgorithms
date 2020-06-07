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
