import java.util.*;

public class Palindrome
{
    public static boolean isPalindrome(String string)
    {
        int i = 0, j = string.length() - 1;
        
        while (i < j)
        {
            if (string.charAt(i) != string.charAt(j))
            {
                return false;
            }
                
            i++;
            j--;
        }
        return true;
    }
    
    public static void main(String[] args)
    {
        Scanner k = new Scanner(System.in);
        System.out.println("Enter string: ");
        String str = k.nextLine();
        
        if (isPalindrome(str))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
        
    }
}  
