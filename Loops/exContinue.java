import java.util.Scanner;

public class exContinue {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        do{
            System.out.print("Enter a number : ");
            long num= sc.nextLong();
            if(num%10==0){
                System.out.println("***************************************");
                continue;
            }
            System.out.println(num);
        }while(true);
    }
}
