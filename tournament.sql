-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP TABLE IF EXISTS player CASCADE;
DROP TABLE IF EXISTS match CASCADE;

-- Now Define Tables
-- USER
CREATE TABLE player (
    id serial PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL
);

-- MATCH
CREATE TABLE match (
    id serial PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    loser INTEGER REFERENCES player(id),
    winner INTEGER REFERENCES player(id)
);


-- VIEWS
CREATE VIEW wins AS
  SELECT player.id, count(match.winner) AS num FROM player
  LEFT JOIN match ON player.id =  match.winner
  GROUP BY player.id;

CREATE VIEW count AS
  SELECT player.id, count(match.winner) AS num FROM player
  LEFT JOIN match ON player.id = match.winner
  OR player.id = match.loser
  GROUP BY player.id;

CREATE VIEW standings AS
  SELECT player.id, player.name, wins.num AS wins, count.num AS match_played
      FROM player, wins, count
      WHERE player.id = wins.id and player.id = count.id
      ORDER BY wins DESC;