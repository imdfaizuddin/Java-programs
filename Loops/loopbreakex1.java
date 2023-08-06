import java.util.Scanner;

public class loopbreakex1 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
     for(int i=0; i>0;i++){
        System.out.print("Enter a Number");
        int n= sc.nextInt();
        if(n%10==0){
            break;
        }
        System.out.println(n);
     }
     sc.close();
     
    }
}
