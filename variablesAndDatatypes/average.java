import java.util.*;
public class average {  
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter three numbers");
        int $= sc.nextInt();
        int b= sc.nextInt();
        int c= sc.nextInt();
        int average= ($+b+c)/3;
        System.out.println("Average is "+ average);
    }
}