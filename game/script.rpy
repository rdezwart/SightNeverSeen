# Main Characters
define leo = Character("Leo")
define lyr = Character("Lyra")
define ewa = Character("Ewan")

# Love Interests
define sil = Character("Silas")
define nox = Character("Nox")
define ern = Character("Ernest")
define aur = Character("Aurora")

# Enabled Routes
default silRoute = True
default noxRoute = False
default ernRoute = True
default aurRoute = False
default ewaRoute = True

# Variables
default affection = 0
default persistent.secretRoute = False

# Config
define config.menu_include_disabled = True

label start:

    play music "peaceful1.mp3" loop

    # TODO: Start game with LEO HOUSE
    scene bg house inside day

    show leo at left
    leo "Lyra, hurry up or we'll be late to meet Ewan."

    show lyr at right
    lyr "I'm hurrying, I'm hurrying!"

    # TODO: Change BG to meeting spot
    scene bg plaza day

    show lyr sad at right
    show leo annoyed at left

    lyr "I'm not sure if you heard, since you tend to mind your own business, but there have been some concerning rumours going around."

    leo "What kind of rumours?"

    lyr """
    Apparently, magicians have been causing a ruckus around Veritas!

    You don't believe that right? I bet it's just rumors made up by some teenagers to try and scare people!
    """

    leo "That's true, I mean, magicians like us tend to lay low because of our bad status anyway. It might be a good idea to be careful though, I don't want you to cause trouble."

    show leo suffer

    lyr "When have I caused trouble?"

    leo """
    ...

    I can remember all the things you did when we were kids. Our parents would scold me and you all the time because of all the things you did.
    """

    show lyr angry

    lyr "That was when we were kids! It's different now!"

    # QUESTION: Maybe scene change?

    show lyr smile closed
    show leo
    show ewa

    "When they approach the meeting spot, Lyra spots Ewan and waves her hand."

    lyr "Ewan! It's been so long!"
    # TODO: Insert running sounds

    leo "Sorry if we kept you waiting. Lyra took a long time to get ready."

    ewa "Hey, it’s fine, I just arrived as well, and Lyra, I see some things never change."

    lyr "It's been a looong while since the three of us were together! We haven't gotten a chance to see you that often."

    leo "We've finally got some free time since our trading business has been going well. Is there anywhere you want to go?"

    ewa "Ah, since I don't know the town that well, maybe you guys can decide?"

    show leo annoyed
    show lyr

    "Leo and Lyra look at each other, and they both start thinking."

    # TODO: Add animations showing protags
    jump routeChoice


# Menu label for route
label routeChoice:

    # If game has been finished at least once
    if persistent.secretRoute:
        menu:
            "{i}Where should we take Ewan?{/i}"

            "Go to the Market - Play as Leo" if silRoute:
                jump market

            "Go to the Library - Coming Soon" if noxRoute:
                jump library

            "Go to the Park - Play as Lyra" if ernRoute:
                jump park

            "Go to the Cafe - Coming Soon" if aurRoute:
                jump cafe

            "Walk around Veritas - Unlocked" if ewaRoute:
                jump secret

    # If first time through
    else:
        menu:
            "{i}Where should we take Ewan?{/i}"

            "To the Market - Play as Leo" if silRoute:
                jump market

            "To the Library - Coming Soon" if noxRoute:
                jump library

            "To the Park - Play as Lyra" if ernRoute:
                jump park

            "To the Cafe - Coming Soon" if aurRoute:
                jump cafe


# Label for ending the game
label finale:

    scene bg black

    "Thank you for playing! We hope you enjoyed your experience of \"A Sight Never Seen\"."

    if persistent.secretRoute:
        """
        This is all the content this game has to offer. Have you tried all the routes? More is to come in future versions.
        """
    else:
        "You have now unlocked an additional secret route! Begin the experience again, and enjoy!"

    $ persistent.secretRoute = True

    return
