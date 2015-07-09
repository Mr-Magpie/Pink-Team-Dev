-- recreates all article and list tables

-- Table: article_rec

DROP TABLE IF EXISTS article_rec CASCADE;

CREATE TABLE article_rec
(
  article_id serial NOT NULL,
  article_url text,
  article_title text,
  article_description text,
  article_source text,
  article_published TIMESTAMP,

  CONSTRAINT pk_article_rec PRIMARY KEY (article_id)
)

WITH (
  OIDS=FALSE
);

ALTER TABLE article_rec
  OWNER TO postgres;

-- Index: idx_article_rec

DROP INDEX IF EXISTS idx_article_rec;

CREATE INDEX idx_article_rec
  ON article_rec
  USING btree
  (article_url COLLATE pg_catalog."default");

-- Table: word_rec

DROP TABLE IF EXISTS word_rec CASCADE;

CREATE TABLE word_rec
(
  word_id serial NOT NULL,
  word text,
  CONSTRAINT pk_word_rec PRIMARY KEY (word_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE word_rec
  OWNER TO postgres;


-- Table: word_frequency_rec

DROP TABLE IF EXISTS word_frequency_rec CASCADE;

CREATE TABLE word_frequency_rec
(
  word_frequency_id serial,
  article_id integer,
  word_id integer,
  frequency integer,
  CONSTRAINT word_frequency_id PRIMARY KEY (article_id, word_id),
  CONSTRAINT fk_word_id FOREIGN KEY (word_id)
      REFERENCES word_rec (word_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_article_id FOREIGN KEY (article_id)
      REFERENCES article_rec (article_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE word_frequency_rec
  OWNER TO postgres;

-- Index: fki_word_frequency_rec

DROP INDEX IF EXISTS fki_word_frequency_rec;

CREATE INDEX fki_word_frequency_rec
  ON word_frequency_rec
  USING btree
  (word_id);


DROP TABLE IF EXISTS feed_rec CASCADE;

CREATE TABLE feed_rec
(
  feed_id serial,
  feed_url text,
  feed_title text,
  feed_etag text,
  feed_source text,

  CONSTRAINT pk_feed_rec PRIMARY KEY (feed_id)
)
WITH (
  OIDS=FALSE
);


DROP TABLE IF EXISTS profile_rec CASCADE;

CREATE TABLE profile_rec
(
  profile_id integer,
  twitter_handle text,
  user_id integer,

  CONSTRAINT pk_profile_rec PRIMARY KEY (profile_id),
  CONSTRAINT fk_user_id FOREIGN KEY (user_id)
      REFERENCES auth_user (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION

)
WITH (
  OIDS=FALSE
);

