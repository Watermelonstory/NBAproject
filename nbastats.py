#connect sqlite database
import sqlite3

conn = sqlite3.connect('nbaplayerstats.db')
print("Opened database successfully")
print("INSTRUCTIONS: Select a mode to filter different nba stats for nba players enter exit to go back or exit program. All records are from 1950-2017\n WARNING: Do not enter a blank field or the program will stop working.")
val = 1
val2 = 1
mode = 1
while mode:
    mode = input ('''Please select mode. teams, avgpoints, allplayers, alldata, playeryears.\n''')
    #TEAMS QUEARY
    if mode == "teams":
        while val:
            val = input('Enter NBA playername you want to know every team they have played for. EXAMPLE: "Larry Bird" \n')
            if val == "exit":
                val = "1"
                break
            cursor = conn.execute('SELECT DISTINCT teamname FROM nbaplayer WHERE playername = "'+str(val)+'"; ' )
            for row in cursor:
                print("Teams:", row[0], "\n")
    #Average Points
    if mode == "avgpoints":
        while val:
            val = input('Input playername you want to see average points per game. EXAMPLE: "Larry Bird"\n')
            if val == "exit":
                val = "1"
                break
            val2 = input('Input the year you want to see the average points per year for. EXAMPLE: "1985"\n')
            cursor = conn.execute('SELECT AVG(pts) FROM nbaplayer WHERE playername ="'+str(val)+'" AND seasonyear = "'+str(val2)+'" ')
            for row in cursor:
                print("AVG PPG for "+str(val)+" in season "+str(val2)+":", row[0], "\n")
    #Players Queary
    if mode == "allplayers":
        while val:
            val = input('Enter "list" to see all searchable players otherwise wise exit to go back.\n ')
            if val == "exit":
                val = "1"
                break
            elif val == "list":
                cursor = conn.execute('SELECT DISTINCT playername FROM nbaplayer')
                for row in cursor:
                    print("PLAYER:", row[0], "\n")
    #all data Queary
    if mode == "alldata":
        while val:
            val = input('Enter a year to see all records in that year. 1950-2017\n')
            if val == "exit":
                val = "1"
                break
            cursor = conn.execute('SELECT * FROM nbaplayer Where seasonyear = "'+str(val)+'"')
            for row in cursor:
                print(row,"\n")
    if mode == "playeryears":
        while val:
            val = input('Enter a player name to see years they played.\n')
            if val == "exit":
                val = "1"
                break
            val2 = input('Input D fore decending years. or A for acending years')
            if val2 == "D" or "d":
                val2 = "DESC"
            if val2 == "A" or "a":
                val2 = "ASC"
            if val2 == "exit":
                break
            cursor = conn.execute('SELECT DISTINCT seasonyear FROM nbaplayer Where playername = "'+str(val)+'" ORDER BY seasonyear '+str(val2)+'')
            for row in cursor:
                print(row,"\n")