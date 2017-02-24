#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    return execute("DELETE from match;")


def deletePlayers():
    """Remove all the player records from the database."""
    return execute("DELETE from player")


def countPlayers():
    """Returns the number of players currently registered."""
    query = "SELECT count(*) FROM player"
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchone()
    conn.commit()
    conn.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    query = "INSERT INTO player(name) VALUES (%s)"
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, (name,))
    s = cursor.rowcount
    conn.commit()
    conn.close()
    return s


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = "SELECT * from standings;"
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    standings = cursor.fetchall()
    conn.commit()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO match(winner,loser) VALUES (%s,%s)"
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, (winner, loser))
    standings = cursor.rowcount
    conn.commit()
    conn.close()
    return standings


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    query = "SELECT * from standings;"
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    standings = cursor.fetchall()
    conn.commit()
    conn.close()
    
    i = 0
    pairings = []

    while i < len(standings):
        player_1_id = standings[i][0]
        player_1_name = standings[i][1]
        player_2_id = standings[i + 1][0]
        player_2_name = standings[i + 1][1]
        pairings.append((player_1_id, player_1_name, player_2_id, player_2_name))
        i = i + 2

    return pairings

def execute(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    s = cursor.rowcount
    # print "s = ", s
    conn.commit()
    conn.close()
    return s
