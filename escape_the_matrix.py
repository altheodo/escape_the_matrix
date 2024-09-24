# Import for printing animation & 'Outro'
from time import sleep
# Import for 'Intro' & ' Outro'
from random import randint
# Import for replaying game
import os

# This loop will only be broken when player chooses to replay the game
while True:
    # Initialize variables
    username = ""
    end = 0
    step_a = 0
    step_b = 0
    step = 0
    choice_a = ""
    choice_b = ""
    choice = ""
    true_meter = 0
    text_speed = 0.01
    text_wait = 0.02

    # Define printing animation
    def printani(text):
        print("     ", end="")
        for letter in text:
            print(letter, end="", flush=True)
            sleep(text_speed) # <----------------------------------------------------------------[allow user to choose speed]
        sleep(text_wait)
        print("")

    # Define continue reading prompt
    def cont_read(next_se):
        entered = "entered"
        while entered != "":
            entered = input("---->")
            if entered == "":
                return next_se

    # Define choices function
    def choices(choice_a, step_a, choice_b, step_b):
        print(f"     A) {choice_a} or B) {choice_b}")
        choice = ""
        while choice not in ["A", "a", "B", "b"]:
            choice = input("PICK:")
            if choice in ["A", "a"]:
                return step_a
            elif choice in ["B", "b"]:
                return step_b

    # Define alternate ending text
    def alt_end(end_case):
        for times in range(3):
            print("")
        printani("CONGRATULATIONS!")
        printani(f"You reached ending #{end_case}, User #{rng}.")
        printani("Feel free to replay and find different endings.")
        print("")

    # Define true ending text
    def true_end():
        for times in range(3):
            print("")
        printani("CONGRATULATIONS!")
        printani(f"You reached the True End of the story, User #{rng}.")
        printani("Feel free to replay and find alternate endings.")
        print("")
        if true_meter == 10:
            printani("You followed the True Path by making all the right choices!")
            printani("The True Path was adapted from ACT I of the movie 'The Matrix' (1999).")
            printani("The rest is original text written for this game.")
            print("")

    # Define replay or exit game prompt
    def replay_exit():
        printani("Thank you for playing!")
        printani("A) Replay or B) Exit")
        end_prompt = ""
        while end_prompt not in ["A", "a", "B", "b"]:
            end_prompt = input("PICK:")
            # Player chooses to replay the game
            if end_prompt in ["A", "a"]:
                print("")
                printani("Restarting game.....")
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                return False
            # Player chooses to exit the game
            elif end_prompt in ["B", "b"]:
                print("")
                printani("Exiting game.....")
                sleep(3)
                exit()

    # Print title of the game
    printani(r"  ___                         _   _          __  __      _       _      ")
    printani(r" | __|___ __ __ _ _ __  ___  | |_| |_  ___  |  \/  |__ _| |_ _ _(_)_ __ ")
    printani(r" | _|(_-</ _/ _` | '_ \/ -_) |  _| ' \/ -_) | |\/| / _` |  _| '_| \ \ / ")
    printani(r" |___/__/\__\__,_| .__/\___|  \__|_||_\___| |_|  |_\__,_|\__|_| |_/_\_\ ")
    printani(r"                 |_|                                                    ")         
    for times in range(2):
        print("")

    # Ask user for username ('Intro')
    rng = randint(1, 999)
    fouls = 0
    printani(f"Hello, User #{rng}.")
    printani("Please enter your name:")
    while not username.isalpha():
        username = input("NAME:")
        if not username.isalpha() and fouls <= 1:
            printani(f"Please enter a name including only alphabetical characters, User #{rng}.")
            fouls += 1
        elif not username.isalpha() and fouls > 1:
            # Fun interaction to exit the game if user doesn't provide proper name
            if fouls == 5:
                print("")
                printani(f"You failed to comply too many times, User #{rng}.")
                printani(f"Your right to play this game has been revoked.")
                print("")
                printani(f"Exiting game...")
                sleep(5)
                exit()
            printani(f"Please comply, User #{rng}.")
            fouls += 1

    # Welcome quote
    printani(f"Welcome, {username}.")
    printani("Your adventure is about to begin. Your choices matter. Remember that!")
    for times in range(2):
        print("")

    # Instructions for playing the game
    printani("Enter Aa or Bb to make choices.")
        # Allow user to choose speed of text
    printani("How fast would you like the text to appear?")
    print("     A) Fast or B) Slowly")
    choice = ""
    while choice not in ["A", "a", "B", "b"]:
        choice = input("PICK:")
        if choice in ["A", "a"]:
            text_speed = 0.001
            text_wait = 0.01
        elif choice in ["B", "b"]:
            text_speed = 0.015
            text_wait = 0.3
    print("")
    printani("Press Enter when prompted with “---->” to keep reading.")
    step = cont_read(1)


    # Main game code running until an end is met
    while end == 0:
        match step:
            # Code for 'Chapter 1' (step 1)
            case 1:
                for times in range(2):
                    print("")
                # Print all text for this step
                printani("*beep* *beep* *beep*")
                printani("“Hmm? What’s that?”")
                printani("You are slowly waking up. The beeping sound is coming from your computer. You fell asleep on your desk. You look at your computer screen.")
                printani("It is empty. Some text suddenly writes itself. It reads:")
                printani(f"“Wake up, {username}.”")
                printani("“The Matrix has you…”.")
                printani("“Follow the white rabbit.”")
                printani(f"“Knock, knock, {username}.”")
                printani("Before you have any chance to realize what is going on, there is a knock on the door.")
                printani("“Wait, how did it know?”")
                printani("No time to think.")

                # Present choices and read user's choice. Then move to next step
                step = choices("Open the door", 2, "Ignore it", 3)

            case 2:
                printani("You decided to open the door.")
                printani("There is a group of colorful individuals standing there. You remember you had an appointment. They are 2 hours late.")
                printani("The one standing at the front hands you a stack of cash. It is $2,000.")
                printani("“Just a moment guys.” You are back at the door with a floppy disk. It is a hack you wrote yourself.")
                printani("“Don’t get caught using this. You were never here. You don’t know me.”")
                printani("“I know, I know. Relax.” As you are about to close the door, the man at the front stops the door with his hand.")
                printani("“Hey, you wanna join us tonight? You’ve been locked in here for ages. You really need to unplug. What do you think, Alice?”")
                printani("She is the one standing next to him. She smiles. “Sure.”")
                printani("You notice an interesting tattoo on her shoulder, as she is speaking. It’s a white rabbit. “Huh…”")

                # If player makes all "cacon" choices, there will be a comment at the end
                true_meter += 1
                step = choices("Stay home", 4, "Join them", 5)

            case 3:
                printani("“I’m almost out of time, gotta get back to work. Whoever it is, they’ll go away.”")
                printani("Your screen is somehow back where you had left it, before dozing off.")
                printani("After one or two more knocks, whoever was at the door seems to have left.")
                printani("Whatever that was, it could not have been all too important.")
                printani("You need to complete your assignment for work. The deadline is tomorrow.")
                printani("After a couple of hours of hard work, you feel satisfied and decide to go to bed.")
                printani("It is a weekday, after all. You have to go to work tomorrow.")

                # Prompt to continue reading when there is no choice between chapters (steps) or a chapter is too long and needs breaking up
                step = cont_read(6)

            case 4:
                printani("“Thanks for the invitation guys, but I’m cool. I’m really tired tonight, I need to get some sleep. Deadlines to meet, too. You have fun though. See ya.”")
                printani(f"“Whatever you say, {username}. You’re the one missing out. Let’s go guys.” You close the door.")
                printani("You decided to stay at home tonight. You are too tired for parties these days.")
                printani("After all, you need to complete your assignment for work. The deadline is tomorrow.")
                printani("You cannot be slacking off when working for such a respectable software company.")
                printani("After a couple of hours of sanding off some rough edges and applying some final touches to your project, you decide to go to bed.")
                printani("You are satisfied with the results, but cannot help wondering: “What if I’d gone along? Huh… I guess next time.”")

                step = cont_read(6)

            case 5:
                printani("You decided to join them.")
                printani("About a half hour of commuting later, you arrive at a nightclub. It is almost too dark and smells of sweat and cigarette smoke.")
                printani("Everyone is wearing black leather and the music playing is some sort of oppressive, dark techno.")
                printani("The others are greeting some people they seem to know. You lose them in the crowd.")
                printani("You do not regret coming here, but you are tired. It was a long day. You decide to grab a drink and stand in a corner that looks a little less crowded.")

                true_meter += 1
                step = cont_read(5.1)

            case 5.1:
                printani(f"After a while, a mysterious, alluring woman is approaching you, amongst the dancing crowd. “Hey, {username}.”")
                printani("“How do you know that name?” She proceeds to explain how she knows more things about you than just your name. Somehow she knows where you work, where you live, who you are…")
                printani("“Who are you?” you ask, a bit stressed out. “I'm Trinity.”")
                printani("“No way! THE Trinity?” “The very same.” It sort of makes sense now. You have definitely heard of her.")
                printani("She is a world-famous hacker. Notorious for cracking the IRS database back in the mid 90’s.")
                printani("She is probably working on something even bigger for the turn of the millennium. She does not look the part though. Maybe it is just you.")

                step = cont_read(5.2)

            case 5.2:
                printani("She leans closer to whisper in your ear. “It was me on your computer; I believe you have realized that by now.")
                printani(f"I brought you here to warn you. You’re in danger, {username}. They’re watching you.")
                printani("I know why you’re here, I know what you’ve been doing, why you hardly sleep at night, wasting away in front of your computer, why you live alone.")
                printani(f"You’re looking for Him, like I once was. Morpheus. The same question that brought me to Him, brought you here tonight, {username}.")
                printani("You know what question I’m talking about, don’t you?”")
                printani("“What is the Matrix?” “The answer you’re looking for will find you, if you allow it to…”")
                printani("It suddenly occurs to you, that you have no idea what her intentions are.")

                step = choices("Don't trust her", 8, "Trust her", 7)

            case 6:
                printani("You wake up the next morning having lost your sense of time. You were tired. You overslept.")
                printani("You are more than an hour late for work. You probably didn’t hear the alarm go off.")
                printani("All in a rush, you get up from bed. Same old routine. Get dressed, have breakfast, drive to work. Frankly, you are somewhat getting sick of it.")
                printani("Finally, you arrive at work, after a long, exhausting drive, because of all the traffic.")

                step = cont_read(9)

            case 7:
                printani("You decide to stay silent. She backs off, looking you deep in the eyes, for a moment, before walking away.")
                printani("What she said sounded rather important as well as intriguing.")
                printani("You are too tired to think about it at the moment, or even stay here any longer. You decide to go home and sleep it off.")
                printani("You have a good feeling about this…")

                true_meter += 1
                step = cont_read(6)

            case 8:
                printani("It is actually becoming clear to you that she is using her good looks to manipulate you. You feel uneasy and push her off.")
                printani("“Please stay away from me. I don’t even know you, or what you’re talking about. Goodbye.”")
                printani("You storm out of the nightclub. You prefer not to think about it right now.")
                printani("It is rather late and you have to get up early for work tomorrow. You head home to get as much sleep as you can until the alarm goes off.")

                step = cont_read(6)

            case 9:
                printani("Not even an hour goes by, before your boss calls you in his office. “This can’t be good.”")
                printani("On your way there, you reflect on these last few weeks.")
                printani("“What could this be about? Ah, whatever, I don’t care anymore. I hope he fires me. Maybe I’ll even quit.”")
                printani("The moment you step into his office, he starts going off about how you are almost always late to work lately, how you apparently have a problem with authority and so on and so forth…")
                printani("You are clearly not interested in any of it. You’re getting distracted by the window cleaner just outside the office.")
                printani("You start wondering: “Why does this feel familiar?")
                printani("Kinda like he’s always here cleaning the same windows, using the same motions. Must be just me…”")
                printani("You snap back to reality. You cannot take your boss’ scolding anymore.")
                printani("You realize your boss has been abusing you for years. You were just desensitized to it.")
                printani("What will you do?")

                step = choices("Nod along in compliance", 11, "Stand up for yourself", 10)

            case 10:
                printani("“That’s it, I’ve had enough of this abuse. I f**king quit!” You storm out of his office, slamming the door behind you, without looking back.")
                printani("You grab your things from your cubicle and leave the building. You rush to the park on the other side of the street.")
                printani("There’s an empty bench, on which you take a seat to think things over, take it all in.")
                printani("You feel good about having quit that pointless, dead-end job. In fact, you do not even want to think about ever again.")
                printani("You lean your head back, close your eyes and take a deep breath. It is actually beautiful outside at this time of the year.")
                printani("You remember you love the spring. You feel someone standing next to you. You did not see them walk up to the bench.")
                printani("“Excuse me. Do you mind sharing that bench?”")
                printani("A kind, smiling woman, holding a couple of books is standing right in front of you.")
                printani("“No, no, of course.”")

                end = cont_read(1)

            case 11:
                printani("You are too scared to stand up for yourself or talk back at him. After all, he is not all that wrong.")
                printani("“Yes, sir, I’ll try harder from now on. I’m getting back to work immediately.”")
                printani("His abuse is not really getting to you. You find it easy to ignore him completely. You return to your desk.")
                printani("After a few minutes of staring at the fake wall of your cubicle, you hear your name across the room. It’s a courier.")
                printani("She walks up to you, carrying a small package. “What’s this? I wasn’t expecting anything.”")
                printani("You open it up. There is just a mobile phone inside. Not a moment later, it rings, startling you.")
                printani("What will you do?")

                true_meter += 1
                step = choices("Pick up the phone", 12, "Don't pick it up", 13)

            case 12:
                printani("There is a strange man on the phone. You do not know him, but he knows you. You cannot shake the feeling that he is someone important.")
                printani("He claims his name is Morpheus and that he has been looking for you.")
                printani("You start feeling uneasy, so you take a peek over the fake wall of your cubicle, to see if anyone is overhearing.")
                printani("There are three suspicious-looking, suited men at the other end of the hall. They are wearing black sunglasses and earpieces.")
                printani(f"“They are there for you, {username}. We’re out of time. If you don’t want to find out what they want from you, I suggest you listen to me and get out of there.”")
                printani("“How?” “I can guide you, but you must do exactly what I say.”")
                printani("You decide to trust him, for now…")

                true_meter += 1
                step = cont_read(12.1)

            case 12.1:
                printani("After a bit of heart-pounding sneaking around the suited men, you end up at an empty office at the end of the hall.")
                printani("Outside, there is a scaffold. There is no time, you have to climb the scaffold to get to the roof.")
                printani("“There are two ways out of there: the one is through the scaffold, the other is in their custody. You take a chance either way.")
                printani(f"I leave it up to you, {username}.”")

                step = choices("Trust Morpheus, take the scaffold", 14, "Don’t do it, it’s too risky", 15)

            case 13:
                printani("You feel like someone is watching you. This phone call could be anything from a harmless prank to something dangerous.")
                printani("Something definitely feels off about this and you want nothing to do with it. You decide to throw the phone away and get to work.")
                printani("You cannot give your boss any more reasons to be mad at you.")
                printani("After a good, productive day at work, you head home. You do some chores, have dinner and go to bed early.")
                printani("One would say that you are a model citizen.")

                step = cont_read(25)

            case 14:
                printani("“Why is this happening to me? I’m nobody. I didn’t do anything.”")
                printani("Your mind is flooded with such thoughts and theories. Nothing is making sense right now. But you believe it will soon enough.")
                printani("You decide to climb the scaffold as you were told.")
                printani("You take a deep breath and put your left foot out the window and onto the wooden plank.")
                printani("“It’s okay, I can do this.”")
                printani("You had not even completed this thought when, upon putting your other foot on the scaffold, you slip right off.")
                printani("You were not fast enough to grab onto anything, so you fell off the building, right onto the pavement.")

                end = cont_read(2)

            case 15:
                printani("You decide the risk is too high. It is not worth it.")
                printani("Inevitably, the suited men make their way into this room. Without resisting, you let them take you in their custody and drive you away.")
                printani("You have no idea what you have done wrong, why they were after you. Everything is probably going to make sense soon enough.")
                printani("Upon entering their car, your hands cuffed behind your back, someone throws a black hood over your head. You cannot see or hear anything.")
                printani("You do not know where they are taking you.")

                true_meter += 1
                step = cont_read(15.1)

            case 15.1:
                printani("After a while, you find yourself sitting at a small, empty desk in a brightly lit, white, sterile room. The hood was just removed from your head by one of the suited men.")
                printani("It looks like an interrogation room, along the lines of those you have seen in those crime films.")
                printani("You feel confused. You cannot tell how much time has passed since you were apprehended. Is it even the same day?")
                printani("You have no recollection of how you got here. Where even is “here”?")
                printani("Before you are able to get a grasp of the situation, the other two suited men from before enter the room.")

                step = cont_read(15.2)

            case 15.2:
                printani("One of them seems to be some sort of their superior. He seems cold and lifeless, almost as if he was a robot.")
                printani("He sits at the table, across from you, whipping out a large folder that seems to contain information about you. He glances through its contents.")
                printani("“As you can see, we’ve had our eye on you for some time now.”")
                printani("You cannot help but wonder: “Could it be them that were watching me?”")
                printani("“It seems you have been living… two lives. In one you appear to be a normal, law-abiding citizen.")
                printani(f"In the other an online criminal, known by the hacker name {username}, guilty of virtually every computer crime we have a law for.")
                printani("Only one of these lives has a future. I think we understand each other, so I am going to make you an offer.")
                printani("Help us get Morpheus, the man who contacted you today and your slate will be wiped clean.")
                printani("Before you make your decision, you must know, this man is considered by many the most dangerous man alive, a known terrorist.”")
                printani("You are not intimidated, or at least you try to make it look that way. You manage to keep your cool.")

                step = choices("Cooperate", 17, "Flip them off", 16)

            case 16:
                printani("“Wow that really sounds like a great deal. But I got a better one for you. How about I give you the finger…”")
                printani("You flip him off.")
                printani("“…and you give me my phone call? I know my rights, you can’t scare me.”")
                printani("He seems disappointed. “Tell me, what good would a phone call be if you’re unable to speak?”")
                printani("“What?” Your thought does not seem to materialize into words. You cannot even open your mouth. You do not have one!")
                printani("You jump out of your chair, shocked to your very core. “This can’t be happening.” you think.")
                printani("The other two men restrain you with relative ease. They force you on your back, right on the table.")
                printani("You have no mouth, and you must scream.")
                printani("“You are going to help us, whether you want to or not.” he says as he pulls out of his chest pocket, what looks like a robotic bug.")
                printani("He places it onto your bellybutton and before you know it, it starts burrowing into your belly, causing you excruciating pain.")

                true_meter += 1
                step = cont_read(18)

            case 17:
                printani("You weigh things in your mind for a moment.")
                printani("The idea of going to prison, possibly for life, does not seem very appealing to you at the moment.")
                printani("You decide to cooperate. The suited men bug you.")
                printani("“You will be meeting one of Morpheus’ people tonight. She is going to be at the Adams Street Bridge.”")
                printani("You go back home to kill some time until the rendezvous.")
                printani("You are very tired from all these crazy things that happened today. You lie on your bed for a moment, but before you know it, you are fast asleep.")
                printani("All the stress, the built up anxiety manifest in a terrible nightmare.")
                printani("You are in that interrogation room from earlier. You are lying on a table. A hostile-looking robotic bug jumps on your abdomen out of nowhere.")
                printani("It starts attacking you and then violently enters your body through your bellybutton, splattering blood all over.")

                step = cont_read(18)

            case 18:
                printani("“Aaaahh!” You wake up in your bed, drenched in sweat. “Was that a dream?”")
                printani("Your phone rings. You picked it up, all confused and stressed out.")
                printani("“This line is tapped, so I must be brief. They have no idea how important you are, or they wouldn’t have let you go.")
                printani(f"I’ve been looking for you my entire life, {username}. You are more important than you realize.")
                printani("This is not the time to discuss this any further. Do you still want to meet?”")

                step = choices("Accept the invitation", 19,"Decline", 20)

            case 19:
                printani("“Okay. I’ll be there.”")
                printani("“Good. You'll be meeting Trinity. You can trust her.”")
                printani("After a few minutes you arrive at the rendezvous point. It is a rainy night, so you take shelter under the bridge, hoping they will not miss you.")
                printani("So you wait… After a while, an old, but fancy black car approaches and stops right beside you.")
                printani("The door opens and there sits Trinity inviting you in. At this point, it only makes sense to at least listen to them, so you enter the car.")
                printani("A strange woman on the passenger’s seat turns around, pointing a gun at you.")
                printani("You have to do what they tell you to do.")

                true_meter += 1
                step = choices("Get out of the car", 22, "Do whatever they say", 21)

            case 20:
                printani("“I don’t know who you people are. I want nothing to do with you or your little cult. Please, leave me alone.”")
                printani("You hang up. Hopefully, they got the message. Hopefully, they will leave you alone now.")
                printani("You decide to go back to sleep. You got work tomorrow after all.")

                step = cont_read(25)

            case 21:
                printani("You take your shirt off, like you were instructed to.")
                printani(f"Trinity whips out a weird-looking device with a big tube and places it on your bellybutton. “We know they bugged you, {username}.”")
                printani("“You mean that wasn’t a dream? How do you know about it?”")
                printani("“That’s not important right now. This is gonna hurt.”")
                printani("The device stats sucking air violently out of your bellybutton, feeling like a very intense vacuum.")
                printani("Suddenly, a small, bug-like robot pops right out of your body and into the tube, causing you brief, but intense pain. It’s over.")
                printani("You feel relief, but confused about the nature of that dream you had, being interrogated by the suited men.")
                printani("Maybe it really was not a dream after all.")

                true_meter += 1
                step = cont_read(21.1)

            case 21.1:
                printani("After a not so long car ride, you arrive at an old, grimy, dimly lit, shady-looking building.")
                printani("“No human beings could really be living here. It’s terrible.” you think to yourself.")
                printani("After walking up a long flight of swirling stairs, being led by Trinity, she stops dead in her tracks.")
                printani("There is a closed door in front of you. She stares at it for a moment.")
                printani("“This is it. Let me give you a bit of advice. Be honest. He knows more than you could ever imagine.”")
                printani("You feel a sense of anxiety rising up your chest, but before you could process it, she opens the door, leading you in.")

                step = cont_read(21.2)

            case 21.2:
                printani("A strange man is standing by the window with his back turned to you, watching the rain pouring down outside.")
                printani("You can feel it. It is Him. Morpheus.")
                printani("He turns around. He has been eagerly expecting you.")
                printani(f"“Welcome, {username}. As you’ve probably guessed, I am Morpheus.”")
                printani("You reply as normally as you can: “It’s an honor to meet you.”")
                printani("“The honor is mine. Please, take a seat.” You sit opposite of each other.")
                printani("He looks friendly. You feel great anticipation to listen to what he has to say.")
                printani("This is when you are finally going to get the answers you have been looking for all this time.")

                step = cont_read(21.3)

            case 21.3:
                printani("“You have the look of a person who accepts what they see, because they are expecting to wake up at any time.")
                printani("Kinda like Alice tumbling down the rabbit hole, don’t you think?")
                printani("Ironically, this is not far from the truth. You are here because you know something is not right with the world.")
                printani("You have felt it your whole life, but you don’t know what it is. Do you know what I’m talking about?”")
                printani("He is expecting an answer from you. You both know what you are going to say: “The Matrix?”")
                printani("“Do you want to know what it is?” You cannot form words at this point. You nod.")

                step = cont_read(21.4)

            case 21.4:
                printani("“The Matrix is everywhere around us. It’s in every little thing around us, in every single one of your actions, every day, all the time.")
                printani("You can feel it. It is like a curtain falling over your eyes, obstructing you from seeing the truth.")
                printani("The truth is you’re a slave. Like everyone else, you were born into a prison for your mind.")
                printani("Unfortunately, no one can be told what the Matrix is in so many words. You have to see it for yourself.")
                printani("This is your last chance. After this, there is no turning back.")
                printani("I know you don’t believe in fate, because you like to think you make your own choices in your life. Am I correct in assuming this?”")
                printani("You nod. He continues: “Well, this is it.”")

                step = cont_read(21.5)

            case 21.5:
                printani("He presents you with two pills, each sitting comfortably in each of his open palms.")
                printani("“You take the blue pill, this madness ends. You wake up in your bed, free to believe whatever you want to believe.")
                printani("You take the red pill, you stay in Wonderland and I show you how deep the rabbit hole goes.")
                printani("Remember. All I’m offering is the truth. Nothing more.”")
                printani("This is the moment your life has been leading to. This is where you make the choice that matters.")
                printani("A choice that will alter your life and maybe even other people’s lives. It is entirely up to you.")
                printani("Which pill is it going to be?")

                step = choices("BLUE", 23, "RED", 24)

            case 22:
                printani("“You people are insane. Pointing a gun at me. I’ve changed my mind. Please, don’t ever come near me again.”")
                printani("You get out the car as fast as you can, slamming the door behind you.")
                printani("You decide to waste no time hanging around or even thinking about it. You just start walking home.")

                end = cont_read(3)

            case 23:
                printani("You decide to take the blue pill.")
                printani("All this madness seems too much to handle. You are actually not that dissatisfied with you boring life, now that you think about it.")
                printani("Thus, the blue pill sounded like the right choice.")
                printani("Morpheus seems crushed, but he remains silent for a moment. He offers you a glass of water to help the pill go down easily.")
                printani("“Maybe I’ve been wrong about you. Maybe it was never you. Only way to find out is to keep looking for the One.")
                printani("Regardless, thank you for humoring me. I wish you the best. You are free to go.”")
                printani("You get up, smile at him, say your goodbyes and leave the room. It is over. It all seems so surreal in retrospect.")
                printani("“Huh… I guess this is going to make one crazy story.”")
                printani("You chuckle to yourself. It is time to go home.")

                step = cont_read(25)

            case 24:
                printani("You decide to take the red pill.")
                printani("Your life has always felt pointless. There must be something more to it.")
                printani("Thus, the red pill sounded like the right choice.")
                printani("Morpheus seems pleased and excited. He offers you a glass of water to help the pill go down easily.")
                printani("He gets up in a rush. “Follow me.”")

                true_meter += 1
                step = cont_read(24.1)

            case 24.1:
                printani("After he shows you what the Matrix is, you agree to exit this fake, made-up world and join them in the real world.")
                printani("The real world is in a dire state.")
                printani("Humans are slave-batteries feeding energy to the Machines, who have taken over.")
                printani("The Matrix is an illusion, imprisoning the minds of humans, keeping them submissive to the Machines. A simulation.")
                printani("A few humans have managed to escape this prison and create a community for themselves.")
                printani("They have created a legend about the Chosen One who will lead a revolution against the Machines and free humankind forever.")
                printani("Morpheus believes you are the One.")
                printani("You will join the Revolution, lead humans to their rise against the Machines and eventual freedom, like the prophecy foretold.")

                end = cont_read(5)

            case 25:
                printani("*yawn* You wake up a little earlier than your alarm today. You feel some kind of strange satisfaction.")
                printani("Whoever those people were, you want to forget about them. You made the right choice to not get involved.")
                printani("You go to work like any other morning, but today seems different. You feel motivated to do better.")
                printani("This goes on for a few days and your boss takes notice. He rewards you for that.")
                printani("You decide to leave your hacker days behind, wasting away behind that computer screen. Instead, you feel like hanging out with people more.")
                printani("That is how you meet Sarah.")

                step = cont_read(25.1)

            case 25.1:
                printani("You end up falling for each other.")
                printani("It is her quirky sense of humor that got to you and that is what you tell people when they ask how you met each other.")
                printani("She motivates you to do better. You do better at work, so you get promoted.")
                printani("You can now afford a real family. Real according to society that is. So Sarah and you decide to adopt a child.")
                printani("You are finally truly happy with your life. All those thoughts of hopelessness and despair are gone.")
                printani("You no longer feel like everything is pointless or that you are wasting your life doing nothing important.")
                printani("Your family is important. In fact, it is the greatest thing that happened to you. You cherish every single moment with them.")

                step = cont_read(25.2)

            case 25.2:
                printani("But the Matrix had different plans for you.")
                printani("On your 57th birthday, while having one of those long baths you love after work, to unwind and relax, you suddenly feel excruciating pain in your chest.")
                printani("You can tell this is the end. Your heart just stops.")
                printani("Your son will find you a couple hours later. You were expecting him to visit you at home, now that he is back from university for the holidays.")

                end = cont_read(4)


    # Differentiate between 'canonical ending' and 'other endings' ('Outro')
    match end:
        case 1:
            printani("You had no idea at that point that you had just met the love of your life.")
            printani("You ended up talking for hours that day at the park, you started dating, got married and had three beautiful children.")
            printani("She was always there for you and you were always there for her. You loved your family more than anything.")
            printani("You started an animal rescue for stray dogs and in your free time, you sometimes repaired motorcycles for fun.")
            printani("There was nothing missing. You lived a happy life.")
            printani("However, you never stopped wondering. The same question in the back of your mind remained:")
            printani("“Was this really my true calling in life? I guess it doesn’t matter anymore. I’m happy. That’s what’s important.”")

            # Notification for finding an ending
            alt_end(1)
            
            # Prompt to reaply the game or exit
            replay_exit()

        case 2:
            printani("Your death was instant.")
            printani("Maybe you should not have been trusting everyone and anyone so blindly.")
            printani("Sometimes one has to make their own choices.")

            alt_end(2)
            replay_exit()

        case 3:
            printani("This was your last chance to make a choice that matters. They will never contact you or approach you again.")
            printani("In fact, you will more or less never be able to make any choices that matter again, because you will never be free.")
            printani("On your way home, the suited men intercept you. They forcibly take you into their custody and shove you into their car, without saying a word.")
            printani("You are headed to prison. There is not going to be a trial for some time, but when it happens, you will be sentenced for three lifetimes for your online crimes.")
            printani("That is enough time to think about your mistakes and regrets in life.")
            printani("Should you have been braver? Should you have led a bolder life? Should you have taken that leap of faith?")
            printani("You can never know any of that. You left your last breath in a cold, empty cell.")
            printani("You failed to make a difference.")
            printani("Nobody will miss you.")

            alt_end(3)
            replay_exit()

        case 4:
            printani("How could you have known the Matrix was actually real?")
            printani("Everything sounded so crazy back then. You had not thought about it in years.")
            printani("Maybe you could have changed your fate. Too late now.")
            printani("You will never know. And neither will anybody else.")
            printani("What could have been?")

            alt_end(4)
            replay_exit()

        case 5:
            printani("Your life was not easy. You experienced many losses.")
            printani("After all, it was war. But you made a difference. You created a better world for humankind.")
            printani("The natural environment of Earth was destroyed, but there is still hope. We can rebuild. This time using our own hands.")
            printani("Leaving everything up to A.I., with the explicit intent to maximize profit, was the biggest mistake humans ever made.")
            printani("We robbed ourselves of our humanity. We had the Machines experience more of a human life than us.")
            printani("The new world will be a different one. A more human one. The new technology will never be more than tools. Not to make our lives easier, but better.")
            printani("Your legend will forever inspire future generations.")

            # Notification for finding the true ending
            true_end()
            replay_exit()
