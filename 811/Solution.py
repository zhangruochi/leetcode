from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for count_domain in cpdomains:
            count,domain = count_domain.split(" ")
            domains = domain.split(".")
            string = ''
            for i in range(len(domains)):
                counter[".".join(domains[i:])] += int(count)
        
        return ["{} {}".format(count,string) for string,count in counter.items()]
                        
                
            