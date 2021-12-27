import pyglet
from pyglet import shapes
from pyglet.window import key


def solve():
    f = open("Sudoku.txt", "r")
    board = []
    nums_rows = [[], [], [], [], [], [], [], [], []]
    nums_columns = [[], [], [], [], [], [], [], [], []]
    nums_sqrs = [[], [], [], [], [], [], [], [], []]
    for i, val in enumerate(f.read()):
        try:
            board.append(int(val))
            nums_rows[i // 9].append(int(val))
            nums_columns[i % 9].append(int(val))
            nums_sqrs[i // 3 % 3 + (i // 3 // 3 // 3)*3].append(int(val))
        except:
            board.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    f.close()

    print(nums_rows)
    print(nums_columns)
    print(nums_sqrs)

    solved = False
    t = 0
    while not solved:
        solved = True
        t += 1

        for i, val in enumerate(board):
            if isinstance(val, list):
                solved = False
                for j, possible_n in enumerate(val):
                    if possible_n in nums_rows[i // 9] or possible_n in nums_columns[i % 9]:    # rows and columns check
                        val.remove(possible_n)
                    elif possible_n in nums_sqrs[i // 3 % 3 + (i // 3 // 3 // 3)*3]:
                        val.remove(possible_n)
                if len(val) == 1:
                    board[i] = val[0]
                    nums_rows[i // 9].append(val[0])
                    nums_columns[i % 9].append(val[0])
                    nums_sqrs[i // 3 % 3 + (i // 3 // 3 // 3)*3].append(val[0])

            print(val)

        if t == 300:
            return board

    return (board)


def main():
    win_dim = (700, 700)
    window = pyglet.window.Window(win_dim[0] + 10, win_dim[1] + 10)
    batch_sqrs = pyglet.graphics.Batch()

    squares = []
    for i in range(9):
        squares.append(shapes.Rectangle(x=(i % 3) * win_dim[0] / 3 + 10, y=(i // 3) * win_dim[0] / 3 + 10,
                                        width=win_dim[0] / 3 - 10,
                                        height=win_dim[1] / 3 - 10, color=(100, 100, 100), batch=batch_sqrs))
    for i in range(81):
        squares.append(shapes.Rectangle(x=(i % 9) * win_dim[0] / 9 + 10, y=(i // 9) * win_dim[0] / 9 + 10,
                                        width=win_dim[0] / 9 - 10,
                                        height=win_dim[1] / 9 - 10, color=(255, 255, 255), batch=batch_sqrs))

    f = open("Sudoku.txt", "r")

    batch_nums = pyglet.graphics.Batch()
    nums = []
    for i, num in enumerate(f.read()):
        if num == '-': num = ' '

        nums.append(pyglet.text.Label(num, font_name='Ariel', font_size=30, x=(i % 9) * win_dim[0] / 9 + 35,
                                      y=(i // 9) * win_dim[0] / 9 + 30, color=(100, 100, 100, 100), batch=batch_nums))

    f.close()

    batch_solu = pyglet.graphics.Batch()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.SPACE:
            solution = solve()
            for j, sol in enumerate(solution):
                nums[j] = pyglet.text.Label(str(sol), font_name='Ariel', font_size=30, x=(j % 9) * win_dim[0] / 9 + 35,
                                      y=(j // 9) * win_dim[0] / 9 + 30, color=(100, 100, 100, 100), batch=batch_nums)


    @window.event
    def on_draw():
        window.clear()
        batch_sqrs.draw()
        batch_nums.draw()

    pyglet.app.run()


if __name__ == '__main__':
    main()
