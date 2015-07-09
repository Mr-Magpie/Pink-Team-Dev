#!/usr/bin/python2.4
#
# Small script to read words.csv into postgres tables 
#
import csv
import psycopg2

conn_string = "dbname='nlstudent' user = 'nlstudent' password ='2015pink'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# check if the word is already in the database
def word_not_in_db(word):
    cursor.execute("SELECT word_id FROM word_rec WHERE word = %s", (word,))
    return cursor.fetchone() is None

# knowing the word is in db, get its word_id
def get_word_id(word):
    cursor.execute("SELECT word_id FROM word_rec WHERE word = %s", (word,))
    return cursor.fetchone()

# check if the url is already in the database
def url_not_in_db(url):
    cursor.execute("SELECT article_url FROM article_rec WHERE article_url = %s", (url,))
    return cursor.fetchone() is None

# knowing the url is in db, get the article_url
def get_article_id(url):
    cursor.execute("SELECT article_id FROM article_rec WHERE article_url = %s", (url,))
    return cursor.fetchone()

def delete_word_frequency_rec(article_id):
    delete_word_frequency_rec = "DELETE FROM word_frequency_rec WHERE article_id = %s;"
    cursor.execute(delete_word_frequency_rec,[article_id])
    conn.commit()

def print_db():
    read_all = """SELECT article_url,a.article_id,word,w.word_id,frequency
       FROM article_rec AS a
       JOIN word_frequency_rec AS f
       ON a.article_id = f.article_id
       JOIN word_rec AS w ON f.word_id = w.word_id
       ORDER BY article_id ASC """
    cursor.execute(read_all)
    rows = cursor.fetchall()
    for row in rows:
        print (" ", row)

#print_db()

prev_url = ' '
# prev_word = ' '
prev_article_id = 0
word_id = 0

# read url-word frequencies, format [url,word,frequency]
# reader = csv.reader(open('words.csv','rb'))

with open('words.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for current_line in reader:
        url = current_line[0]
        word = current_line[1]
        frequency = current_line[2]
        #print current_line
        #print "prev_url: ",prev_url
        if prev_url != url:
            #change of url, check if it's already in database
            if url_not_in_db(url):
                #it's not in database so store this as a new url
                #print "new article, storing in database"
                store_article_rec = """INSERT INTO article_rec(article_id,article_url)
                                        VALUES (DEFAULT,%s)
                                        RETURNING article_id """
                cursor.execute(store_article_rec,[url])
                #store the current value of article_id sequence
                article_id = cursor.fetchone()[0]
                conn.commit()
            else:
                #get article id
                article_id = get_article_id(url)
                #delete word_frequency_rec for this article
                delete_word_frequency_rec(article_id)

            #don't run this the first time through
            #print "prev_article_id: ", prev_article_id
            # if prev_article_id != 0:
                # #get records for the previous article, sort them add the rank order and store to db
                # get_words_sorted = """SELECT word_id,frequency FROM word_frequency_rec
                                    # WHERE article_id = %s
                                    # ORDER BY article_id ASC , frequency DESC"""
                # cursor.execute(get_words_sorted,[prev_article_id])
                # rows = cursor.fetchall()
                # article_word_rank = 1
                # for row in rows:
                    # #print " ", row
                    # word_id = row[0]
                    # frequency = row[1]
                    # #add the rank (for that aricle,word combination)
                    # update_word_frequency_rec = """UPDATE word_frequency_rec
                                                # SET article_word_rank = %s
                                                # WHERE article_id=%s AND word_id = %s;"""
                    # cursor.execute(update_word_frequency_rec,(article_word_rank,prev_article_id,word_id))
                    # conn.commit()
                    # article_word_rank=article_word_rank+1

        if word_not_in_db(word):
            #print "new word"
            #print word
            check_word_rec = """INSERT INTO word_rec(word_id,word)
                                VALUES (DEFAULT,%s)
                                RETURNING word_id"""
            cursor.execute(check_word_rec,[word])
            #store the current value of word_id sequence
            word_id = cursor.fetchone()[0]
            conn.commit()
        else:
            # word in db already - look up its word_id
            word_id = get_word_id(word)

        #print url,word,frequency
        #print article_id,word_id,frequency
        #print url,article_id,word,word_id
        store_word_frequency_rec = """INSERT INTO word_frequency_rec(article_id,word_id,frequency)
                                    VALUES (%s,%s,%s);"""
        cursor.execute(store_word_frequency_rec,(article_id,word_id,frequency))
        conn.commit()

        #keep this url,word
        prev_url = url
        prev_word = word
        prev_article_id = article_id

# #now we've stored all records except for the last article in this set, add rank order for this one now
# get_words_sorted = """SELECT word_id,frequency FROM word_frequency_rec
                    # WHERE article_id = %s
                    # ORDER BY article_id ASC , frequency DESC"""
# cursor.execute(get_words_sorted,[article_id])
# rows = cursor.fetchall()
# #article_word_rank = 1
# for row in rows:
    # #print " ", row
    # word_id = row[0]
    # frequency = row[1]
    # #add the rank (for that aricle,word combination)
    # update_word_frequency_rec = """UPDATE word_frequency_rec
                                    # SET article_word_rank = %s
                                    # WHERE article_id=%s AND word_id = %s;"""
    # cursor.execute(update_word_frequency_rec,(article_word_rank,article_id,word_id))
    # conn.commit()
    # article_word_rank=article_word_rank+1


# print_db()

#============================================================

# # read user-word frequencies, format [user_email,word,frequency]
# reader = csv.reader(open('user_words.csv','rb'))

# article_urls = []

# prev_user_email = ' '

# for current_line in reader:
    # #save this user_email
    # current_user_email = url

    # if prev_user_email == current_user_email:
        # #if it's another record for the same user, just store user_prefs_rec
        # store_user_prefs_rec = "INSERT INTO user_prefs_rec(user_id,word,user_word_id,frequency) VALUES (%s,%s,DEFAULT,%s);"
        # cursor.execute(store_user_prefs_rec,(user_id,word,frequency))
        # conn.commit()
    # else:
        # # it's a new user so store this in user_rec
        # store_user_rec = "INSERT INTO user_rec(user_id,user_email) VALUES (DEFAULT,%s) RETURNING user_id"
        # cursor.execute(store_user_rec,[current_user_email])
        # #store the current value of user_id sequence
        # user_id = cursor.fetchone()[0]
        # store_user_prefs_rec = "INSERT INTO user_prefs_rec(user_id,word,user_word_id,frequency) VALUES (%s,%s,DEFAULT,%s);"
        # cursor.execute(store_user_prefs_rec,(user_id,word,frequency))
        # conn.commit()

    # #store this user_email
    # prev_user_email = current_user_email






