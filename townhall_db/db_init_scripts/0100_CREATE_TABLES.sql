-- guild table
CREATE TABLE public.guilds
(
    id serial,
    guildname text COLLATE pg_catalog."default" unique,
    gtype text COLLATE pg_catalog."default",
    faction text COLLATE pg_catalog."default",
    date_created timestamp default current_timestamp,
    date_modified timestamp default current_timestamp,
    PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.guilds
    OWNER to admin;
