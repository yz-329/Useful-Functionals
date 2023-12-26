"""
COMPSCI 130 Creative Extension GUI file by:
Starr Zhang
UPI: yzhb172
Last Modified: 14 Oct 2023 1:00 am
"""

##### Definition of Class #####
class Card: #single cards
    def __init__(self, init_data, init_next = None):
        self.data = init_data
        self.next = init_next
    
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        if self.get_data() == 13:
            return "{:^12}".format("K")
        elif self.get_data() == 12:
            return "{:^12}".format("Q")
        elif self.get_data() == 11:
            return "{:^12}".format("J")
        elif self.get_data() == 1:
            return "{:^12}".format("A")
        else:
            if self.get_data() != None:
                return "{:^12}".format(self.get_data())
            else:
                return "{:^12}".format("None")
    


class SinglePile:
    def __init__(self, cards = None): #cards = single pile of random cards
        self.remove_count = 13
        if cards == None:
            self.cards = []
        else:
            self.cards = cards
            for i in range(len(self.cards)):
                self.cards[i] = Card(self.cards[i])
    
    def get_cards(self):
        return self.cards
    
    def size(self):
        count = 0
        for card in self.cards:
            if card.get_data() == None:
                count += 0
            else:
                count += 1
        return count
    
    def not_empty(self):
        return len(self.cards) != 0
    
    def peek_bottom(self):
        return self.cards[self.size()].get_data()
    
    def add_bottom(self, card):
        self.cards.append(Card(card))
    
    def remove_bottom(self):
        return self.cards.pop(self.size() - 1)
    
    def add_cards(self, new_cards = []): 
        size = self.size()
        if self.cards[self.size()].get_data() == None:
            for i in range(len(new_cards)):
                self.cards[size + i] = new_cards[i]
    
    def is_card_move_valid(self, remove_index):
        if self.cards[remove_index] == self.peek_bottom():
            return True
        else:
            for i in range(remove_index, self.size()):
                if self.cards[i].get_data() - 1 != self.cards[i + 1].get_data():
                    print(False)
                    return False
        return True

    def remove_cards(self, pile_index, remove_index):
        lst = []
        # check if it's bottom and check if it's linked all the way to bottom
        valid = True

        if remove_index == self.size() - 1:
            lst.append(self.cards[remove_index])
        else:
            lst.append(self.cards[remove_index])
            for i in range(remove_index, self.size() - 1):
                if self.cards[i].get_data() == self.cards[i + 1].get_data() + 1:
                    lst.append(self.cards[i + 1])
                    print([", ".join(str(x.get_data()) for x in lst)])
                else:
                    valid = False

        if valid:
            for n in range(len(lst)):
                self.remove_bottom()
            
            for n in range(len(lst)):
                self.add_bottom(None)
        else:
            lst = []

        return lst
    
    def get_remove_count(self):
        return self.remove_count

    def __str__(self):
        return " ".join(str(x) for x in self.cards)
    
    def __len__(self):
        if self.cards == []:
            return 0
        else:
            if self.cards[0] == None:
                return 0 + len(self.cards[1:])
            else:
                return 1 + len(self.cards[1:])



class Piles:
    def __init__(self, deck1, deck2):
        self.piles = []
        self.num_cards = 13 * 2
        self.num_piles = (self.num_cards // 8) + 5
        self.undo = []

        for i in range(self.num_piles):
            self.piles.append(SinglePile())
        
        for n in range(len(self.piles)):
            for i in range(len(deck1)):
                if n == 0:
                    self.piles[n].add_bottom(deck1[i])
                elif n == 1:
                    self.piles[n].add_bottom(deck2[i])
                else:
                    self.piles[n].add_bottom(None)
    
    def add_bottom_undo(self, index = []):
        self.undo.append(index)
    
    def remove_bottom_undo(self):
        return self.undo.pop(-1)
    
    def size(self):
        return len(self.piles)

    def get_piles(self):
        return self.piles
    
    def is_pile_move_valid(self, i1, j1, i2, j2):
        move_from = True
        move_to = True
        if i1 < 2:
            if self.piles[i1].get_remove_count() < 1:
                move_from = True
            elif j1 != self.piles[i1].get_remove_count() - 1:
                print(self.piles[i1].size(), self.piles[i1].get_remove_count())
                print("计算bug")
                return False
        elif j1 == self.piles[i1].size() and j2 == self.piles[i2].size():
            print("两堆同时最后一张：empty + empty？")
            return False

        if j1 != self.piles[i1].size() and j2 != self.piles[i2].size():
            print("非最后一张")
            return False
        
        elif i2 <= 1 or j2 != self.piles[i2].size():
            print("其他")
            print("pile1", self.piles[i1])
            print("pile2", self.piles[i2])
            print("len func", j2, self.piles[i2].size() - 1, len(self.piles[i2]) - 1)
            move_to = False
        
        #only decrements can be added if statement
        
        if self.piles[i2].size() == 0:
            move_to = True
        elif self.piles[i2].get_cards()[j2 - 1].get_data() == self.piles[i1].get_cards()[j1].get_data() + 1:
            move_to = True
        else:
            move_to = False
        
        if move_from and move_to:
            print("pile move test success")
            return True
        else:
            print("pile move test fail")
            return False

    def move(self, i1, j1, i2, j2):
        if self.is_pile_move_valid(i1, j1, i2, j2):
            try:
                self.piles[i2].add_cards(self.piles[i1].remove_cards(i1, j1))
                if i1 < 2:
                    self.piles[i1].remove_count -= 1
                
                self.create_undo(i1, i2, j1, j2)
            except:
                return
            # for i in range(self.piles[i2].size(), 13):
            #     self.piles[i2].add_bottom(None)
        else:
            #clear all selection
            print("clear all selection")
    
    
    def display(self):
        for i in range(len(self.piles)):
            print(f"size: {self.piles[i].size()}, {i}: {self.piles[i]}")

    ###still needs work
    def is_complete(self):
        test_list = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        valid = False
        valid_count = 0
        for i in range(self.num_piles):
            lst = []
            if self.piles[i].size() == self.num_cards / 2:
                for j in range(self.piles[i].size()):
                    lst.append(self.piles[i].get_cards()[j].get_data())
                if lst == test_list:
                    valid_count += 1
            else:
                valid = False
        
        if valid_count == 2:
            valid = True

        return valid
    
    def create_undo(self, i1, i2, j1, j2):
        self.add_bottom_undo((i1, i2, j1, j2))
    
    def undo_move(self):
        if self.undo == []:
            return
        else:
            (i1, i2, j1, j2) = self.remove_bottom_undo()
            
            self.piles[i1].add_cards(self.piles[i2].remove_cards(i2, j2))
            if i1 < 2:
                self.piles[i1].remove_count += 1


##### Graphical User Interface #####
import tkinter as tk
import random

selected_pile = []
buttons = []

### initial game window ###
game = tk.Tk()
game.title("COMPSCI 130 Solitaire    :)")


### game logic
def generate_random():
    deck = list(range(1, 14))
    random.shuffle(deck)
    return deck

#initial assign of cards
deck0 = generate_random()
deck1 = generate_random()

piles = Piles(deck0, deck1)

def open_rule(): 
    rule_page = tk.Toplevel()
    rule_page.title("Game Rule")
    rule_text = tk.Label(rule_page, text = "\n"
                + "Welcome to Solitaire COMPSCI130 version!\n"
                + "Your goal is to move cards and in-line them from K to A!\n"
                + "\n"
                + "To move cards:\n"
                + "Click on a card or a pile of cards to select them, and click on the pile you wish to move the card(s) to.\n"
                + "You are only allowed to move card(s) to the 'empty' space.\n"
                + "\n"
                + "Tip: You can move partial deck of cards that are linked by descending order.\n")


    rule_text.pack()

def move_pile(piles):
    global selected_pile, buttons

    if len(selected_pile) == 4:
        i1 = selected_pile[0]
        j1 = selected_pile[1]
        i2 = selected_pile[2]
        j2 = selected_pile[3]

    valid = piles.is_pile_move_valid(i1, j1, i2, j2)

    if valid:
        piles.move(i1, j1, i2, j2)
        
        piles.display() #terminal debug purpose
        
        card_frame.destroy()

        buttons = []
        create_frame(piles)

    selected_pile = []

    
def button_clicked(piles, button, i1, j1):
    global selected_pile, buttons

    if len(selected_pile) < 4:
        button.config(bg = '#bbbbbb')
        selected_pile.append(i1)
        selected_pile.append(j1)
        move_pile(piles)
    else:
        selected_pile = []
        
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j] != None:
                buttons[i][j].config(bg = "SystemButtonFace")


#function buttons
def undo_clicked(piles):
    global card_frame, buttons
    piles.undo_move()
    piles.display()

    if card_frame != None:
        card_frame.destroy()

    buttons = []
    create_frame(piles)

def restart_game():
    global buttons
    piles = Piles(deck0, deck1)
    card_frame.destroy()

    buttons = []
    create_frame(piles)

def shuffle():
    global buttons
    deck0 = generate_random()
    deck1 = generate_random()

    piles = Piles(deck0, deck1)
    card_frame.destroy()

    buttons = []
    create_frame(piles)


#create frame for buttons on top of the main window
def create_frame(piles):
    global card_frame, buttons
 
    card_width = 754
    card_height = 400

    card_frame = tk.Frame(game, width = card_width, height = card_height)
    card_frame.grid(row = 2, column = 1)

    card_frame.grid_propagate(False)
    
    buttons = []
    display(piles, buttons)
    print(piles.is_complete())
    if piles.is_complete():
        print("_"*20)
        print("game ends")

        card_frame.destroy()
        card_frame = tk.Frame(game, width = card_width, height = card_height)
        card_frame.grid(row = 2, column = 1)

        card_frame.grid_propagate(False)

        congrats = tk.Label(card_frame, text = "Well Done!")
        congrats.pack()



buttons = []

# create buttons
def display(piles, buttons):
    for i in range(piles.size()):
        buttons.append([])
        for j in range(len(piles.get_piles()[i])):
            #append empty button
            if piles.get_piles()[i].get_cards()[j].get_data() == None:
                if j == piles.get_piles()[i].size():
                    buttons[i].append(tk.Button(card_frame, width = 12,
                                                text = "{:^12}".format("empty")))
                    buttons[i][j].config(command = lambda button = buttons[i][j], i = i, j = j: (button_clicked(piles, button, i, j)))
                    
                    buttons[i][j].grid(row = j, column = i)
                else:
                    buttons[i].append(None)
            elif i == 0 or i == 1:
                # replace size with count
                if j >= piles.get_piles()[i].get_remove_count() - 1:
                    buttons[i].append(tk.Button(card_frame, text = piles.get_piles()[i].get_cards()[j], width = 12))
                    buttons[i][j].config(command = lambda button = buttons[i][j], i = i, j = j: (button_clicked(piles, button, i, j)))
                    buttons[i][j].grid(row = j, column = i)
                else:
                    buttons[i].append(tk.Button(card_frame, text = "{:^12}".format("*"), width = 12))
                    buttons[i][j].config(command = lambda button = buttons[i][j], i = i, j = j: (button_clicked(piles, button, i, j)))
                    buttons[i][j].grid(row = j, column = i)
            else:
                buttons[i].append(tk.Button(card_frame, text = piles.get_piles()[i].get_cards()[j], width = 12))
                buttons[i][j].config(command = lambda button = buttons[i][j], i = i, j = j: (button_clicked(piles, button, i, j)))
                buttons[i][j].grid(row = j, column = i)
                

rule_button = tk.Button(game, text = "Rule", width = 10, command = open_rule)
rule_button.grid(row = 0, column = 0)

empty = tk.Label(game, text = " ")
empty.grid(row = 1)

###initial call when game startss
create_frame(piles)

undo_button = tk.Button(game, text = "Undo", width = 10, command = lambda: undo_clicked(piles))
undo_button.grid(row = 0, column = 2)

restart_button = tk.Button(game, text = "Restart", width = 10, command = restart_game)
restart_button.grid(row = 3, column = 2)

shuffle_button = tk.Button(game, text = "Re-shuffle", width = 10, command =shuffle)
shuffle_button.grid(row = 4, column = 2)


game.mainloop()
