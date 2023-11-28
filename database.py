"""
Author: Marc-Antoine Romao
Module: Proj-DBPY
Date: 14.11.2023
"""

import csv
import mysql.connector

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password='root', database='braintraining',
                                   buffered=True, autocommit=True)


def close_dbconnection():
    db_connection.close()


def add_students(user):
    query = "INSERT INTO players (name) values (%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (user,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def add_scores(date_start,number_of_successes, number_of_tries, duration, Players_id, Exercises_id):
    query = "INSERT INTO scores (date_start,number_of_successes, number_of_tries, duration, Players_id, Exercises_id) values (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (date_start,number_of_successes, number_of_tries, duration, Players_id, Exercises_id,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def get_exercisesid(exercise):
    query = "SELECT id FROM exercises WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercise,))
    row = cursor.fetchone()
    cursor.close()
    return row


# Function to get students ID
def get_playerid(player):
    query = "SELECT id FROM players WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (player,))
    row = cursor.fetchone()
    cursor.close()
    return row

def get_allScores():
    query = "SELECT * FROM scores"
    cursor = db_connection.cursor()
    cursor.execute(query, multi=True)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def get_playersnames(player_id):
    query = "SELECT name FROM players WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (player_id,))
    row = cursor.fetchone()
    cursor.close()
    return row


# Function to get exercises name by the ID
def get_exercisesname(exercises_id):
    query = "SELECT name FROM exercises WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercises_id,))
    row = cursor.fetchone()
    cursor.close()
    return row