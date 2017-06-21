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


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [[values[i + j*n] for i in range(n)] for j in range((len(values))//n)]


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [raw[pos[1]] for raw in values]


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    kv=(pos[0]//3)*3+pos[1]//3
    lst=[]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if ((i//3)*3+j//3)==kv:
                lst.append(values[i][j])
    return lst


def find_empty_position(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_position([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_position([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_position([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j]=='.':
                return (i, j)
    return (-1, -1)

def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    poss_vals=set([str(i) for i in range(1, 10)])
    poss_vals=poss_vals.difference(get_col(grid, pos)).difference(get_block(grid, pos)).difference(get_row(grid, pos)) 
    if len(poss_vals)==1:
        return poss_vals.pop()
    else:
        return poss_vals


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for i in range(len(solution[0])):
        for j in range(len(solution)):
            box, solution[i][j] = solution[i][j], '.'
            if not ( box in find_possible_values(solution, (i, j)) ):
                solution[i][j]=box
                return False
            solution[i][j]=box
    return True


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    curr_pos=find_empty_position(grid)
    curr_vals=find_possible_values(grid, curr_pos)
    if curr_pos==(-1, -1):
        if check_solution(grid):
            return grid
        return grid
    elif not curr_vals:
        return grid
    for val in curr_vals:
        grid[curr_pos[0]][curr_pos[1]]=val
        solution=solve(grid)
        if find_empty_position(grid)==(-1, -1):
            return grid
            if check_solution(solution):
                return grid
        else:
            grid[curr_pos[0]][curr_pos[1]]='.'

if __name__ == '__main__':
    out=open("output.txt", mode='w')
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        solve(grid)
        display(grid)
    out.close()