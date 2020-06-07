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
    public bool ValidPalindrome(string s) {
        
        return ValidPalindrome(s, true);
    }
    
     public static bool ValidPalindrome(string s, bool chance)
        {

            int len = s.Length;
            int middle = len / 2;
           
            for (int i = 0, j = len - 1; i < middle; ++i, --j)
            {
                if (s[i] == s[j])
                    continue;
                else if (!chance)
                   return false;
                else
                {
                    //Ignore invalid character only once
                    if (s[i] == s[j - 1] || s[i + 1] == s[j])
                    {
                        Console.WriteLine($"Assessing {s.Substring(i, j - i)}");
                        return ValidPalindrome(s.Substring(i, j - i), false) || ValidPalindrome(s.Substring(i + 1, j - i), false);
                    }
                    else
                    {
                        return false;
                    }
                }
            }

            return true;
        }
}
