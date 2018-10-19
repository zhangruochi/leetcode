## Steps to developing a usable algorithm. 

1. Model the problem.
2. Find an algorithm to solve it. 
3. Fast enough? 
4. Fits in memory?
5. If not, figure out why.
6. Find a way to address the problem.
7. Iterate until satisfied.

## Implementing the operations
- **Find query.** Check if two objects are in the same component. 

- **Union command.** Replace components containing two objects with their union.


## Quick Find

![Screen Shot 2018-08-30 at 17.02.40.png](resources/602A064DBBEA141EA01952A19BE2DF52.png)

![Screen Shot 2018-08-30 at 17.03.48.png](resources/136BA6EDC60864679135621150B276C8.png)

- 连接两个 node 时，要把和这两个 node 具有相同 id 的所有 node 设置为同样的 id
- Union is too expensive. It takes $N^2$ array accesses to process a sequence of N union commands on N objects.

## Quick Union

![Screen Shot 2018-08-30 at 17.07.36.png](resources/47039C0458EFF64B24D9DB7DBF883C9F.png)

- 连接两个 node 时，将两个 node 的root 连接在一起
- Trees can get tall.
- Find too expensive (could be N array accesses).

![Screen Shot 2018-08-30 at 17.08.04.png](resources/215325F4D0337DC238B083290AAE52C7.png)


## Union Find

### Improvement 1: weighting

1. Modify quick-union to avoid tall trees.
2.  Keep track of size of each tree (number of objects).
3.  Balance by linking root of smaller tree to root of larger tree.
![Screen Shot 2018-08-30 at 17.13.06.png](resources/7963C88C67983992683AE279FCC28A03.png)
![Screen Shot 2018-08-30 at 17.29.03.png](resources/E51887108DA01340E5E3CB804645D28D.png)

### Improvement 2: path compression
1. Quick union with path compression. Just after computing the root of p, set the id of each examined node to point to that root.

![Screen Shot 2018-08-30 at 17.29.44.png](resources/2F7E738AE3DEF265D853B9A95D4DD7D9.png)

![Screen Shot 2018-08-30 at 17.34.29.png](resources/BB43749A16866F12D811835782EDF83B.png)