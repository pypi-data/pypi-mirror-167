#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pylint:disable=bad-whitespace
# pylint:disable=line-too-long
# pylint:disable=too-many-lines
# pylint:disable=invalid-name


journal_prompts = [
    'What’s an indulgence that you haven’t let yourself partake in recently?',
    'If you had $500 to spend with no regrets, how would you use it to make your most perfect day?',
    'Go somewhere that you can people-watch.  Notice the different ways that people react to one another (or the ways they don’t).  Write some thoughts about what you notice.',
    'Write about a big or small vacation you have taken.',
    'How can you reframe one of your biggest regrets in life?',
    'What do you wish more people knew about your ...',
    'What would a day in your life look like 10 years from now? Walk through it step-by-step.',
    'When you were a child, how did you imagine your adult life? How does that compare to the way it is now?',
    'Analyze a personal victory. Think of something that you did well and break down the active ingredients that allowed you to kick ass in that situation.',
    'What is the most expensive thing you own? What is the story behind it?',
    'What is a product that you wish you could convince people NOT to buy? Try writing an anti-ad for that product.',
    'I wish I didn’t have to go to ...',
    'Write about a time that you assumed the worst and things turned out better than expected.',
    'Who have you genuinely helped in your life?',
    'Who has been your greatest teacher?',
    'What biases do you need to work on?',
    'If you could choose between having a personal chef, a housekeeper, or a personal trainer for free, which would you choose and why?',
    'What role does anger play in your life?',
    'What are the 5 most beautiful things in your immediate environment?',
    'Write about something (or someone) that is currently tempting you.',
    'Do you believe the idea that you are the sum of the people you spend the most time with? Why or why not?',
    'Where does your story really begin?',
    'Find two unrelated objects near you and think of a clever way they might be used together.',
    "What are five things you'd like to do before you die?",
    'What are some positive things that you have taken away from the family culture in which you were raised?',
    'In what ways are you currently self-sabotaging or holding yourself back?',
    'It’s been a while since I have ...',
    'React to the following quote from Martin Luther King Jr: "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that".',
    'Write a letter to someone to whom you would like to apologize. Be as clear and unfiltered as possible. DO NOT send the letter.',
    'What is your relationship to physical exercise? How might you need to change that?',
    'What would be a "force multiplier" skill or habit that you could work on, which would make all the other things you are doing with yout life just a bit easier?',
    'React to the following quote from Axteria by Rebecca McKinsey: "One thing you have to realize from now on is that it doesn’t matter if this is a dream or not. Survival depends on what you do, not what you think".',
    'What are your attitudes and opinions about medication?',
    'How do you take praise? How do you take criticism?',
    'I learned a long time ago that ...',
    'What would you like your last meal to be?',
    'Name 5 smells that trigger happy memories for you and explain where they take you.',
    'What is one thing you can change about today to make it more productive?',
    'In what ways have you become more resilient over the years?',
    'When I was younger I ...',
    'What can you do tonight to make sure that your body feels better tomorrow than it did today?',
    'How could you be taking better care of yourself?',
    'React to the following quote from Into the Wild by Jon Krakauer: "Happiness is only real when shared"',
    'Do you feel like it’s ever appropriate to be dishonest? Why or why not?',
    'Do you feel like people understand you well? Why or why not?',
    'How do you feel about the concept of nonmonagomous relationships (polyamorous, open relationship etc)?',
    'What can you recognize you are totally hypocritical about?',
    'I wish my parents would have ...',
    'Pick something within 5 feet of where you are and draw it. Any style. Try to draw without judgment, even if you’ve never tried to draw before.',
    'If you could live one other person’s life, whose would it be and why?',
    'Describe your favorite sound and what it means to you.',
    'Try meditating for 10 minutes. If you already meditate, try meditating in a different way. Write about your experience.',
    'What have you learned from previous jobs or involvements you’ve held?',
    'Write the perfect guide that someone else could use to bring you comfort when you are feeling down.',
    'Write a mantra that you can use today.',
    'What plants and flowers do you feel most drawn to? What do they remind you of? How do they make you feel?',
    'What is the most intense dream you can remember ever having?',
    'What are your feelings and opinions about travel?',
    'What is something that will seem barbaric 200 years from now?',
    'If I were president, i would ...',
    'What are some of the self-fulfilling prophecies that have played out in your life?',
    'What advice would you give to someone very much like you right now?',
    'What is an opportunity that you are glad did not work out?',
    'What small thing are you actually really proud of? Why does this mean so '
    'much to you?',
    'Practice a call or conversation that you are avoiding. Write out both sides '
    'of the roleplay from start to finish.',
    "Draw your life's timeline including the most relevant events that shaped "
    'you.',
    'What are 5-10 of the most important aspects of your identity?',
    'How do you feel about your city or town?',
    'Where in your life are you taking things too personally?',
    'Use one continuous line without lifting your pen/pencil and don’t look down '
    'at your page until you’re done.',
    'Who was your best friend from your youth? Do you still keep in touch? How '
    'has your relationship changed?',
    'What kind of friend could you use right now?',
    'If you could know one thing about the future, what would you want to know?',
    'Close your eyes and imagine yourself somewhere safe. Describe the place that '
    'came to mind and reflect on what felt safe about it.',
    'Who is someone in your life that you have always admired from afar, but '
    'never become close with? What do you admire about them?',
    'What are a few things you could do to help you focus more when you need to?',
    'What are the best and worst qualities you have inherited or learned from '
    'your parents/primary caregivers?',
    'How do you know when it’s time to let something (or someone) go?',
    'What are the first things that typically come to your mind upon waking up. '
    'What do you make of that?',
    'Try to write a short summary of the last thing you read.',
    'Use the memories function or scroll back about a year on social media or '
    'your phone’s camera roll. Reflect on what you see.',
    'React to the following quote from Friedrich Nietzsche: "It is not a lack of '
    'love, but a lack of friendship that makes unhappy marriages".',
    'Reflect on a time that you got into someone else’s business when you should '
    'have kept to yourself.',
    'Do something you do often, but in a different way. For instance, walk a '
    'completely different path than you normally do or drive to work silently '
    'rather than listening to music. Record your feelings and observations after.',
    'Think of a negative assumption about yourself (ex: I can’t make friends) and '
    'design an experiment to challenge that assumption.',
    'Write a letter of support to someone that you care about. This can be '
    'someone you actually know or someone that you have never actually met. You '
    'don’t need to send them the letter.',
    'What is something that you have successfully grieved?',
    'What would it look like if you planned for success?',
    'Write about your happiest childhood memory.',
    'Reflect on the nicest conversation you have had recently.',
    'How has the past year changed you?',
    'What are your top five comfort foods? What do they remind you of?',
    'What are some simple tweaks that you can make to your environment to reduce '
    'anxiety?',
    'Write about a recent experience that you loved being a part of.',
    'What is an appointment that you can make for joy/pleasure/indulgence?',
    'Who are you able to be vulnerable with? What makes them a person you are '
    'able to be yourself with?',
    'Invent a holiday. How would you celebrate it each year?',
    'What makes you feel most lonely?',
    'What purchase under $100 has made the biggest impact in your life lately?',
    'How would you like to die?',
    'What is the title of your life story so far?',
    'What is your relationship to debt? Are there any ways you would like this to '
    'change? If so, what’s one step you can take in that direction?',
    "What is a principle or ideal you'd like to pass down to the next generation?",
    'If you could only keep three of your possessions, which would you pick and '
    'why?',
    'What is a relationship that you need to improve in your life? What can you '
    'do to work toward improving it?',
    'I wish I had ...',
    'Pick an item from your environment. Spend 2-5 minutes writing all the '
    'alternative ways you could use that item that do not include its intended '
    'use.',
    'What is a belief that you are unwilling to change? What is one that you are '
    'still figuring out?',
    'What are your feelings about the afterlife, ghosts, spirits, etc?',
    'How do you typically react when you realize you’ve made a mistake? Would you '
    'like to change that at all?',
    'Write 10 words that you think are beautiful',
    'React to the following quote from Bill Watterson: "At school, new ideas are '
    "thrust at you every day. Out in the world, you'll have to find your inner "
    'motivation to seek for new ideas on your own"',
    'Build a list of 10-15 songs that you can use to change your mood for the '
    'better',
    'What are some unique talents that you have?',
    'React to the following quote from Tom Hiddleston: "Every villain is a hero '
    'in his own mind"',
    'What organizations or structures do you think should no longer exist?',
    'How do you feel about your job, current area of study, etc?',
    'What is a chance that you have taken that paid off in the end?',
    'When I think about the future, I ...',
    'What are your feelings about meditation?',
    'Write 10 qualities that you appreciate in yourself (push yourself to get to '
    '10) and 2 that you’d like to change or work on.',
    'List 10 things that make you smile.',
    'If you could ask one single yes or no question to the universe and get an '
    'answer, what would you ask?',
    'What is something that you recently blamed yourself for? Now that some time '
    'has passed, how do you think about it differently?',
    'If you were to give your anxiety a name, what would it be and why?',
    'How do you feel about the age you currently are?',
    'What is your first memory?',
    'How did you like having fun as a kid? Has any of that carried over into '
    'adulthood?',
    'Write about a favorite pet, past or present.',
    'Which cultural mores, pleasantries, or standards do you find pointless?',
    'What was the best part of the last year?',
    'Assign a role (like peacekeeper, joker, or golden child) to each of your '
    'immediate family members.',
    'What influences your attitudes toward sex and pleasure?',
    'Are you satisfied with your sleep? If so, how did you achieve that? If not, '
    'what could you do to improve it?',
    'If you could choose another career, vocation, or field of study than what '
    'you currently have, what would it be and why?',
    'What fictional character do you most identify with and why?',
    'What is a habit that you were successfully able to break?',
    'If you could put anything you want on a billboard next to the busiest '
    'highway in the world, what would you put on it?',
    'Make up a silly sport that doesn’t already exist. What equipment is used? '
    'What are the rules?',
    'What are some weird things you do when nobody else is around?',
    'I hope that one day ...',
    'How could you improve upon the standard model human body?',
    'What are some things that you judge others for that you would NEVER judge '
    'yourself for?',
    'Right now I am / I want to be.',
    'What would the complete opposite of you look like?',
    'React to the following quote from The Invention of Hugo Cabret by Brian '
    'Selznick: "1 like to imagine that the world is one big machine. You know, '
    'machines never have any extra parts. They have the exact number and type of '
    'parts they need. So I figure if the entire world is a big machine, I have to '
    'be here for some reason. And that means you have to be here for some reason, '
    'too".',
    'What are the top 3 emotions that you would like to embody today?',
    'Describe the kind of person you are looking for right now.',
    'Write a scene from your day in a poetic, descriptive way, as if it took '
    'place in a novel.',
    'React to the following quote from Man’s Search Jor Meaning by Viktor Frankl: '
    '"Everything can be taken from a man but one thing: the last of the human '
    'freedoms—to choose one’s attitude in any given set of circumstances, to '
    'choose one’s own way.',
    'What activities make you enter a "flow" state and totally lose track of '
    'time? Could you integrate any of these into your life more?',
    'React to the following quote from The Alchemist by Paulo Coelho: "No matter '
    'what he does, every person on earth plays a central role in the history of '
    'the world  and normally he doesn\'t know it""',
    'React to the following quote from Lance Armstrong: "Pain is temporary,  '
    'Quitting lasts forever""',
    'What is the best thing you have ever created?',
    'Stare in the mirror for two whole minutes.  How did that make you feel?',
    'Pull a random book from the closest shelf/pile and flip to a random page.  '
    'Try to find a way that the words (or numbers or pictures) on the page apply '
    'to your life right now',
    'What does normal mean to you? Is it good to be normal?',
    'React to the following quote from Coraline by Neil Gaiman: "Fairy tales are '
    'more than true: not because they tell us that dragons exist, but because '
    'they tell us that dragons can be beaten".',
    'What is a high and a low from your week so fare.',
    'What is your metric for success right now? What would you like to judge '
    'yourself based on?',
    'React to the following: Many people forget that grief isn’t only for people '
    'that have died . You also need to grieve lost experiences and expectations".',
    'What do you feel like you have run out of time to do? Can you challenge '
    'that?',
    'React to the following quote from Stranger in a Strange Land by Robert A '
    'Heinlein: "Love is that condition in which the happiness of another person '
    'is essential to your own"',
    'Go outside and look at the clouds (or trees if you have no clouds today) and '
    'see what objects animals etc. jump out at you.  Write each one down.',
    'What is a memory that fills you with gratitude?',
    'What freedoms are you most grateful for?',
    'Which fictional world would you like to live in and why?',
    'I wish i thought about less often.',
    'Aside from your own, whose voice do you hear in your head most often? What '
    'do they say?',
    'What defense mechanisms kept you safe in the past, but may need to be let go '
    'now?',
    'If you could design the perfect carnival or fair, what would be there?',
    'In what ways do you need to change your physical health?',
    'What was yout last "light bulb moment" about?',
    'What would someone learn about you if they could observe you for an entire '
    'day?',
    'What is the best compliment that you have ever received?',
    'If you had to go on stage and sing one song without making any mistakes, '
    'which would you pick? Prove it. Write all the lyrics to that song without '
    'looking them up.',
    'What is the closest you’ve come to death? Reflect on that experience',
    'Realistically, what is the best way for you to have a positive impact on the '
    'world?',
    'Which emotion is most difficult for you to experience and why?',
    'If you aren’t familiar with the idea of chakras, look them up. Do you feel '
    'like the idea has validity? How do you see them fitting into your life?',
    'What is a cause that you are passionate about and why are you passionate '
    'about it?',
    'What is something that moves you emotionally?',
    'If i had more time I would ...',
    'lf you could change one aspect of your romantic partner or best friend, what '
    'would you change and why?',
    'Mentally walk through your day and identify ways you could change your '
    'environment to make things easier or smoother.',
    'What are the major influences on your self- worth?',
    'Make a doodle using only basic geometric shapes like lines, rectangles, '
    'circles, triangles etc',
    'Identify two random people in your environment and secretly wish for them to '
    'be happy. Say to yourself, "I wish for them to be happy" How did that feel?',
    'Which words do you overuse the most?',
    'How has your ability to entertain yourself changed since you were young?',
    'What relatives have you felt closest to?',
    'Write some lyrics to a favorite song and reflect on why they resonate with '
    'you so much.',
    'If you could modify your living space to make it more pleasant or '
    'comfortable for you, what would you do?',
    'Write about a time that your own strength surprised you',
    'Write a letter to your younger self when you were in a pivotal moment in '
    'your development',
    'Which animal embodies you and why?',
    'If you had a million dollars, but could not use a single dollar on yourself, '
    'what would you do?',
    'What can you not imagine living without?',
    'What scares you the most? Why?',
    'Reflect on your current relationship to social media. Do you feel like your '
    'social media habits (or lack thereof) are healthy?',
    'Nobody knows that I ...',
    'When i think about my childhood, i feel ...',
    'What is something that you are insecure about? What is something that you '
    'are confident in?',
    'What is a value of yours that you are not spending as much time as you would '
    'like on? What is something you don’t value that you are spending TOO much '
    'time on?',
    'If karma were real, what would you have coming your way?',
    'What is the most important question to ask yourself every day?',
    'React to the following quote from ‘Tim Ferriss: "Being busy is most often '
    'used as a guise for avoiding the few critically important but  uncomfortable '
    'actions"',
    'Write a eulogy for a friend that is still alive.',
    'When do you feel most comfortable in your own skin?',
    'Are there any figures from history that most admire but you really don’t '
    'like? Why?',
    'How do you feel about the idea that one person should fulfill all the needs '
    'of their partner?',
    'Reflect on something that used to be hard for you.',
    'Write about a vehicle that can take you somewhere different from where you '
    'are now.',
    'Write about something ordinary that made you smile in the past week.',
    'What are some qualities that you admire in others? In what small ways can '
    'you integrate more of those into your life?',
    'Why can’t I just ...',
    'What is your relationship to spirituality? Has that changed over time?',
    'What are your most common emotions these days? How do you feel about that?',
    'What is something from your life that you still feel guilty for? What would '
    'help you feel more closure.',
    'What do people get wrong about you?',
    'What is a situation that caused you to confront your ethics?',
    'What is currently your biggest time waster and what can you do about it?',
    'Someday, I will ...',
    'If i could have one more chance, I would ...',
    'If you could talk to someone that you have lost for just five more minutes, '
    'what would you say?',
    'What is your favorite weather or time of year and why?',
    'What was your most embarrassing moment? Did you learn anything from it?',
    'What would you do if you won the lottery?',
    'If you could choose a superpower, which would you pick and why?',
    'Who do you think of when you think of the word "successful" and why?',
    'What does the word "courage" mean to you? How have you shown courage '
    'recently? How would you like to show courage?',
    'React to the following quote from Maya Angelou: "I’ve learned that people '
    'will forget what you said, people will forget what you did, but people will '
    'never forget how you made them feel".',
    'I find it very confusing that ...',
    'What standards do you apply to yourself that you would never apply to '
    'others?',
    'If you could bring back one extinct animal, which would you bring back and '
    'why?',
    'Write about something for which you would like to forgive yourself.',
    'What are a few ways that you could use the evening to set yourself up for '
    'success the next day?',
    'When I think about my future, I feel ...',
    'How do you feel about the concept of mentalhealth diagnoses?',
    'React to the following quote from The Perks of Being a Wallflower by Stephen '
    'Chbosky: "We accept the love we think we deserve".',
    'What are some of the worst pieces of advice that you have gotten? 466. How '
    'could you add more fun or play into your life?',
    'How could you better support your loved ones?',
    'React to the following quote from Rumi: "If you are irritated by every rub, '
    'how will your mirror be polished?"',
    'What is a necessary conversation that you are scared of having? Why?',
    'How has your perspective on love changed over time?',
    'If your life had been easier or harder, how would you be different now?',
    'I wish I knew ...',
    'What are your main coping mechanisms right now? How are they serving you? '
    '474. Build a list of 5 videos that you can watch when you need motivation.',
    'Write about a near-miss in your life. Something that was almost perfect but '
    'ended up not working out. Could be a relationship, a job, or something else '
    'entirely.',
    'Write three things that you have done well today.',
    'I wish knew that I ...',
    'How do you tend to respond to crises? Write about your response to one that '
    'you can remember. How do you feel about that?',
    'What age would you consider the prime of your life? If you haven’t hit it '
    'yet, when do you think it will be?',
    'What is the most beautiful thing you have ever seen?',
    'When do you most trust your instincts?',
    'What motivates you right now?',
    '484, What would make you feel more a part of your community?',
    'Where will you be in 5 years if your physical health continues on its '
    'current trajectory?',
    'If you won the lottery, who would you take care of and how?',
    'What feelings do you have about your name? Were you named after anyone? '
    'Would you change your name if you could easily?',
    'What is your relationship to crying?',
    'What is something that you are avoiding right now? What makes it feel so '
    'insurmountable?',
    'Are you satisfied with your sex life? Why or why not?',
    'In what ways are you different than your parents or primary caregivers? How '
    'does that impact your relationship with them?',
    'How would you like to feel in your body today?',
    'React to the following quote from The Kindly Ones by Neil Gaiman: "Have you '
    "ever been in love? Horrible isn't it? It makes you so vulnerable. It opens "
    'your chest and it opens up your heart and it means that someone can get '
    'inside you and mess you up"',
    'What memory makes you feel compassion for yourself?',
    'Some say that animals are good judges of character. What do you make of '
    'that?',
    'Who is the most charismatic person you can think of? What makes them that '
    'way?',
    'Look up the lyrics to a song that you have never bothered to learn. Write '
    'down anything interesting that comes to mind',
    'What are your attitudes and opinions about therapy?',
    'Consider a misfortune or roadblock in your life right now. Ask yourself, '
    '"What does this allow me to do?"',
    'How do you feel about your country?',
    'I treat myself like ...',
    'Do you truly hate anyone? Who and why?',
    'React to the following quote from The Picture of Dorian Gray by Oscar Wilde: '
    '"Every impulse that we strive to strangle broods in the mind and poisons us"',
    'Write about a favorite memory of being recognized for something you did',
    'Write about a mistake that taught you something about yourself',
    'What is a reasonable way that you can adjust your morning routine to work '
    'better for you?',
    'In what way is your biggest flaw also your superpower?',
    'What do you know about the way your parents were raised? How did this '
    'influence their treatment of you?',
    'In your mind, how do you imagine God or any higher power you might connect '
    'with?',
    'What is a boundary that you need to draw in yout life?',
    'I got where I am today because ...',
    'How have you been able to gain the trust of others in the past? Write about '
    'a specific example',
    'How do you feel about humans traveling to, and possibly inhabiting, other '
    'planets?',
    'Write an apology to yourself for a time you treated yourself poorly. '
    'Remember, a good apology should feature an acknowledgment of what happened, '
    'how it made the person feel, and how you will do better in the future.',
    'What is a made-up rule about your life that you are applying to yourself? '
    'How has this held you back and how might you change it?',
    'If you could travel to anywhere in the world to live in another era, where '
    'and when would you go? If your gut instinct was that you’d rather stay where '
    'you are, why?',
    'Write about a time you can remember being blindsided by something someone '
    'told you.',
    'How do you feel toward other people that you know have anxiety?',
    'What is a positive habit that you would really like to cultivate? Why and '
    'how could you get started?',
    'Which songs have vivid memories for you?',
    'When was the last time you had to hold your tongue? What would you have said '
    "if you didn't have to?",
    'What are 5-10 things that your parents don’t know about you?',
    'Make up an imaginary story about someone you see in your environment.',
    'How do the opinions of others affect you?',
    'What part of life has surprised you the most?',
    'What is a reminder that you would like to tell yourself next time you are in '
    'a downward spiral?',
    'How would your friends describe you? How do you feel about those '
    'descriptions?',
    'Who is someone that significantly influenced the person you ate now?',
    'What are you looking forward to right now?',
    'Think about the last time you cried. If those tears could talk, what would '
    'they have said?',
    'Figure out where you do your best thinking and see how you can spend more '
    'time there.',
    'What is the last song that you listened to on repeat? Why?',
    'What are some movies or TV shows that make you feel encouraged or motivated?',
    'What do you know about your genealogy? How do you feel about it?',
    'React to the following quote from The Fault in Our Stars by John Green: '
    '"What a slut time is. She screws everybody"',
    'Draw a small scribble on the page then use your imagination to turn that '
    'scribble into a full drawing.',
    'How have you changed in the last year?',
    'What is the quickest way to gain your trust?',
    'Write a letter to your own body, thanking it for something amazing it has '
    'done. What happens when you are angry?',
    'What are five creative hobbies that you have never tried?',
    'At what point in your life have you had the highest self-esteem?',
    'What is a question that you are really scared to know the answer to?',
    'Is there something that you could do a little bit less of to keep it from '
    'feeling like a chore or a burden?',
    'What kind of worker are you? Are you satisfied with that?',
    'If I could have it my way, everyone would just ...',
    'Write down 10 ambitious goals for the next decade.',
    'What is a mistake you made in the past week. How can prevent it from '
    'happening again?',
    'Which movies are your "comfort" movies? Any idea why?',
    'If you could re-do a decade of your life, which would you re-do and why?',
    'Write about an item from your past that you miss.',
    'If you could eliminate any one disease or illness from the world, what would '
    'you choose and why?',
    'Write about a dream that you can remember from the past. What does this '
    'dream mean to you now?',
    'What is the hardest day you’ve ever gotten through? How did you get through '
    'it?',
    'Scroll back through your camera roll and find the first picture that makes '
    'you smile. Write about the moment captured there and how it makes you feel.',
    'What did you learn from your last relationship? If you haven’t had one, what '
    'could you learn from a relationship that you’ve observed?',
    'What is holding you back from being more productive at the moment? What can '
    'you do about that?',
    'Who were your models of love and affection? What did you learn from them?',
    'In your life, do you find that it works out better to plan ahead or go with '
    'the flow?',
    'What life lessons, advice, or habits have you picked up from fiction books?',
    'When is physical violence appropriate?',
    'React to the following quote from We All Looked Up by Tommy Wallach: "Do you '
    'think it is better to fail at something worthwhile, or to succeed at '
    'something meaningless?"',
    'I have always survived by ...',
    'Describe your upbringing as you understand it today.',
    'What was a seemingly inconsequential decision that made a big impact in your '
    'life?',
    'List 5 things that you have enjoyed in the past. List 5 things that other '
    'people do that seem like they would be fun to try.',
    'How would you like to be remembered? I’m looking forward to. What are your '
    'strongest sense memories?',
    'Write about the last time you felt palpable heartache.',
    'What is an experience you wish you could have again for the first time?',
    'What is something that you grew out of that meant a lot to you at the time?',
    "How did you bond with one of the best friends you've ever had?",
    'Who was your first love? Reflect on the experience of falling in love for '
    'the first time.',
    'Write about something that you would like to let go of.',
    'Try giving yourself a topic to think about or problem to solve while you '
    'sleep. Be specific and write it down. Come back in the morning and '
    'free-write on the topic',
    "249, What were your parents’ or caregivers' expectations of you growing up?",
    'What is something that you feel a lot of people misunderstand about your '
    'family of origin?',
    'How much do your current goals reflect your desires vs someone else’s?',
    'Why do you dress the way that you do?',
    'Which emotions in others do you have a difficult time being around? Why?',
    'What is your relationship with money and how has it changed over time?',
    'Think of a cliché like "time heals all wounds" and argue for or against it',
    'How do you feel about the place that you grew up in? Would you change it?',
    'What are some of the worst character traits that a person can have? When '
    'have you demonstrated these traits?',
    'Write a letter to yourself 5 years ago.',
    'You have been temporarily blinded by a bright light.  When your vision '
    'clears, what do you see?',
    'What would you change about your school experience if you had the ability to '
    'do so?',
    'What would be the best random act of kindness that someone could perform for '
    'you today?',
    'What do you need to give yourself more credit for?',
    'Talk about a time that you are proud to have told someone "no".',
    'Write about 3 ways that anxiety has helped you in the past.',
    'Who currently owes you an apology? What would you like them to say?',
    'How do you feel when you spend time alone?',
    'I’ve always felt too afraid to ...',
    'How does your internal self match (or not) your external presentation?',
    'What role does jealousy play in your life?',
    'React to the following quote from The Art of Seeing by Aldous Huxley: '
    '"Consciousness is only possible through change; change is only possible '
    'through movement".',
    '170, What are you world-class at? Big or small.',
    'When was the last time you felt let down? Think back on the experience and '
    'determine whether you feel the same way in retrospect.',
    'How would you re-write the ending of a movie, show, fairy tale, etc. to make '
    'it more satisfying?',
    'What made you feel most alive when you were young?',
    'Write a letter to your 13-year-old self.',
    'Consider and reflect on what might be your "favorite failure".',
    '‘Take a task that you’ve been dreading and break it up into the smallest '
    'possible steps.',
    'What is your most meaningful possession? What is the story behind it?',
    'What were the best and worst parts about your adolescence?',
    'Write a letter to yourself 10 years from now',
    'What do you know about the start of your parents’ relationship?',
    'Do you believe that life has a purpose? Why or why not?',
    'React to the following quote from Jim Butcher: "When everything goes to '
    'hell, the people who stand by you without flinching — they are your family"',
    'React to the following quote from Emma Bull: "Coincidence is the word we use '
    'when we can’t see the levers and pulleys"',
    'The world would be a lot better if ...',
    'React to the following quote from Bob Marley: "The truth is, everyone is '
    'going to hurt you  You just got to find the ones worth suffering for""',
    'Try to write your full name with your non- dominant hand.  Keep practicing '
    'until you fill up the page',
    'What sensations or experience do you tend to avoid in your life? Why?',
    'What part of your work do you most enjoy? What part do you least enjoy? Why?',
    'List 20 things that make you happy.',
    'What are some small things that other people have done that really make your '
    'day?',
    'How could you make something you dread just a little bit more fun?',
    'Which quotes or pieces of advice do you have committed to memory? Why have '
    'those stuck with you?',
    'How did/do your parents deal with adversity?',
    'What situation is probably less risky or complicated than you are imagining?',
    'Do you have any guilty pleasures? If so, why is it hard for you to own them?',
    'What are your views on suicide?',
    'React to the following quote from Steven Hawking: "We are just an advanced '
    'breed of monkeys on a minor planet of a very averagestar.  But we can '
    'understand the Universe. That makes us something very special"',
    'My life is nothing without my ...',
    'Write about the weather outside right now.  What does it make you feel like? '
    'Does it conjure up any memories? If you could do anything given the weather '
    'right now, what would it be?',
    'Describe yourself in one sentence.',
    'Do you feel like you gained anything from the books you were required to '
    'read in school? Why or why not?',
    'What are some of your core values?',
    'React to the following quote from Alice Walker: "The most common way people '
    'give up their power is by thinking they don\'t have any"',
    'Imagine that you have arrived at a closed door.  What does it look like and '
    'what’s on the other side?',
    'What would you consider to be your love language? What role does that play '
    'in your life?',
    'I wish I never ...',
    'What is an assumption you have made about somebody else that turned out to '
    'be wrong?',
    'What could you do to make your life more meaningful?',
    'What images from your past (if any) make you feel safest? If none do, why '
    'not?',
    'What keeps you going these days? Is that sustainable?',
    'I wish someone would ...',
    'What pet peeves do you have? Any idea why they drive you so crazy?',
    'Write a thank you note to someone. Sending is optional',
    'What do you wish you could do more quickly? What do you wish you could do '
    'more slowly?',
    'Who is the most difficult person in your life and why?',
    'How has your fashion sense changed over time? Would you like it to change '
    'more?',
    'To me, love is ...',
    'What would things be like in 6 months if you continued your current '
    'trajectory?',
    'What does the word "confidence" mean to you? What makes you feel confident?',
    'What is something that you have a hard time being honest about, even to '
    'those you trust the most? Why?',
    'What is your worst childhood memory? How do you feel thinking back on it?',
    'What are some things that frustrate you? Can you find any values that '
    'explain why they bug you so much?',
    'I can’t believe that',
    'Are you taking enough risks in your life? Would you like to change your '
    'relationship to risk? If so, how?',
    'Are there any superheroes or other fictional heroes that you can’t stand? '
    'Why?',
    'Think about a "what if?" or worst-case scenario and work your way through '
    'the problem, identifying your options to get through it if it were to happen',
    'I deserve ...',
    'React to the following quote from Anais Nin: "We don\'t see things as they '
    'are, we see them as we are"',
    'What is a fad that you totally fell into? How do you feel about it now?',
    'Who do you consider to be courageous and why?',
    'React to the following quote from Albert Einstein: "Life is like riding a '
    'bicycle. To keep your balance, you must keep moving"',
    'Start by writing "why do I feel so ?" Fill in that blank with whatever you '
    'are feeling today. Then try to work out the answer to that question',
    'What is the best thing you have ever written?',
    'Listen to a song from a genre that you don’t typically listen to. What '
    'thoughts, feelings, or other reactions are you getting?',
    'Where in your life are you engaging in all-or- nothing thinking?',
    'What are your favorite forms of self-care? How might you need to adjust your '
    'relationship to self-care at this point in your life?',
    'How did your parents or caregivers try to influence or control your behavior '
    'when you were growing up?',
    'How do you feel about asking for help?',
    'Write a complete story with just six words. For example: Turns out the pain '
    'was temporary.',
    'Observe your environment and try to notice 3-10 things that you’ve never '
    'noticed before. Write about them.',
    'Write a letter to your 18-year-old self',
    'What unexpected event or disaster would you be totally unprepared for right '
    'now? Which would you be ready for?',
    'Draw 25 circles on a page (5x5 grid of circles). Now set a timer for 3 '
    'minutes and try to turn each one into something unique. Could be a ball, '
    'hand cuffs, a logo, or an eye for instance',
    'React to the following quote from Elie Wiesel: "The opposite of love is not '
    "hate, it's indifference. The opposite of art is not ugliness, it's "
    "indifference. The opposite of faith is not heresy, it's indifference. And "
    'the opposite of life is not death, it\'s indifference"',
    'What are some things that you could invest more money in to make life '
    'smoother and easier for yourself?',
    'Who do you feel like is treated unfairly in the world?',
    'Which famous person (dead or alive) do you feel like you could be good '
    'friends with? How would you like to spend time with them?',
    'What is an assumption people tend to make about you? How do you feel about '
    'that?',
    'Who is somebody that you miss? Why?',
    'What is a view about the world that has changed for you as you’ve gotten '
    'older?',
    'Where in your body do you feel your anxiety?',
    'What is the first hint that anxiety is coming on?',
    'Write 10-20 possible words to serve as a theme/goal for your year (my past '
    'two are "power" and "balance").',
    'Who is on your team?',
    'What does family mean to you?',
    'If you’ve had a first kiss, write about what you remember.   If not, how do '
    'you feel about that?',
    'If you believe in an afterlife, what do you imagine it to be like? If not, '
    'how would you design the perfect afterlife?',
    'If someone was narrating your life today, what would they be saying?',
    'Write a letter to someone you miss dearly',
    'What are are some things you did with your dad/mom/other primary caregiver '
    'when you were young?',
    'Use an online tool like the Random Classic Art Gallery to find a classic '
    'piece of art. Write about the thoughts or feelings generated by that piece',
    'Reflect on any meaningful family traditions you have. If you have none, '
    'which would you like to create?',
    'Write a bit about physical pain and how it impacts your life and mood.',
    'Invent your own planet. Draw a rough sketch of the planet and its '
    'inhabitants. How is it different than Earth?',
    'Do you trust your intuition? Why or why not?',
    'How has your self-worth changed over time?',
    'What is a skill that you are proud of?',
    'What are 3-5 memories that would help someone understand who you are as a '
    'person?',
    'What are your strengths when working in a group with other people?',
    'Do you think it’s important to learn another language? Why or why not?',
    'How could you be utilizing technology better?',
    'Write a letter to your 9-year-old self.',
    'Write about an aspect of your personality that you appreciate in other '
    'people as well.'
]
