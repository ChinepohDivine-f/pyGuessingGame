import random
import time
import emojis

def logo():
    text = """

      ___     ___      _          _____                       __    
  / _ \___/ (_)  __(_)__  ___ / ___/__  ___  _______ ___  / /____
 / // / _  / / |/ / / _ \/ -_) /__/ _ \/ _ \/ __/ -_) _ \/ __(_-<
/____/\_,_/_/|___/_/_//_/\__/\___/\___/_//_/\__/\__/ .__/\__/___/
                                                  /_/            
    
    """
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.0005)
    print()

def game_help():
    print("'help' for help")
    print("'play' to start game")
    print("'quit' to leave the game")

def mode(num, r):
    #good emojis
    winner_emojis = [":smilling_face", ":winking_face", ":star_struct", ":grinning_face_with_sweat"]
    #bad emojis
    loser_emojis = [":wozzy_face", ":pensive-face", ":face_with_rolling_eyes", ":face_with_head_bandage"]
    
    
    #define the game mode by varying i and the random number
    print("------------easy mode-------------")
    print("You have ", r, "chances. Good Luck!")
    i = 0
    while i != r:
        my_num = int(input(print(f"Guess {i+1}: ", end="")))
        if my_num == num:
            print("You win ", random.choice(winner_emojis))
            time.sleep(2)
            break
            return
        elif my_num > num:
            print("try again. that was too large", random.choice(loser_emojis))
        elif my_num < num:
            print("try again. that was too small", random.choice(loser_emojis))
        i = i + 1

def play():
    logo()

    random_number = random.randint(1,100)
    print("Choose Your mode \n 'easy' or 'hard' :face_savoring_food")
    choice = input(print(">> ", end=""))
    if choice == 'easy':
        mode(random_number, 10) # 10 is for easy mode
    elif choice == 'hard':
        mode(random_number, 5) # 5 is for hard mode

def run():

    game_help()
    state = input(print("Choose Your your option: ", end=""))
    
    if state == "play":
        play()
    elif state == "help":
        game_help()
    elif state == "quit":
        print("Closing game . . .")
        time.sleep(2)
        exit(0)

if __name__ == '__main__':
    logo()
    print("Guessiing game in python v2")
    while True:
        try:
            run()
            
        except KeyboardInterrupt:
            logo()
            print("closing game . . .")
            time.sleep(2);
            exit()
        logo()
       
