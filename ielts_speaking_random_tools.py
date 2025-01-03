# question part1-3 reference : https://www.ieltsadvantage.com/2023/02/19/ielts-speaking-questions/
# question part2 reference : https://magoosh.com/ielts/ielts-speaking-part-2-topics-questions/

from gtts import gTTS
import os
import random
import time

part_one = {
    "Accommodation": [
        "Tell me about the kind of accommodation you live in.",
        "Do you live in a house or a flat?",
        "Is it a big place?",
        "Does the place you live in have many amenities?",
        "What do you like about living there?",
        "Is there anything you would like to change about the place you live in?",
        "How long have you lived there?",
        "Do you plan to live there for a long time?",
        "Is there a garden in the place you live in?"
    ],
    "Advertisements": [
        "Do you like watching advertisements?",
        "Will you buy something because of an advertisement?",
        "How do you feel when you see pop-up ads on the internet?",
        "Do you like funny or serious advertisements?",
        "What makes a good advertisement?"
    ],
    "Art": [
        "Do you like art?",
        "Do you think art classes are necessary?",
        "How do you think art classes affect children’s development?",
        "What benefits can you get from painting as a hobby?"
    ],
    "PhotographyandPhotos": [
        "Do you like to take photographs?",
        "Do you prefer to take photos yourself or to have other people take photos?",
        "How often do you take photographs?",
        "Do you prefer to take pictures of people or of scenery?",
        "Do you prefer to take photos with a phone or with a camera?",
        "Do you take many photographs when you travel?",
        "Do you like looking at photographs of yourself?",
        "Have you put any photographs you have taken on the walls in your house?",
        "Who do you usually take photos of?",
        "How do you keep your photos?",
        "Do you keep your photographs on your computer?",
        "Have you framed any of your photos?",
        "Do you prefer to send postcards to people or to send photos that you took yourself?",
        "Are there any photos on the walls of your home?"
    ],
    "Animals": [
        "Do you like animals?",
        "What is your favourite animal?",
        "What types of animals do you have in your country?",
        "What types of animals are kept as pets in your country?",
        "Do you think animals should be kept in zoos?",
        "Do you have any animals in your home as a pet?",
        "Did you have a pet when you were a child?",
        "Would you like to have a pet in the future?",
        "Do you have a pet?",
        "What types of animals do you think make the best pets?",
        "Why do people have pets?",
        "Should dogs be left in the house alone while their owners are at work?",
        "Is there any type of animal that you think should not be kept as a pet?"
    ],
    "Boat": [
        "Have you ever taken a ride on a boat?",
        "Do you like travelling by boat?",
        "What are the advantages of travelling by boat?",
        "Do people in your country like to travel by boat?",
        "Will it get more popular in the future?"
    ],
    "Bags": [
        "Do you like bags?",
        "What types of bags do you like?",
        "Do you usually carry a bag (when you go out)?",
        "What types of bags do you use in your everyday life?",
        "What do you put in these bags?",
        "What sorts of bags do women like to buy?"
    ],
    "Birthdays": [
        "What did you usually do on your birthday when you were a child?",
        "How do you normally celebrate your birthday now?",
        "Is your birthday now still as important to you as when you were a child?",
        "Do you think it’s important to give someone a card when it’s their birthday?",
        "Do you think the price of gifts/presents is important?"
    ],
    "Books": [
        "Do you like reading books? Why?",
        "How often do you read?",
        "Do you have many books at home?",
        "Do you prefer to buy books or borrow them?",
        "What are the benefits of reading?",
        "What book would you take on a long journey?",
        "How easy is it for you to read books in English?",
        "Have you given up reading a book recently?",
        "What kind of people like reading and what kind of people don’t like reading very much?",
        "What kinds of books do you like to read?",
        "What is the best book you’ve ever read?",
        "Is reading books a popular activity in your country?",
        "Do you think that electronic books / eReaders are better than real books?"
    ],
    "Celebrity": [
        "Who is your favourite celebrity?",
        "Do you like any foreign celebrities?",
        "Would you want to be a celebrity in the future?",
        "Do you think we should protect famous people’s privacy?",
        "How do celebrities influence their fans in your country?"
    ],
    "ClothesandFashion": [
        "What is your favourite item of clothing?",
        "Are there any traditional clothes in your country?",
        "Where do you usually purchase your clothes?",
        "Have you ever bought clothes online?",
        "Were you interested in fashion when you were a child?",
        "Is fashion important to you now?",
        "What types of clothes are fashionable for young people in your country these days?",
        "Does fashion change for people as they get older?"
    ],
    "Colours": [
        "What colours do you like?",
        "What’s the most popular colour in your country?",
        "Do you like to wear dark or bright colours?",
        "What’s the difference between men and women’s preference for colours?",
        "Do colours affect your mood?"
    ],
    "Computer": [
        "Do you use computers?",
        "What do you use a computer to do?",
        "Did you use computers when you were little?",
        "Do people often use computers these days?",
        "Will people continue to use computers in the future?"
    ],
    "Country": [
        "What is your country famous for?",
        "Where do you live in your country?",
        "Is it an interesting place to live?",
        "Are you planning to live there in the future?"
    ],
    "Daily Routine": [
        "Tell me about your daily routine?",
        "Has your daily routine changed since you were a child?",
        "Is your daily routine different at the weekend to during the week?",
        "What would you like to change about your daily routine?",
        "Do you think it’s important to have a daily routine?"
    ],
    "Dictionaries": [
        "Do you ever use a dictionary?",
        "Do you prefer paper or electronic dictionaries?",
        "Are dictionaries used a lot in schools in your country?",
        "Do you think dictionaries are useful for learning a language?"
    ],
    "Dreams": [
        "Do you dream much at night?",
        "Do you often remember your dreams?",
        "Do you think we can learn anything from dreams?",
        "Do people in your country talk about their dreams?",
        "Do you think that dreams can come true?"
    ],
    "Email": [
        "What kinds of emails do you receive about your work or studies?",
        "Do you prefer to email, phone, or text your friends?",
        "Do you reply to emails as soon as you receive them?",
        "Are you happy to receive emails that are advertising things?",
        "Do you email people often?",
        "Do you chat with friends or family more with email?",
        "Do you think people prefer to receive an email or a letter?",
        "Do you think it’s easier to write an email or a letter?",
        "Do you think email will eventually replace letter writing?"
    ],
    "Exercise": [
        "Do you do much exercise?",
        "Do you do more exercise now than when you were a child?",
        "Do people in your country do a lot of exercise?",
        "What do you think is the best exercise to keep fit?",
        "Have the types of exercise people like to do changed since you were a child?"
    ],
    "FamilyandHousework": [
        "How many people are there in your immediate family?",
        "Who do you get on best within your family?",
        "Do you have a large extended family?",
        "What do you do together with your family?",
        "Why is family important to you?",
        "Do you do housework at home?",
        "What kind of housework do you often do?",
        "Did you do housework when you were a child?",
        "Do you think that children should do housework?",
        "Do you all live in the same house?",
        "Who is your favourite family member?",
        "Do you have a large family or a small family?",
        "Can you tell me something about your family members?",
        "How much time do you manage to spend with members of your family?",
        "Do you get on well with your family? Why?"
    ],
    "Flowers": [
        "Have you ever given anybody flowers?",
        "Is it popular to give flowers to people in your country?",
        "On what special occasions do people give flowers in your country?",
        "What kinds of flowers would you like to receive as a present?"
    ],
    "Friends": [
        "Do you have a lot of friends?",
        "Who is your best friend and why?",
        "Who would you most like to be friends with and why?",
        "What kind of person can you make friends with easily?",
        "Which is more important to you, friends or family?"
    ],
    "Food": [
        "Do you enjoy cooking?",
        "What type of things can you cook?",
        "What kinds of food are popular in your country?",
        "Is it an important part of your culture to have dinner parties?",
        "Do you prefer to eat with other people or on your own?",
        "Do you have a healthy diet?",
        "Do you prefer eating at home or eating out?",
        "Do you like ordering food to be delivered?",
        "Who do you get food delivered with?",
        "Do you eat meals differently now compared to when you were little?"
    ],
    "Noise": [
        "Do you mind noises?",
        "What types of noise do you come across in your daily life?",
        "Are there any sounds that you like?",
        "Where can you hear loud noises?",
        "Do you think there’s too much noise in modern society?",
        "Are cities becoming noisier?"
    ],
    "Gift": [
        "When do you send gifts?",
        "When was the last time you received a gift?",
        "Have you received a gift you didn’t like?",
        "How do you feel when you receive a gift?",
        "Do people in your country send gifts to show their generosity?"
    ],
    "High School": [
        "Who was your favourite teacher in high school?",
        "What was your favourite subject in high school?",
        "Do you still remember what happened on your first day of high school?",
        "Do you still keep in touch with your friends from high school?",
        "Do you miss your life in high school?"
    ],
    "Home": [
        "Who do you live with?",
        "What is your favourite room in your home?",
        "How is your home decorated?",
        "Do you like visitors coming to your home?"
    ],
    "Hometown": [
        "Where is your hometown?",
        "What do you like about it?",
        "What do you not like about it?",
        "Is there any way your hometown could be made better?",
        "How important is your hometown to you?",
        "Can you tell me about your hometown?",
        "How has your hometown changed over the years?",
        "Do you think you will continue to live in your hometown?",
        "How often do you visit your hometown?",
        "How many people live in your hometown?",
        "What kind of jobs do the people in your hometown do?",
        "What is your hometown famous for?",
        "What’s the oldest part of your hometown?"
    ],
    "Humour": [
        "What type of programmes do you find funny on TV?",
        "Which types of programmes are most popular in your country?",
        "What kind of things make you laugh?",
        "Do you like to make people laugh?"
    ],
    "Indoor Activities & Transportation": [
        "Do you prefer public transportation or private transportation?",
        "What’re the most popular means of transportation in your hometown?",
        "Is it easy to catch a bus in your country?",
        "Is driving to work popular in your country?",
        "What do you think will become the most popular means of transportation in your country?",
        "Do you like indoor activities?",
        "What indoor activities do you like?",
        "How much time do you spend indoors every week?",
        "What types of indoor activities are popular in your country?"
    ],
    "Internet": [
        "How important is the Internet to you?",
        "Do you use the Internet more for work or in your free time?",
        "What are your favourite websites?",
        "Do you think you use the Internet too much?",
        "How will the Internet develop in the future?",
        "What are the positive and negative things about the Internet?"
    ],
    "Lifestyle": [
        "What do you do in your free time?",
        "Do you have a busy social life?",
        "Do you lead an active life?",
        "Has your life changed much in the last year?",
        "What would you like to change about your lifestyle?",
        "What type of activities do you like to do in your free time?",
        "How long have you been interested in these activities?",
        "Do you like to do these activities alone or with other people? (Why)?",
        "Do you think people have enough free time?"
    ],
    "Major": [
        "Do you work or study?",
        "What is your major? Or what was your major?",
        "Did you or do you like it?",
        "Is it a popular major at your university?",
        "Why did you choose that major?",
        "What is the most difficult part of studying that subject?",
        "Do you plan to use the subject you are studying in the future?",
        "If you could change to another major, what would it be?",
        "Would you change it if you had the chance?"
    ],
    "Mobile Phones": [
        "Do you have a mobile phone?",
        "At what age did you first get a mobile?",
        "What do you most use it for?",
        "Is it a nuisance if people use mobiles in public places such as trains and buses?"
    ],
    "Movies": [
        "How often do you go to the cinema?",
        "Are cinema tickets expensive in your country?",
        "What are the advantages of seeing a film at the cinema?",
        "Do you usually watch films alone or with others?",
        "Which actor would you like to play you in a film?"
    ],
    "Museums": [
        "Are museums popular in your country?",
        "Did you visit museums when you were a child?",
        "Do you like to visit museums nowadays?",
        "Do you think you should pay to visit museums?"
    ],
    "Music": [
        "How do you listen to music?",
        "When do you listen to music?",
        "What’s your favourite kind of music?",
        "Is music an important subject at school in your country?",
        "What kinds of music are (most) popular in your country?",
        "Do you like to listen to live music?",
        "Is live music popular in your country?",
        "Have you ever been to a concert before? Or Have you ever been to a musical performance?",
        "How much time do you spend listening to music every day?",
        "Are your music tastes varied?",
        "What is your favourite song?",
        "Do you like to sing along to your favourite songs?",
        "Are you learning to play a musical instrument at the moment?"
    ],
    "Musical Instruments": [
        "Do you think it’s important for children to learn to play a musical instrument?",
        "Do children have to learn to play a musical instrument at school in your country?",
        "Have you ever learned to play a musical instrument?",
        "What do you think is the best age to start learning to play a musical instrument?",
        "What do you think would be the most difficult musical instrument to learn to play?",
        "Do you think it is important to have a sense of humour? (Why)?"
    ],
    "Neighbours": [
        "Do you know the people who live next door to you?",
        "How often do you see each other?",
        "What kind of relationship do you have?",
        "How can neighbours be helpful?",
        "What kind of problems can people have with their neighbours in a big city?"
    ],
    "Newspaper And Magazine": [
        "Which do you prefer reading, newspapers or magazines?",
        "What type of stories do you like to read about?",
        "Do you think reading a magazine or a newspaper can help you learn a language?",
        "Why do you think some people prefer magazines to newspapers?",
        "Do you often read newspapers?",
        "Do you prefer to read local news or international news?",
        "Which is more popular where you live, newspapers or magazines?",
        "Do many people today read newspapers?",
        "In the future, do you think more people than today will read magazines or fewer people?",
        "Do you think newspapers will be very important to you in the future?"
    ],
    "Outdoor Activities": [
        "Do you like outdoor activities?",
        "What outdoor sports do you like?",
        "How much time do you spend outdoors every week?",
        "What types of outdoor activities are popular in your country?"
    ],
    "Patience & Politeness": [
        "What do you think patience is?",
        "Do you think patience is important?",
        "Do you think you are a patient person?",
        "Have you ever lost your patience?",
        "Are you a polite person?",
        "Who taught you to be polite?",
        "Is it important to be polite?",
        "What do you do if others are not polite to you?"
    ],
    "Public Transport": [
        "What kinds of public transport do you have in your country?",
        "What kinds of public transport do most people use?",
        "What is your favourite type of public transport?",
        "What do you do when you are travelling on public transport?",
        "How could public transport in your country be improved?"
    ],
    "Seasons": [
        "What is your favourite season?",
        "Tell me about the different seasons in your country.",
        "How do the clothes people wear in your country change with the seasons?",
        "Do any types of jobs people do in your country change with the seasons?",
        "Is tourism popular in a particular season in your country?",
        "What season (or weather) do you think is most suitable for work and/or study?"
    ],
    "Sports": [
        "Do you play any sports?",
        "Do you watch sports on TV?",
        "What is the most popular sport in your country?",
        "How do people in your country stay fit?",
        "Is it important for children to play sports?",
        "Is there a lot of sports on television in your country?",
        "What sports do children normally do at school?",
        "Do you think people do enough sport these days?"
    ],
    "The Internet": [
        "Do you use The Internet?",
        "Are children allowed to use The Internet at school in your country?",
        "Do you think that The Internet is useful for study?",
        "Have you ever used The Internet to buy something?",
        "Are there any dangers in buying things online?"
    ],
    "The Sea": [
        "Do you like to go on holiday by sea?",
        "Are there many hotels by the sea in your country?",
        "What kind of activities can people do by the sea?",
        "How long do people normally visit the sea when they go on holiday?"
    ],
    "Timing": [
        "Is being late acceptable in your culture?",
        "Are you ever late for appointments?",
        "What type of excuses do you think are alright for lateness?",
        "How do you feel when someone is late for an appointment with you?",
        "What is the importance of being on time?"
    ],
    "TV Programs": [
        "Do you like watching TV?",
        "How often do you watch TV?",
        "What types of TV programmes are popular in your country?",
        "What is your favourite TV programme?",
        "Do you like to watch TV on your own or with others?",
        "Would you like to be on TV?"
    ],
    "Weather & Seasons": [
        "Do you have a favourite type of weather?",
        "What’s the weather like in your country?",
        "Is there any type of weather you really don’t like?",
        "Do you prefer hot or cold weather?",
        "What type of weather do you like most?",
        "What do you usually do during your favourite weather?",
        "What’s your favourite season?",
        "Do you like the weather in your country?"
    ],
    "Weekends": [
        "How do you usually spend your weekends?",
        "Which is your favourite part of the weekend?",
        "Do you think your weekends are long enough?",
        "How important do you think it is to have free time at the weekends?",
        "Do you do different things at the weekend now from when you were a child?"
    ],
    "Work/Job": [
        "Do you work or are you a student?",
        "What is your job?",
        "What do you do at your work?",
        "Do you enjoy your work?",
        "Why did you choose to do that job?",
        "What do you like most about your job?",
        "What do you dislike about your job?",
        "What was your first day at work like?",
        "What responsibilities do you have at work?",
        "Do you remember your first day at work?",
        "If you had the chance, would you change your job?",
        "Do you plan to continue with your job in the future?",
        "What is your typical day like at work?",
        "Is your job common in your country?",
        "Is your job popular in your country?",
        "Do you want to change your current job?",
        "Are there more young people or older people at your workplace?",
        "Is your job easy to get?",
        "Is your job easy?"
    ]
}
part_two = [
    ("Describe a time when you gave someone advice.", "You should say:", [
        "to whom you gave the advice",
        "what the advice was",
        "whether that person took your advice",
        "and explain why you gave the person that advice."
    ]),
    ("Describe an activity you enjoy doing on the weekends.", "You should address:", [
        "What the activity is and what it involves.",
        "When you first started doing the activity.",
        "Whether you do the activity alone or with other people.",
        "And explain why you enjoy the activity."
    ]),
    ("Describe your favorite method of travel.", "You should address:", [
        "What the method of travel is,",
        "How often you travel by this method.",
        "Whether this travel method is cheap or expensive.",
        "And explain why this method of travel is your favorite."
    ]),
    ("Describe your dream job.", "You should address:", [
        "What the job is.",
        "The job requirements.",
        "The activities that are done on the job.",
        "And explain why this job is your dream job."
    ]),
    ("Describe an important tradition in your family.", "You should address:", [
        "What the tradition is.",
        "How it's celebrated.",
        "When it's celebrated.",
        "And explain why the tradition is important to your family."
    ]),
    ("Describe a place you enjoy going to in your hometown.", "You should address:", [
        "Do you prefer to spend time at places in your hometown, or explore new places elsewhere?",
        "How often you go there.",
        "What you do there.",
        "And explain why you enjoy going to this place."
    ]),
    ("Describe your best friend.", "You should address:", [
        "Who this person is.",
        "How you met your best friend.",
        "How often you see this friend.",
        "And explain why this person is your best friend."
    ]),
    ("Describe your favorite season of the year.", "You should address:", [
        "Which season it is.",
        "What the weather is like during the season.",
        "What you like to do during the season.",
        "And explain why this season is your favorite."
    ]),
    ("Describe a snack food you enjoy.", "You should address:", [
        "What the food is.",
        "What it tastes like.",
        "How often you eat it.",
        "And explain why you enjoy this food."
    ]),
    ("Describe a song that's very meaningful to you.", "You should address:", [
        "The name of the song.",
        "Who sings it.",
        "What the song is about.",
        "And explain why the song is meaningful to you."
    ]),
    ("Describe a sport you find interesting.", "You should address:", [
        "What the sport is.",
        "Whether you play the sport, watch the sport, or both.",
        "How long you've been interested in the sport.",
        "And explain why you think the sport is interesting."
    ]),
    ("Describe a holiday that you celebrate with other people.", "You should address:", [
        "What the holiday is.",
        "Who you celebrate the holiday with.",
        "How you celebrate the holiday.",
        "And explain why you celebrate this holiday with other people."
    ]),
    ("Describe a technological device you recently purchased.", "You should address:", [
        "What the device is.",
        "What it can do.",
        "Whether you use the device for fun, for work, or both.",
        "And explain why you purchased the device."
    ]),
    ("Describe something you usually do at the beginning of the day.", "You should address:", [
        "What you do.",
        "Why you do it.",
        "How important it is.",
        "And explain why you do this thing at the beginning of the day."
    ]),
    ("Describe an important piece of furniture in your house.", "You should address:", [
        "What the piece of furniture is.",
        "How long you've had the furniture.",
        "Where it is in the house.",
        "And explain why that piece of furniture is important."
    ]),
    ("Describe a recent news story that surprised you.", "You should address:", [
        "What happened.",
        "When the story happened.",
        "Where the story happened.",
        "And explain why you found this news story surprising."
    ]),
    ("Describe a place where you often go shopping.", "You should address:", [
        "Where this place is.",
        "What you can buy there.",
        "How often you go there.",
        "And explain why you often shop at this place."
    ]),
    ("Describe a good decision you made.", "You should address:", [
        "What the decision was about.",
        "What you decided to do.",
        "Why you made the decision.",
        "And explain why you feel you made a good decision."
    ]),
    ("Describe a piece of art that you think is good.", "You should address:", [
        "What kind of art it is.",
        "What the art looks like.",
        "Where you saw the art.",
        "And explain why you think this piece of art is good."
    ]),
    ("Describe a gift that someone gave you.", "You should address:", [
        "Who gave you the gift.",
        "What the gift was.",
        "When you received the gift.",
        "And explain why the gift was given to you."
    ]),
    ("Describe a kind thing you did for someone.", "You should address:", [
        "What you did.",
        "Why you did it.",
        "How the person or people responded to your kind act.",
        "And explain the reasons that the act was kind."
    ]),
    ("Describe a time you had difficulty in learning a new language.", "You should address:", [
        "What language you were learning.",
        "What the difficulty was.",
        "Whether or not you overcame the difficulty.",
        "And explain why you found learning the language so difficult at the time."
    ])
]
part_three = {
    "A Challenging Thing You Did": [
        "What challenges do young people face today?",
        "How do (young people) handle difficult or challenging tasks?",
        "Which do you think is better, to face these difficulties and challenges alone or to seek the help of others?",
        "Do you think people need to be challenged?"
    ],
    "A Member of A Team": [
        "In a team, is it more important to pursue individual development or to achieve team targets?",
        "Do you think it's important for children to join teams to learn to cooperate with others?",
        "Do you think disagreements among team members have a great influence on teamwork?",
        "Can you suggest how teamwork could be cultivated in classes at school?"
    ],
    "Advertisements": [
        "What are popular types of advertising in today's world?",
        "What type of media advertising do you like most?",
        "Do you think advertising influences what people buy?",
        "What factors should be taken into account when making advertisements?",
        "Is advertising really necessary in modern society?",
        "How does advertising influence children?",
        "Is there any advertising that can be harmful to children?"
    ],
    "Animals": [
        "Why do people like to keep pets?",
        "What should we do to protect endangered animals?",
        "Do you support doing experiments on animals?",
        "Why do some people refuse to eat animals?",
        "What would happen when some species disappear on earth?",
        "Do you think that aquatic animals are dangerous?",
        "What is it like to be a professional athlete?",
        "A lot of animals are getting extinct these days. What do you think about this? Why is it happening?",
        "Earlier people used animals for their work. Now, what do people use to do their work?",
        "Research is being conducted on animals; is this a good idea?"
    ],
    "Art": [
        "How do people in your country feel about art?",
        "Do people in your country prefer music over art?",
        "What are some traditional art forms in your country?",
        "How has art changed in the past few decades in your country?",
        "Do you think children should study art in school?",
        "How can children benefit from learning about art?",
        "Do you think the government should provide support for art and cultural activities?",
        "How could art exhibitions attract more visitors?",
        "Are art exhibitions popular in your country?",
        "Do you think people should have to pay to visit art exhibitions?",
        "How will art exhibitions change in the future?",
        "What can you do to support an artist?"
    ],
    "Books": [
        "Do people read more nowadays?",
        "Do you read before going to bed?",
        "In your opinion, how will e-books affect paper books?",
        "What's the difference between films and books?",
        "What is one example of traditional literature in your country?",
        "Do you like reading the traditional literature of your country?",
        "Do you prefer books or movies?",
        "Do you think it is important to read the book before watching the movie version of it?",
        "Do boys and girls like the same kinds of books?",
        "What kind of books do Indian people like to read?"
    ],
    "Business": [
        "In your opinion, do business people have to work long hours?",
        "How do business people relax?",
        "How can a small business grow big?",
        "In your opinion, what kind of small businesses will young people have in the future?",
        "In your opinion, what skills are required to start a small business?",
        "What are the impacts of globalisation on small and large businesses?",
        "What qualities are required to become a company leader (or CEO or manager)?",
        "In general, what factors do you think to determine whether a small company will become successful or not?",
        "Do you think the latest technology plays an important role in a company's development?",
        "What do you think of charitable organisations?",
        "Which do you think is better, to start your own business or to work for someone else?"
    ],
    "Change": [
        "Do you think change is good?",
        "What are some of the major changes that occur to people throughout their lives?",
        "Is your country changing rapidly?",
        "In what ways have changes in technology changed people's lives?",
        "Why do old people not accept change?"
    ],
    "City": [
        "In your opinion, what makes a city a good one to live in?",
        "What are the advantages of living in a city?",
        "In your opinion, what are the negative aspects of crowded cities?",
        "How can governments improve living standards in crowded cities?",
        "What can people do to improve the air quality in the city?",
        "What are the advantages and disadvantages of living in tall buildings?",
        "Do you think there will be more tall buildings in the future?",
        "Why aren't there many tall buildings in the countryside?",
        "Why do some people like to live in tall buildings nowadays?",
        "Is it true that tall buildings are more beneficial than small buildings?",
        "Why do a lot of people enjoy going to crowded places?",
        "Where (or what) would you say is the most crowded place in your city?",
        "Would you say it's important for a city to have amusement (and/or recreational) facilities?",
        "Why do you think people choose to live in big cities (despite certain problems)?",
        "How do you think cities overseas are different from those in your country?",
        "Would you say urban planning is important?"
    ],
    "Clothes": [
        "Can clothing tell you much about a person in your country?",
        "Do people still wear traditional clothing in your country?",
        "How has clothing fashion changed in your country over the last few decades?",
        "Why do some companies ask their staff to wear uniforms?",
        "What are the advantages and disadvantages of having uniforms at work?",
        "For which jobs are people required to wear a uniform in your country?",
        "Do you think people are treated differently when they are in uniform?",
        "Where do people from your country buy clothes?",
        "What's the difference between men and women's choices of clothes?",
        "Do clothes affect people's mood?",
        "What do people consider when buying clothes?",
        "What would you say are the advantages and disadvantages of wearing a uniform?",
        "In your country, do schools provide similar uniforms to their students?",
        "What kinds of professionals need to wear uniforms?",
        "Do you think people wear clothes that reflect their personality?",
        "Do you think women's clothes show more variety than men's clothes?"
    ],
    "Company": [
        "What is the difference between big companies and small companies?",
        "Are there many big companies in your country?",
        "What are the good things about working for a big company?",
        "Should big companies be punished more seriously than small companies?",
        "Why do some people choose to work at an international company?",
        "How can a company maintain the quality of the service that it gives to the public?",
        "Do you think it's important for a company to provide after-sales service?"
    ],
    "Daily Routine": [
        "What are a few things that make you happy?",
        "Do you believe that engaging in artistic activities might make people happier? (Why/Why not)",
        "Do you think people who have more talent are happier than others? (Why/Why not)",
        "Do you think money makes people happy?",
        "Are the things or events that make people happy today the same as several decades ago?",
        "What are the benefits of getting up early?",
        "Why do some people like to stay up late?",
        "Do you think it is important to be punctual?",
        "What kind of situations need people to arrive early?",
        "Why do children and youngsters generally wake up late?",
        "Do you know anyone who likes to get up early?"
    ],
    "Decision": [
        "Why do some people find it hard to make decisions?",
        "How important is it to get advice from other people when making decisions?",
        "Why is it sometimes difficult to accept advice?",
        "What are some of the most important decisions young people have to make?",
        "Do you agree that parents should make important decisions for their children?",
        "Is it better to make a decision thinking about what you want or thinking about what other people want?"
    ],
    "Desired Change to Local Area": [
        "Why do old people not like changes?",
        "Do you think it's important for people to socialise with their neighbours?",
        "How do people socialise with their neighbours?"
    ],
    "Eating habits": [
        "Tell me about the types of food that people eat in your country.",
        "How are the eating habits now in your country different from eating habits in the past?",
        "How healthy is your country's food?",
        "Why do you think different cultures have different table manners?",
        "How may eating habits change in coming decades?",
        "Do you think our diet is important?",
        "What is a balanced diet?",
        "How might eating habits change in the coming decades?"
    ],
    "Education": [
        "How are education priorities today different from those in the past?",
        "What is your opinion on the way languages are taught in schools?",
        "How can the type of school you go to affect career success?",
        "What changes do you think will happen in the classroom in the near future?"
    ],
    "Electronic Devices": [
        "What are the most popular electronic devices in today's world?",
        "What devices do you think will be popular in the future?",
        "Do you think people spend too much money on electronic devices?",
        "In what ways can electronic devices make our lives harder?",
        "What would the world be like without computers?",
        "Should children be taught to use computers at school?"
    ],
    "Entertainment": [
        "Do you think traditional performances are important?",
        "What do you think is the difference between watching a live performance and watching it on TV?",
        "How do you think watching a dance performance or a stage play influences children?"
    ],
    "Environment": [
        "What are some of the main environmental problems in your county?",
        "Why should people be concerned about the environment?",
        "Is water pollution a problem in your country?",
        "What are some of the causes of water pollution?",
        "Do you think problems with the cleanliness of water will improve in the future?",
        "How can people protect the environment?",
        "Do you think money should be spent on protecting animals?",
        "Do you think more should be done to protect natural scenic spots in your country?",
        "What can individuals do to try and ensure water is kept clean?"
    ],
    "Events": [
        "What rewards can children get from school?",
        "Should parents push their children to get prizes?",
        "Is it good for children to compete for prizes at school?",
        "What kinds of rewards can companies offer to their outstanding employees?",
        "Is it good to have competition?",
        "What are the most common resolutions in your country?",
        "How difficult would it be for you to save money this year?",
        "How difficult would it be for you to get fit this year?",
        "What do you think this year will be like for you?",
        "Do you personally think that resolutions help us achieve our goals?",
        "What are the benefits of taking New year resolutions?",
        "Describe an event that you attended recently.",
        "Describe an important choice you had to make in your life.",
        "Describe a very difficult task that you succeeded in doing.",
        "Describe an interesting discussion you had related to your work or studies."
    ],
    "Exciting Experience": [
        "Can you compare some exciting activities people do now with activities people did 20 years ago?",
        "Why do some people enjoy doing dangerous sports?",
        "Do you think some dangerous activities should be banned?",
        "Should people try doing new things?",
        "What problems can people have when they try new activities for the first time?",
        "Do you think it's best to do new things on your own or with other people?",
        "Do people in your country spend a lot of money on celebrating birthdays?",
        "Do you think it's necessary to spend a lot of money on holding a party?",
        "Do people in your country usually go out to celebrate traditional festivals with others?"
    ],
    "Family": [
        "Is family important in your country?",
        "Who should be responsible to care for the elderly? Should it be the family or the government?",
        "How has the size of the average family changed in your country in the last few decades?",
        "How do you think families will change in the future?",
        "Should husbands and wives have different roles within the family?",
        "What role do grandparents play in the family in your country?",
        "What qualities does a person need to have to take care of old people?",
        "Do you think old people should be taken care of at home?",
        "How can people in the neighbourhood help the elderly during an epidemic?",
        "Do you see this kind of help occurring in your neighbourhood?",
        "Do you think teenagers must indulge in building a community for elderly?",
        "What kind of jobs need physical activity?",
        "Can physical workers have higher salaries in the future?",
        "Do you think machines could replace manual labour in the future?",
        "What's the difference between payment for physical work and payment for mental work?",
        "How can a person's energy affect others?",
        "Do you think children are born smart or do they learn to become smart?",
        "How do children become smart at school?",
        "Why are some people well-rounded and others only good at one thing?",
        "Why does modern society need talent of all kinds?",
        "How can we assist youngsters in realising their potential?",
        "Who is the head of the family in your culture?",
        "Are men better at decision-making in a family?",
        "How do you see leadership qualities now and in the future?",
        "Do you think that in the future there will be more women leaders?",
        "Should a leader discuss with team members when making decisions?",
        "What are the advantages of strong family relationships?",
        "How many generations are usually living under one roof in your country?",
        "What are the benefits, and drawbacks of a family of several generations living together?",
        "Do both parents have equal responsibilities in taking care of their children?"
    ],
    "Festival": [
        "What is the importance of traditional festivals?",
        "What is the difference between festivals that are celebrated now and in the past?",
        "Do you think festivals like Christmas are replacing traditional festivals in your country?",
        "Do you think it is wrong for children to not celebrate traditional festivals?",
        "Do you think teens should learn about traditions?",
        "Do you think the traditions in your country are restricted, especially for women in any sense?"
    ],
    "Food": [
        "What are the types of food that people eat in your country?",
        "What about foreign food? What kinds of foreign food are popular in your country?",
        "In your country, is it important to have a meal together with your family?",
        "Is food now better than in the past?",
        "What kind of people would like to go to a cafe?",
        "Why do young people like studying in a cafe instead of at home?",
        "Do older people like to drink coffee?",
        "Do Indian people like to drink coffee?",
        "Does the taste of coffee vary by country?"
    ],
    "Friends": [
        "What is the importance of friends?",
        "Would you like to have a few very good friends or a lot of just friends?",
        "If you had a problem, would you go to your friends or family? Why?",
        "Do you think it is always better to talk to your friends about such a problem?",
        "Is it important to have friends from other countries?"
    ],
    "Furniture" : [
        "In what situations do people in your country buy furniture?" ,
        "In families in your country, who usually decides what furniture to buy for the home?" ,
        "How do people in your country decide what furniture to buy for the home or office?" ,
        "Do people in your country prefer traditional or modern styles of furniture?"
    ],
    "Health" : [
        "How can people improve their health?" ,
        "Do elderly people exercise much in your country?" ,
        "Do you think all illnesses can be prevented?" ,
        "Do you think that illnesses will be less common in the future?",
        "Do you think healthcare should be free?" ,
        "What makes someone a good doctor?" ,
        "Why is it that different people want to see different magazines?" ,
        "What type of magazines do teens prefer to read?",
        "What is the distinction between information on TV and information in magazines?",
        "Do folks like to read the information on the World Wide Web?",
        "Do people still purchase magazines in their own country?",
        "Do you feel that people now are healthier than people previously?",
        "Do you think we have to restructure our lifestyle to improve our health?",
        "How do you think people could become healthier?",
        "Are there any differences between the way old people and young people try to stay healthy?",
        "Do schools in your country have any special activities to enhance the fitness of students?",
        "Do you think people in the future will be doing more exercise and eating healthier than they are today?"
    ],
    "Help" : [
        "Do you like helping others?",
        "Do you think people are less willing to help others these days compared to the past?",
        "Do people today trust others as much as they used to in the past?",
        "How do people in your community help each other?",
        "Let’s move on to the topic of educating children to help people. In your view, should children be taught to help others?",
        "In your opinion, how can we encourage children to help others?",
        "What about students? How can students, such as high-school students, help each other?"
    ],
    "History" : [
        "Do you think history is important?",
        "Do you like to learn about history?",
        "What do you think we can learn by studying history?",
        "Let’s move on to different ways of learning about history. In your opinion, how can people learn about history?",
        "Do you think people can learn history from films or TV programs?",
        "Do you think the internet is a good place to learn about history?",
        "What is the effect of technology on how people learn about history?"
    ],
    "Holiday" : [
        "First of all, why do people go on holiday?",
        "How important is it for families to go on holiday together?",
        "Why do some people go on holiday alone?",
        "How have holidays changed over the past few decades?",
        "What kind of holidays will be popular in the future?",
        "Let’s move on to talk about taking holidays in a foreign country. Do you think is it better to take a holiday in your own country or in a foreign country?",
        "What problems can people have on holiday in a foreign country?"
    ],
    "Home" : [
        "Why do people move to a new home?",
        "What problems do people face after moving to a new place?",
        "What are the advantages and disadvantages of living in the same place?",
        "Is it good to move to a new place frequently? Why?",
        "Do you think it’s better to rent or to buy a place to live in?",
        "How easy is it to find a place to live in your country?",
        "Do you agree that there is a right age for young adults to stop living with their parents?",
        "What options are available to young couples looking for accommodation in your country?",
        "What are some of the pleasures involved in making a home for ourselves?"
    ],
    "Influence" : [
        "What types of people influence the young in your country?",
        "What type of people, such as parents, teachers, or friends, are best to influence young people’s behaviour?",
        "Why is it important for young people to have role models?",
        "What do you think young people will be influenced by the most in the future?",
        "Why is it important to have role models?",
        "Do you think the education system in your country influences young people’s behaviour?",
        "What type of person (parents, teachers, friends etc) are best to influence young people’s behaviour?",
        "What do you think young people will be most influenced by in the future?"
    ],
    "Internet" : [
        "How do you think the Internet will change people’s buying habits in the future?",
        "What are the pros and cons of shopping online?",
        "Is the Internet important for education?",
        "Do you think parents should supervise their children’s use of the Internet?",
        "What’s the best age for children to use the Internet?",
        "Why do children start using the Internet very early nowadays?",
        "Let’s move on to what people do on the Internet. What do you think people do on the Internet?",
        "What about elderly people? Do elderly people use the Internet very much?",
        "What can people do on social media?",
        "Do you think older people and younger people will use the same kind of social media software?",
        "Do older people spend much time on social media?",
        "Are non-social media like television and newspapers still useful?",
        "What are the advantages and disadvantages of using social media?"
    ],
    "Job" : [ 
        "How do you think AI (artificial intelligence) will affect people’s work?",
        "What would you say are the important factors to consider when choosing a career?",
        "That technology will make some people lose their jobs. How do you think this problem should be handled?",
        "Would you ever move to work and live in another city?",
        "Is it common in your country for people to move to other cities because of work?",
        "When young people choose their jobs, which do you think is usually more important, the salary or their interest in the work?"
    ],
    "Late" : [
        "What is the general attitude towards arriving somewhere late in your country?",
        "What is an example of a time when it is very important for people to arrive on time in your country?",
        "Can you suggest some ways to make sure you are not late for anything?",
        "Let’s move on to how modern technology influences the way that people manage time. Do you think computers make it easier or more difficult to manage time?",
        "How can modern technology help people arrive early?",
        "Do you think it is easy to manage your time in the modern world?"
    ],
    "Leisure activities": [
        "What types of leisure activities are popular in your country?",
        "Why is it important for people to have time for leisure activities?",
        "Why are some activities more popular than others?",
        "Are the types of leisure activities that are popular today the same as those that were popular when your parents were young?",
        "What types of leisure activities may become more popular in the future?",
        "Do you think (watching) films have (has) any educational benefits?",
        "In what ways are documentary films and films only for entertainment different?",
        "Why do you think documentary films are not so popular?",
        "How are movies and real life different?",
        "Do men and women watch the same kind of films?",
        "Do different age groups like the same kind of films?",
        "Do you like any particular film star? Why?",
        "Do you like movie stars who were treated like God?"
    ],
    "Machine" : [
        "What kinds of machines are used for housework in modern homes in your country?",
        "How have these machines benefited people? Are there any negative effects of using them?",
        "Do you think all new homes will be equipped with household machines in the future? Why?",
        "Let’s move on to technology. Do you think people rely too much on technology?",
        "Do you think men and women view technology differently?",
        "Finally, let’s talk about the impact of technology on employment. How have developments in technology affected employment in your country?",
        "Some people think that technology has brought more stress than benefits to employed people nowadays. Do you agree or disagree with this statement?",
    ],
    "Memory" : [
        "Do you think it’s important to have a good memory?",
        "Why do sometimes people forget things?",
        "Which do you think is more important to remember, a business meeting or a meeting with a friend?",
        "Are there any things that are especially important for people to memorise?",
        "Let’s move on from memory to family history. Why do people want to remember their family history?",
        "What can you do to learn more about your family history?"
    ],
    "Mobile phones" : [
        "Do you think there should be regulations on the use of mobile phones?",
        "What do you think of primary school students owning a mobile phone?",
        "What (minimum) age do you think is appropriate for owning a cell phone?"
    ],
    "Money" : [
        "Is money important to you?",
        "What is the relationship between money and power?",
        "Let’s move on to teaching children about money. How do you think parents can teach the value of money to their children?",
        "Do you think it is important to teach children money skills?",
        "Should we let children buy whatever they want with money they’ve saved?"
    ],
    "Music" : [
        "What kind of music is popular in your country?",
        "How does pop music now compare to when you were growing up?",
        "Is foreign music or music from your country more popular with people your age?",
        "Let’s move on to the role of government on music. Do you think is it necessary for the government to require all children to learn music?",
        "Do you think the government needs to do more to preserve traditional music? What could they do?",
        "Finally, let’s talk about illegal downloading of music. There’s a lot of pirated music. Do you agree that we should support official music?",
        "What are some possible advantages and disadvantages of being stricter about the illegal downloading of music?",
        "Do you think CDs will have any role in the music industry in the future?",
        "Do singers play an important role in your country?",
        "Do you think celebrities have a lot of income?",
        "In your country, do people prefer to listen to traditional music or foreign music?",
        "Do you prefer live performances?",
        "What do you think about the role of singers on the national level?",
        "What types of songs are the most popular among today’s young generation in your country?",
        "Why do you think pop music is so popular?"
    ],
    "News" : [
        "How do people get their news in today’s society?",
        "How do you think people will get their news in the future?",
        "How does modern technology affect the delivery of news?",
        "Do you believe everything you read in the newspaper?",
        "Let’s move on to the topic of good news. In your opinion, when do people share good news?",
        "How do people share good news?",
        "What is the difference between new media and old media?",
        "Do you think the contents in the newspapers are reliable?",
        "Do you think it’s necessary for people to watch foreign news?",
        "How has social media changed how we consume news?",
        "What kinds of (famous) people are usually in the news in your country?"
    ],
    "Parenting" : [
        "For parents, what is important when bringing up their children?",
        "Do you think mothers and fathers have different roles to play in bringing up a child?",
        "Let’s move on to the education of children. Do you think hitting children is sometimes necessary for discipline?",
        "Do you think sweets are a good thing to reward children with?"
        "Do you think parents spend too much on buying toys for their children?"
    ],
    "Party" : [
        "When do people usually have parties in your country?",
        "What makes a good party?",
        "What are the main reasons why people organise family parties in your country?",
        "In some places people spend a lot of money on parties that celebrate special family events. Is this ever true in your country? Do you think this is a good trend or a bad trend?",
        "How important is it to celebrate important events with a group of people?",
        "Why do some people think that national celebrations are a waste of government money? Do you agree or disagree with this view? Why?",
    ],
    "Personal" : [
        "What decisions do people generally make in their daily life?",
        "Which is easier, making a decision by oneself or making a decision after a group discussion?",
        "Why are many young people unwilling to listen to their parent’s advice?",
        "Why do middle-aged people tend to second guess their decision?",
        "Should people consider the consequences of their decisions that impact others or only think of themselves?",
        "Do you think adults can have lots of imagination?",
        "Do you think imagination is necessary for scientists?",
        "What kind of jobs need imagination?",
        "What subjects are helpful for people’s imagination?",
        "Do you think children can have a good imagination level ?",
        "Do children like to change opinions?",
        "Why do people change their opinion?",
        "Who do young people turn to for advice?",
        "Do people like giving an opinion about politics?",
        "Is changing opinions good for society?",
        "On what occasions do people usually need to wait?",
        "Who behaves better when waiting, children or adults?",
        "Compared to the past, are people less patient now, why?",
        "What are the positive and negative effects of waiting on society?",
        "Are you a patient person?",
        "Do you think it is possible to teach people to be more patient?",
        "Some people believe that impatience helps the development of technology. Do you agree with that?– Why do you think so?",
        "Where do you go to get good advice? ",
        "Whose advice do you follow more parents or your friend’s advice?",
        "Have your parents given you much advice?",
        "What kind of advice do parents give their children?",
        "What kind of advice do friends give each other?",
        "What can we learn from our mistakes? ",
        "Do children make mistakes easily?",
        "What should parents do if their children make mistakes?",
        "What do children learn from teachers and parents?",
        "How should a person be remorseful for their mistakes?",
        "How do children benefit from using dictionaries?"
    ],
    "Plans" : [
        "In general, do you think planning is important?",
        "Do you think people should make highly detailed plans or just general plans?",
        "What types of people like to make plans?",
        "Why do you think some people dislike making plans?",
        "Let’s move on from planning to career plans. Do you think it’s important for a person to have a career plan?",
        "How do most people plan their futures in their education and careers?",
        "Do you think it’s important for young people to get advice from their parents when planning a career?"
    ],
    "Products" : [
        "What kinds of products are mostly imported into your country?",
        "In your opinion, why do some people like to buy imported products?",
        "Let’s move on to local products. What are some famous local products in your country?",
        "Do you think a country should make everything it needs or import some things?",
        "What are the disadvantages of a country producing everything it needs?",
        "Finally, let’s talk about globalisation. Do you think the globalisation of industries and commerce is a good thing?",
        "What are the impacts of globalisation on international trade?"
    ],
    "Restaurants" : [
        "Do many people eat in restaurants in your country?",
        "Why do some people enjoy eating out?",
        "Is it expensive to eat out in your country?",
        "Let’s move on from eating in restaurants to cooking at home. Do you like to cook at home?",
        "Nowadays, more and more people are unwilling to cook. Why is this happening?",
        "What’s the difference between restaurant food and home-cooked food?"
    ],
    "Rules" : [
        "Why do we have rules in society?",
        "Do you think it’s necessary to set up rules about overworking people?",
        "What are some examples of rules that exist in many families?",
        "What are some rules that exist in schools or workplaces in your country?",
        "Do you think that the students themselves should have a say in what kinds of school rules there are?"
    ],
    "School" : [
        "Is higher education too expensive in your country?",
        "Should all students pay for their university education?",
        "Can you compare the education your parents had with the education that you received?",
        "What changes do you think will happen in the classrooms of the near future?",
        "Let’s move on to university education. What advantages do universities bring to society?",
        "Which is more important, research or teaching?",
        "What makes a good university student?",
        "Do you think students should be taken to school by their parents or go by themselves?",
        "Should children rely on their parents or be independent?",
        "How can children become more independent?",
        "What is the effect if parents interfere with children’s life too much?",
        "How does changing school affect children?"
    ],
    "Science" : [
        "Do you think science is important?",
        "Do you think science can change our society?",
        "Which area of science has been the most important in the last one hundred years?",
        "Why do you think some inventions have not been successful in the marketplace?",
        "Do you think it’s good that new inventions are appearing so often?",
        "Do you think there will be any negative effects resulting from future technology?"
    ],
    "Shopping" : [
        "Is shopping a popular activity in your country?",
        "How have shopping habits changed over recent years?",
        "To what extent do you think advertising affects the way people shop?",
        "Do you think shopping habits are likely to change in the future?",
        "Why do some people prefer to purchase brand name products produced abroad?",
        "Is service better in large shops or in small shops?",
        "What do people do when they get bad service?"
    ],
    "Social Problems" : [
        "What social problems are there in your country?",
        "What about poverty? What can be done to alleviate poverty?",
        "Are there many charities in your country?",
        "Let’s move on to talk about the overpopulation problem. Why do so many people move to live in cities?",
        "What problems does overpopulation cause?",
        "Finally, let’s talk about crime. What is the difference between major and minor crime?",
        "Do you think all criminals should go to prison?"
    ],
    "Something Difficult to Use" : [
        "Do you often buy new things?",
        "Would you say that advertising makes people buy more news things than they would if there was no advertising?",
        "Do you think old(er) people have difficulties using some things that young people do not?"
    ],
    "Sports" : [
        "What types of sports are popular in your country?",
        "Do you think the types of sports that are popular will change in the future?",
        "Let’s move on to talk about some positive aspects of sports. In your opinion, what are the benefits of playing a sport?",
        "What about cultural aspects? How can sports bring people from different countries closer together?",
        "Do you think old people can keep fit by playing sports or exercising?",
        "Finally, let’s talk about the Olympic Games. How are the Olympic players trained in your country? Do they usually start training when they are born?",
        "Why would somebody dislike watching the Olympic Games?",
        "Do you think the types of sport that are popular will change in the future?",
        "How often do people go to buy clothes?",
        "Why do parents let their children play with puzzles?",
        "What kind of puzzles improve people’s intelligence?",
        "Why are detective stories attractive to people?",
        "Which do you think is better? A detective movie or its original novel?",
        "Which age group plays puzzles the most?",
        "What kinds of exercises do Indian people like?",
        "What characteristics do you think an athlete should have?",
        "Why are there so few top athletes?",
        "What’s the best way to become a top athlete?"
    ],
    "Shopping" : [
        "What are your thoughts about the trend that people buy new things instead of repairing the old ones?",
        "Is increasing consumerism a good trend?",
        "Do you think adults and youngsters’ shopping lists have a vast difference?",
        "Which products are most consumed in your country? Why?"
    ],
    "Study" : [
        "What skills do students need to master?",
        "Is it hard for students to learn new skills?",
        "Is it hard for old people to learn new skills?",
        "Is a good teacher very important for students’ learning experience? Why?",
        "What is necessary to learn and improve a skill?",
        "Why do some people have a better memory?",
        "Which can help people remember things better, words or photos?",
        "Can technology help people remember things better? How?",
        "How can people improve their memory?",
        "Should old people read books?",
        "What is the most important practical skill in modern society?",
        "What kind of job requires practical skills?",
        "What kinds of skills are difficult to learn?",
        "How can you teach your skills to others?"
    ],
    "Teacher" : [
        "How well-respected are teachers in your society?",
        "Do you think teachers get paid enough money in your country?",
        "What role should the teacher have in the classroom?",
        "In your opinion, what are the most important qualities for a good teacher to have?",
        "Let’s move on to teaching aspects. In your opinion, how can a teacher make lessons for children more interesting?",
        "Do you think computers will one day replace teachers in the classroom?"
    ],
    "Technology" : [
        "What’s the best invention in the past hundred years?",
        "What’s the influence of science on human life?",
        "What can individuals do for scientific research?",
        "What influence can international cooperation in science bring about?",
        "Do you think it is mandatory to teach science in schools?"
    ],
    "Text Message" : [
        "Why do some people dislike using text messages?",
        "Have the ways that people communicated with each other changed much in the last few decades?",
        "Why do people prefer texting as compared to phone calls?",
        "Do you think modern technology has any negative influence on communication?",
        "What do you think are some of the main differences between written communication and spoken communication?"
    ],
    "Things" : [
        "What kinds of possessions are considered high-status to people in your country?",
        "Were different possessions thought of as valuable in the past?",
        "Why do you think people need to show their status in society?",
        "Do advertisements give correct information, or do they encourage people to buy things that they may not need?",
        "Where can people hear a lot of noise?",
        "What may happen when someone listens to very loud music using headphones while they are running or hiking?",
        "What can be done to reduce traffic noise?",
        "Do you think the world will be noisier in the future?",
        "What rules should be imposed to reduce noise pollution in the near future?"
    ],
    "Time When Someone Apologised to You" : [
        "What kinds of people are most likely to say sorry?",
        "In what situations do you think people need to (or, should) apologise?",
        "What do you think of those people who don’t apologise very often?"
    ],
    "Traditional Products" : [
        "What different types of traditional products are produced in your country?",
        "In your opinion, why do traditional products attract tourists?",
        "Do you think there are benefits of traditional products to locals?",
        "Do you think the government should help in the promotion of traditional products?",
        "Let’s move on from traditional products to traditions. Do you think because of globalisation countries are adopting each other’s traditions?",
        "Did the traditional things of the past are of better quality than present day things?",
        "Do you think it is necessary to protect traditions?"
    ],
    "Transport" : [
        "How do most people travel long distances in your country?",
        "Have the types of transport people use changed much over the last few decades?",
        "What kinds of improvement have there been in transport in your country in recent years?",
        "Do you think transport is likely to continue to improve in the future?",
        "Have the types of transportation people use changed much over the last few decades?",
        "How has transportation improved in recent years?",
        "Do you think transportation is likely to continue to improve in the future?",
        "What is your take on introducing transportation passes?",
        "Let’s move on to the transportation system in your country. Is it faster to travel by public transportation or by car in your country?",
        "What are the impacts of Uber on transportation in your country?",
        "Do you think traffic jams would be reduced if people could travel on public transport for free?",
        "Why do you think more and more people prefer to travel by plane?",
        "What kinds of obstacles do you think some local governments have to face when they develop transportation infrastructure?"
    ],
    "Travel" : [
        "Why do some people prefer to travel abroad rather than travel in their own country?",
        "Do you think travelling to another country can change the way that people think?",
        "Do you think it’s safer to travel today than in the past?",
        "Let’s move on to tourism. What are some famous tourist spots in your country?",
        "What are the positive impacts of tourism in your country?",
        "What are the negative impacts of tourism in your country?",
        "What can you say about the future of the tourism industry in your country?",
        "Does the rating of the people influence their choice?",
        "How do people reserve rooms?",
        "What influences people’s choice of a hotel?",
        "What is the difference between a hotel in our country and a hotel abroad?",
        "Which feature is the most important facility you look for while staying in a hotel? "
    ],
    "TV" : [
        "Tell me about the types of programmes that are generally on television in your country.",
        "Do you think state or private television is better?",
        "Let’s move on from TV programmes to television in general. How has TV changed our lives?",
        "Do you think TV influences the way we think?",
        "Should children be allowed to watch a lot of TV?",
        "Are all people on TV famous?",
        "How popular is watching television in your country?",
        "Tell me about the types of programmes that are generally on television in your country.",
        "Why do people like watching television?",
        "What effects can watching television have on children?"
    ],
    "Vegetables" : [
        "What vegetables are common in your country?",
        "Do people like to grow vegetables in your country?",
        "How do people feel when they eat vegetables that they grew on their own?",
        "Let’s move on to the topic of organic vegetables. As we know organic fruits and vegetables are more expensive than conventional fruits and vegetables, but they are actually worth the extra cost. Do you think organic fruit deserves a higher price?",
        "Do you think the government should encourage farmers to grow more organic vegetables?"
    ],
    "Work" : [
        "Do you think job satisfaction is more important than your salary when choosing a job?",
        "What skills do you think are needed to get a good job these days?",
        "Do you think that women should be able to do the same jobs as men?",
        "What’s the difference between white-collar and blue-collar jobs?",
        "What jobs do you think are most valuable to society?"
    ]
}

while True:
    print("Which part do you want to practice?")
    user_input = input("Enter 'one' for part 1, 'two' for part 2, and 'three' for part 3 (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye <3")
        break
    
    # Part one random tools
    elif user_input.lower() == 'one':
        available_categories = list(part_one.keys())
        # Run the process 3 times
        for i in range(3):
            # Select a random category and remove it from the available categories
            ctgr_1 = random.choice(available_categories)
            available_categories.remove(ctgr_1)  # Remove the selected category to avoid repetition

            # Shuffle the list of answers in the selected category to ensure randomness
            answers = random.sample(part_one[ctgr_1], k=4)  # Pick 4 unique answers from the category

            print(f"Category: {ctgr_1}")
            
            # Loop 4 times for the answers in the chosen category
            for idx, ans in enumerate(answers, start=1):  # Start enumerating from 1
                tts = gTTS(text=ans, lang='en')
                filename = f"part1_topic{i+1}_q{idx}.mp3"  # Use a unique filename
                tts.save(filename)
                os.startfile(filename)
                print(ans)
                time.sleep(30)

            # Add a delay between the 3 runs if needed (skip the last message)
            if i < 2:
                print("Let's change the category\n")
                time.sleep(2)  # Adjust the sleep time between cycles if desired

    # Part two random tools
    elif user_input.lower() == 'two':
        main_prompt, instruction, sub_prompts = random.choice(part_two)
        print(" ")
        print(main_prompt)
        print(instruction)
        for sub_prompt in sub_prompts[:-1]:
            print(f"-{sub_prompt}")
        print(sub_prompts[-1])
        print("\nPlanning time: 1 minute")
        time.sleep(60)
        print(" ")
        print("No more planning time!! Speak now")
        print("Talking time: 2 minutes")
        time.sleep(120)        
        print("Time is up!")
        time.sleep(2)

    # Part three random tools
    elif user_input.lower() == 'three':
        available_categories_3 = list(part_three.keys())
        ctgr_3 = random.choice(available_categories_3)
        available_categories_3.remove(ctgr_3)  # Remove the selected category to avoid repetition
        # Shuffle the list of answers in the selected category to ensure randomness
        answers = random.sample(part_three[ctgr_3], k=4)  # Pick 4 unique answers from the category
        print(f"Category: {ctgr_3}")            
        # Loop 4 times for the answers in the chosen category
        for idx, ans in enumerate(answers, start=1):  # Start enumerating from 1
            tts = gTTS(text=ans, lang='en')
            filename = f"part3_q{idx}.mp3"  # Use a unique filename
            tts.save(filename)
            os.startfile(filename)
            print(ans)
            time.sleep(70)
    
    else:
        print("I can only respond to 'one', 'two', 'three', and 'exit' requests.")