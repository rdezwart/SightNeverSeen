# Market Route
# This is for SILAS

# Side Characters
define grd = Character("???")
define sus = Character("Suspicious Man")
define bod = Character("Bodyguard")
define hug = Character("Hugh")
define jul = Character("Julius")
define tp1 = Character("Townsperson 1")
define tp2 = Character("Townsperson 2")

# Main flow
label market:

    call .day01

    # TODO: Change scene to outside LEO AND LYRA'S HOUSE
    scene bg house out

    call .day02

    # TODO: Change scene to outside LEO AND LYRA'S HOUSE
    scene bg house out

    call .day03

    call .day04

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    call .day05

    # TODO: Change scene to SILAS'S OFFICE
    scene bg silasOffice

    call .day06

    # TODO: Change scene to OUTSIDE LEO AND LYRA'S HOUSE
    scene bg house outside

    call .day07

    # TODO: Change scene to INSIDE LEO AND LYRA'S HOUSE
    scene bg house inside

    call .day08

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    call .day09

    # TODO: Change scene to TOWN PLAZA
    scene bg plaza

    call .day10

    return

# Market, Day 01
label .day01:

    leo "What about the marketplace? It is what Veritas is known for, anyways."

    lyr "Ooh, that's a good idea!"

    ewa "Let's head off then."

    # TODO: Change scene to marketplace
    scene bg market

    lyr """
    Oh wow, the market sells some extravagantly expensive items, like those crystals.

    ...!

    We have to check that item out. Let's go!
    """

    ewa "Huh? Lyra-?!"

    "I watched as Lyra grabbed Ewan --the poor soul who happened to be standing next to her-- and she darts off with him in hand. In less than a few seconds, I've lost them in the crowd already."

    leo """
    Ah, and just like that, I've been separated from them.

    She's always like this...

    (Maybe I'll walk around by myself until I can regroup with them.)
    """

    """
    I wander around the marketplace for a little bit. A little company alone sometimes is nice.

    Suddenly, a strange man bumps into me. An item from his hand slips out.
    """

    leo """
    Oh, sorr-

    (A magic item...?)
    """

    grd "Where did that guy go?!"

    "A group of bodyguards are gathered around, shouting. I peer at the strange man in front of me. There's a look of panic in his eyes, as he scrambled to grab the item and get up to run away."

    leo """
    (What should I do? That guy was holding a potentially dangerous magic item...)

    ...
    """

    """
    I stand for a moment to contemplate my options.

    Actually, is there a even a reason why I shouldn't act?!
    """

    leo "(Ah, whatever! If that man uses that magic item and blames it on magicians, then it'd be bad for Lyra and I.)"

    "I run after the strange man, and I see him turn into the corner of an alleyway. This might be my chance!"

    # TODO: Change scene to ALLEYWAY
    scene bg alley

    leo "(It's dangerous to use my magic in public, but the alleyway is secluded enough to be fine, I think.)"

    """
    I use my magic to forcefully take the magic item out of the man's hand. The magic item flies towards me, but I catch it and don't release my grip on it.

    The man's face shifted with realization upon seeing what I did.
    """

    sus "Ugh! You're a magician? That's-"

    "With a look of fear in his eyes, the man darts out of the alleyway faster than he had entered."

    leo "Seriously?"

    "I inspect the magic item to see if it's safe."

    leo "It's fine... I think. I should probably go return this to whoever was selling it."

    "As I turn around to exit the alleyway, I come face to face with someone who wasn't there before."

    leo """
    Oh.

    (I think this guy's the head of that famous trade company? What was his name... Silas? Oh crap, did he see me?)
    """

    "Silas walks up to me."

    sil "Are you a magician?"

    leo """
    OH. Uhhh. Umm...

    (I can't think of any good excuses-!)
    """

    sil "I'll take that as yes. How about we make a deal: I'll keep quiet about what I saw, in exchange for some information."

    leo "What kind of information are you looking for? How do you want me to find it?"

    sil "I'll keep in touch with you and handle it later."

    """
    Silas takes the magic item from my hands and I let him, my grip already weakend after being questions about being a magician.

    I put my hands to my head.
    """

    leo "(What have I done? I hope I don't get Lyra into trouble as well...)"

    # TODO: Change scene to marketplace
    scene bg market

    "I sigh, and exit the alleyway. Making a mental note to inform Lyra that our secret was out, I go to look for Lyra and Ewan."

    lyr "There he is! Sorry for draggin Ewan off and leaving you alone, Leo."

    leo "Yeah, it's fine."

    "I smile at Lyra, pretending to be fine. I'll tell her later when we get home, then..."

    ewa "Lyra was about to buy that item but decided to change her mind after noticing the price."

    lyr "Why does everything here have to be so expensive?"

    "The three of us walk around the marketplace until late."

    leo "Ah, it's getting late now."

    lyr "Already? I guess we'll show you more of town tomorrow, Ewan!"

    ewa "Yeah, that's fine. I'll see you guys tomorrow!"

    "Lyra and I wave goodbye to Ewan and head out separate ways. Lyra skips ahead of my happily."

    # TODO: Change scene to INSIDE LEO/LYR HOUSE
    scene bg house

    "As soon as we both entered our house, I closed the door and slumped against it."

    leo "Uh, Lyra. There's something I have to tell you."

    lyr "Huh? What is it?"

    leo "Uh. Well, earlier when I got separated from you and Ewan, I got caught by someone using magic-"

    "Lyra suddenly begins to shake me in a panic."

    lyr "What?! By whom?! And weren't you the one who said we had to be careful because of the rumours going around? Leo!"

    leo "I stopped a suspicious person from stealing a magic item. I thought no one could see me because we were in a secluded alleyway, but..."

    lyr "But what?! Just tell me already!"

    leo """
    Turns out that item belonged to Silas. You know, THAT Silas, the head of that famous trading company?

    He said he would keep my identity a secret if I provided him with whatever information he wanted. Said he'd call me when he needed me, but I honestly don't know...
    """

    "I look up and see Lyra's worried expression."

    leo """
    (Ahhh, this is bad, I can't let her be worried about me...)

    Don't worry, if the situation gets really bad, I'll bear the burden for both of us so you can live peacefully, at least. It was my fault in the end, after all.
    """

    lyr "I can't agree with that, but I can't do anything about it either."

    "I step towards Lyra and pat her back in an attempt to console her."

    leo "(Everything will be okay... right?)"

# Market, Day 02
label .day02:

    """
    The next day.

    As Lyra and I were heading out for the day again, I notice a person standing by the entrance. They seemed to be dressed in a bodyguard outfit. Lyra and I exchange eye contact and we approach the person. Who are they exactly?
    """

    leo "Uhm. Is there something you need?"

    bod "Yes. Silas has asked to meet with you today."

    leo """
    Huh? Already?

    (I wonder how they even managed to find where I live?)
    """

    lyr "Wait! If you're going to take Leo, I'm coming too!"

    bod "Who is this young lady?"

    leo """
    Ah, she's like my family member.

    Lyra, it's okay. I can go alone. Plus, we still have to show Ewan around, right? Tell him something came up for me.
    """

    "Lyra looks like she wants to protest my words."

    lyr "Fine. But you better tell me what happens later!"

    leo "Yeah. Sorry, I'll see you later, okay?"

    "I try to give Lyra a reassuring smile, then wave goodbye to her as I follow the bodyguard."

    # TODO: Change scene to INSIDE TRADE OFFICE
    scene bg tradeOffice

    "When we arrive at the Trade Headquarters, I couldn't help but look around."

    leo "(Woah. This place is way bigger on the inside than it seemed.)"

    """
    Even though I've been living in Veritas for a while, I've never actually had to step foot in here before.

    The bodyguard made a gesture at me to continue following them, and I obliged.
    """

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    "When I stepped into the office, I take notice of Silas immediately. I walk up to his desk."

    leo "We only met yesterday, but you called me in pretty quickly."

    sil "..."

    leo "So, what was it that you called me for?"

    sil "I want to see what the capabilities of a magician are. Since people like you hide yourself all the time, it would be wise to take advantage of this situation, no?"

    leo "(Huh, so that's what he wanted to know?)"

    sil "So, let's see... Try making that table float for a bit."

    """
    Silas gestures at the table right in front of him.

    I'm a bit unsure of wheteher or not I should use magic so openly... but I guess it didn't really matter in the end, since this guy already knows.

    I raise my hand and make the table float a bit in midair. The potted plant on the table tumbles, but Silas stands up to catch it.
    """

    leo "Is this fine?"

    sil "Hm. That's fine. There are some questions I'd like to ask you too."

    """
    Silas starts rapid-firing questions relating to magic towards me, and I tried my best to keep up.

    At some point his questions started going in one ear and out the other, I'm surprised I even managed to answer all of them.
    """

    leo "(Is this like an interview or something?)"

    sil "I think that's all for today. You may leave now."

    leo "Right."

    "I stand up and walk towards the door."

    leo "(Should I be expecting more calls from that guy soon?)"

# Market, Day 03
label .day03:

    """
    The next day.

    A familiar sight greeted Lyra and I as we walked out the door: the same bodyguard was waiting in the same position, presumably to take me to see Silas again.
    """

    lyr "Today again?!"

    leo """
    I guess so. Expect the same as yesterday, I guess.

    (Ah... I have a feeling it's going to be like this for a little while.)
    """

    """
    Unfortunately for me, I was right. The next few days pass quickly with always the same routine: the bodyguard would be at our front doors to take me to Silas for questioning.

    When can I catch a break...?
    """

# Market, Day 04
label .day04:
    """
    A few more days later.

    I head out the front door expecting a bodyguard again, but surprisingly, there's no one there. Lyra skips ahead of me and looks into the mailbox.
    """

    lyr "Leo, there's something here for you."

    "She takes the letter out and hands it to me. I open it to find a single slip of paper reading \"Come.\""

    leo "This letter would have only come from one place."

    "I sigh and slip the letter into my pocket. Even if there was no signature or anything, I had already known it came from Silas. And here's to thinking I'd get a break..."

    leo "Seems like I have to head over again."

    lyr "Aw, again? You've been saying that for the past few days, and it gets lonely with only Ewan and I."

    leo "It can't be helped. At least he didn't send a bodyguard this time."

    lyr "That's true. I'll see you later, then?"

    leo "Yeah."

    # TODO: Change scene to INSIDE TRADE OFFICE
    scene bg tradeOffice

    "When I arrived at the Trade Headquarters, the bodyguards take notice of me."

    bod "The meeting isn't for another hour."

    leo """
    Ah, okay. I'll come back in an hour, then.

    (Sheesh, I wish they'd written a time on the letter, at least...)
    """

    "As I turn to leave, another bodyguard stops me."

    leo "(This person is... I think I heard Silas call him Hugh a few times?)"

    hug "Excuse me. It's actually fine that you're early. Please follow me."

    leo "Huh?"

    "Hugh stars heading towards an exit, and I rush to go follow him."

    leo "Uhm. Where are we going, exactly?"

    "Hugh doesn't reply, and keeps walking."

    # TODO: Change scene to OUTSIDE GREENHOUSE
    scene bg greenhouse outside

    "Eventually, a greenhouse comes into view. Hugh stops a short distance from the entrance."

    hug "Silas is inside the greenhouse."

    """
    Hugh gestures towards the building. Am I supposed to go in...?

    I look at Hugh, but he's not giving me any instructions.

    What am I supposed to do...? Am I allowed to go inside?

    I look at Hugh again, then back towards the greenhouse.

    I steel myself, and head towards the entrance.
    """

    leo "(It should be okay, right? I mean, why else would they lead me here?)"

    # TODO: Change scene to INSIDE GREENHOUSE
    scene bg greenhouse inside

    "When I stepped inside the greenhouse, I notice the abundant amount of flowers immediately. There were more kinds than I could name, and they all look well taken care of."

    leo "(These flowers are really nice! Whoever looks after the greenhouse probably works hard to keep it nice.)"

    """
    I peer around, trying to look for Silas.

    He should be inside here... right? I hope the bodyguards aren't playing a prank on me.

    I spot Silas a distance away, his back turned from me. I begin to approach him.
    """

    sil "Samantha!"

    "I freeze in my tracks."

    leo "(Oh god, did I come at a bad time? First having my magic being found out by this man, and now I'm probably intruding on a moment between him and his secret lover?! What's with all these landmines I'm stepping on recently?!)"

    "In the middle of my mental dillema and lamenting, I squint to take a closer look to try and calm myself. In Silas' arms is... a plant?"

    leo """
    (Samantha is a plant? Ah, that means Silas is the person who tends the greenhouse. I guess even someone like him would have hobbies.)

    (Maybe it would be better if I left and pretended like I didn't see anything. He does have an image to maintain, after all.)
    """

    """
    I turn to leave. It'd be best to sneak out and pretend like I was clueless. Right. Feign ignorance.

    Unfortunately, my plan was short-lived as I stepped on a branch, or was it a twig?

    Whatever it was, it made a crack sound that could draw anyone's attention in the midst of a quiet atmosphere like this.
    """
    # TODO: Make the crack word italic

    leo "(Not good, not good! I stepped on another land mine! Is he going to chew me out for catching him in the act?! How am I going to explain this?!)"

    "I cursed silently"

    leo """
    Um.

    (I don't have any options, so I'll just talk it out.)
    """

    """
    I turn and approach Silas.

    He looks a bit uneasy, and I point to the plant in his hands. Maybe if I compliment him, he'll let me go?
    """

    leo "Um. Is gardening your hobby? If it is, then your greenhouse is really nice! I'm, err, not saying that just to flatter you or anything, I really do think it's nice! All the plants here look well taken care of."

    sil "So you're not here to find out about my secrets?"

    leo """
    Uh, no? I mean, I DID find out, but it was by accident. I don't think it's a big deal, because maintaining a greenhouse like this just proves you work hard?

    Also, you have bigger leverage over me with my identity as a magician.
    """

    """
    At any rate, Silas could turn me over as a magician any time, and I can't really do anything about it.

    As Silas registered what I said, he makes a surprised expression but quickly recovers.
    """

    sil "I see. Thank you. Since you're here this early, do you want to see the rest of the greenhouse?"

    leo "Oh, sure. Uhh, your letter just had the words \"Come.\", and I'm a little confused."

    "Silas ignores me and starts talking about his various plants in the greenhouse. I try to keep up, but at some point, his words went out one ear to another. Before I knew it, an hour had already passed."

    leo "(He must really like plants.)"

    "Hoever much he likes plants, I notice that it's about time for our meeting. If we don't leave now, we would be late."

    leo "Silas, isn't it time for our meeting?"

    "Silas doesn't hear me and keeps talking."

    leo "(He's really into the plant talk, but I have to snap him out of it.)"

    "I lightly tug at his sleeve."

    leo "Uhhh, isn't it time for us to get going for our appointed meeting?"

    sil "Right. Let us be on our way."

    leo "Mhmm."

    "Silas puts down \"Samantha\" and walks towards the exit, and I follow him out. I couldn't help laugh at what had unfolded before my eyes."

    leo "(That sudden change in person is kind of funny!)"

# Market, Day 05
label .day05:

    """
    A few days later.

    I was sitting in Silas' office, doing the usual thing Silas wanted from me, when he stopped all of a sudden.
    """

    sil "Do you know about the language of the flowers?"

    leo "Huh? I know a little bit, but it's not something I know very well."

    sil "I see. Well, the other day, I-"

    leo """
    (Aha. He just wants someone to talk about his hobbies, I guess? You wouldn't have imagined someone as business-like as Silas to be so passionate about flowers and gardening, of all things.)

    You seem to know a lot about this topic? Where did you learn?
    """

    "Silas stops for a moment."

    sil "Gather your belongings. We're heading out somewhere."

    leo """
    Huh?! Wait, where are we going?

    (And why do I have to go with him?!)
    """

    "I run after Silas."

    # TODO: Change scene to TOWN PLAZA
    scene bg plaza

    leo "Wait, I still don't know where we're going."

    sil "I just have something to pick up. Follow me."

    leo "(Aah. Maybe I should start getting used to this straightforwardly vague aspect of him.)"

    # TODO: Change scene to FLOWERSHOP
    scene bg flower

    leo "A flower shop?"

    sil "We're heading inside."

    leo "Right."

    "When we entered the flower shop, I saw Lyra and Ewan."

    lyr "Leo? What are you doing here?"

    leo "Silas had something he had to pick up here, and made me follow him. Though, I could ask you the same thing."

    lyr "Apparently, Ewan knows the florist who works here! His name is Julius!"

    "The florist --Julius-- approached Silas."

    sil "I'm here to pick up some flowers."

    jul "Ah, Mr. Silas, I've been expecting you. I'll have it ready right away."

    "Julius leads Silas away to look at some flowers. Lyra puts one hand on my shoulders and whispers something into my ear."

    # NOTE: Maybe make italic?
    lyr "I didn't think that someone like Silas would personally come and pick out flowers for himself!"

    leo "Aha."

    ewa "I haven't seen you in a while, have you been doing well?"

    # TODO: Affection points
    menu:
        "It's a bit odd, but I'm having more fun than I expected.":
            # +1 affection point
            $ affection = 1

        "It's a bit tough recently, but I'm keeping up.":
            # +0 affection point
            $ affection = 0

    ewa "I see. I'm glad you're doing fine, though. Don't push yourself too hard, alright?"

    leo "Yeah, thanks."

    lyr "It's so lonely without Leo, ever since Mr. Grouchy Businessman keeps calling for him every single day!"

    "Lyra skips over to Silas and Julius."

    lyr "If you overwork Leo, then I won't hesitate to throw hands!"

    sil "Hm?"

    leo "Lyra, don't threaten Silas like that."

    "As Silas pays for his initial purchase, Julius hands him an extra bundle of yellow flowers."

    jul "Take these as well."

    sil "Hmm? What type of flowers are these?"

    jul "Haha, I'll tell you next time."

    "While saying so, Julius looked at me and winked."

    leo """
    (Did he just wink at me?)

    (I don't know if this is a good omen or not...)
    """

# Market, Day 06
label .day06:

    """
    A few days later.

    I was at Silas' office, as per usual, when a bodyguard came rushing in.
    """

    bod "Sir! I have something I need to discuss with you in private."

    "Silas stands up, and the bodyguard whispers something to him."

    leo "(I wonder if it's somethign serious? Silas looks a bit concerned.)"

    "Afterwards, Silas came up to me."

    sil "Something came up, and I have to take care of it. You can leave early today."

    leo """
    Ah, sure. See you later, then.

    (I'm surprised he let me leave early, when he's usually so stingy the other times. Something serious must've come up.
    """

# Market, Day 07
label .day07:

    """
    The next day.

    When I left my house, I saw no bodyguard waiting to escort me. I checked inside the mailbox and there was no letter, either.
    """

    leo "It seems like I'm finally free today."

    lyr "Really?! Yay! You can come hang out with Ewan and I today!"

    "Lyra happily grabs my arm and drags me to meet with Ewan."

    # TODO: Change scene to TOWN PLAZA
    scene bg plaza

    lyr "I'm so happy we could all hang out like this! It's been such a long time."

    leo "Sorry, I didn't exactly expect to be caught up in that whole ordeal, leading to this and that."

    ewa "I'm glad you're doing okay! It's nice to have the three of us together again."

    "As we wander around town, we decide to take a rest on a bench."

    tp1 "Did you hear about the rumour recently? Apparently, the head of the famous trade company in town might be harbouring a magician!"

    tp2 "That's terrible! How could anyone hide a magician like that... There's a law that states we have to turn in magicians for a reason! Maybe we should stop relying on his company."

    leo "(That's...)"

    "Lyra gives me a worried expression."
    menu:
        "Go check up on Silas.":
            # +1 affection point
            $ affection += 1
            call .day07_good

        "Trust Silas to handle the situation.":
            # +0 affection point
            $ affection = affection
            call .day07_bad

# Market, Day 07 (Good)
label .day07_good:

    """
    The situation is bad.

    I abruptly stand up.
    """

    leo "Sorry! There's something important I remembered I have to do. I gotta run, see you later!"

    "Before Lyra or Ewan could react, I run off--but not in the direction of home, but rather in the direction of the Trade Headquarters."

    lyr "Don't worry, Ewan! Leo is just worried abou that flower-loving, grouchy-faced businessman. After all, they managed to become friends!"

    ewa "Yeah."

    # TODO: Change scene to TRADE OFFICE
    scene bc tradeOffice

    """
    When I entered the trade headquarters, I noticed that the amount of bodyguards has increased. Heightened security, possibly?

    I hide behind a pillar to contemplate my thoughts.
    """

    leo "(I don't think they'll let me in so easily. Maybe I can use magic?)"

    """
    I went to a secluded location and checked thoroughly to make sure no one could see me. Once I knew the coast was clear, I used my magic to divert attention away from me.

    It was almost like invisibility, but not quite. I just lowered my presence so I could sneak in.
    """

    leo "(Sometimes I think magic is really too overpowered. Ah, whatever, I'll worry about it another time!)"

    """
    I took my time to sneak into Silas' office. With the help of my magic, everything was considerably easier with nobody looking for me.

    When I got to the hall before Silas' office, i noticed that there was virtually no one around.
    """

    leo """
    (Surprisingly, there aren't many people inside.)

    (It's probably save now...)
    """

    "I increased my pace, but came face to face with Hugh, who was standing in front of the door."

    leo "(Damn, I let my guard down too easily! I forgot this guy's always near Silas-)"

    hug "Mr. Leo? How did you get in here? Maybe it's better not to ask. Sorry, I'm going to have to ask you to leave. Silas said to keep everyone out."

    leo """
    (That guy is an even bigger pain than I thought he'd be!)

    (I don't have time to waste...)

    And keep me in the hidden about an incident that involved me? Unfortunately, I'm not going to leave until I beat some common sense into that anthophile!
    """

    hug "Anthophile?"

    "I had just insulted Silas to Hugh's face, but he just started laughing."

    leo "Huh?"

    hug "It's just, I've been serving Silas since he was a child. I've never seen him enjoy himself as much as he did until you were around, so go ahead! Give him a good beating."

    leo "(Since Silas was a child...?)"

    "Hugh nodded towards me and gestured to the door. I look at him one last time, and open the door to Silas' office."

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    """
    As I entered the office, Silas immediately noticed me.

    However, he didn't look okay at all--in fact, he looked like he was in a daze.
    """

    sil "That's strange. I swear I didn't call for Leo today, but he's standing in front of me."

    leo "(Is Silas okay? He looks like he's really out of it. Plus, whatever he's saying means he doesn't think I'm actually here.)"

    sil "Maybe the stress is making me hallucinate? It hasn't been that long since I saw him, but my mind is probably playing tricks on me because I wanted to see him again."

    leo """
    ...

    (Yeah, I don't think he's alright.)
    """

    "I walk up to Silas and grab his shoulders and start shaking him."

    leo "Am! I! Still! An! Illusion! When I'm standing right in front of you?"

    sil "Leo?"

    leo "(About time he snapped out of it.)"

    sil "Why are you here? I didn't call for you."

    leo """
    (He seriously...)

    And I just so happen to hear about the rumours going around town about me, that you've been trying to hide?
    """

    sil "It doesn't concern you. I can handle it myself."

    leo """
    Of course it does!

    Those rumours have come out because of me hanging around your office. How could it not involve me? Why are you like this?

    There's no point in trying to hide anything anymore, because aren't we already in this together? I'll find out eventually, so if you don't tell me now it'll just make everything worse! And I'm kind of pissed right now!
    """

    sil """
    Sorry. You're right.

    I was acting under the pressures of stress, so I didn't think it would be fair to involve you.

    I'll tell you everything after I investigate something, then I'm yours.
    """

    leo "I trust you to tell me everything afterwards."

    sil "By the way, how did you get in here?"

    "I laugh sheepishly. About that..."

    leo "Ah. Uhm. Right. It's just some magic. Don't worry, I'll leave the same way so no one gets suspicious."

    "Now that I said what was on my mind, I smile and wave at Silas as I leave the way I came in."

# Market, Day 07 (Bad)
label .day07_bad:

    # TODO: Change scene to TOWN PLAZA
    scene bg plaza

    leo """
    (It might be best to lay low. I can trust Silas to handle this situation, I think.)

    Should we get going? We've rested enough and I think there are some places Lyra still wants to check out.
    """

    lyr "Right! Let's get going!"

    "I tried to get my mind off whatever those two townspeople said. If something was seriously happening, then Silas could handle it... right?"

# Market, Day 08
label .day08:

    """
    A few days later.

    Lyra looks outside nervously.
    """

    lyr "Uwah. It's getting dangerous around town recently."

    leo "Yeah, ever since we heard about the rumour from those townspeople, there have been a lot of strange incidents."

    lyr "Earlier when I was out, there was a fire that suddenly broke out in one of the homes! I was there and it just.. randomly exploded! No one was home, either, it's so strange."

    leo "Haven't a lot of shops recently had their windows suddenly breaking, too? It's kind of concerning, it's like some form of bad omen."

    lyr "I'm worried. They're going to blame magicians for these incidents, aren't they?"

    leo "I can't deny that."

    lyr "Leo, you should be careful. Especially because of everything that has happened around you recently."

    leo "Yeah, I will."

# Market, Day 09
label .day09:

    """
    A few days later.

    I was called to Silas' office, after a few days of no communication.
    """

    sil """
    I should properly explain to you what happened.

    There were rumours about me harbouring a magician, and while that's true, it's not something the general public should know. Because of the recent spike in incidents as well, people have been warier.
    """

    leo "I guess people are willing to blame those incidents on magicians?"

    sil """
    Yes. The public is also demanding answers from me, and business partners have been pressuring me.

    I've been trying to solve it without getting you involved, but people have noticed you frequenting and are getting suspicious.
    """

    leo "(Silas looks way more stressed than I've ever seen him. There's probably something I can do to help.)"

    sil "There are even rumours about how I've been using a magician to do underhanded tactics, like taking out my rivals."

    leo """
    (Ah, I know what I can do.)

    I can investigate the incidents for you, if that helps? You look way more stressed than usual, so I feel a bit bad.
    """

    sil "But-"

    leo "Also, you should be handling your own business affairs for now, so just leave everything else to me."

    sil "If you say so. I'll trust you to handle the investigation."

# Market, Day 10
label .day10:

    """
    The next day.

    Lyra had offered to help me with the investigation. We talked to people around town to see if they knew anything, then regrouped after.
    """

    lyr "Sorry, Leo. Everyone I asked only had the same information that we do."

    leo "Yeah, same here. It doesn't seem like we've found any leads at all."

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    leo """
    Sorry, I couldn't find more information about the incidents after all. They all seemed like random attacks more than anything.

    Are you alright? You look even worse than last time.
    """

    sil "Why don't we head to the greenhouse and get some fresh air?"

    leo "Sure. That sounds like a good idea."

    # TODO: Change scene to OUTSIDE GREENHOUSE
    scene bg greenhouse outside

    "As we were heading towards the greenhouse, a bodyguard runs up to us."

    bod "Sir! We've got trouble! The greenhouse, it's on-"

    leo "Fire?"

    "Silas and I rush over, and see the greenhouse engulfed in flames."

    leo """
    (Aah, Silas looks like he wants to faint!)

    (I can probably use magic to put out the fire, but it wouldn't be a great idea because Silas' reputation would likely go up in flames as well.

    (What should I do...?)
    """

    menu:

        "Run inside the greenhouse and attempt to save that 'one' plant.":
            # +1 affection
            $ affection += 1
            call day10_good

        "Tell Silas to not act rashly."
            # +0 affection
            $ affection = affection
            call day10_bad

# Market, Day 10 (Good)
label .day10_good:

    leo "(Well, if I can't use magic, then I should at least...)"

    "This might've been a dumb decision, but I broke out into a run towards the greenhouse."

    sil "Leo?!"

    # TODO: Change scene to INSIDE BURNING GREENHOUSE
    scene bg greenhouse burn

    leo """
    (Everything really is up in flame, this entire place is a fire hazard!)

    (I should just 'Samantha' and leave as fast as I can.)
    """

    "I look around and spot 'Samantha'."

    leo """
    (There it is!)

    (Thank goodness it's okay! At least the one plant Silas is fond of ended up being unharmed.)

    (It's dangerous for me to stay inside here for any longer. I should get out while I still can.)
    """

    # TODO: Change scene to OUTSIDE GREENHOUSE
    scene bg greenhouse outside

    "When I arrived back outside, I turn to look at the greenhouse. The bodyguards are going everything they can to put out the fire."

    leo "Whoah. The greenhouse is more like a flame-house."

    "When I turned back around, Silas was immediately in front of me, shaking my shoulders."

    sil """
    What were you thinking?! Why did you run inside a flaming building like that!

    Don't you know how worried I was?! If something happened to you, then-
    """

    leo """
    Oh. Uhm. Sorry?

    I couldn't rescue more of your plants. I know they're important to you, but-
    """

    "I hold up the plant Silas referred to as 'Samantha' in front of him."

    leo "I got Samantha at least?"

    "Silas stops."

    leo "Are you alright? You look like you want to cry."

    "Silas lets go of me and turns around."

    sil "The bodyguards will handle everything here. You look like a mess. We should head back."

    "I look at myself and realized I was covered in soot. Lyra's going to freak out at me later..."

    leo "Oh. You're right, I didn't notice."

    """
    Silas starts walking away, but I turn around to give one last look to the greenhouse.

    Out of the corner of my eyes, I notice something.
    """

    leo """
    (Hm? Are those... Fireflies?)

    (I probably shouldn't think much of it.)
    """

    """
    I blink my eyes a few times and noticed the fireflies were gone again, probably just my imagination.

    I try to catch up with Silas, still carrying 'Samantha'.
    """

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    "After making myself presentable again, Silas spoke."

    sil "I don't have anything for you to do, so... you can leave for the day."

    leo """
    Huh? Okay.

    (He probably needs some time to process what happened. Is he okay, though? He hasn't turned his face to look at me once since earlier.)
    """

    # TODO: Change scene to OUTSIDE LEO AND LYRA'S HOUSE
    scene bg house outside

    "As I arrived in front of our house, Lyra rushes out."

    lyr "Leo?! Why are you covered in soot?"

    leo "Aha. Some things happened earlier."

    lyr "I'd demand you to tell me what happened, but go get washed up first! Then you HAVE to tell me, or else I'm gonna get real mad..."

    leo "Aren't you already freaking out right now, though?"

    "Lyra pushes me inside as I smile."

# Market, Day 10 (Bad)
label .day10_bad:

    leo """
    (Even though this situation is bad...)

    Don't act rashly. Your position is delicat right now.
    """

    sil "You're right..."

    "We watched as the bodyguards frantically put out the fire. Afterwards, we head back to Silas' office."

    # TODO: Change scene to SILAS' OFFICE
    scene bg silasOffice

    sil "I don't have anything for you to do, so... You can leave for the day."

    leo """
    Okay.

    (He probably needs some time to process what happened. I hope he's okay.)
    """
