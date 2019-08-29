from collections import defaultdict
class Solution:
    
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def path_parser(path):
            contents = path.split(" ")
            directory = contents[0]
            for file in contents[1:]:
                content_index = file.index("(")
                content_path_table[file[content_index+1:-1]].append(directory + "/" + file[:content_index] )
                
        content_path_table = defaultdict(list)
        for path in paths:
            path_parser(path)
        
        return [  value for value in content_path_table.values() if len(value) > 1]