import java.util.*;

class Solution {
    public List<Integer> sortArray(int[] nums) {
      ArrayList<Integer> res = new ArrayList<>();
      PriorityQueue<Integer> heap = new PriorityQueue<>();
    for(int i = 0; i < nums.length; i ++){
      heap.add(nums[i]);
    }
      while(!heap.isEmpty()){
        res.add(heap.poll());
      }
    return res;
  }
}