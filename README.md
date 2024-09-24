# ESCAPE THE MATRIX
#### Video Demo:  https://youtu.be/7CKZvPZm4wg
## Description:
The entirety of the project is written within a single .py file named 'escape_the_matrix.py'. There was the option to move my custom functions to a secondary helper file, but I chose to keep everything in a single file for the sake of simplicity and also avoid possible complications with circular imports between the two files.
### Imports
Firstly, I imported **sleep** from **time**. This allows for short pauses after printing each letter of my text, in order to simulate text being typed on a screen. It is also used at the end of the script in order to simulate a game loading its assets. More will be explained later, in each of the functions this was used in.

Secondly, I imported **randint** from **random** in order to pick a random number and assign it to the **rng** variable to address the user playing the game with strings like ```f"Hello, User #{rng}."```. Just a fun interraction, not something functionally significant.

Finally, I imported **os**. This will be used in the **replay_exit** function, if the player chooses to replay the game, in order to use the 'clear' command to start over with a blank terminal.
### While True Loop
I nested the entire script in a **while True loop** so that it can always repeat with the **replay** function at the end, should the player choose to replay the game. On the other hand, should the player choose to exit, the whole script shuts down. The first thing that happens in the loop is to initialize the variables used in the script. This way, I can always ensure they won't end up storing a value that can cause a problem later on.
### Custom Functions
#### printani
The first function I defined in the script is a function that simply adds a visual element, an animation, to the text being shown to the player. Specifically, the line ```print("     ", end="")``` is used to indent the text by five spaces so that it isn't printed right on the edge of the screen, for a more visually pleasing result. A fortunate side effect of this indentation is that when the player needs to make a choice the prompt will stand out from the rest of the text by replacing the gaps of the indentation. Next, there is a **for** loop to iterate through every single letter of a given string and add a pause after printing each one. How fast each letter is printed and how fast each line of text is printed depends on the values of the variables **text_speed** and **text_wait** respectively. Thus, the typing animation is achieved. The value given to the function is the string to be printed.
#### cont_read
This function is simply an arrow (---->) prompt for the user to press **Enter** to keep reading (show the next bit of text). It only moves forward with the text if the user presses **Enter**. This moves the game from one bit of text to the next, when there is **NO** choice to be made by the player. The value given to the function is the **ID** of the next bit of text.
#### choices
This function is used to move the game from one bit of text to the next when there **IS** a choice to be made by the player. Firstly, the options are presented to the player with ```print(f"     A) {choice_a} or B) {choice_b}")```, in which **choice_a** and **choice_b** are strings of text for the player to know what they are choosing to do. These are given to the function as values each time it's called. Next, the function forces a user input of **A, a, B** or **b** with the prompt ```choice = input("PICK:")```. Depending on what the player chose, the function returns one of the possible values **step_a** or **step_b** which are the **IDs** of two different bits of text that come next.
#### alt_end & true_end
These are two variations of the same concept. They appear when a text bit that is marked as an **ending** is reached by the player. The difference is, if the player has made all the choices that correspond to the actual script of the original 1999 film along the way (which is tracked with the **true_meter** variable), the **true_end** function will display a slightly different text compared to the **alt_end** function, notifying the player that they found the **"True Ending"**.
#### replay_exit
This function appears at the very end of the game, prompting the player for a choice. Should they choose to replay the game, the terminal is cleared with ```os.system('cls' if os.name == 'nt' else 'clear')``` and the game starts over (by breaking the **while True loop**) with a blank terminal, as if playing for the first time. Should the player choose to exit, the script just stops running with ```exit()```. The ```sleep(3)``` line is just used to visually pause the game for the **restarting** or the **exiting** bit to be less abrupt.
### Introduction
Before the actual game begins, I chose to print out the title of the game, ask the player for a name of their own choosing and give them instructions on how to play.

For printing the title of the game in **ASCII art**, I used **raw strings** to avoid complications with escape sequences using slashes and underscores.

Then I ask the user for a **name**, which is only allowed to consist of letters. This name will be used in the text multiple times later on. Should the user fail to comply with the rule for typing in a name a certain number of times (which is tracked with the **fouls** variable), I chose to add a fun interraction, where the game exits automatically, after scolding the player for not typing in a proper name. Of course, the script can be re-run after exiting, without any leftover changes.

Next, after being welcomed by the game, the player gets to choose how fast the text prints on the terminal. This is achieved by inputing a choice, A or B, each of which correspond to two different sets of values for **text_speed** and **text_wait** which will be used by **printani** under the hood.

Finally, after a last bit of instructions, the **tutorial/introduction** to the game is complete. The main game is now about to begin.
### Main Game Code
The game is nested within a ```while end == 0:``` loop. This ensures that the game will keep runnig until a bit of text that is explicitly marked as an **ending** is reached by the player.

Within this **while loop** is a large **match-case statement** in which every case is a separate bit of text (a **chapter** or a **paragraph** of the story, so to speak). The variable **step** is used here to keep track of each **case's ID**, so that the game can bounce around the different cases. What the player sees is a seamless flow of text.

At first, I created an array of strings, each of which would be assigned a new value (one or two sentences) at the beginning of each **case**. Once every string from the array was printed, the values would be reset to blank, preparing the array for the next case. However, that would take up a lot of memory for no apparent reason. Therefore, that idea got scrapped and instead all the text of each case is directly printed to the terminal, using the **printani** function.

At the end of each case, a value is assigned to **step**. If there is **NO** choice to be made by the player, **cont_read** assigns the value of the next bit of text automatically (which bit of text follows which bit of text is predetermined by me, not the player, and is written in the code without the possibility of changes). In the case where there **IS** a choice to be made by the player, the value is assigned to **step** by the **choices** function. In other words, the player picks one of two possible next bits of text.

Some of the cases actually assign their value to the **end** variable, not the **step** one. When that happends, the ```while end == 0:``` loop is broken and the game moves on to a different **match-case statement**, which includes a separate case for each possible ending. This statement is structured in the same way as the previous one. Upon reaching one of the endings, the player gets a message telling them which ending they found and encouraging them to play again and find more endings.

Finally, this is where the **replay_exit** function is used, prompting the player to choose either of these options.
