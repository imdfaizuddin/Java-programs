import java.util.*;
public class sumofevenandodd {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int evenSum=0;
        int oddSum=0;
        int choice;
        int number;
        do{
            System.out.print("Enter a number: ");
            number= sc.nextInt();
                if(number%2==0){
                    evenSum +=number;
                } else{
                    oddSum += number;
                }
            System.out.print("Enter 1 to continue 0 to stop:");
            choice= sc.nextInt();
        } while(choice==1);

        System.out.println("Sum of even Numbers: "+evenSum);
        System.out.println("sum of odd Numbers: "+ oddSum);
    }
}