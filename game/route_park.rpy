# Park Route
# This is for ERNEST

# Side Characters
define man = Character("Man")
define per = Character("Person")

# Main Flow
label park:

    call .day01
    call .day02
    call .day03
    call .day04
    call .day05
    call .day06
    call .day07
    call .day08
    call .day09

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

# Park, Day 03
label .day03:

    # TODO: [Change scene to OUTSIDE LEO AND LYRA'S HOUSE (DAY)]
    scene bg house outside

    "The next day. "

    leo "Are you going to meet, uhm, Ernest again? That's his name right?"
    lyr "Yeah. He said he wanted to introduce me to another one of us."
    leo "I didn't think there would be another person like us in town."
    leo "I'll show Ewan around again, so be careful."
    lyr "See you later!"

    "I head off to the flower shop Ernest had mentioned the day before. "

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "I see Ernest standing outside the mentioned flower shop."

    ern "Lyra!"

    "I run over to him."

    lyr "Hmm? I've never been here before."
    ern "Let's go inside!"

    # TODO: [Change scene to FLOWER SHOP]
    scene bg flower

    "When Ernest and I walked inside, there was no customers inside. However, the florist noticed us. "

    ern "Julius!"

    "The man Ernest called 'Julius' gives us a teasing smile. "

    jul "Oh? You're with a girl? I didn't know you had it in you~ I was starting to think you only liked men."
    ern "That's not the point! This girl is also a ma-"

    "Before Ernest could say the word 'magician,' Julius was already over in a speed of light and shoved whatever flowers he had in his hands into Ernest's mouth. "

    lyr "Ehh?! Eh?"

    "Ernest coughs on the flowers, and I pat his back."

    ern "Julius... tulips don't taste very good, you know."
    lyr "Uhmm, Ernest? You shouldn't be shouting the word 'magician' out in public so loudly like that."

    "I look at Julius. So he's a magician too?"

    jul "My apologies for the commotion. As you've heard from Ernest, I'm Julius."
    lyr "Oh! I'm Lyra."
    lyr "So, I'm guessing you're the magician that Ernest told me about..."
    jul "Ernest told you?"
    ern "I didn't say much! Or barely anything!"
    lyr "He just said that he had a friend who is also a magician like I am."
    jul "I've mentioned it a couple of times, but you just never seem to listen, do you."

    "Julius doesn't look phased at all, as if he was expecting this to happen."

    jul "The topic of magicians is received quite unfavorably around these parts, not everyone is as open as you."
    jul " Plus, you should be careful, not just from the public ears but also not all of us are good people, you know?"

    "As he's saying that, Julius makes a smile that seems to suggest something I can't figure out."

    ern "That's not true! Both you and Lyra are good people and magicians! People will understand!"

    "Julius turns to look at me."

    jul "What do you think Lyra?"
    lyr "Huh?! Well-"

    # DECISION 1:
    # "We can't speak for every magician out there." (+1 good end point)
    # "If you're a good person, then people would surely understand." (no increase in good end point)

    menu:
        "We can't speak for every magician out there.":
            # +1 affection
            $ affection += 1

        "If you're a good person, then people would surely understand.":
            # +0 affection
            $ affection = affection

    # This decision is for points only that add up at the end to determine whether or not you get the good or bad end.
    # [*Ernest is good end point instead of affection point bc we constantly need to disprove of his naive thinking LMAOOO]

    jul "Mhmm. I see."
    lyr "But that's just what I think, so.."

    "I look around the shop to try to divert the talk away from the topic of magicians. If we talk about it any longer, there'll only be conflict..."

    lyr "Oh! There are a lot of pretty flowers here. Maybe I should buy some to bring home."
    jul "If there's anything that catches your eye, then please tell me."
    ern "Oh! I'll help you look for flowers then!"

    "Ernest grabs my hand, and drags me around the shop to look at the flowers. "
    "In the end, Julius just gave me some azalea flowers as a gift for our meeting. "
    "Azaleas huh... they're quite pretty. "

    jul "Feel free to come back anytime, even if you're running into trouble."
    lyr "You're making yourself sound like a consultant booth and a flower shop at the same time."
    ern "I'll walk you to the plaza!"

    "We say goodbye to Julius, and head out."

    # TODO: [Change to TOWN PLAZA (NIGHT)]
    scene bg plaza night

    "I didn't realize how late it was until we had left the flower shop. "

    ern "You know Lyra, I was thinking about what you said earlier."
    ern "I don't think magicians are bad people."
    ern "When I first met Julius, he wasn't close to anyone, but he didn't try to get close to anyone either."
    ern "I managed to befriend him by hanging around him because he always seemed lonely."
    lyr "(That's...)"

    "I skipped ahead of Ernest, then turn back to face him. "

    lyr "If you're worried about me not having anyone to rely on, then you don't need to worry."
    lyr "Did you maybe see Julius in me?"
    ern "No-! Well, I-"

    "I laugh. He's really an honest person. "

    lyr "You don't need to worry about me at all, there's someone that I can confide in."
    lyr "Plus now you and Julius both know right? So I'm not alone anymore."

    "Ernest smiles."

    ern "Yeah! You're right. You can trust me and Julius!"

    "Afterwards, I part ways with Ernest and head home. "

    return

# Park, Day 04
label .day04:

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "The next day. "
    "I walk around town with Leo for a bit. Ewan said he was busy with something today, so we just decided to idly spend our day off. "

    lyr "So, I don't think Ernest is a bad person after all, so there's nothing to worry about."
    leo "Well that's good to hear."
    lyr "Though he's a bit idealistic about people coming to accept magicians..."
    leo "That sounds a bit troublesome. Will you be okay?"
    lyr "Well, I sure hope so."

    "As Leo and I are talking, I hear a familiar voice calling out to me. "

    ern "Lyra!"
    lyr "Speaking of the person."

    "Ernest runs up to where I was standing. "

    lyr "Ernest! What are you doing?"
    ern "I was planning on going to the library, there was something I wanted to search up! Do you want to come?"

    "Ernest looks at Leo."

    ern "Oh sorry! Are you two doing something right now? I'm Ernest, it's nice to meet you!"
    leo "No, it's fine. I'm Leo."

    "Leo gives me a look, as if he knew that hanging around Ernest would mean possibly delving into magician talk based on what I had told him before. "

    leo "You should go with Ernest if you want to, Lyra. I'll just walk around the marketplace and see if there's anything we need to pick up."
    lyr "Ah, okay... I'll see you later then."

    "Leo nods, and walks off in the direction of the marketplace."
    "Ernest and I start walking to the library. "

    ern "Is Leo your friend?"
    lyr "Leo? We've been friends since we were kids."
    ern "Huuh. So does he know you're a magician?"
    lyr "(I mean Leo is also a magician, but I can't just say that so easily.)"
    lyr "Mhmm."
    ern "So is he the person who you said you could confide in?"
    lyr "Yeah, since he knew since we were younger."
    ern "He doesn't hate you? For being a magician."
    lyr "Huh? Of course not."
    ern "See! There are people like me and Leo out there, who don't think magicians are terrible!"
    ern "If people could realize that magicians aren't bad people then..."
    lyr "..."

    "I didn't know how to reply to Ernest's statement. "
    "Before I knew it, we were already outside the library. "
    "What did Ernest want to come here for? I didn't want to be rude, but he didn't seem like the type who'd go to the library often. "

    ern "Alright! Let's head in!"
    lyr "Ernest, you shouldn't shout inside a library!"

    "I shouted at him, as he ran inside."

    # TODO: [Change scene to LIBRARY]
    scene bg library

    "When we entered the library, Ernest seemed to be aimlessly wandering around. I didn't know what he came here for, so I followed him, confused. "
    "Sooner or later, we came to a stop. "

    lyr "What did you want to come here for?"
    ern "Comics."
    lyr "Huh?"

    "Ernest takes out a book and shows me. It was a graphic novel. "

    lyr "Are you going to take some of these out?"
    ern "Yeah! They're fun to read in my spare time when I'm not agonizing over business ventures."

    "Oh right, when I had first met Ernest he was chasing after some business documents."

    lyr "So you run a business too?"
    ern "Yeah!"

    "Well, it's common in Veritas to be a trader or run a business. This IS a trading port town after all. "
    "Ernest is already in his own world, reading whatever graphic novel he picks up. "
    "I peer over his shoulder to see what he is reading. "

    ern "Are you interested, Lyra?"
    lyr "It'd be a waste if I came to the library to sit around."
    ern "Oh, I didn't come to the library just to read, you know. I could just do that at home."

    "Then what did you come here for?!"

    "Ernest picks up a few books, and heads to another section of the library. I follow him, once again, confused. "

    lyr "History?"
    ern "Well I wanted to see what magicians did in the past that made people hate them so much."
    ern "I've looked through some, but they never really explained."
    ern "Why magicians are hated, huh? To be honest, I've never really thought about it before. "
    ern "It was only a natural thing in this country. "
    ern "'Magicians are different from regular people'"

    lyr "Do you really think that magicians could be accepted by normal people?"

    "Ernest answered, unwavering. "

    ern "Of course!"

    "If things could only be like that. "

    lyr "Why are you trying to hard for the sake of magicians?"
    ern "I want to show Julius that being a magician isn't something he should be afraid of."
    ern "He always tells me not to be careful, saying that it's bad in some way or another."
    ern "But meeting you proves that magicians can be accepted!"
    lyr "..."

    "I watch as Ernest looks through the books, and I think about his words. "
    "If magicians can be accepted then..."

    lyr "(I only survived this long hiding my status as a magician because I had Leo to rely on.) "
    lyr "(If people could really accept magicians then...) "
    lyr "(If it's Ernest then maybe...)"

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "When Ernest and I left the library, it was still bright out. I still had some time to kill. "

    ern "Do you have anything you need to do?"
    lyr "Oh, no. It's my day off today. That's why earlier, I was doing nothing with Leo until you showed up."
    ern "Is that right! C'mon, let's hang out then!"

    "Before I could reply, Ernest is already dragging me off to... god knows where. "
    "I ended up spending the entire day with him."

    return

# Park, Day 05
label .day05:

    # TODO: [Change scene to FLOWER SHOP]
    scene bg flower

    "A few days later. "
    "Ernest brings me to the flower shop again. "
    "He seems to like annoying Julius a lot. But I don't think Julius seems to mind, considering how Julius seems used to whatever Ernest pulls. "

    ern "Julius! I'm here again! And with Lyra!"

    "Ernest opens the door of the flower shop and shouts inside. "

    jul "Welcome back."
    lyr "Welcome back?"
    jul "Ernest was here this morning."

    "Julius smiles at me."

    jul "Oh right. You know of Ewan right?"
    lyr "Ewan? Yeah I do."

    "Julius steps to the back, and comes out with some flowers. "

    jul "Pass these to Ewan next time you see him. Tell them they're from me."
    lyr "Huh..? Sure."
    ern "Ewan? Whose that?"
    lyr "Oh! He's one of my friends. Uhm, you remember Leo right? Ewan is with him today."
    ern "Julius! You didn't tell me you had other friends than me!"

    "Julius laughs. "

    jul "We're not friends. More like 'partners'? Or would 'partners in crime' be better?"
    lyr "I'm not sure if I want to know what that means."

    "We chat with Julius for a bit before leaving. Ernest drags me out of the flower shop, and I weakly wave goodbye to Julius as we head out the door. "
    "Now that I think about it, I've been spending a lot of time with Ernest recently haven't I?"
    "Well that can't be helped, since he always seems to invite me out whenever I see him around town."

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "Ernest and I head out from the flower shop. I was still holding onto the bunches of flowers Julius had told me to give to Ewan. I didn't know what kind of flowers they were, and Julius didn't tell me either. "
    "I look up, and I just happen to see the person in question: Ewan was standing with Leo, a bit off in the distance. "
    "I tug Ernest's sleeve. "

    lyr "Over there, that's Ewan."

    "Ernest squints. "

    ern "Oh! The purple haired person standing next to Leo?"
    lyr "Mhmm!"
    lyr "Leo! Ewan!"

    "I call out to Leo and Ewan. They take notice of me, and I hurry over with Ernest. "

    ewa "Lyra. I haven't seen you in a while. Are you doing fine?"
    leo "You have flowers?"
    lyr "Mhmm! Uhm, Julius says it's for you, Ewan."

    "I smile and hand over the flowers to Ewan. Ewan accepts it, but narrows his eyes. "

    ewa "Julius...?"

    "Ewan looks at the flowers. He smiles, but I don't sense something pleasant at all?!"
    "Before I could analyze what Ewan was possibly thinking, he gave me his usual kind smile."

    ewa "Thank you."

    "Ewan takes notice of Ernest. "

    ewa "Oh. You must be Ernest. Leo told me about you."
    ern "A-ah. Yeah. I heard Lyra and Julius talk about you earlier. It's finally nice to meet you."
    ewa "You've been hanging out with Lyra recently right? Thank you for taking care of her. Leo's always worried that she's causing trouble for the people around her."
    lyr "I'm not causing trouble this time! Leo!"
    leo "Uh-huh. Right."

    "I hit Leo's arm lightly. "
    "When I turn back to Ernest, I notice him staring at me. "

    lyr "Ernest? Are you okay?"

    "Ernest snaps out of it. "

    ern "I-i'm fine!"

    "Ernest looks around a bit. "

    ern "Ah! I have to do something now! I'll see you later!"

    "Before any of us could reply, Ernest runs off back in the direction of the flower shop. "
    "Is he really alright...?"

    lyr "I wonder if he's okay..."

    "Leo sighs, and Ewan laughs nervously. "

    leo "Maybe you should be more aware of your surroundings."
    lyr "What's that supposed to mean?!"
    ewa "Ahaha..."
    lyr "(I was supposed to hang out with Ernest but he just ran off all of sudden like that.)"
    lyr "What are you two doing today? Ernest said he'd take me somewhere but he ran off earlier."
    leo "Well he ran off for sure... this is a hopeless case for him."
    ewa "We were just going to walk around the marketplace again. Would you like to come?"
    lyr "Mhmm!"

    "I spent the rest of the day with Leo and Ewan, while wondering why Ernest had run off earlier. He was giving me a weird look too..."

    return

# Park, Day 06
label .day06:

    # TODO: [Change scene to PARK]
    scene bg park

    "A few days later."
    "I had come to the park to walk around. When Leo had asked me where I was going, I said I was going to clear my head. "
    "I hadn't seen Ernest in a few days. I was so used to him dragging me around in recent times, it felt kind of strange having free time of my own. "

    lyr "(Now that I think about it, didn't I first meet Ernest here?) "

    "I laugh about the thought. As I was strolling around, I notice someone. "

    lyr "(Hm? That red hair...)"

    "It was Ernest. "
    "He seemed to be sitting on the bench, lamenting about something. "
    "I watch for a bit. Maybe I should go over and greet him? "
    "I walk over to the bench where he was sitting and call out to him."

    lyr "Ernest?"
    ern "Gah! L-Lyra? What are you doing here?"
    lyr "I haven't seen you around recently, so I was worried..."
    lyr "Is something wrong?"
    ern "N-no! Nothing at all."

    "Ernest goes quiet. It felt strange. "
    "I go sit next to him. "

    lyr "Uhm, did I do something wrong? If I did then-"
    ern "You didn't! It's just..."
    lyr "????"
    ern "The other day, I heard some people talking about how magicians are bad, and useless, and a threat to society. I couldn't turn a blind eye to that, especially since I know personally that magicians aren't bad!"
    ern "So I got into an argument with them. What made me really frustrated was how no one would even try to understand me when I said that I knew magicians weren't bad people! I could even show them!"

    "At this point, Ernest got really heated up and started talking loudly. "
    "Some people turned around to look at us, and I saw them making suspicious glances while whispering.  "

    lyr "(This guy...) "

    # DECISION 2:
    # → Hit him (+1 good end point)
    # → Hug him (no increase in good end point)

    menu:
        "Hit him.":
            # +1 affection
            $ affection += 1
            call .day06_good

        "Hug him.":
            # +0 affection
            $ affection = affection
            call .day06_bad

    return

# Park, Day 06 (Good)
label .day06_good:

    # TODO: [Change scene to PARK]
    scene bg park

    "I'm sure Ernest had good intentions towards us magicians. "
    "I'm absolutely sure. "
    "But his naiveness in the end of only going to cause trouble and pain for me--no, every magician that possibly lived in Veritas. "
    "I try to give him a wake up call. So I slapped him. "
    "It wasn't my proudest moment, but I had to get my point across!"

    "Ernest was surprised at my action."

    ern "Wha..."
    lyr "I'm sure you have good intentions, but..."
    lyr "You shouldn't speak for every magician like that."
    lyr "Especially if you don't know what it's like, personally."

    "Ernest seemed a bit shell shocked at what I did, that he might not have been able to process my words. He could only weakly reply back. "

    ern "R-right. Sorry."

    "I glance around. I hope people don't think this is a lovers quarrel or something. "
    "I started to feel bad for hitting him. "

    lyr "No, I'm also sorry. For hitting you suddenly like that."
    lyr "It's just if you kept talking, everyone would've gotten the wrong idea."
    lyr "If my identity was found out, then I'd be in danger."
    ern "..."
    ern "Sorry, I wasn't thinking about that earlier..."

    "Ernest looks a bit disheartened. "

    lyr "(Now I feel really bad for scolding him.)"
    lyr "(But... it was necessary.)"

    "We sit in silence for a while, before Ernest gets up. "

    ern "How about we head back to town? Since it's been a while since we've hung out. "
    lyr "It's only been a few days though..."
    lyr "But sure!"

    "We walk back to the town plaza together."

    return

# Park, Day 06 (Bad)
label .day06_bad:

    # TODO: [Change scene to PARK]
    scene bg park

    "I had to make him stop talking before people started getting suspicious."
    "But he seemed in pain, thinking about the sake of us magicians, I felt a bit bad. "
    "I was touched, but also it's not a topic you should deluge into in public. "
    "So I suddenly hugged him. "

    ern "W-wha?! Lyra?!!"
    lyr "That's enough."
    lyr "(If you care about us magicians so much then...)"
    lyr "You're a good person, Ernest."
    ern "H-huh? Yeah..."

    "I didn't know what to say to him. "
    "When I let go of him, Ernest seemed to be a bit flustered from when I suddenly gave him a hug."

    lyr "Uhm. I'm sorry about that, suddenly--"
    ern "N-no! It's fine! Really!"

    "Ernest averts his eyes, and he suddenly stands up. "

    ern "Let's head back to the town!"
    lyr "Hm? Sure."

    "Ernest hurries ahead, and I run after him."

    return

# Park, Day 07
label .day07:

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "As Ernest and I were walking back, a question appeared in my mind. "

    lyr "Oh yeah. The other day, why did you run off?"
    ern "The other day...? Oh!"

    "Ernest averts his eyes from me."

    ern "Uhh. That's a secret."
    lyr "Huh. I see."
    lyr "(Well if he doesn't want to tell me, that's fine.) "

    "Ernest stops all of a sudden, and he peers through one of the alleyways. "

    ern "...!"

    "Ernest grabs my hand, and run into the alleyway."

    lyr "E-Ernest?!"

    # TODO: [Change scene to ALLEYWAY]
    scene bg alley

    "Upon entering the alleyway, I spot an injured person. They were laying on the floor, and I could easily tell they seemed really badly injured. "

    ern "Lyra! There's an injured person here! We have to help them!"
    lyr "They look like they've lost a lot of blood... how can I..."
    ern "Magic! Use your magic! If you heal then, then maybe then everyone will recognize how great magicians are...!"
    lyr "But I..."

    "I hesitate."

    lyr "I don't think this is-"
    ern "Please! They might actually die, unless we do something!"

    "Seeing a person die in front of you can be pretty traumatic. I reluctantly put my hands on the body of the injured person and began to heal them."
    "Almost in an instant, the injured person was no longer injured, as if their wounds were never there in the first place. "

    per "Huh...?"

    "The person looked surprised when they saw all their injuries had disappeared. They stared at me straight in the eyes. Their hands are shaking."

    per "Y-you.... Healed me...? With magic?"
    per "So you're... a magician..?"
    lyr "..."

    "I divert my eyes. I knew what was coming next. Even though it was never directed at me straight before, I knew I could never be ready for it."

    per "You're a magician.... You monster! What did you do to me?!"
    ern "Huh?!"

    "Ernest wasn't expecting that kind of reaction from someone who had just been saved, so he stood there in shock. "
    "I had to get out of here. My body moved on instinct, and I bolted out of the alleyway. "

    # TODO: [Change scene to OUTSIDE LEO AND LYRA'S HOUSE]
    scene bg house outside

    "I had ran all the way home. When I reached the entrance, I didn't realize how hard I was panting."

    leo "Lyra?!"
    leo "What happened?! Are you alright? You're crying..."
    lyr "Leo..."

    "I touch my face. Ah, he was right, I am crying. "

    lyr "(Aah. This is pathetic.)"

    "Leo grabs my hand, and pushes me inside the house. I have to explain to him what happened..."

    return

# Park, Day 08
label .day08:

    # TODO: [Change scene to INSIDE LEO AND LYRA'S HOUSE (DAY)]
    scene bg house inside

    "A week had passed since that incident. I didn't know what to do."

    leo "This is bad... you know that person you said you healed?"
    lyr "Yeah...?"
    leo "Apparently there are rumours that they mysteriously passed away..."
    leo "I don't know how true it is, since I have no way of confirming it myself."
    leo "People have also said it was a magician behind it, so everyone is being more cautious now."

    "Leo stares at me. "

    lyr "So what if I did cause their death...?"
    leo "That's not possible. You healed their injuries right?"
    lyr "Yeah..."

    "Leo puts out his hand. "

    leo "Use the same healing magic on me that you used on that person."
    lyr "Huh? Sure..."
    leo "You can check up on me in a few days. I won't be dead."
    lyr "..."
    leo "What?"
    lyr "Is this your way of reassuring me?"
    leo "If I had just told you it isn't your fault, you wouldn't believe me."

    "There's a knocking sound from the front door. "

    leo "Oh, that's probably Ewan. He wanted to come to see if you were okay."
    lyr "Ah..."

    "Leo opens the door, and I peer over his shoulder to see Ewan. "

    # TODO: [Change scene to OUTSIDE LEO AND LYRA'S HOUSE (DAY)]
    scene bg house outside

    ewa "I heard from Leo you weren't feeling well all week. Are you okay?"
    lyr "Ah, I wish I can say I am now... it might've gotten worse."

    "Ewan gives me a worried look. "

    lyr "Sorry for worrying you."
    ewa "It's fine, you didn't do anything wrong. I was worried because there were rumours going around about Ernest."
    lyr "Leo told me that apparently someone disappeared? Or mysteriously died all of a sudden..."
    ewa "Someone... mysteriously disappeared?"

    "Ewan makes a really serious face upon hearing what I said. Leo looks confused. It wasn't a face that Ewan had usually wore. When Ewan had noticed us looking at him, concerned, he smiled reassuringly. "

    ewa "What do you plan on doing today? I heard you stayed home all week. If you don't want to go out, I'll just head out with Leo again today."

    "I ponder what I wanted to do. I had stayed home for the entire week following that incident."

    lyr "(What should I...?)"

    "I couldn't keep moping around like this. There was one place I had to go. "

    lyr "No I... There's somewhere I have to go today."
    leo "Do you want us to come with you?"
    lyr "I can go alone, it's fine. Keep Ewan company."

    "I wave goodbye to Leo and Ewan, and head out."
    "If there's one place Ernest could be it's there right?"
    "I couldn't keep avoiding him forever."

    # TODO: [Change scene to FLOWER SHOP]
    scene bg flower

    "I rush in and push open the door of the flower shop. I had ended up running to the flower shop before I could stop myself."
    "I looked around and saw no one at first, but then I heard Julius' voice. "

    jul "Ernest? You're back again? We've talked about this befo-"

    "Julius appeared and realized that I am not Ernest."
    "He laughs."

    jul "Oh,I apologize. I thought you were Ernest."
    lyr "N-no, it's fine. Sorry for coming suddenly."
    jul "No need. You and Ernest have been hanging around each other so much recently, you've picked up some of his habits."
    lyr "Huh?"
    jul "The only person who'd haphazardly run in and open the door to the shop without a care like that is Ernest. Most customers usually worry about slamming the door into something, wouldn't they?"
    lyr "Oh! Uhm- I didn't mean to-"

    "He was talking about how I suddenly swung open the door. I felt embarrassed. "

    lyr "Ah! You mentioned Ernest right? Was he here earlier?"
    jul "Are you looking for him?"
    lyr "..."
    jul "..."
    jul "He's been coming around more often, looking like a sad lost puppy."
    jul "... but not the kind I like to tease."
    jul "It's usually not like him to be down for this long."
    lyr "I, I see..."
    jul "You were involved right? That incident that Ernest got himself into."
    lyr "...!"
    lyr "Is it that obvious?"
    jul "Well, you seem to have an huge effect on how Ernest acts these days."
    lyr "I..."
    lyr "(I can't deny that.)"

    "I've already noticed that, but I pretended not to. "

    jul "That incident, you used magic right?"
    lyr "Yeah."
    lyr "(Of course Julius would figure it out, he is also a magician that knows what Ernest is like.)"
    jul "Then back during the incident, what did you think about Ernest?"
    lyr "What I thought..?"

    # DECISION 3:
    # → "Naive" (+1 good end point)
    # → "Well-intentioned" (no increase in good end point)

    menu:
        "Naive.":
            # +1 affection
            $ affection += 1
            call .day08_good

        "Well-intentioned.":
            # +0 affection
            $ affection = affection
            call .day08_bad

    return

# Park, Day 08 (Good)
label .day08_good:

    lyr "I think... Ernest is naive."
    jul "Naive?"
    lyr "You and I have constantly told Ernest that it's not good to talk about magicians when he's not one himself right?"
    lyr "I don't think he means any harm, but he's blindly following his own ideal when he's not actually seeing the whole picture."
    lyr "So that's why I think... he's naive."
    jul "I thought so as well. I'm glad you can see his faults and aren't blinded by his good intentions."
    jul "He's the type that blindly follows his heart and don't realize what he's done wrong until someone gets hurt."
    lyr "Ah. So he doesn't realize his actions have consequences."
    jul "That's a harsh way to put it, but yes."
    jul "But the fact that you're able to see this, and able to criticize him, is why I think you two are a good match."

    return

# Park, Day 08 (Bad)
label .day08_bad:

    lyr "He... has good intentions. I think."
    jul "You can speak honestly, but if that's really what you think..."
    lyr "???"
    jul "No nevermind. It's nothing. I wouldn't be able to support him like that the way you do."

    "He laughs then looked at me with a somewhat sad smile. It kind of reminded me of Ewan's... "
    "Maybe they're closer than I had thought. "

    jul "Being supportive can only take someone so far sometimes but if that's the path you chose then I won't tell you otherwise."

    return

# Park, Day 09
label .day09:

    jul "But... despite everything that's happened, please take care of him."
    jul "He's been coming around to ask about you, you know?"

    "It was unlike Julius to look like this, it made me feel kind of uneasy. I try to give him a reassuring smile."

    lyr "Yeah. I'll do my best."
    jul "Ernest has told you right? We've known each other for a while."
    lyr "He mentioned it, but I didn't feel like it was right to be prying."
    jul "Well I refused to get close to anyone because I'm a magician. But Ernest, no matter how hard I tried to push him away, he'd bounce back up like it didn't matter."
    jul "He might be stupidly straightforward but.... It's that trait about him that is able to reach out to others."
    jul "Meeting him was probably one of the more positive points in my life."

    "I laugh."

    lyr "You know, even though you tease him all the time, you're surprisingly soft on him."
    jul "It can't be helped right? We all have people who are special to us."
    jul "It's the same for 'him' too."
    jul "But I can't change what you want to do. That's for you to decide on your own. But I hope you and Ernest can get along again soon."

    "Julius coughs."

    jul "After all I'm not the type to kick a puppy while it's down."
    lyr "Aha."

    "He seems to have changed back to his usual persona now. "

    lyr "Julius?"
    jul "Yes?"
    lyr "Thank you."

    "I give him a smile and wave."

    lyr "I'll take my leave now, but seriously... thanks."

    "Julius laughs, and waves back at me."

    jul "Yeah. Take care."

    # TODO: [Change scene to TOWN PLAZA (DAY)]
    scene bg plaza day

    "I had decided to go look for Ernest after leaving the flower shop."

    lyr "(After all, that's the only proper thing to do after talking with Julius, right?)"

    "I ran around the town plaza and marketplace. While running around, there were some fireflies around. "

    lyr "Hm? Fireflies out in the daytime? That's strange..."

    "I notice that the fireflies were gathered in certain locations, but then kept moving along to elsewhere. "

    lyr "(This isn't the time to be focused on the fireflies!)"

    "I run around a bit more, but I still couldn't find Ernest at all."

    lyr "Maybe I should head home and ask Leo for help..."

    # TODO: [Change scene to INSIDE LEO AND LYRA'S HOUSE]
    scene bg house outside

    "I open the door and was about to look for Leo, when I see Ernest sitting at the table with Leo. "

    leo "Oh. Welcome back Lyra."
    lyr "Y-yeah. Uhm."

    "I make eye contact with Ernest, but look away immediately. "

    leo "Are you wondering why Ernest is here?"
    lyr "Y...yeah."
    leo "Well..."

    return
