# works but could be made to follow DRY a bit better.

import random

def generate_lore() -> tuple[str, int, list[str]]:
    """
    Generates the first half of the lore string.
    """
    lore: str = ""
    personality_cat: list = []
    secondary_option: int = random.randint(1, 5)
    choose_option: int = random.randint(1, 12)
    match choose_option:
        case 1:
            lore += "they lost their village "
            personality_cat = ["traumatized", "emotionless", "depressed"]
            match secondary_option:
                case 1:
                    lore += "to a fire"
                case 2:
                    lore += "to a natural disaster"
                case 3:
                    lore += f"to {random.choice(["a dragon", "a tarrasque", "a wyrm", "a wyvern", "a bandit raid", "a lich", "war", "a plague"])}"
                case 4:
                    lore += "long ago"
                case 5:
                    lore += "in a great tragedy"
        case 2:
            lore += "they are known "
            personality_cat = ["smug", "self concious", "annoying"]
            match secondary_option:
                case 1:
                    lore += f"for committing {random.choice(["arson", "theft", "murder", "robbery", "burglary", "a series of serious crimes"])}"
                case 2:
                    lore += "for reasons few can clearly explain"
                case 3:
                    lore += f"for {random.choice(["their presence", "their voice", "their kindness", "their blunt manner", "protecting the innocent", "their remarkable agility", "their sharp wit", "their exceptional skill in their chosen craft"])}"
                case 4:
                    lore += f"to {random.choice(["lose their temper without warning", "help others", "deceive others for personal gain", "display remarkable physical agility", "defuse tense situations", "act with reckless energy", "use humor at inappropriate moments", "speak confidently on matters they poorly understand"])}"
                case 5:
                    lore += "throughout the local community"
        case 3:
            lore += "they secretly "
            personality_cat = ["helpful", "shy", "secretive"]
            match secondary_option:
                case 1:
                    lore += "help others"
                case 2:
                    lore += "are trying to escape their past"
                case 3:
                    lore += f"love {random.choice(["their own company", "hobgoblins", "taking advantage of the vulnerable", "avoiding responsibility", "helping others", "wandering in solitude"])}"
                case 4:
                    lore += f"hate {random.choice(["themselves", "hobgoblins", "those they consider outsiders", "the circumstances they live under", "helping others", "a party member"])}"
                case 5:
                    lore += "harbor feelings for a member of the party"
        case 4:
            lore += "they are on a quest "
            personality_cat = ["devoted", "happy", "determined"]
            match secondary_option:
                case 1:
                    lore += "for vengeance"
                case 2:
                    lore += "for redemption"
                case 3:
                    lore += f"to find {random.choice(["themselves", "their greatest rival", "a lost lover", "a missing child", "a lost companion", "salvation", "a purpose", "solitude"])}"
                case 4:
                    lore += "to revive a long-lost relative"
                case 5:
                    lore += f"to regain their {random.choice(["honor", "memory", "wisdom", "love"])}"
        case 5:
            lore += "they believe "
            personality_cat = ["gullible", "determined", "passive"]
            match secondary_option:
                case 1:
                    lore += "that their life has little worth unless they accomplish something significant"
                case 2:
                    lore += "that the gods guide mortal lives"
                case 3:
                    lore += f"that they {random.choice(["can change the world", "can overcome any obstacle", "are destined to change the world", "have an important role to play", "are incapable of making a difference", "understand more than others give them credit for"])}"
                case 4:
                    lore += "that no one can truly be trusted"
                case 5:
                    lore += "that the party ultimately intends them harm"
        case 6:
            lore += "they "
            personality_cat = ["arrogant", "smug", "suspicious"]
            match secondary_option:
                case 1:
                    lore += "often act in ways that invite suspicion"
                case 2:
                    lore += "know very little about the wider world"
                case 3:
                    lore += f"believe that they are {random.choice(["more important than those around them", "useless", "beyond redemption"])}"
                case 4:
                    lore += "habitually leave their responsibilities to others"
                case 5:
                    lore += "place little value on the opinions of others"
        case 7:
            lore += "they are hiding " 
            personality_cat = ["secretive", "depressed", "traumatized"]
            match secondary_option:
                case 1:
                    lore += "who " + random.choice(["they really are", "they once were", "they are trying to become"])
                case 2:
                    lore += "what " + random.choice(["they have done", "was done to them", "shaped them into who they are now"])
                case 3:
                    lore += "something from " + random.choice(["their past", "everyone around them", "their loved ones", "the party"])
                case 4:
                    lore += "from " + random.choice(["a looming threat", "someone pursuing them", "their past"])
                case 5:
                    lore += "the extent of their trauma"
        case 8:
            lore += "they hope "
            personality_cat = ["hopeful", "optimistic", "motivated"]
            match secondary_option:
                case 1:
                    lore += "to change the world"
                case 2:
                    lore += "to accomplish something of lasting importance"
                case 3:
                    lore += f"to escape {random.choice(["their past", "the consequences of their actions", "this world"])}"
                case 4:
                    lore += f"to become {random.choice(["immortal", "powerful", "influential", "respected", "feared", "loved"])}"
                case 5:
                    lore += f"to find {random.choice(["a lasting love", "a lost family member", "their purpose"])}"
        case 9:
            lore += "they recently lost "
            personality_cat = ["depressed", "traumatized", "emotional"]
            match secondary_option:
                case 1:
                    lore += f"a {random.choice(["close friend", "family member", "parent", "lover", "pet"])}"
                case 2:
                    lore += f"a treasured {random.choice(["pickaxe", "hammer", "spear", "sword", "rapier", "shield", "axe", "heirloom"])}"
                case 3:
                    lore += "something of great personal value"
                case 4:
                    lore += f"their {random.choice(["way of life", "beliefs", "will to live", "hope", "aspirations"])}"
                case 5:
                    lore += "their true love"
        case 10:
            lore += "they keep having "
            personality_cat = ["paranoid", "fearful", "hopeful"]
            match secondary_option:
                case 1:
                    lore += f"nightmares about {random.choice(["a great tragedy", "darkness", "a plague", "lost love", "death", "the end of the world"])}"
                case 2:
                    lore += f"dreams about {random.choice(["someone they love", "darkness", "a distant light", "a happier life", "a lost family member", "the gods", "a life of wealth"])}"
                case 3:
                    lore += f"thoughts about {random.choice(["ending their own life", "abandoning everything and fleeing", "pursuing an impossible ambition", "revealing feelings they have kept hidden", "something beyond mortal understanding"])}"
                case 4:
                    lore += f"dreams from the perspective of {random.choice(["a deity", "a wild animal", "an unknown person", "a member of the party"])}"
                case 5:
                    lore += "recurring episodes of breathlessness"
        case 11:
            lore += "they dislike "
            personality_cat = ["lonely", "arrogant", "psychopathic"]
            match secondary_option:
                case 1:
                    lore += f"a {random.choice(["local blacksmith", "member of the party", "local merchant", "local ruler", "one of their parents"])} due to {random.choice(["a minor disagreement", "a conflict of interest", "a conflict of beliefs", "a perceived slight", "a tragedy"])}"
                case 2:
                    lore += "warlocks"
                case 3:
                    lore += f"talking to the party due to {random.choice(["their attitude", "a difference in beliefs", "a minor disagreement"])}"
                case 4:
                    lore += "their job"
                case 5:
                    lore += "other people"
        case 12:
            lore += f"they {random.choice(["recently ", ""])}heard a rumor "
            personality_cat = ["gullible", "hateful", "greedy"]
            match secondary_option:
                case 1:
                    lore += f"that {random.choice(["dragons", "wizards", "dragonborn", "spellcasters", "the party"])} are {random.choice(["murderers", "criminals", "cultists", "dangerous", "untrustworthy"])}"
                case 2:
                    lore += "everything they care for has been destroyed"
                case 3:
                    lore += f"about {random.choice(["a monster's", "a king's", "a deity's", "a party member's", "the party's"])} {random.choice(["greed", "past", "crimes", "curse", "hatred"])}"
                case 4:
                    lore += "about the party"
                case 5:
                    lore += f"of {random.choice(["a legendary treasure", "a terrible curse", "an ancient spell", f"a powerful {random.choice(['warlock', 'wizard', 'sorcerer', 'paladin', 'warrior'])}"])}"
        
    return lore, choose_option - 1, personality_cat
    
def generate_lore_2(lore_cat: int) -> str:
    """
    Generates the second half of the lore string, 
    based on the lore_cat variable set in generate_lore().
    """
    lore: str = ""
    secondary_option: int = random.randint(1, 2)
    tertiary_option: int = random.randint(1, 5)
    if secondary_option == 1:
        lore += "and "
    else:
        lore += "but "

        #beware of the evil and intimidating lore cat! /j
    
    match lore_cat:
        case 0: #"they lost their village"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "they have sworn to rebuild what was lost"
                        case 2:
                            lore += "they survived only by fleeing"
                        case 3:
                            lore += "their entire family was lost with it"
                        case 4:
                            lore += "they continue to mourn what was lost"
                        case 5:
                            lore += "they have sworn never to forget what happened"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they were absent when the disaster occurred"
                        case 2:
                            lore += "they managed to save nearly everyone"
                        case 3:
                            lore += "they had already grown bitter toward the place"
                        case 4:
                            lore += "they may have played a part in its destruction"
                        case 5:
                            lore += "the event lies far in their past"
        case 1: #"they are known"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have earned that reputation through their actions"
                        case 2:
                            lore += "remain unaware of how others speak of them"
                        case 3:
                            lore += "are actively trying to change that reputation"
                        case 4:
                            lore += "do not understand how the reputation began"
                        case 5:
                            lore += "consider that reputation their greatest achievement"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "the reputation does not reflect who they truly are"
                        case 2:
                            lore += "cannot understand why others see them that way"
                        case 3:
                            lore += "resent the reputation they have acquired"
                        case 4:
                            lore += "may be the only person who believes they are known for it"
                        case 5:
                            lore += "the claim is entirely false"
        case 2: #"they secretly"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have no intention of revealing it to anyone"
                        case 2:
                            lore += f"are hiding it {random.choice(['convincingly', 'exceptionally well', 'poorly'])}"
                        case 3:
                            lore += "hope no one discovers the truth"
                        case 4:
                            lore += "intend to keep it hidden for as long as possible"
                        case 5:
                            lore += "they deeply resent this part of themselves"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "are remarkably poor at concealing it"
                        case 2:
                            lore += "struggle to keep anything hidden for long"
                        case 3:
                            lore += "do not realize how obvious it has become"
                        case 4:
                            lore += "are becoming increasingly desperate to conceal it"
                        case 5:
                            lore += "are rarely believed when they attempt to reveal the truth"
        case 3: #"they are on a quest"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have recently made significant progress"
                        case 2:
                            lore += "refuse to abandon the quest regardless of the obstacles before them"
                        case 3:
                            lore += "have only recently begun their journey"
                        case 4:
                            lore += "only recently began to believe success was possible"
                        case 5:
                            lore += "have devoted themselves fully to the task"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "have recently suffered a major setback"
                        case 2:
                            lore += "other obligations have repeatedly drawn them away from it"
                        case 3:
                            lore += "abandoned the quest long ago"
                        case 4:
                            lore += "have already failed once before"
                        case 5:
                            lore += "see little chance of ever succeeding"
        case 4: #"they believe"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "stand firmly by this belief"
                        case 2:
                            lore += "refuse to let anyone persuade them otherwise"
                        case 3:
                            lore += "will challenge anyone whose worldview conflicts with their own"
                        case 4:
                            lore += "readily share this belief with others"
                        case 5:
                            lore += "attempt to apply this belief to every part of their life"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "remain willing to consider a different worldview"
                        case 2:
                            lore += "this is merely what they allow others to believe"
                        case 3:
                            lore += "hold this belief largely because of tradition"
                        case 4:
                            lore += "prefer to keep this belief private"
                        case 5:
                            lore += "believe that the world holds truths beyond this conviction"
        case 5: #"they"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "the reason for this remains unclear"
                        case 2:
                            lore += f"this is due to a {random.choice(['recent', 'long-standing', 'unexplained'])} condition"
                        case 3:
                            lore += "make little effort to hide it from others"
                        case 4:
                            lore += "refuse to alter their behavior"
                        case 5:
                            lore += "do not believe others have noticed"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "their behavior is already widely known"
                        case 2:
                            lore += "few people believe this is actually true"
                        case 3:
                            lore += "they consider the matter unimportant"
                        case 4:
                            lore += "others seem largely unaware of it"
                        case 5:
                            lore += "their claim is clearly untrue"
        case 6: #"they are hiding"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have no intention of revealing it to anyone"
                        case 2:
                            lore += f"are hiding it {random.choice(['convincingly', 'exceptionally well', 'poorly'])}"
                        case 3:
                            lore += "hope no one discovers the truth"
                        case 4:
                            lore += "intend to keep it hidden for as long as possible"
                        case 5:
                            lore += "they deeply resent this part of themselves"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "are remarkably poor at concealing it"
                        case 2:
                            lore += "struggle to keep anything hidden for long"
                        case 3:
                            lore += "do not realize how obvious it has become"
                        case 4:
                            lore += "are becoming increasingly desperate to conceal it"
                        case 5:
                            lore += "are rarely believed when they attempt to reveal the truth"
        case 7: #"they hope"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "believe nothing will prevent them from succeeding"
                        case 2:
                            lore += "work toward it with relentless determination"
                        case 3:
                            lore += "remain convinced that success is possible"
                        case 4:
                            lore += "are unwavering in their determination to achieve it"
                        case 5:
                            lore += "possess the means necessary to pursue it"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "privately fear that it will never happen"
                        case 2:
                            lore += "have found every path toward it blocked"
                        case 3:
                            lore += f"nobody {random.choice(["believes they can succeed", "is willing to support them"])}"
                        case 4:
                            lore += "someone is actively working to stop them"
                        case 5:
                            lore += "have endured one setback after another"
        case 8: #"they recently lost"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "they continue to mourn the loss"
                        case 2:
                            lore += "they bear responsibility for what was lost"
                        case 3:
                            lore += "they hold themselves entirely responsible"
                        case 4:
                            lore += "they place the blame on everyone but themselves"
                        case 5:
                            lore += "would do almost anything to undo the loss"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they refuse to confront what happened"
                        case 2:
                            lore += "have never allowed themselves the chance to mourn"
                        case 3:
                            lore += "they have not yet learned of the loss"
                        case 4:
                            lore += "have told no one about what happened"
                        case 5:
                            lore += "part of them had wanted this outcome"
        case 9: #"they keep having"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "are increasingly concerned by these experiences"
                        case 2:
                            lore += "feel compelled to confide in someone"
                        case 3:
                            lore += "find themselves returning to the subject repeatedly"
                        case 4:
                            lore += "are attempting to conceal it from others"
                        case 5:
                            lore += "are deeply disturbed by it"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "forget the details soon afterward"
                        case 2:
                            lore += "do not consider it significant"
                        case 3:
                            lore += "have not told anyone"
                        case 4:
                            lore += "have come to regard it as normal"
                        case 5:
                            lore += "are determined to keep it from everyone"
        case 10: #"they dislike"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "the hostility has become a burden for everyone involved"
                        case 2:
                            lore += "refuse to offer any apology"
                        case 3:
                            lore += "their own actions are largely responsible for the conflict"
                        case 4:
                            lore += "the conflict has severely damaged their life"
                        case 5:
                            lore += f"this has made them {random.choice(['notorious', 'well known'])}"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "few others consider the matter important"
                        case 2:
                            lore += "they rarely act on their dislike"
                        case 3:
                            lore += "keep their feelings entirely private"
                        case 4:
                            lore += "their feelings may still change"
                        case 5:
                            lore += "the dislike is rooted in a deeper history"
        case 11: #"they (recently) heard a rumor"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have begun allowing the rumor to shape their worldview"
                        case 2:
                            lore += "are completely convinced that it is true"
                        case 3:
                            lore += "repeat the rumor to anyone willing to listen"
                        case 4:
                            lore += "have become fixated on discussing it"
                        case 5:
                            lore += "accepted it without seriously questioning its source"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "dismissed it as unreliable"
                        case 2:
                            lore += "were secretly responsible for starting the rumor"
                        case 3:
                            lore += "can no longer recall the rumor accurately"
                        case 4:
                            lore += "resent the rumor and the attention it has drawn"
                        case 5:
                            lore += "suspect that only part of it may be true"

    return lore

def generate_rep() -> tuple[str, list[str]]:
    """
    Generates the NPC's reputation.
    """
    rep: str = ""
    personality_cat: list = []
    secondary_option: int = random.randint(1, 5)
    choose_option: int = random.randint(1, 12)

    match choose_option:
        case 1:
            rep += "they often "
            personality_cat = ["fearful", "disloyal", "distracted"]
            match secondary_option:
                case 1:
                    rep += "give conflicting accounts of " + random.choice(["their past", "their involvement in local events", "people they once knew"])
                case 2:
                    rep += "leave their responsibilities unfinished"
                case 3:
                    rep += "become distracted during important conversations"
                case 4:
                    rep += "speak " + random.choice(["critically of those around them", "favorably of people they barely know", "harshly when frustrated"])
                case 5:
                    rep += "look over their shoulder as though expecting to be followed"

        case 2:
            rep += "they are "
            personality_cat = ["secretive", "emotional", "depressed"]
            match secondary_option:
                case 1:
                    rep += "widely regarded as " + random.choice(["kind", "supportive", "abrasive", "unpleasant"])
                case 2:
                    rep += "believed to be hiding something from their past"
                case 3:
                    rep += "not considered trustworthy by those who know them"
                case 4:
                    rep += "regarded as a traitor by former allies"
                case 5:
                    rep += "known throughout the local area as " + random.choice(["a controversial figure", "someone with a troubled past", "someone best avoided"])

        case 3:
            rep += "they cannot "
            personality_cat = ["unconfident", "anxious", "lonely"]
            match secondary_option:
                case 1:
                    rep += "remember " + random.choice(["much of their past", "where they originally came from", "an important period of their life"])
                case 2:
                    rep += "help but feel remorse for their past actions"
                case 3:
                    rep += "properly perform " + random.choice(["their usual duties", "a particular craft", "a task they are frequently expected to handle"])
                case 4:
                    rep += "maintain many close friendships"
                case 5:
                    rep += "keep a secret for very long"

        case 4:
            rep += "they refuse "
            personality_cat = ["arrogant", "selfish", "lazy"]
            match secondary_option:
                case 1:
                    rep += "to speak with " + random.choice(["adventurers", "warlocks", "local officials", "outsiders"])
                case 2:
                    rep += "to admit when they are at fault"
                case 3:
                    rep += "to let anybody get close to them"
                case 4:
                    rep += "to maintain unnecessary social ties"
                case 5:
                    rep += "to help " + random.choice(["those they dislike", "anyone who has wronged them", "strangers without compensation"])

        case 5:
            rep += "they have "
            personality_cat = ["traumatized", "regretful", "brave"]
            match secondary_option:
                case 1:
                    rep += "fought " + random.choice(["in a major war", "in a long-running local conflict", "during the defense of their home"])
                case 2:
                    rep += "done something in their past that they deeply regret"
                case 3:
                    rep += "no desire to return to their former life"
                case 4:
                    rep += "a great deal of unresolved guilt"
                case 5:
                    rep += "lost " + random.choice(["their closest friend", "their lover", "a family member", "someone they depended upon"])

        case 6:
            rep += "they once tried to "
            personality_cat = ["aggressive", "depressed", "paranoid"]
            match secondary_option:
                case 1:
                    rep += "abandon their former life entirely"
                case 2:
                    rep += "save " + random.choice(["their family", "their lover", "a friend", "a stranger"]) + " from a disaster, but failed"
                case 3:
                    rep += "take revenge on someone they blamed for their problems"
                case 4:
                    rep += "join " + random.choice(["a cult", "a criminal organization", "a forbidden order"])
                case 5:
                    rep += "cause a major local tragedy"

        case 7:
            rep += "they are known to "
            personality_cat = ["determined", "kind", "empathetic"]
            match secondary_option:
                case 1:
                    rep += "be an accomplished " + random.choice(["cook", "artist", "baker", "musician", "craftsperson"])
                case 2:
                    rep += "help those in need"
                case 3:
                    rep += "defend " + random.choice(["those they care for", "their community", "the sick and injured"])
                case 4:
                    rep += "support others during difficult circumstances"
                case 5:
                    rep += "honor their commitments even when doing so is difficult"

        case 8:
            rep += "there are rumors that they "
            personality_cat = ["secretive", "suspicious", "untrustworthy"]
            match secondary_option:
                case 1:
                    rep += "have dealings with " + random.choice(["local criminals", "smugglers", "corrupt officials"])
                case 2:
                    rep += "are hiding " + random.choice(["their true identity", "their real name", "where they originally came from"])
                case 3:
                    rep += "were involved in a disappearance several years ago"
                case 4:
                    rep += "have secretly worked against their own allies"
                case 5:
                    rep += "know something about " + random.choice(["a local disappearance", "a concealed crime", "a powerful local figure", "a recent tragedy"])

        case 9:
            rep += "they are respected for "
            personality_cat = ["devoted", "helpful", "reliable"]
            match secondary_option:
                case 1:
                    rep += "keeping their word"
                case 2:
                    rep += "remaining dependable during times of crisis"
                case 3:
                    rep += "treating " + random.choice(["their allies", "their employees", "strangers", "those under their authority"]) + " fairly"
                case 4:
                    rep += "taking responsibility for their mistakes"
                case 5:
                    rep += "offering aid to " + random.choice(["those abandoned by others", "people with nowhere else to turn", "those unable to repay them"])

        case 10:
            rep += "they are disliked for "
            personality_cat = ["arrogant", "selfish", "aggressive"]
            match secondary_option:
                case 1:
                    rep += "frequently involving themselves in other people's disputes"
                case 2:
                    rep += "holding grudges against " + random.choice(["former friends", "old rivals", "people who have embarrassed them"])
                case 3:
                    rep += "placing their own interests ahead of those around them"
                case 4:
                    rep += "refusing to forgive old disagreements"
                case 5:
                    rep += "creating conflicts with " + random.choice(["local authorities", "former allies", "neighbors", "members of competing groups"])

        case 11:
            rep += "they are associated with "
            personality_cat = ["secretive", "loyal", "suspicious"]
            match secondary_option:
                case 1:
                    rep += "a group involved in " + random.choice(["smuggling", "organized crime", "illegal trade"])
                case 2:
                    rep += "a local organization with a questionable reputation"
                case 3:
                    rep += "people suspected of criminal activity"
                case 4:
                    rep += "a faction involved in " + random.choice(["a long-running local dispute", "a political struggle", "a violent feud"])
                case 5:
                    rep += "someone whose actions have made them widely feared"

        case 12:
            rep += "opinions of them are divided because "
            personality_cat = ["controversial", "independent", "unpredictable"]
            match secondary_option:
                case 1:
                    rep += "they have both helped and harmed the local community"
                case 2:
                    rep += "different people give conflicting accounts of " + random.choice(["their past", "their motives", "their involvement in an old incident"])
                case 3:
                    rep += "they have worked alongside " + random.choice(["rival factions", "people on opposing sides of the same conflict", "groups that openly distrust one another"])
                case 4:
                    rep += "some consider their past actions justified while others consider them unforgivable"
                case 5:
                    rep += "their actions have earned them " + random.choice(["both loyal supporters and bitter enemies", "respect from some and resentment from others", "admiration in some circles and hostility in others"])

    return rep, personality_cat

    return rep, personality_cat