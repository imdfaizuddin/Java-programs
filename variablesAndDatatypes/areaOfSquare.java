/*
Simple Java program to calculate area of a square.
*/
import java.util.*;
public class areaOfSquare {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("enter side of a square: ");
            int side= sc.nextInt();
            int area= side*side;
        System.out.println("Area of the square: "+area);

    }
}
