import java.util.*;
public class reverseOfaNumber {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a Number: ");
        int number= sc.nextInt();
        int i;
        long reverse=0,j;
        String rev="";
        while(number>0){
            j=number%10;
            reverse=(reverse*10)+j;
        //    reverse=number%10;
            // System.out.println(reverse);
            // rev += String.valueOf(number%10);
            number/=10;        
        }
        // System.out.println(Integer.parseInt(rev));
        System.out.println(reverse);
        System.out.println(2+0);
       
    }
}