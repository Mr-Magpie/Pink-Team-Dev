# -*- coding:utf-8 -*-

import codecs
import random
import time
import tweepy
import os
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import re
import psycopg2
from django.db import transaction

conn_string = "dbname='nlstudent' user='James' host="

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def get_keys_matix(path):
    matrix = [['' for x in range(4)] for y in range(9)]
    dict = [{} for x in range(9)]
    inner_dict = {'con_key':'', 'con_sec':'', 'acc_key':'', 'acc_sec':''}
    index = 0
    for line in open(path, 'r'):
        if not line.strip():
            continue

        a_line = line.strip().split(":")
        print(a_line[1])
        # re_line = re.compile(":")
        # print(re_line.findall(line))
        matrix[int(index / 4)][int(index % 4)] = a_line[1]
        index += 1
    return matrix

def initialization(consumer_key, consumer_secret, access_key, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

def get_friends(id, matrix, index_matrix):
    api = initialization(matrix[index_matrix][0], matrix[index_matrix][1], matrix[index_matrix][2], matrix[index_matrix][3])
    print ('the index is: ' + str(index_matrix))
    return put_into_file(id, matrix, api, index_matrix)

def put_into_file(id, matrix, api, index_matrix):
    while True:

        try:
            user = api.get_user(id)
            break
        except tweepy.TweepError as e:
            if e.args[0][-3:] == '403' or e.args[0][-3:] == '404':
                logfile = codecs.open('log', 'a')
                logfile.write('skip ' + str(id) + '\n')
                logfile.close()
                id += 1

                pass
            elif e.args[0][-3:] == '429':
                print ('change another key at ' + time.strftime("%H:%M:%S"))
                if index_matrix == 8:
                    index_matrix = -1
                index_matrix += 1
                api = initialization(matrix[index_matrix][0], matrix[index_matrix ][1], matrix[index_matrix][2], matrix[index_matrix][3])

                pass
            else:
                time.sleep(10)

    screen_name = user.screen_name
    print (user.listed_count)
    # print(user.lists_memberships( screen_name=screen_name))

    #get the lists that the user is in
    try:
        for list_obj in user.lists_memberships(screen_name=screen_name):
            print ('*******' + time.strftime("%H:%M:%S") + '*******')
            file = codecs.open('datawithqoute1', 'a', 'gbk')
            print ('list_id: ' + str(list_obj.id))
            put_into_list_rec(list_obj.id, list_obj.name, list_obj.description)
            contents = []
            index = 0
    #code error
            try:
                for member in tweepy.Cursor(api.list_members, list_obj.user.screen_name, list_obj.slug).items():
                    index += 1
                    if (index % 100) == 0:
                        print ('->', end='')
                    store_list_member_rec(list_obj.id, member.id)    
                    contents.append(str(member.id))

            except tweepy.TweepError as e:
                if e.args[0][-3:] == '429':
                    print ('change another key at ' + time.strftime("%H:%M:%S"))
                    if index_matrix == 8:
                        index_matrix = -1
                    index_matrix += 1
                    api = initialization(matrix[index_matrix][0], matrix[index_matrix][1], matrix[index_matrix][2], matrix[index_matrix][3])
                    user = api.get_user(id)
                    screen_name = user.screen_name
            try:
                if len(contents) != 0:
                    file.write(str(list_obj.id_str) + ', ' + str(list_obj.name) + ", '" + str(list_obj.description) + "', " + '*'.join(contents) + '\n')
                    file.flush()
                    print ('write into file successfully!')       
                    file.close()
                else:
                    print ('the contents is zero')
            except:
                print ('skip')
            print ("next")

    except tweepy.TweepError as e:
        print(e)
        if e.args[0][-3:0] == '503':
            print ('easy boy, the system will restart in 5s')
            time.sleep(10)
    return index_matrix

def store_list_member_rec(list_i, member_i):
    store_list_member = """INSERT INTO list_member_rec(list_id,member_id)
                                        VALUES (%s,%s)"""
    #try:
    check_exist = """SELECT member_id FROM list_member_rec WHERE list_id= %s"""
    #if cursor.execute(check_exist, (list_i,)) == member_i:
     #   pass
    #else:
    try:
        cursor.execute(store_list_member, (list_i, member_i))
    except psycopg2.IntegrityError:
        #conn.close()
        pass
    conn.commit()
    #except psycopg2.Error as e:
     #   print('ERROR store_list_member:')
        # conn.close()
   # else:
    #    conn.commit()

def put_into_list_rec(list_id, list_name, list_description):
    #if not list_not_in_db(list_id):
    #    delete_list_rec(list_id)
    try:
        store_list_rec(list_id, list_name, list_description)
    except psycopg2.IntegrityError as e:
        pass
    conn.commit()
  #  else:
    #    print ('list ID is not a digit')


def store_list_rec(listi, listn, listd):
    store_list = """INSERT INTO list_rec(list_id,list_name,list_description)
                                VALUES (%s,%s,%s)"""
    try:
        cursor.execute(store_list, (listi, listn, listd))
    except psycopg2.IntegrityError as e:
        pass
    #print('ERROR store_list:')
        # conn.close()
    #else:
    conn.commit()

# check if list is in db - returns TRUE if not in db
def list_not_in_db(listi):
    try:
        cursor.execute("SELECT list_id FROM list_rec WHERE list_id = %s", (listi,))
        return cursor.fetchone() is None
    except psycopg2.Error as e:
        print('ERROR:')
        # conn.close()

# delete the list_rec for the given list_id
def delete_list_rec(listi):
    delete_list = "DELETE FROM list_rec WHERE list_id = %s;"
    try:
        cursor.execute(delete_list, [int(listi)])
    except psycopg2.Error as e:
        print('ERROR delete_list_rec :')
        transaction.rolllback()
    else:
        conn.commit()


if __name__ == '__main__':
    print('start')
    matrix = get_keys_matix('20_keys')
    people = 12
    index_matrix = 0

    #pass in the username of the account you want to download
    while True:
        print ('this is %s run' %people)
        index_matrix = get_friends(people, matrix, index_matrix)
        logfile = codecs.open('log', 'a')
        logfile.write(str(people) + '\n')
        logfile.close()
        people += 1

