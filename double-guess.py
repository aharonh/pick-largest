import random
import os
import sys 
import numpy as np
import termplotlib as tpl

# settings
MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize
BET_AMOUNT = 1
NUMBER_OF_GAMES_TO_PLAY = 10000
INITIAL_GAME_SATE = { 
    "a": { "value": None }, "b": { "value": None }, "c": { "value": None }, "guess": { "value": None },
    "money": NUMBER_OF_GAMES_TO_PLAY, "wins": 0, "losses": 0, "rounds_played": 0 }
GUESS_LESSER = 0
GUESS_GREATER = 1
ALL_PLAYS_FILE = 'result.csv'

#######################################################################################################
# game model - game state transformation methods
#
# each method gets game state as a parameter and returns game state that is result from it's action

def flip_card(game_state, card):
    new_state = dict(game_state)
    random.seed(a=new_state[card]["seed"])
    random.setstate(new_state[card]["random_state"])
    new_state[card]["value"] = random.randint(MIN_INT, MAX_INT)
    new_state[card]["random_state"] = random.getstate()
    return new_state 

def guess_s1(game_state): 
    new_state = dict(game_state)
    random.seed(a=new_state["guess"]["seed"])
    random.setstate(new_state["guess"]["random_state"])
    new_state["guess"]["value"] = random.choice(CHOICES) 
    new_state["guess"]["random_state"] = random.getstate()
    return new_state

def guess_s2(game_state):
    new_state = dict(game_state)
    new_state["guess"]["value"] = GUESS_LESSER if (new_state["a"]["value"] < new_state["c"]["value"]) else GUESS_GREATER
    return new_state

def flip_a(game_state):
    return dict(game_state) if game_state["a"]["value"] is not None else flip_card(game_state, "a") 

def flip_b(game_state):
    return dict(game_state) if game_state["b"]["value"] is not None else flip_card(game_state, "b")

def flip_c(game_state):
    return dict(game_state) if game_state["c"]["value"] is not None else flip_card(game_state, "c")

def eval_game(game_state):
    new_state = dict(game_state)
    won = ((game_state["a"]["value"] < game_state["b"]["value"]) and (game_state["guess"]["value"] == GUESS_LESSER)) or \
        (game_state["a"]["value"] > game_state["b"]["value"] and (game_state["guess"]["value"] == GUESS_GREATER))
    new_state["money"] += BET_AMOUNT if won else -BET_AMOUNT
    new_state["wins" if won else "losses"] += 1
    new_state["rounds_played"] += 1
    return new_state

def reset_cards(game_state):
    new_state = dict(game_state)
    for card in ["a", "b", "c"]:
        new_state[card]["value"] = None
    return new_state

#######################################################################################################
# display/save/runner helper functions 

def display_stats(game_state, performance, message = "game state"):
    for card in ["a", "b", "c"]:
        print("{}: {}, seed: {}".format(card, game_state[card]["value"], game_state[card]["seed"]))
    print("last_guess: {}, seed: {}".format(game_state["guess"]["value"], game_state["guess"]["seed"]))
    print("money: {}, wins: {}, losses: {}".format(game_state["money"], game_state["wins"], game_state["losses"]))
    print("performance:")
    fig = tpl.figure()
    fig.plot(np.linspace(0, NUMBER_OF_GAMES_TO_PLAY, NUMBER_OF_GAMES_TO_PLAY), 
        performance[1, :], width=60, height=20)
    fig.show()

def save_play(all, game_state, play_number):
    all[play_number, 0] = game_state["a"]["value"]
    all[play_number, 1] = game_state["b"]["value"]
    all[play_number, 2] = game_state["guess"]["value"]

def save_performance(performance, play_number, money):
    performance[0, play_number] = play_number
    performance[1, play_number] = money

def run_all_games(strategy):
    state = dict(INITIAL_GAME_SATE)
    all_plays = np.zeros((NUMBER_OF_GAMES_TO_PLAY, 3), dtype=int)
    performance = np.zeros((2, NUMBER_OF_GAMES_TO_PLAY), dtype=int)
    for i in range(0, NUMBER_OF_GAMES_TO_PLAY):
        for step in strategy["steps"]:
            state = step(state)
        state = eval_game(state)
        save_performance(performance, i, state["money"])
        save_play(all_plays, state, i)
        state = reset_cards(state)
    display_stats(state, performance = performance, message = "{} game state".format(strategy["name"]))
    np.savetxt("{}_{}".format(strategy["name"], ALL_PLAYS_FILE), all_plays, 
        delimiter=',', newline='\n', header="a,b,guess", fmt=['%d', '%d', '%d'], comments='' )

#######################################################################################################
# main program start

# initialize
CHOICES = [ GUESS_LESSER, GUESS_GREATER ]
for card in ["a", "b", "c"]:
    INITIAL_GAME_SATE[card]["seed"] = int.from_bytes(os.getrandom(16, 0), byteorder='big')
    random.seed(INITIAL_GAME_SATE[card]["seed"])
    INITIAL_GAME_SATE[card]["random_state"] = random.getstate()
INITIAL_GAME_SATE["guess"]["seed"] = int.from_bytes(os.getrandom(16, 0), byteorder='big')
random.seed(INITIAL_GAME_SATE["guess"]["seed"])
INITIAL_GAME_SATE["guess"]["random_state"] = random.getstate()
strategy_1 = { "name": "blind_guess", "steps": [ flip_a, guess_s1, flip_b ] }
strategy_2 = { "name": "advanced_guess", "steps": [ flip_a, flip_c, guess_s2, flip_b ] }
# run all games player 1 and 2
run_all_games(strategy_1)
run_all_games(strategy_2)
