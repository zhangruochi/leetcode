

# Write your MySQL query statement below
    select 
         actor_id,director_id
    from 
    (select 
        actor_id,director_id, count(timestamp) as co_count
    from ActorDirector 
    group by actor_id,director_id) AS T
    
    where T.co_count >= 3