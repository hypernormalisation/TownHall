-------------------------------------------------------------------------------
-- testing data for guilds and associated officer/GM members

insert into guilds (guild_name, guild_type, faction, gm_id, discord_url,
realm, region) values(
    'ZugZuggers', 'HC', 'Horde', 12345, 'https://discord.gg/lightclubtbc',
    'Golemagg', 'EU');

insert into guilds (guild_name, guild_type, faction, gm_id, discord_url,
realm, region) values(
    'Barmy Barries', 'Semi-HC', 'Horde', 45678, 'https://discord.gg/worms',
    'Golemagg', 'EU');

insert into members (discord_id, guild_id, is_gm)
    values(12345, 1, true);

insert into members (discord_id, guild_id, is_gm)
    values(45678, 2, true);

insert into members (discord_id, guild_id, is_officer)
    values(78910, 2, true);

-- testing data for toons data
insert into toons (discord_id, toon_name, toon_class)
    values(12345, 'Mrzug', 'warrior');

insert into toons (discord_id, toon_name, toon_class)
    values(45678, 'Bigbarry', 'warlock');


-------------------------------------------------------------------------------
-- testing data for guild vacancies

insert into vacancies_guilds (
    guild_id,
    rogue,
    tank
) values(
    1,
    true,
    true
);

--insert into vacancies_players (
--    discord_id,
--    hunter,
--    mm_hunter
--) values(
--    12345,
--    true,
--    true
--);

