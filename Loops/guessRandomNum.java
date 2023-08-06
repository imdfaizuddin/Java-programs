import java.util.*;

public class GuessRandomNum {
    public static void main(String[] args) {
        int randomNo;
        int l=1;
        int m=1;

        Scanner sc= new Scanner(System.in);
        do{
            System.out.println("Game Begins-----------------");
            randomNo= (int)(Math.random()*100);
            System.out.println(randomNo);
        do{
            System.out.print("Enter a Number: ");
            int num= sc.nextInt();
            if(num>randomNo){
                System.out.println("The number is too large.");
            }else if(randomNo>num){
                System.out.println("The number is too small.");
            }else if(num==randomNo){
                System.out.println("Correct!!---press 1 to continue  0 to exit");
                m=sc.nextInt();
                break;
            }

        }while(l==1);
        }while(m==1);    }
}