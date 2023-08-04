import java.util.*;
public class leapYear {
    public static void main(String args[]){
        System.out.print("Enter Year : ");
        Scanner sc= new Scanner(System.in);
        int year= sc.nextInt();
        if (year%4==0) {
                if((int)year%100==0){
                    if ((int)year%400==0){
                        System.out.println(year+" is a Leap Year");
                    }else System.out.println(year+" is not a leap year");

                } else System.out.println(year + " is a Leap year");
        } else {
            System.out.println(year+" is Not a leap year");
        }
    }
    
}