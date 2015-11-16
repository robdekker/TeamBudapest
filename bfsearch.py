import sys, rushutils, os.path, collections
from timeit import default_timer as timer


def bfs():
    while len(queue) > 0:
        node = queue.pop(0)
        for move in node.get_moves():
            child = node.move(move[0], move[1])
            if move[0] == '?':
                if child.win():
                    return child
            if child.get_hash() not in states:
                states.add(child.get_hash())
                queue.append(child)

# check if file is supplied
if len(sys.argv) <= 1:
    print "No file is supplied"
    print "Usage: python BFS.py <board.txt>"
    sys.exit()

# check if file exists
elif not os.path.isfile(sys.argv[1]):
    print "File can't be loaded"
    print "Usage: python BFS.py <board.txt>"
    sys.exit()

# load board from file
else:

    # initialize root node
    root = rushutils.Board(None, None, None, None)
    root.load_from_file(sys.argv[1])

    # initialize queue and states archive
    states = set()
    queue = list()
    states.add(root.get_hash())
    queue.append(root)

# start the timer
start = timer()

# get first route to solution
current = bfs()

# stop the timer
end = timer()

# get the moves from to the winning state
moves = collections.deque()
while current.parent is not None:
    moves.appendleft(current.moved)
    current = current.parent

# print results
print "\nSolved in %d moves, in the time of %f seconds" % (len(moves), (end - start))
print moves
print