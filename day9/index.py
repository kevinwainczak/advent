from collections import deque

class MarbleGame:
    def __init__(self):
        self.marble_circle = deque()
        self.marbles_played = 0
        self.elves_playing = 459
        self.elf_scores = {}
        self.current_marble_index = -1
        self.current_player = 0
    
    def place_marble(self):
        # get the marble to play
        curr_marble = self.marbles_played
        
        # see if it's the first marble in play
        if self.marbles_played == 0:
            self.marble_circle.append(curr_marble)
        else:
            # if it's not a multiple of 23
            if curr_marble % 23 != 0:
                self.marble_circle.rotate(-2)
                self.marble_circle.appendleft(curr_marble)

            # we have our special case
            else:
                # remove the marble from seven counter clockwise
                self.marble_circle.rotate(7)
                
                    #marble_to_remove = self.marble_circle.pop(self.current_marble_index)
                
                # add the appropriate score to the elf
                extra_marble = self.marble_circle.popleft()
                score = curr_marble + extra_marble
                if str(self.current_player) not in self.elf_scores:
                    self.elf_scores[str(self.current_player)] = score
                else:
                    self.elf_scores[str(self.current_player)] += score
        
        # make it the next elf's turn
        self.current_player = (self.current_player + 1) % self.elves_playing
        self.marbles_played += 1
        #print(self.current_player)
        return curr_marble

    def get_elf_scores(self):
        return self.elf_scores
    
    def get_board(self):
        return self.marble_circle



def find_highest_score(last_marble_points):
    game = MarbleGame()
    last_marble_played = -1
    while last_marble_played != last_marble_points:
        last_marble_played = game.place_marble()
        #if last_marble_played % 1000 == 0:
            #print(((last_marble_played/last_marble_points) * 100), '%')
    best_elf = ''
    best_score = -1
    scores = game.get_elf_scores()
    for key in scores:
        if scores[key] > best_score:
            best_score = scores[key]
            best_elf = key
    return (best_elf, best_score)

def get_gameboards(last_marble):
    game = MarbleGame()
    for _ in range(last_marble):
        game.place_marble()
        print(_, game.get_board())

print(find_highest_score(71320))
print(find_highest_score(7132000))
        