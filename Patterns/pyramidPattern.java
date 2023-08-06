import java.util.Scanner;

public class star {
    public static void main(String[] args) {
         do{
            Scanner sc= new Scanner(System.in);
            System.out.print("Enter line Number : ");
            int n= sc.nextInt();
            for (int i = 1; i <= n; i++) {

                // loop to print the number of spaces before the star
                for (int j = 1; j <=n-i; j++) {
                    System.out.print(" ");
                }
    
                // loop to print the number of stars in each row
                for (int j = 1; j <= 2*i-1; j++) {
                   
                    System.out.print("*");
                }
    
                // for new line after printing each row
                System.out.println();
            }
            

        }while(true);
    }
}
