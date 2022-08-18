insert into guilds (
    guild_name,
    guild_type,
    faction,
    gm_id,
    discord_url
) values(
    'HIVE',
    'Semi-HC',
    'Horde',
    12345,
    'https://discord.gg/lightclubtbc'
);

--INSERT INTO GUILDS (
--    guild_name,
--    guild_type,
--    faction,
--    gm_id
--) VALUES(
--    'Sunced',
--    'HC',
--    'Horde',
--    6789
--);

insert into users (
    discord_id,
    guild_id,
    is_gm
) values(
    12345,
    1,
    true
);

--INSERT INTO USERS (
--    discord_id,
--    guild_id
--) VALUES(
--    6789,
--    2
--);


insert into vacancies (
    guild_id,
    rogue,
    tank
) values(
    1,
    true,
    true
)
