-- for lists---------------------------------------------------------
-- Table: list_rec

DROP TABLE IF EXISTS list_rec;

CREATE TABLE list_rec
(
  list_id bigint NOT NULL,
  list_description text,
  list_name text,
  CONSTRAINT pk_list_rec PRIMARY KEY (list_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE list_rec
  OWNER TO postgres;

-- Table: list_member_rec

DROP TABLE IF EXISTS list_member_rec CASCADE;

CREATE TABLE list_member_rec
(
  list_id bigint NOT NULL,
  member_id bigint NOT NULL,
  CONSTRAINT pk_list_member_rec PRIMARY KEY (list_id, member_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE list_member_rec
  OWNER TO postgres;

-- Index: fki_list_member_rec

DROP INDEX IF EXISTS fki_list_member_rec;

CREATE INDEX fki_list_member_rec
  ON list_member_rec
  USING btree
  (member_id);