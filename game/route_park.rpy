# Park Route
# This is for ERNEST

# Side Characters
define man = Character("Man")

# Main Flow
label park:

    call .day01
    call .day02

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

    "Without thinking, I instinctively used magic to gather the paper in my hands. The documents landed in my hands in a neat pile, and I sigh in relief seeing they were safe."

    "But I didn't account for the young man that stood in front of me, who had seen what I've done. "

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

# Park, Day 02
label .day02:

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "The next day. "
    "I left Leo to handle showing Ewan the rest of town."
    "I'm waiting at the fountain near the town plaza nervously. I had no ideas what the intentions of Ernest were, after he found out I was a magician. He said he wanted to thank me, but I couldn't help but be a bit suspicious. "
    "There's no way someone would let a magician off like that... right?"

    "I hear a voice calling for me."

    ern "Hey! Lyra!"

    "Ernest runs up to me. "

    ern "I'm so glad you came! I was worried because I thought you might not show up."
    lyr "R-right."
    lyr "(I don't know what he wants... should I ask him now-?)"
    ern "Anyways, I'm really grateful you helped me yesterday,let me treat you to lunch today!"

    "Before I could protest, Ernest is already running off. "

    ern "This way! I know a place!"

    "I follow after him. "

    lyr "Uhm. Ernest? Yesterday you asked me if I was a magician-"
    ern "Oh yeah! I wanted to ask you that! You know about magic and stuff!"
    lyr "Huh?"
    ern "People are always talking about magicians, and I didn't think they were real at first."
    ern "Plus, I think magic is cool!"

    "Ernest turns to me. "

    ern "You know yesterday when you caught all my papers and they floated smoothly into your hands?! It was super cool!"
    ern "Like you controlled the way they were moving and stuff!"
    lyr "Eh? Uhm..."
    lyr "(This kind of reaction is...)"
    ern "Plus, you used it to help me! If those documents had landed in the water, I would've been in big trouble!"
    lyr "B-but aren't magicians supposed to be bad people?"
    ern "You helped me though right? So there's no way you can be a bad person!"
    lyr "(This guy... is kind of simple minded, but..) "

    "I laugh. "

    ern "Hm?"
    lyr "I've never met someone who reacted that way about magicians."
    ern "Huuh."
    lyr "You're a good person, Ernest!"
    ern "You don't have to tell me for me to know!"
    lyr "Though uhm, you shouldn't go around telling people that I'm a magician though."
    ern "Hmm? Sure, I don't really understand why people hate magicians so much though..."

    "Ernest trails off, and he brings me inside the cafe."

    # TODO: [Change scene to CAFE]
    scene bg cafe

    "Ernest and I are seated by a waitress. We both look over the menu. "

    ern "Order anything you like! It's on me."

    "After ordering, Ernest and I talk for a bit. "

    ern "Actually, I have a friend who is similar to you."
    lyr "Oh?"
    ern "Yeah! He's also a m-"

    "Before Ernest could say the word 'magician,' I cut him off."

    lyr "Is that right?! I'd uh, love to meet them sometime!"
    ern "I can introduce you! He's my best friend!"
    lyr "(Dangerous, too dangerous! If I didn't cut Ernest off then, it would've spelled trouble for me!)"

    "We ate our food when it arrived. As promised, Ernest paid for my meal, and we left the cafe. "

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    ern "I would introduce you to my friend today but I have things to do at the marketplace..."
    lyr "It's okay, don't worry about it."
    ern "Oh! I know! You know that flower shop near the outskirts of the town plaza? Meet me there tomorrow!"
    lyr "Huh?! Sure..."
    ern "Alright, thanks for today! I'll get going now!"
    lyr "B-bye..."

    "I wave, and watch as Ernest runs off in the direction of the marketplace. "

    lyr "(He has a lot of energy... I can't keep up.)"
    lyr "(But he doesn't seem to be a bad person.)"

    "I head home for the day."

    return
