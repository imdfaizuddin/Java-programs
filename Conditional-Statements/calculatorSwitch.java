import java.util.*;
public class calculatorSwitch {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a : ");
        int a= sc.nextInt();
        System.out.print("Enter b : ");
        int b= sc.nextInt();
        System.out.print("Enter Operator : ");
        char Operator= sc.next().charAt(0);
        switch (Operator) {
            case '+': System.out.println("Sum of "+a+"+"+b+" is "+ (a+b));
                
                break;
            case '-': System.out.println("Diff of "+a+"-"+b+" is "+ (a-b));
                break;
            case '*': System.out.println("Product of "+a+"*"+b+" is "+ (a*b));
                break;
            case '/':
            double x=a;
            double y=b;
            System.out.println("division of "+a+"/"+b+" is "+ (x/y));
                break;
            default:   System.out.println("Not that advance");
                break;
        }
    }
}
