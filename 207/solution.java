class Solution {
    //图
    HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
    //所有的课
    Boolean flag = false;
    HashSet<Integer> rootSet = new HashSet<>();
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(prerequisites.length == 0) return true;
        if(prerequisites.length == 1 ) return true;
        graph(prerequisites);
        
        if(this.cycle()) return false;
        
        else  return true;
        
                      
    }
    
    public void graph(int[][]courses){
  
        for(int i = 0; i < courses.length; i ++){
            
            if(!map.containsKey(courses[i][0])) map.put(courses[i][0], new ArrayList<>()); 
            if(!map.containsKey(courses[i][1])) map.put(courses[i][1], new ArrayList<>()); 
            
            map.get(courses[i][0]).add(courses[i][1]);
        }

    }
        
    public Boolean DFS( Integer root, HashSet<Integer> visited){
        visited.add(root);
        this.rootSet.add(root);
        for(int child : map.get(root)){
            if(visited.contains(child)) return true;
            if(this.DFS(child,visited)) return true;   
        }
        visited.remove(root);
        return false;
    }

    
   public Boolean cycle(){
       HashSet<Integer> visited = new HashSet<Integer>();
       
       for(int root : map.keySet()){
          if(! this.rootSet.contains(root)){
              if(this.DFS(root,visited))
                return true;
          }
       }
    
        return false;
   }
}