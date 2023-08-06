import java.util.*;
/**
 * revstar
 */
public class revstar {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        do{
            System.out.print("Enter a number: ");
            long num= sc.nextLong();
            for(long i=num;i>=1;i--){
                for(long j=i;j>=1;j--){
                    System.out.print("*");
                }
                System.out.println();
            }

        }while(true);
    }
}
