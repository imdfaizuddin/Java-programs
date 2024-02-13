import java.util.*;
public class ContainerWithMostWater {
    // Brute force approach
    public static int maxContainer(ArrayList<Integer> height){
        int maxWater = 0;
        int val1 = 0 , val2 = 0;
        for( int i = 0 ; i < height.size() ; i++){
            for( int j = i+1 ; j< height.size(); j++){
                int b =  j - i;
                int h = 0;
                if(height.get(i)> height.get(j)){
                    h = height.get(j);
                }else{
                    h = height.get(i);
                }
                int area = b * h;
                if( area > maxWater){
                    maxWater = area;
                    val1 = height.get(i);
                    val2 = height.get(j);
                }
            }
        }
        System.out.println(val1);
        System.out.println(val2);
        return maxWater;
    }

    // Two pointer approach
    public static int maxContainerOptimized(ArrayList<Integer> height){
        int i = 0;
        int j = height.size() - 1 ;
        int max = 0;

        while (i< j) {
            int h = Math.min(height.get(i), height.get(j));
            int b = j - i;
            int area = b * h;
            max = Math.max(max, area);

            if( height.get(i) >= height.get(j)){
                j--;
            }else if( height.get(j) >= height.get(i)){
                i++;
            }
        }
        return max;
    }
    public static void main(String[] args) {
        ArrayList<Integer> height = new ArrayList<>();
        height.add(1);
        height.add(5);
        height.add(3);
        height.add(1);
        height.add(8);
        height.add(2);
        height.add(8);
        height.add(3);
        height.add(7);
        System.out.println(maxContainer(height));
        System.out.println(maxContainerOptimized(height));
    }
}
