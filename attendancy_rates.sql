SELECT 
team_capacity.team_id team_id,
team_capacity.team_name team_name,
AVG(CAST(team_attendancy.attendancy as float)/CAST(team_capacity.capacity as float)) occupancy_rate,
CASE  
    WHEN (team_attendancy.home_team_score-team_attendancy.away_team_score)<=0 THEN 0
    WHEN (team_attendancy.home_team_score-team_attendancy.away_team_score)>0 THEN 1
END as win
FROM
team_attendancy
LEFT JOIN team_capacity ON team_capacity.team_id=team_attendancy.home_team_id
GROUP BY team_id,team_name,win
ORDER BY team_id;