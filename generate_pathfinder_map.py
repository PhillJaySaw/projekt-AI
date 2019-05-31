import sys
from os import path


def generate_pathfinder_map():
    map_info = []
    # data_file = open('map.txt')
    # map_data = data_file.readlines()

    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, 'map.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)

    for row, tiles in enumerate(map_data):
        y = []
        for col, tile in enumerate(tiles):
            if tile == '1':
                y.append(1)
            if tile == '0' or tile == 'P':
                y.append(0)
        map_info.append(y)

    return(map_info)
