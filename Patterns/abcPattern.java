import java.util.Scanner;

public class abcPattern {

    public static void main(String[] args) {
        char ch;
        boolean T=true;
        Scanner sc = new Scanner(System.in);
        while (T) {
            System.out.print("Enter a Number: ");
            int n= sc.nextInt();
            ch='A';
            for(int i=1;i<=n;i++){
                for(int j=1;j<=i;j++){
                    System.out.print(ch);
                    ch++;
                }
                System.out.println();
            }
            System.out.print("Print 1 to continue 0 to end: ");
            int cont= sc.nextInt();
            if(cont!=1){
                T=false;
            }
        }
        sc.close();
    }
}
