import java.util.Scanner;

public class primeOrnot {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        long i;
        long p;
        
        do {
            boolean pr=true;
            System.out.print("Enter a number: ");
            long num= sc.nextLong();
            if(num<=1){
                System.out.println("Invalid input");
                break;
            }
            for( i=2;i<=Math.sqrt(num);i++){
                 p=num%i;
                if(p==0){
                    
                    pr=false;
                    System.out.println(num/i+"*"+i+"="+num);
                    break;
                }
            }
            if(pr==false){
               System.out.println(num+" is not prime.");
            }else{
                 System.out.println(num+" is a Prime Number.");
            }
        } while (true);
    }
}
