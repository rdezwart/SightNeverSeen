# Transforms
transform close:
    linear 0.1 zoom 1.1

transform default:
    linear 0.1 zoom 1.0

init python:
    def speakZoom(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
            if renpy.showing("leo"):
                renpy.show("leo", at_list=[close])
        elif event == "end":
            if renpy.showing("leo"):
                renpy.show("leo", at_list=[default]);

# Main Characters
define leo = Character("Leo", image="leo")
define lyr = Character("Lyra", image="lyra")
define ewa = Character("Ewan", image="ewan")

# Love Interests
define nox = Character("Nox", image="nox")
define sil = Character("Silas", image="silas")
define ern = Character("Ernest", image="ernest")
define aur = Character("Aurora", image="aurora")

# Variables
default affection = 0

label start:

    # TODO: Start game with LEO HOUSE
    scene bg house

    show leo long at left
    leo "Lyra, hurry up or we'll be late to meet Ewan."

    show lyr long at right
    lyr "I'm hurrying, I'm hurrying!"

    # TODO: Change BG to meeting spot
    scene bg meeting

    lyr "I'm not sure if you heard, since you tend to mind your own business, but there have been some concerning rumours going around."

    leo "What kind of rumours?"

    lyr """
    Apparently, magicians have been causing a ruckus around Veritas!

    You don't believe that right? I bet it's just rumors made up by some teenagers to try and scare people!
    """

    leo "That's true, I mean, magicians like us tend to lay low because of our bad status anyway. It might be a good idea to be careful though, I don't want you to cause trouble."

    lyr "When have I caused trouble?"

    leo """
    ...

    I can remember all the things you did when we were kids. Our parents would scold me and you all the time because of all the things you did.
    """

    lyr "That was when we were kids! It's different now!"

    # QUESTION: Maybe scene change?
    "When they approach the meeting spot, Lyra spots Ewan and waves her hand."

    lyr "Ewan! It's been so long!"
    # TODO: Insert running sounds

    leo "Sorry if we kept you waiting. Lyra took a long time to get ready."

    ewa "Hey, it’s fine, I just arrived as well, and Lyra, I see some things never change."

    lyr "It's been a looong while since the three of us were together! We haven't gotten a chance to see you that often."

    leo "We've finally got some free time since our trading business has been going well. Is there anywhere you want to go?"

    ewa "Ah, since I don't know the town that well, maybe you guys can decide?"

    "Leo and Lyra look at each other, and they both start thinking."

    jump choice


label choice:

    # TODO: Add animations showing protags
    menu:
        "Go to Marketplace":
            jump market

        "Go to Library":
            jump library

        "Go to Park":
            jump park

        "Go to Cafe":
            jump cafe
        # TODO: Add secret route
