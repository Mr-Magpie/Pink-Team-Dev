-- delete all data

DELETE FROM word_frequency_rec;
DELETE FROM article_rec;
DELETE FROM word_rec;
DELETE FROM user_prefs_rec;
DELETE FROM user_rec;

ALTER SEQUENCE word_rec_word_id_seq RESTART WITH 1;
ALTER SEQUENCE article_rec_article_id_seq RESTART WITH 1;
ALTER SEQUENCE user_prefs_rec_user_word_id_seq RESTART WITH 1;
ALTER SEQUENCE user_rec_user_id_seq RESTART WITH 1;