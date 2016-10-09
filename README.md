# Checkmate Patterns

This simple python script will find the most common chess checkmatting patterns if given a database of chess games.

### Usage

Place this script and your PGN chess database named *game_database.pgn* in the same directory and execute the script. All outputed information will be found in *output.txt*.

### How it works

The script first opens the database file (standard Portable Game Notation (PGN) format), and then plays through each game (using Python's chess library) to reach the final position; if this final position is a checkmate (not a draw or resignation) that was reached after a default *min_plycount* of five moves, the position is outputed to a text file. A frequency algorithm sorts through all the positions to find the most common occurences (specify this number with *num_occurences*). 