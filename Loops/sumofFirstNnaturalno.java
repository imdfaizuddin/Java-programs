import java.util.*;
public class sumofFirstNnaturalno {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a number: ");
        long n= sc.nextLong();
        long sum=0;
        long i=1;
        System.out.print("First "+n+" natural numbers: ");
        while(i<n){
            sum += i;
            System.out.print(i+",");
            i++;
        }
        sum+=i;
        System.out.println(i);
        System.out.println("Sum of first "+n+" natural number is "+sum);
    }
}