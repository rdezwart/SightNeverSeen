# Park Route
# This is for ERNEST

# Side Characters
define man = Character("Man")

# Main Flow
label park:

    call .day01

    "end of route"
    jump finale

# Park, Day 01
label .day01:

    lyr "Why don't we head over to the park? Enjoy the great outdoors!"
    leo "Oh yeah, the park here is nice. We don't really go often, so this will be a good chance."
    ewa "Let's head off then."

    # TODO: Change scene to PARK
    scene bg park

    "When we arrived at the park, the three of us admired nature."

    lyr "We've always been busy with our business, so we never got a chance to visit the park often."
    leo "Yeah. It'll be a nice experience for us too."
    ewa "Let's walk around."

    "While walking, Leo stops and spots something."

    leo "Ah. I've seen it in a book, but apparently that monument over there is one the more popular tourist locations in Veritas."
    ewa "You've lived here for a long time and have never seen it before?"
    leo "Well, I don't stop by here often."
    ewa "I see."
    lyr "Do you two want to take a look at it? I'm not interested, so I'll wait by the pond. I heard there are ducks there!"
    leo "Sure, why not."

    "Leo turns to Ewan."

    ewa "I'll go with you then."
    lyr "I'll be waiting for you guys then! I brought some bread to eat as a snack later, but maybe I'll feed it to the ducks instead~."
    leo "I don't think we're allowed to feed the animals here..."
    lyr "It's fine! There's no signs that says I can anyways~"

    "I run off to the pond. There really isn't that big of a distance between where Ewan and Leo are from me, because I could still see them from where the pond is."

    "I feed the ducks the little crumbs from the bread. "
    "All of a sudden, a huge gust of wind blew. The gust was really strong, that it had caused me to stumble a bit and the piece of bread in my hand slipped."

    lyr "Ah!"

    "I hear the shriek of someone behind me. I turned around, and see a cluster of papers flying towards me; probably ones that got blown away from the wind. "
    "A young man was running, trying to catch the papers. "

    "I squint, and notice those papers are ones of high value; since Leo and I ran a business, I could tell that if those documents were tarnished, then it would spell really bad news. "

    "Without thinking, I instinctively used magic to gather the paper in my hands. The documents landed in my hands in a neat pile, and I sigh in relief seeing they were safe. But I didn't account for the young man that stood in front of me, who had seen what I've done. "

    lyr "Uh..."
    lyr "(Oh no! I instinctively used my magic... I totally forgot that these papers weren't mine! What should I do? How do I explain this to him?)"

    "The young man sees his documents in my hands. His eyes light up. "

    man "You really saved me there! If I had lost those papers, then I would've been a goner! Thank you so much!"
    lyr "Y-you're welcome."

    "I hand the papers over to the man. "

    man "You're a magician right?! I saw what you did earlier! It was so cool, like, the papers just floated into your hands like that!"
    lyr "Huh?"
    man "Oh, sorry, I got too excited. My name is Ernest! I really can't thank you enough for helping me back there!"
    lyr "R-right. I'm Lyra."

    "Ernest gives me a bright smile. "

    ern "Since you saved me, I owe you big time!"
    lyr "Uhm, what you saw earlier-"
    ern "Don't worry, since you helped me out, you can't be a bad person! In fact, let me treat you to lunch next time or something!"
    lyr "(This guys overwhelming energy-)"
    ern "Ah, crap! I have to get going or I'll be late!"
    ern "Uhmm, Lyra! Is it okay if we meet in the town plaza tomorrow at 12pm? I really want to repay you the favour!"
    lyr "Huh-? Uhm, sure?"
    ern "Thanks! See you then!"

    "Ernest smiles brightly, then runs off into the direction of town. "
    "I put my hands to my face. What was that...?"
    "It all happened so quickly that I couldn't process it. Someone had found out that I was a magician, but they didn't even bat an eye to it...?"

    lyr "(I should meet him tomorrow to make sure he doesn't say anything...)"

    "While I was lamenting to myself, I hear Leo and Ewan call out to me."

    ewa "Lyra? Are you alright? Why are you covering your face with your hands?"
    lyr "(Ah, I need to make up an excuse!)"

    "I lower my hands, and spot the piece of bread that I dropped floating in the pond. "

    lyr "The wind blew the piece of bread out of my hands and I dropped it..."
    lyr "(Nice save, me! I have to pretend like everything is alright!)"

    "Leo narrows his eyes at me, and sighs. "

    leo "Well that gust of wind earlier was really strong..."
    lyr "Right?!"

    "Ewan laughs, and the three of us continue to explore the park. I try to push my worries about Ernest for later. "
    "I should probably tell Leo what happened too..."

    "After a while, we headed back to town to explore."

    # TODO: Change scene to TOWN PLAZA (NIGHT)
    scene bg plaza night

    leo "Ah, it's getting late now."
    lyr "Already? I guess we'll show you more of the town tomorrow!"
    ewa "Yeah, that's fine. I'll see you guys tomorrow then."

    "Leo and I wave goodbye to Ewan and head our separate ways."

    # TODO: Change scene to INSIDE LEO AND LYRA'S HOUSE (NIGHT)
    scene bg house inside night

    "When me and Leo arrived home, I closed the door behind us and laughed nervously. Leo turned around and gave me a questioning look. "

    leo "Lyra? What's wrong?"
    lyr "Uhmm, Leo? Remember what you said this morning about being careful? About our magic?"
    leo "Yeah?"

    "The floor suddenly looked really interesting now. "

    lyr "Earlier, I might have used my magic and someone saw me...."

    "Leo stare at me, and I laugh nervously. Before he can say anything, I start talking again."

    lyr "It's okay! The guy, he was overly thankful for my help apparently? So uh, he wanted to meet me tomorrow at the town plaza to thank me or something?"
    leo "Isn't it dangerous? What if he outs you in public?"
    lyr "You're right but... also if I don't go, he might start spreading rumours about me, plus I want to check to see if he had any bad intentions."

    "Leo looks like he wants to protest my words, but he just sighs. "

    lyr "Plus if I do get outed then, I'll make sure you won't be affected! So it'll all be okay!"
    leo "..."
    leo "Fine, but if any trouble happens, you come tell me immediately, okay?"
    lyr "Understood!"

    return
