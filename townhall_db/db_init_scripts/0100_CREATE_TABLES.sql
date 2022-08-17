-- guild tables
CREATE TABLE public.guilds
(
    id serial,
    guildname text COLLATE pg_catalog."default" unique,
	level text,
	faction text,
    date_created timestamp default current_timestamp,
    date_modified timestamp default current_timestamp,
)

TABLESPACE pg_default;

ALTER TABLE public.guilds
    OWNER to admin;
