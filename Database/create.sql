-- Table: public.sensor

-- DROP TABLE public.sensor;

CREATE TABLE public.sensor
(
    id bigint NOT NULL DEFAULT nextval('sensor_id_seq'::regclass),
    hexid text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    temperature integer,
    location text COLLATE pg_catalog."default",
    CONSTRAINT sensor_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.sensor
    OWNER to postgres;