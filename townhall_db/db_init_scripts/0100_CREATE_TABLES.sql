-- guild table
create table public.guilds
(
    guild_id            serial primary key,
    realm               text,
    region              text,
    guild_name          text unique,
    guild_name_alt      text default null,  -- for when guild name is different in game
    discord_url         text,
    discord_logo_url    text default null,
    gm_id               int,
    guild_type          text default 'Casual',
    faction             text default 'Horde',
    loot_system         text default 'LC',
    guild_language      text default 'English',
    toons_required      int default 1,
    date_created        timestamp default current_timestamp,
    date_modified       timestamp default current_timestamp
);
--tablespace pg_default;
--alter table public.guilds
--    owner to admin;

-- users table
create table public.users
(
    discord_id  int unique primary key,
    guild_id    int references public.guilds default null,
    is_gm       boolean default false,
    is_officer  boolean default false
)
tablespace pg_default;
--alter table public.users
--    owner to admin;

-- vacancies table
create table public.vacancies_guilds
(
    guild_id            int primary key references public.guilds on delete cascade,

    -- general types
    dps                 boolean default false,
    melee_dps           boolean default false,
    ranged_dps          boolean default false,
    tank                boolean default false,
    healer              boolean default false,
    pvp                 boolean default false,

    -- classes
    dk                  boolean default false,
    druid               boolean default false,
    hunter              boolean default false,
    mage                boolean default false,
    paladin             boolean default false,
    priest              boolean default false,
    rogue               boolean default false,
    shaman              boolean default false,
    warlock             boolean default false,
    warrior             boolean default false,

    -- individual specs
    blood_dk            boolean default false,
    frost_dk            boolean default false,
    unholy_dk           boolean default false,

    balance_druid       boolean default false,
    feral_druid         boolean default false,
    feral_dps_druid     boolean default false,
    feral_tank_druid    boolean default false,
    resto_druid         boolean default false,

    bm_hunter           boolean default false,
    mm_hunter           boolean default false,
    surv_hunter         boolean default false,

    arcane_mage         boolean default false,
    fire_mage           boolean default false,
    frost_mage          boolean default false,

    holy_paladin        boolean default false,
    prot_paladin        boolean default false,
    ret_paladin         boolean default false,

    disc_priest         boolean default false,
    holy_priest         boolean default false,
    shadow_priest       boolean default false,

    assassin_rogue      boolean default false,
    combat_rogue        boolean default false,
    sub_rogue           boolean default false,

    ele_shaman          boolean default false,
    enhance_shaman      boolean default false,
    resto_shaman        boolean default false,

    affli_warlock       boolean default false,
    demo_warlock        boolean default false,
    destro_warlock      boolean default false,

    dps_warrior         boolean default false,
    arm_warrior         boolean default false,
    fury_warrior        boolean default false,
    prot_warrior        boolean default false

)
tablespace pg_default;
--alter table public.vacancies_guilds
--    owner to admin;

--
---- Duplicate the table for the user vacancy posts
--create table vacancies_players as (select * from vacancies_guilds) with no data;
--
----alter table vacancies_players drop constraint vacancies_players_pkey;
--alter table vacancies_players rename column guild_id to discord_id;
--alter table vacancies_players add primary key (discord_id);
--
--alter table vacancies_players
--    add constraint fk_vacancies_players_users foreign key (discord_id) references users (discord_id);


-- vacancies table
create table public.vacancies_players
(
    discord_id          int primary key references public.users on delete cascade,

    -- general types
    dps                 boolean default false,
    melee_dps           boolean default false,
    ranged_dps          boolean default false,
    tank                boolean default false,
    healer              boolean default false,
    pvp                 boolean default false,

    -- classes
    dk                  boolean default false,
    druid               boolean default false,
    hunter              boolean default false,
    mage                boolean default false,
    paladin             boolean default false,
    priest              boolean default false,
    rogue               boolean default false,
    shaman              boolean default false,
    warlock             boolean default false,
    warrior             boolean default false,

    -- individual specs
    blood_dk            boolean default false,
    frost_dk            boolean default false,
    unholy_dk           boolean default false,

    balance_druid       boolean default false,
    feral_druid         boolean default false,
    feral_dps_druid     boolean default false,
    feral_tank_druid    boolean default false,
    resto_druid         boolean default false,

    bm_hunter           boolean default false,
    mm_hunter           boolean default false,
    surv_hunter         boolean default false,

    arcane_mage         boolean default false,
    fire_mage           boolean default false,
    frost_mage          boolean default false,

    holy_paladin        boolean default false,
    prot_paladin        boolean default false,
    ret_paladin         boolean default false,

    disc_priest         boolean default false,
    holy_priest         boolean default false,
    shadow_priest       boolean default false,

    assassin_rogue      boolean default false,
    combat_rogue        boolean default false,
    sub_rogue           boolean default false,

    ele_shaman          boolean default false,
    enhance_shaman      boolean default false,
    resto_shaman        boolean default false,

    affli_warlock       boolean default false,
    demo_warlock        boolean default false,
    destro_warlock      boolean default false,

    dps_warrior         boolean default false,
    arm_warrior         boolean default false,
    fury_warrior        boolean default false,
    prot_warrior        boolean default false

);