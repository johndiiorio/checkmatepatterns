import chess.pgn, time, os
from collections import Counter

path_to_database = 'game_database.pgn'
num_occurences = 100
min_plycount = 10

start_time = time.time()
pgn = open(path_to_database, 'r')
file_fens = open('output_fens.txt', 'w')
game = chess.pgn.read_game(pgn)
while(game):
    if game.headers["Result"] != "1/2-1/2" and int(game.headers["PlyCount"]) > min_plycount - 1:
        node = game
        moves = []
        while not node.is_end():
            next_node = node.variation(0)
            moves.append(node.board().san(next_node.move))
            node = next_node
        if node.comment == "White checkmated" or node.comment == "Black checkmated":
            board = chess.Board()
            for index, move in enumerate(moves):
                board.push(board.parse_san(moves[index]))            
            file_fens.write(board.board_fen() + '\n')
    game = chess.pgn.read_game(pgn)
cnt = Counter()
file_fens.close()
file_fens = open('output_fens.txt', 'r')
file_output = open('output.txt', 'w')
for line in file_fens:
    cnt[line] += 1
file_fens.close()
os.remove('output_fens.txt')
mclist = Counter(cnt).most_common(num_occurences)
file_output.write(str(mclist))
for fen, value in mclist:
    board = chess.Board(fen + " w KQkq - 0 4")
    file_output.write(str(board) + '\n')
    file_output.write(fen + '\n')
file_output.close()
print("Completed in %s seconds" % (time.time() - start_time))
