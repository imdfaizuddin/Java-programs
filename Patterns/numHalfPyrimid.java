import java.util.*;
public class numberHalfPyramid {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        do{
            System.out.print("Enter Lines: ");
            long line= sc.nextLong();
            for(long i=1;i<=line;i++){
                    for(long j=1;j<=i;j++){
                        System.out.print(j);
                    }
                System.out.println();
            }


        }while(true);
    }
}

