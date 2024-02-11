import java.util.*;
public class FindMax {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(42);
        list.add(21);
        list.add(32);
        list.add(72);
        list.add(27);
        
        int max = Integer.MIN_VALUE;

        for(int i = 0 ; i< list.size() ; i++){
            // if(list.get(i)> max){
            //     max = list.get(i);
            // }
            max = Math.max(max, list.get(i));
        }
        System.out.print("max value is " + max);
    }
}