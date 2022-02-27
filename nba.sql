CREATE TABLE nbaplayer
(
	seasonid		INTEGER,
	playerid		INTEGER,
	playername		TEXT,
	teamid			INTEGER,
    teamabbrev      TEXT,
    teamname        TEXT,
    gameid          INTEGER,
    gamedate        TEXT,
    matchup         TEXT,
    wl              TEXT,
    mins            INTEGER,
    fgm             INTEGER,
    fga             INTEGER,
    fgpct           REAL,
    fg3m            INTEGER,
    fg3a            INTEGER,
    fg3pct          REAL,
    ftm             INTEGER,
    fta             INTEGER,
    ftpct           REAL,
    oreb            INTEGER,
    dreb            INTEGER,
    reb             INTEGER,
    ast             INTEGER,
    stl             INTEGER,
    blk             INTEGER,
    tov             INTEGER,
    pf              INTEGER,
    pts             INTEGER,
    plusminus       TEXT,
    seasontype      TEXT,
    seasonyear      INTEGER,
    season          TEXT
);
CREATE INDEX ptsindex
ON nbaplayer (pts);