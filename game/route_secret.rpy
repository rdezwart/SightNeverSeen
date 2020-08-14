# Secret Route
# This is for EWAN

# Side Characters
define tp1 = Character("Townsperson 1")
define tp2 = Character("Townsperson 2")

# Main Flow
label secret:

    call .day01
    call .day02

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


# Secret, Day 02
label .day02:

    # TODO: [Change scene to MARKETPLACE]
    scene bg market

    "The next day. "
    "Leo and Lyra decided to show Ewan around the marketplace today. Lyra had insisted with shining eyes, as she dragged Leo and Ewan off."

    lyr "This is my favorite place in town! I'm so excited!"
    leo "Yeah. And that's why we have to make sure you don't run off because it's crowded so-"

    "Leo nods grabs one of Lyra's hands, and nods at Ewan. "

    leo "Ewan."

    "Ewan looks surprised for a second, but nods in reply, realizing what Leo wants him to do, and takes Lyra's other hand."

    leo "So you don't get overexcited and run off."
    lyr "Wait! Are you two treating me like a child?! I won't run off!"
    leo "You said that last time, and I spent hours looking for you."
    ewa "That doesn't sound pleasant."

    "Lyra tries to protest, but gives up in the end. "
    "While walking around, they see a crowd of people, and hear two people in the middle of an argument."

    ern "You're willing to let that person purchase magic goods so easily? Don't you understand that those types of tools should be thoroughly screened?"
    sil "I'm already following the regulations that were set in place."
    ern "I don't agree with your line of thinking! They've done bad things in the past!"
    sil "And they were cleared of those charges, so I don't see what's the problem."
    ern "The way you run your business is total disregard to people! It's dishonorable!"
    sil "Say what you want. The way I've dealt with my trades have always been fair and follows the laws."

    "The three watches as the commotion goes down."

    lyr "Uwah. It's never pleasant seeing people argue in the marketplace."
    leo "That's for sure"
    ewa "Maybe we should get going?"
    lyr "Mhmm."

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "As the three leave the marketplace, they wander around town. Lyra notices a flower shop up again."

    lyr "Oh! It's that flower shop I pass by often."
    ewa "Let's keep movin-"
    leo "Hmm? The flowers in front of the shop look nice."
    lyr "Let's go inside!"

    "Ewan stops, but Lyra drags him along as she heads towards the entrance. Leo trails from behind."

    # TODO: [Change scene to INSIDE FLOWER SHOP]
    scene bg flower

    "When the three enter the flower shop, they don't see anyone around. Lyra looks around, but then suddenly a person appears from right behind her."

    jul "Young miss and young gentlemen! How may I help you today?"
    lyr "KYAaaa!"

    "Lyra lets out a scream, as she tumbles forward from surprise. Leo manages to catch her before she falls onto the floor. Ewan shoots a disgusted look at the source of the voice that had surprised Lyra."

    lyr "I-I'm sorry! You scared me, appearing behind me like that!"
    jul "Oh. My apologies. That was never my intention. I would never attack a young lady from behind like that."
    ewa "... Sure."
    jul "I believe this is the first time you've been here? My name is Julius, it's nice to make your patronage."

    "Julius looks at Ewan."

    jul "I haven't seen you in a while."
    ewa "I don't know what you're talking about."

    "Leo helps Lyra stand up, and the two look at Ewan with questioning eyes. Ewan immediately reverts, and gives Leo and Lyra an angelic smile."

    lyr "You know him?"
    ewa "No."
    jul "Don't be so cold. We're friends!"
    ewa "Acquaintances."

    "Leo laughs nervously, and Lyra tugs at his sleeve."

    leo "Uhm. Do you think Ewan is alright? I've never seen him like that before."
    lyr "Uwah. He's smiling, but he's not."
    leo "That's because he always looks pleasant in front of us I guess?"
    ewa "I didn't want to trouble you two since you're always so busy."
    lyr "Don't be like that Ewan. We're friends!"
    leo "Yeah. You can come to us for anything."
    jul "They're right you know. You shouldn't underestimate the power of friendship."
    ewa "..."

    "Lyra proceeds to run around the shop, looking at the various flowers set on display. Leo follows her. Julius continues to Ewan, much to Ewan's dismay. "

    "As the three are about to depart, Julius stops Leo and Lyra and hands them some flowers. Julius hands Leo some daffodils, and Lyra some azaleas."

    jul "This one's on Ewan. Come back anytime if you're having trouble."

    "Ewan shoots Julius a glare, and pushes Leo and Lyra out of the shop. "

    # TODO: [Change scene to TOWN PLAZA (NIGHT)]
    scene bg plaza night

    "When they leave the flower shop, Lyra looks up at the sky and realizes it has gotten late. "

    lyr "Ooh. It's dark already."
    leo "I didn't realize it was this late already. Hm?"

    "As Leo is about to turn to Ewan, he notices the fireflies in their presence. "

    leo "There are fireflies around you."
    lyr "They're so pretty! It's like some kind of night-light!"
    ewa "It seems that fireflies like me a lot."
    leo "Well I can tell just by looking at you."

    return
