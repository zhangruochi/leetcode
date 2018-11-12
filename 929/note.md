## 思路

- 用clear函数清洗字符串，然后对emails进行清洗，看清洗完后还剩下多少不同的mails
- 清洗字符串时，只清洗local部分
- 遍历local，遇到+停止，遇到.忽略

```Python
class Solution(object):
    def clear(self,mail):
        local,domain = mail.split("@")
        res = ""
        for char in local:
            if char == ".":
                continue
            elif char == "+":
                break
            else:
                res += char
        
        return res + "@" + domain
        

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        return len(set([self.clear(mail) for mail in emails]))
```