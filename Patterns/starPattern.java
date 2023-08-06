import java.util.*;
/**
 * starpattern
 */
public class starpattern {

    public static void main(String[] args) {
        
        do{
            Scanner sc= new Scanner(System.in);
            System.out.print("Enter line Number : ");
            long line= sc.nextLong();
            for(long i=1; i<=line;i++){
                for(long j=1; j<=i;j++){
                    System.out.print("*");
                }
                System.out.print("\n");
            }
            

        }while(true);
    }
}
