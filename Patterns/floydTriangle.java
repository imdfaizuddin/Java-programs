import java.util.*;
public class floydTriangle {
    public static void main(String[] args) {
       
        int exit=1;
        Scanner sc = new Scanner(System.in);
       while(exit==1){ 
        int count=1;
        System.out.print("Enter a Number: ");
        int n= sc.nextInt();
        for(int i=1; i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.print(count+" ");
                count++;
            }
            System.out.println();
        }
        System.out.print("enter 1 to continue 0 to exit: ");
        exit=sc.nextInt();
    }}
}

