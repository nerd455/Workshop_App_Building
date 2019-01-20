import tkinter
import random


player_speed = 18
game_speed = 1

score = 0
scor = 0
lost = False
player = None
obs_top = None
obs_top_2 = None
obs_bottom = None
obs_bottom_2 = None
score_writer = None

def obstacles():
    global lost, intro_writer, obs_top, obs_top_2, obs_bottom, obs_bottom_2, score, score_writer, scor

    if lost == False:
        ran_height = random.randint(60, random.randint(80, (random.randint(100, 150))))
        scor += 1

        if scor % 100 == 0:
            score += 1

        game_canvas.delete(score_writer)
        score_writer = game_canvas.create_text(44, 10, text='Score: '+str(score))

        yx = game_canvas.coords(player)
        x = game_canvas.coords(obs_top)

        if x[2] > 20:
            if yx[1] < x[3]:
                if yx[2] < x[2] and yx[2] > x[0]:
                    lost = True
                if yx[0] < x[0] and yx[2] > x[2]:
                    lost = True
                if yx[0] < x[2] and yx[0] > x[0]:
                    lost = True
            game_canvas.move(obs_top, -1*game_speed, 0)

        if x[0] == 360 and obs_bottom == None:
            obs_bottom = tkinter.Canvas.create_rectangle(game_canvas, 460, ran_height, 480, 180, fill='orange')
        elif obs_bottom != None:
            xx = game_canvas.coords(obs_bottom)
            if xx[0] == 20:
                game_canvas.delete(obs_bottom)
                obs_bottom = tkinter.Canvas.create_rectangle(game_canvas, 460, ran_height, 480, 180, fill='orange')
            else:
                if yx[3] > xx[1]:
                    if yx[2] < xx[2] and yx[2] > xx[0]:
                        lost = True
                    if yx[0] < xx[0] and yx[2] > xx[2]:
                        lost = True
                    if yx[0] < xx[2] and yx[0] > xx[0]:
                        lost = True
                game_canvas.move(obs_bottom, -1 * game_speed, 0)

        if x[0] == 240 and obs_top_2 == None:
            obs_top_2 = tkinter.Canvas.create_rectangle(game_canvas, 460, 20, 480, ran_height, fill='orange')
        elif obs_top_2 != None:
            xxx = game_canvas.coords(obs_top_2)
            if xxx[0] == 20:
                game_canvas.delete(obs_top_2)
                obs_top_2 = tkinter.Canvas.create_rectangle(game_canvas, 460, 20, 480, ran_height, fill='orange')
            else:
                if yx[1] < xxx[3]:
                    if yx[2] < xxx[2] and yx[2] > xxx[0]:
                        lost = True
                    if yx[0] < xxx[0] and yx[2] > xxx[2]:
                        lost = True
                    if yx[0] < xxx[2] and yx[0] > xxx[0]:
                        lost = True
                game_canvas.move(obs_top_2, -1 * game_speed, 0)

        if x[0] == 120 and obs_bottom_2 == None:
            obs_bottom_2 = tkinter.Canvas.create_rectangle(game_canvas, 460, ran_height, 480, 180, fill='orange')
        elif obs_bottom_2 != None:
            xxxx = game_canvas.coords(obs_bottom_2)
            if xxxx[0] == 20:
                game_canvas.delete(obs_bottom_2)
                obs_bottom_2 = tkinter.Canvas.create_rectangle(game_canvas, 460, ran_height, 480, 180, fill='orange')
            else:
                if yx[3] > xxxx[1]:
                    if yx[2] < xxxx[2] and yx[2] > xxxx[0]:
                        lost = True
                    if yx[0] < xxxx[0] and yx[2] > xxxx[2]:
                        lost = True
                    if yx[0] < xxxx[2] and yx[0] > xxxx[0]:
                        lost = True
                game_canvas.move(obs_bottom_2, -1 * game_speed, 0)

        if x[0] == 20:
            game_canvas.delete(obs_top)
            obs_top = tkinter.Canvas.create_rectangle(game_canvas, 460, 20, 480, ran_height, fill='orange')

        game_canvas.after(10, obstacles)

    else:
        show_end()
        game_canvas.unbind('<Right>')
        game_canvas.unbind('<Left>')
        game_canvas.unbind('<Down>')
        game_canvas.unbind('<Up>')
        game_canvas.bind('<Tab>', start_game)
        game_canvas.bind('<space>', quit_game)


def show_end():
    global intro_writer
    intro_writer = game_canvas.create_text(250, 100, justify='center',
                                           text='GAME OVER!!! Your Score: ' + str(
                                               score) + "\n\nPress 'Tab' to play again\n\nPress 'Space' to quit'",
                                           font='Ariel 19')


def quit_game(event):
    root.quit()


def player_move_up(event):
    x = game_canvas.coords(player)
    if x[1] > 21:
        game_canvas.move(player, 0, -1*player_speed)


def player_move_down(event):
    x = game_canvas.coords(player)
    if x[3] < 180:
        game_canvas.move(player, 0, 1*player_speed)


def player_move_front(event):
    global lost
    yx = game_canvas.coords(player)
    if yx[2] < 480 and lost == False:
        game_canvas.move(player, 1*player_speed, 0)


def player_move_back(event):
    x = game_canvas.coords(player)
    if x[0] > 20:
        game_canvas.move(player, -1*player_speed, 0)


def start_game(event):
    global scor, end_game, score, lost, obs_bottom_2, obs_bottom, obs_top, obs_top_2, player, score_writer
    score = 0
    scor = 0
    game_canvas.delete(obs_top)
    game_canvas.delete(obs_top_2)
    game_canvas.delete(obs_bottom)
    game_canvas.delete(obs_bottom_2)
    game_canvas.delete(score_writer)
    game_canvas.delete(player)
    game_canvas.delete(intro_writer)
    lost = False
    player = None
    obs_top = None
    obs_top_2 = None
    obs_bottom = None
    obs_bottom_2 = None
    end_game = None

    game_canvas.bind('<Right>', player_move_front)
    game_canvas.bind('<Left>', player_move_back)
    game_canvas.bind('<Down>', player_move_down)
    game_canvas.bind('<Up>', player_move_up)

    game_canvas.unbind('<Tab>')
    game_canvas.delete(intro_writer)

    player = tkinter.Canvas.create_rectangle(game_canvas, 40, 90, 80, 110, fill='light green')

    obs_top = tkinter.Canvas.create_rectangle(game_canvas, 460, 20, 480,
                                              random.randint(50, random.randint(80, (random.randint(100, 150)))),
                                              fill='orange')

    score_writer = game_canvas.create_text(44, 10, text='Score:' + str(score))
    lost = False
    obstacles()


root = tkinter.Tk()
root.title('Obstacle Game')
root.resizable(False, False)

game_canvas = tkinter.Canvas(root, height=200, width=500)

line_down = tkinter.Canvas.create_line(game_canvas, 20, 180, 480, 180)
line_top = tkinter.Canvas.create_line(game_canvas, 20, 20, 480, 20)


intro_writer = game_canvas.create_text(250, 100, justify='center',
                                       text="Welcome to 'THE OBSTACLE GAME'\n\nUse the 'Arrow' keys to play\n\nPress 'TAB' key twice to start the game",
                                       font='Ariel 16')

water_mark = game_canvas.create_text(407, 193, text='Developed by a Guy')


game_canvas.bind('<Right>', player_move_front)
game_canvas.bind('<Left>', player_move_back)
game_canvas.bind('<Down>', player_move_down)
game_canvas.bind('<Up>', player_move_up)
game_canvas.bind('<Tab>', start_game)
game_canvas.pack()
root.mainloop()

