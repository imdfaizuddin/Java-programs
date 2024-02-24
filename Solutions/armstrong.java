import java.util.*;
public class armstrong{
        public static boolean armstrongNumber(int n){
            String s = Integer.toString(n);
            int size = s.length();
            int temp = n , sum = 0;
            while(temp > 0){
                int r = temp%10;
                int pow = (int)Math.pow(r, size);
                System.out.println(pow);
                sum += pow;
                temp /=10;
            }
            if(sum == n){
                return true;
            }
            return false;
    
        }

public static void main(String[] args) {
            // Write your code here
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter a number:");
            int n = sc.nextInt();
            sc.close();
            // int n = 1634;
            boolean ans = armstrongNumber(n);
            System.out.print(ans);
}
}
