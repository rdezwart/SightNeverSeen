# Secret Route
# This is for EWAN

# Side Characters
define tp1 = Character("Townsperson 1")
define tp2 = Character("Townsperson 2")

# Main Flow
label secret:

    call .day01

    "end of route"
    jump finale


# Secret, Day 01
label .day01:

    lyr "Why don't we just walk around and talk for a bit? It's been a long time, so let's catch up!"
    leo "That's true. We can show you places next time."
    ewa "That sounds fine then."

    "The three of them makes their way to the town plaza, while chatting."

    # TODO: [Change scene to TOWN PLAZA]
    scene bg plaza day

    leo "It's been a long time since I saw Ewan in flesh, but you've really changed, haven't you."
    lyr "Mhmm. I think so too!"
    ewa "Is that so?"

    "Thud."
    "A sudden sound of collision catches Ewan and Leo's attention. Lyra, who happened to be the unfortunate recipient out of the three, gets hit right on the back of her head by a ceramic pot."

    lyr "Uwwaaaaaag-!"
    ewa "Lyra?!"
    leo "Wait what was that?! Lyra?!"

    "Lyra starts falling towards the ground, but before she could make impact, Leo catches her. Leo notices that she's been temporarily knocked out. "
    "Leo turns to Ewan for help, but notices his panicked facial expression."

    leo "(Huh? That's-)"

    # [FLASHBACK]
    "(A young Ewan is seen freaking out over something, making the same expression as before. However the reason for Ewan freaking out is unclear.)"

    "Before Leo could decide whether to calm Ewan, or check Lyra for injuries, Lyra starts stirring in Leo's arms. She opens her eyes, and gains consciousness. "

    leo "Lyra?! Are you alright?"
    lyr "Uhm... Something came at me fast and hard..."
    leo "Uh. Yeah. A ceramic pot just came out of the sky and knocked you out for a minute."

    "Leo helps Lyra stand properly, and rubs the back of her head, checking for any major injuries."
    "The two turns to Ewan, and see tears on Ewan's face that don't seem to be stopping anytime soon."

    leo "Ewan?!"
    lyr "Uwahh! Ewan?! I'm fine! There are no threats to my life!"

    "Lyra gives Ewan a hug."

    lyr "Ewan! I'm okay! Don't worry!"

    "Ewan snaps out of it, and comes back to his senses."

    ewa "I'm so glad you're okay."
    ewa "Though, you two have your grip on me a bit too hard-"

    "Leo and Lyra let go of Ewan. notices that Lyra is hugging him, and Leo is holding onto one of his arms with a worried expression."
    "Ewan sighs with relief."

    lyr "Oh..! Sorry."
    leo "We were worried since you started crying all of a sudden."

    "Leo looks up, and notices that the townspeople around are staring at the three. "

    leo "Maybe we should get going. We kind of caused a scene in public."
    ewa "Ah."

    "Lyra takes a step forward but stumblrs a bit. Leo and Ewan supports Lyra, and help her walk. "

    leo "Be careful now. You just got hit with something hard."
    ewa "Don't push yourself too hard Lyra."
    lyr "Eheheh."

    # TODO: [Change scene to CAFE]
    scene bg cafe

    aur "And that's all right?"
    lyr "Yes!"

    "The waitress confirms their order, and leaves."

    leo "Are you really all right Ewan? You started crying earlier so I'm worried."
    lyr "Yeah, I'm fine now though! Don't worry about me it wasn't that big of a deal! I regained my balance now. You worry too much Ewan."
    ewa "It's only natural to worry about your friends though."
    leo "That's true."

    "While Ewan and Leo are talking amongst themselves, Lyra overhears the people from the next table over talking about something."

    tp1 "Aah. You see that waitress with the fuchsia hair? Apparently, her dad is a noble, and he came looking for her recently."
    tp2 "Huh, really?! That's so unexpected. Imagine being raised as a commoner only to find out that you're a noble as well."
    tp1 "That sounds like something out of a novel, to be honest. I couldn't believe it either, but I saw her arguing with her so-called father a few days ago. She ended up storming off."

    "Lyra glances at their general direction."

    ewa "Lyra? Is there something wrong?"
    lyr "Ah. No, everything is fine. I just heard some talk that sounded interesting."
    leo "You shouldn't be eavesdropping to other people's gossip like that."
    lyr "I-I'm not!"

    "Lyra pouts, and Ewan laughs as he watches Leo and Lyra banter. "
    "After a while, they get their meal, and continue talking amongst themselves."

    # TODO: [Change scene to TOWN PLAZA]
    scene bg plaza day

    "The day passes peacefully."

    leo "(Ah. It's kind of peaceful. But it feels a bit off somehow.)"
    lyr "It's getting kind of late, should we continue showing you around tomorrow then?"
    ewa "That's fine. Thanks for today, you two."
    leo "See you tomorrow then."

    "Leo and Lyra wave goodbye to Ewan and goes their separate ways."

    return
