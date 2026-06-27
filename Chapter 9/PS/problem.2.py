# The game() function in a program lets a user play a game and returns the score as an integer.
#You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


def game():
    return 95
# get yhe current score 
score = game()

#  read the previous high score
with open("hiscore.txt") as f:
    data = f.read()

# what if the file is empty
if data == "":
    high_score = 0
else:
    high_score =  int(data)

# compare ; the larger score should stay

if score > high_score:

# save the new high score 
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

    print("New High Score: ", score)
else:
    print("High score remains: ", high_score)



'''Start
   │
   ▼
Get current score
   │
   ▼
Read file
   │
   ▼
Is file empty?
   │
 ┌─┴───┐
 │Yes  │No
 ▼     ▼
0   Convert to int
      │
      ▼
Compare scores
      │
 ┌────┴────┐
 │ score > │
 │ high?   │
 └────┬────┘
      │
 Yes  │  No
 ▼    │
Write │
file  │
      │
      ▼
    Finish'''

#---------------------------------------------------------------------
'''
Whenever you see a problem, ask these questions in order:

What is the input?
Here: game() and Hi-score.txt
What is the output?
Updated high score
What operations are needed?
Read
Compare
Write
Any special cases?
Empty file
Which Python concepts do I know that solve these operations?
open()
if
int()
write()

Now the solution almost writes itself
'''
