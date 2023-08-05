import java.util.*;
public class factorial1 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a number : ");
        long f= sc.nextLong();
        long i,prod=1;
        for(i=f;i>=1;i--){
            prod*=i;
        }
        System.out.println("Factorial is : "+prod);
    }
}
