CREATE TABLE mon
(
    Mon_id SERIAL,
    Mon_Name VARCHAR(255) NOT NULL,
    Mon_Element_1 VARCHAR(255) NOT NULL,
    Mon_Element_2 VARCHAR(255) NOT NULL,
    Mon_Level INT NOT NULL DEFAULT 5,
    Mon_Max_HP INT NOT NULL,
    Mon_Attack INT NOT NULL,
    Mon_Defense INT NOT NULL,
    Mon_Speed INT NOT NULL,
    Mon_Accuracy FLOAT NOT NULL,
    Mon_Evasion FLOAT NOT NULL,
    PRIMARY KEY(Mon_id)
);

CREATE TABLE moves
(
    Move_id SERIAL,
    Move_Name VARCHAR(255) NOT NULL,
    Move_Element VARCHAR(255) NOT NULL,
    Move_PP INT NOT NULL,
    Move_Power FLOAT NOT NULL,
    Move_Accuracy FLOAT NOT NULL,
    Move_Buff BOOLEAN NOT NULL,
    Move_Stat VARCHAR(255),
    Move_Stage INT,
    Move_Target VARCHAR(255) NOT NULL,
    PRIMARY KEY(Move_id)
);

CREATE TABLE elements
(
    Element VARCHAR(255) NOT NULL,
    "vs_Normal" FLOAT NOT NULL,
    "vs_Fire" FLOAT NOT NULL,
    "vs_Water" FLOAT NOT NULL,
    "vs_Electric" FLOAT NOT NULL,
    "vs_Grass" FLOAT NOT NULL,
    "vs_Ice" FLOAT NOT NULL,
    "vs_Fighting" FLOAT NOT NULL,
    "vs_Poison" FLOAT NOT NULL,
    "vs_Ground" FLOAT NOT NULL,
    "vs_Flying" FLOAT NOT NULL,
    "vs_Psychic" FLOAT NOT NULL,
    "vs_Bug" FLOAT NOT NULL,
    "vs_Rock" FLOAT NOT NULL,
    "vs_Ghost" FLOAT NOT NULL,
    "vs_Dragon" FLOAT NOT NULL,
    "vs_Dark" FLOAT NOT NULL,
    "vs_Steel" FLOAT NOT NULL,
    "vs_Fairy" FLOAT NOT NULL,
    PRIMARY KEY(Element)
);