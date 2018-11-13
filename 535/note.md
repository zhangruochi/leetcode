##  思路

- 采用任意的6位字符编码
- 使用两个 table 记录映射关系， long2short 和 short2long
- long2short 记录 longUrl 到 short 的映射，当再次有longUrl到达时，如果已经在long2short中，就不用再保存，可以防止数据冗
- short2long 是为了在用在 decode 中，直接根据 shortUrl 的后面部分找到 longUrl