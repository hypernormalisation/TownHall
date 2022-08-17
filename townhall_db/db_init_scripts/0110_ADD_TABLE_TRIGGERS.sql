CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS '
BEGIN
  NEW.date_modified = NOW();
  RETURN NEW;
END;
'
LANGUAGE plpgsql;

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.guilds
FOR EACH ROW
EXECUTE FUNCTION trigger_set_timestamp();
