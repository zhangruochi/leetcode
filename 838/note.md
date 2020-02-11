## Intuition

Between every group of vertical dominoes ('.'), we have up to two non-vertical dominoes bordering this group. Since additional dominoes outside this group do not affect the outcome, we can analyze these situations individually: there are 9 of them (as the border could be empty). Actually, if we border the dominoes by 'L' and 'R', there are only 4 cases. We'll write new letters between these symbols depending on each case.

```
# L ... R  => L ... R
        
# R ... L  => R R . L L   # odd
# R ....L =>  R R R L L L # even

# R ... R  => R R R R R
# L ... L  => L L L L L
```