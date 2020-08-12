# Market Route
# This is for SILAS

# Side Characters
define grd = Character("???")
define sus = Character("Suspicious Man")
define bod = Character("Bodyguard")

# Main flow
label market:

    call .day1

    # TODO: Change scene to outside LEO AND LYRA'S HOUSE
    scene bg house out

    call .day2

    # TODO: Change scene to outside LEO AND LYRA'S HOUSE
    scene bg house out

    call .day3

# Market, Day 1
label .day1:

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

# Market, Day 2
label .day2:

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
