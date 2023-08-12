 class patterns{
    void evenOdd(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                if((i+j)%2==0){
                    System.out.print("1 ");
                }else{
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
    }
    static int sum(int a,int b){
        return a+b;
    }

}
public class EvenOddIndex {
    public static void main(String[] args) {
        patterns p= new patterns();
        p.evenOdd(5);
        p.evenOdd(8);
        System.out.println(p.sum(6,5));
    }
}
