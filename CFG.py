def GetConfig(index : int):
    f = open("Config.txt", "r")
    txt = f.read().split()
    col1 = txt[3]
    col2 = txt[6]
    resolution = txt[10]
    size = txt[13]
    grid = txt[16]
    col1 = col1.replace('(', '')
    col1 = col1.replace(')', '')
    col1 = col1.split(',')
    col2 = col2.replace('(', '')
    col2 = col2.replace(')', '')
    col2 = col2.split(',')
    if index == 1:
        return tuple((int(col1[0]),int(col1[1]),int(col1[2])))
    if index == 2:
        return tuple((int(col2[0]),int(col2[1]),int(col2[2])))
    if index == 3:
        return int(resolution)
    if index == 4:
        return int(size)
    if index == 5:
        if grid == "True":
            return True
        elif grid == "False":
            return False
        else:
            return True


def Save(grid):
    f = open("Save.txt", "w+")
    for _ in grid:
        for i in _:
            f.write(str(i))
            f.write(' ')
        f.write('\n')

def divide_array(array, chunk_size):
    return [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]


def Load(grid_r : list):
    f = open("Save.txt", "r")
    sf = f.read().split()
    sf = list(map(int, sf))
    grid = divide_array(sf, GetConfig(4))
    if len(grid_r) == len(grid):
        return grid
    else:
        return grid_r
