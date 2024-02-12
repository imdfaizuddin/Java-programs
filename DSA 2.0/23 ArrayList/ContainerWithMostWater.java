import java.util.*;
public class ContainerWithMostWater {

    public static int maxContainer(ArrayList<Integer> height){
        int maxWater = 0;
        for( int i = 0 ; i < height.size() ; i++){
            for( int j = i+1 ; j< height.size(); j++){
                int b =  j - i;
                int h = 0;
                if(height.get(i)> height.get(j)){
                    h = height.get(j);
                }
                int area = b * h;
                if( area > maxWater){
                    maxWater = area;
                }
            }
        }
        return maxWater;
    }
    public static void main(String[] args) {
        ArrayList<Integer> height = new ArrayList<>();
        height.add(1);
        height.add(8);
        height.add(6);
        height.add(2);
        height.add(5);
        height.add(4);
        height.add(8);
        height.add(3);
        height.add(7);
        // System.out.println(list);
        System.out.println(maxContainer(height));
    }
}
