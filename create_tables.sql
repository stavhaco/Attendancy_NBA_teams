CREATE TABLE team_capacity (team_id varchar(30), team_name varchar(30), capacity integer);
COPY team_capacity FROM '/home/stav/projects/attendance/team_stadium_capacity.csv' DELIMITERS ',' CSV;


CREATE TABLE team_attendancy (game_id varchar(30),
       attendancy integer,
       home_team_id varchar(30),
       home_team_score integer,
       away_team_id varchar(30),
       away_team_score integer);
COPY team_attendancy FROM '/home/stav/projects/attendance/attendancy.csv' DELIMITERS ',' CSV;
