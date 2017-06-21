import pprint, random

def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    new_values=[]
    for i in range(len(values)//n):
        new_values.append(values[i*n:i*n+n])
    return new_values

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)), file=out)
        if str(row) in '25':
            print(line, file=out)
    print('', file=out)

def get_row(values, pos): return values[pos[0]]

def get_col(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    new_values = []
    for i in range(len(values)):
        new_values.append(values[i][pos[1]])
    return new_values

def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    new_values = []
    for i in range(3):
        for j in range(3):
            new_values.append(values[3*(pos[0]//3)+i][3*(pos[1]//3)+j])
    return new_values

def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_position([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_position([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_position([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='.': return (i, j)

def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    poss_vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    return sorted(list(set(poss_vals) - set(row) - set(col) - set(block)))

solved=0
def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    empty = find_empty_positions(grid)
    if not empty:
        global solved
        solved+=1
        return grid
    poss = find_possible_values(grid, empty)
    for i in range(len(poss)):
        grid[empty[0]][empty[1]] = poss[i]
        if solve(grid):
            return grid
        else:
            grid[empty[0]][empty[1]] = '.'
    return None

def generate_sudoku(n):
    a = [7,8,9,1,2,3,4,5,6]
    grid=[]
    for i in range(9):
        if i!=(3 or 6):
            for k in range(3):
                box = a[0]
                for j in range(len(a)-1):
                    a[j]=str(a[j+1])
                a[-1]=str(box)
            print(a)
            grid.append(a)
        else:
            for k in range(4):
                box = a[0]
                for j in range(len(a)-1):
                    a[j]=str(a[j+1])
                a[-1]=str(box)
            print(a)
            grid.append(a)
	print(grid)
    return grid
	
if __name__ == '__main__':
    out=open("output.txt", mode='w')
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        solve(grid)
        display(grid)
    out.close()