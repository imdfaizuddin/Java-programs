public class iceCReam2 {
    public static int findIceCreams(int n, int[] p) {
		
        int max=0;
        int max2=0;
        int q[] =  new int[p.length-1];
         for(int i=0;i<p.length;i++){
             if(p[i]>max){
                 max=p[i];
             }
         }
         for(int i=0;i<p.length;i++){
             if(p[i]>max2 && p[i]<max){
                 max2=p[i];
             }
         }
         System.out.println(max+" "+max2);
         return max+max2;

	}
public static void main(String[] args) {
    int arr[] = {5,10,15,25,30} ;
    int result =findIceCreams(5,arr);
    System.out.println("Final answer ="+result);
}
}
