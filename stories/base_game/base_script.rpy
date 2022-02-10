# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

# name of the character.

define narrator = Character(_("Narrator"), color="#c8c8ff")

define me = Character("Me")


# Chapter 1 On discord

define town_hall = Character("Town Hall")

define discord_server = Character("discord")


# Chapter 2 Meetup

define meetup_speaker = Character("Meetup Speaker")


# Chapter 3 The Twitter Space

define lowtower = Character("Lowtower", color="#4eb886")

define kris = Character("Kris", color="#e2e22d")

define levi = Character("levi", color="#1f219c")


# Chapter 4 Web2 data breach

define news_anchor= Character("News Anchor")

define andrew = Character("Andrew")

define britney = Character("Britney")


# Chapter 6 DevDao Conf

define mc = Character("MC")

# Define vars that will change

default project = ""

default blockchain = ""

default blockchain_data = ""

default ux = ""

default protect = ""

default blockchain_data_resp = ""

default ux_resp  = ""

# Dev attributes

define os = "USER_OS"

define text_editor = "USER_TEXT_EDITOR"

define lang = "USER_LANG"

define mind = "USER_MIND"

define vibe = "USER_VIBE"

define clothing = "USER_CLOTHING"

define location = "USER_LOCATION"

define user_bg = "USER_BACKGROUND"

define industry = "USER_INDUSTRY"

define mind = "USER_MIND"

define dev_num = "USER_NUM"

define wallet = "REPLACE_USER_WALLET"

# The game starts here.

label start:

    # Your dev attrbuites

    # Show a background. This uses a placeholder by default, but you can

    # add a file (named either "bg room.png" or "bg room.jpg") to the

    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can

    # replace it by adding a file named "eileen happy.png" to the images

    # directory.

    # show eileen happy

    # These display lines of dialogue.

    narrator "gm fren"

    "Welcome to DevDaoStory, where you will play the role as a builder navigating the web3 space"

    "wagmi"

    scene discord

    with fade

    narrator "Chapter 1: Let's Build"

    town_hall "... and with that, DevDao Conf will be held in miami in 5 weeks!"

    discord_server "cheers!!!"

    town_hall "Can not wait to see what y'all will build!"

    scene devdao_location

    with fade

    me "Wow a new conference!"

    me "this will be great opportunity to show my new project"

    menu:

        me "wait what was I working on again..."

        "PLACE_HOLDER_1":

            $ project = "PLACE_HOLDER_1"

            jump lets_build

        "PLACE_HOLDER_2":

            $ project = "PLACE_HOLDER_2"

            jump lets_build

        "PLACE_HOLDER_3":

            $ project = "PLACE_HOLDER_3"

            jump lets_build


label lets_build:

    me "Thats right! I'm building a... [project]"

    me "I've only got 5 weeks to get ready for the conference."

    me "Let start building!"

    narrator "You open up your [os] laptop and launch your favorite text editor... [text_editor]"

    me "Ok let me put my [lang] skills to use."

    narrator "You begin to code the night away..."

    "Chapter 1 End"

    jump chapter_2


label chapter_2:

    scene black

    with dissolve

    narrator "Chapter 2: Local Meetup"

    scene discord

    with dissolve

    me "gm"

    me "Ah there is a meetup tonight! This will be great place to talk about my [project]"

    me "The community is very welcoming and will spark ideas"

    narrator "Later that night at the meetup..."

    meetup_speaker "... and that's why the future is multi-chain! Thank you"

    me "Wow what a great talk!"

    me "Really gets me thinking about which blockchain infrastructure to commit to for my project"

    menu:

        me "For my [project] I'm going to use this blockchain..."

        "Ethereum":

            $ blockchain = "Ethereum"

            jump post_meetup


        "Polkadot":

            $ blockchain = "Polkadot"

            jump post_meetup

        "Solana":

            $ blockchain = "Solana"

            jump post_meetup


        "Polygon":

            $ blockchain = "Polygon"

            jump post_meetup


        "Terra":

            $ blockchain = "Terra"

            jump post_meetup

        "Internet Computer":

            $ blockchain = "Internet Computer"

            jump post_meetup

        "Tezos":

            $ blockchain = "Tezos"

            jump post_meetup


        "Avalanche":

            $ blockchain = "Avalanche"

            jump post_meetup

        "Cardano":

            $ blockchain = "Cardano"


            jump post_meetup


label post_meetup:

    me "Yea [blockchain] will work for my [project]"

    me "Now let's build!"

    narrator "Energized from the meetup, and deciding on a chain sparks your enthusiasm"

    "Chapter 2 End"

    jump chapter_3

    return 



label chapter_3:

    scene black

    with dissolve

    narrator "Chapter 3: Twitter Spaces"

    scene discord

    with dissolve

    me "gm"

    me "First thing I do each morning is to check my phone"

    me "Woah look at this Twitter Space"

    me "Why web3 matters"

    me "*click*"

    scene twitter_space

    with fade

    lowtower "what is web3?"

    kris "Web3 is the internet owned by the builders and users, orchestrated with tokens."

    levi "Why do I need tokens? My web server is able to handle requests"

    kris "Tokens give users property rights: the ability to own a piece of the internet."

    lowtower "property rights? My code is just code there is no property."

    kris "Correct code on web2 servers are controlled by the centralized entity."

    kris "Blockchains are special computers that anyone can access but no one owns."

    levi "These `blockchains` sound cool but does anyone know how to use them?"

    levi "if you ask 10 developers to architect a system that leverages blockchain, you will get 10 different responses on how to build the system."

    me "*Request to Speak*"

    kris "Well looks like we have a developer here that has an opinion."

    me "Hello, yes... an interesting thought... what data should go on-chain?"

    menu:

        "The least amount of information possible":

            $ blockchain_data = "least"

            $ blockchain_data_resp = "That the least amount of information possible, in the most efficient way possible, should be stored on the blockchain."


            me "The least amount of information possible, in the most efficient way possible, should be stored on the blockchain."

            kris "Yes storing data on blockchains is generally expensive and slow."

            lowtower "Then why should i use it? My raspberry pi has more compute than your `public computer`."

            levi "Yup, Customers don't care about your architectural decisions, they care about value."

            jump kris_ender


        "Some data?":

            $ blockchain_data = "some"

            $ blockchain_data_resp = "That users can decide where to put their data"

            me "Let the developer decide, that's the beauty of the blockchain."

            kris "It's still early, as the ecosystem matures best practices will emerge."

            levi "Customers don't care about your architectural decisions, they care about value."

            lowtower "I don't see me moving my data off from my centralized server."

            jump kris_ender

        "All the data!":

            $ blockchain_data = "all"

            $ blockchain_data_resp = "That all data must be on-chain"

            me "All data, the blockchain is the source of truth."

            kris "Some applications will benefit from all data on-chain."

            lowtower "I don't see me moving my data off from my centralized server."

            levi "Customers don't care about your architectural decisions, they care about value."

            jump kris_ender


label kris_ender:

        kris "Tokens align network participants to work together toward a common goal — the growth of the network and the appreciation of the token."

        kris "This fixes the core problem of centralized networks, where the value is accumulated by one company, and the company ends up fighting its own users and partners."

        kris "Before Web 3, users and builders had to choose between the limited functionality of Web 1 or the corporate, centralized model of Web 2."

        kris "Web 3 offers a new way that combines the best aspects of the previous eras. It's very early in this movement and a great time to get involved."

        me "wagmi"

        me "thank you for hearing my thoughts, now it's time to build!"

        me "*Leave Space*"

        me "Wow what a great discussion"

        me "Got some great ideas on how to construct my data model for my [project]"


        me "Only got 3 more weeks until DevDaoConf!"

        "Chapter 3 End"

        jump chapter_4

# A web2 data breach  - customer focus (how you will protect customers)

label chapter_4:

    scene black

    with dissolve

    narrator "Chapter 4: Data Breach"

    scene discord

    with dissolve

    me "Hmm been a while since a web2 data breach, maybe the servers have been secured."

    narrator "They were not"

    narrator "couple of hours later..."

    news_anchor "Breaking news!!!"

    news_anchor "a big web2 company exposed the personal information of over 500 million users from 100 countries"

    news_anchor "It includes their phone numbers, full names, locations, birthdates, bios, and in some cases email addresses"

    news_anchor "A spokesperson confirmed that the data had been scrapped because of a vulnerability that the company patched last year."

    news_anchor "Our data is valuable, thus our teams need to do better in protecting our customers"

    news_anchor "Let's go to our expert panel, are centralized services good for customers?"

    andrew "Look centralized services produce network effects that create value for customers"

    britney "But what's the cost, it might be easy for me to post a picture to my friends, but now may data is exposed"

    andrew "It's a calculated risk, we don't want everyone to set up a server to post a picture via file transfer protocol. Centralization enables innovation."

    andrew "The biggest web2 companies have great products that their customers use daily."

    britney "Yes they have great products, but the incentives are not aligned."

    britney "A centralized company has to maximize profit for shareholders, not user experience, and if these are ever in conflict, profit will win out."

    britney "Blockchains provide a powerful new way to build networks where the network effects accrue as public goods, as they did in web1."

    andrew "Blockchains!! HA"

    andrew "With such poor user experience, I don't see centralized services going away."

    britney "I agree, centralization in itself is not bad"

    britney "the question is whether these central services become public goods or private goods"

    britney "blockchains provide a new way to build networks that combines the publicly-owned network effects of web1 with the advanced functionality of web2."

    news_anchor "Thank you panel! It seems centralization is here to stay. We'll be back after the break..."

    me "*Your [mind] mind ponders the interview*"

    me "Hmm some good points there. How should I handle user experience for my [project]"

    menu:

        "Develop centralized interface":

            $ ux = "centralized"

            $ ux_resp = "centralized interface"

            me "Centralization enables innovation!"

            me "Let me dictate how the project will play out"

        "Develop decentralized interface":

            $ ux = "decentralized"

            $ ux_resp = "decentralized interface"

            me "Should be a free for all, let the users decide!"

            me "Will have many interfaces for the project"

        "Develop distributed interface":

            $ ux = "distributed"

            $ ux_resp = "distributed interface"

            me "Should be no central endpoints, everything should be distributed"

            me "the community will share the same goal!"

    me "Ok let's get building!!"

    me "Only 2 more weeks until DevDaoConf!"

    jump chapter_5

label chapter_5:

    scene black

    with dissolve

    narrator "Chapter 5: Rug Pull"

    scene discord

    with dissolve

    me "Hmm been a while since a web3 rug pull, wagmi"

    me "*pulls out phone, to check twitter*"

    me "Ha spoke too soon..."

    me "*reads tweet*"

    me "RugGame just sold 500 ETH worth of NFTs and had 800 ETH in secondary sales. The Discord and website closed and the devs have disappeared."

    me "Wow these rug pulls are causing real harm to the community"

    me "Why are these rug pulls happening, would be worth doing some research"

    me "*Searches \"web3 rug pulls\"*"

    me "*clicks bunch of articles*"

    me "Rug Pulls: A problem statement"

    me "\"web3 relies on communities that are built on trust - trust on the founder, trust on the project's mission and trust on other community members\"."

    me "\"When the community founders and ambassadors see their communities as a cash grab opportunity, we see the failures of the web3 idealism.\""

    me "Good point, trust is the core of what we want from our products"

    me "Avoiding Rug Pulls at Web3, Part 2: Social Engineering"

    me "\"Social Engineering is the art of breaking systems by manipulating people instead of hacking code\""

    me "\"being malicious in many contexts is about not disclosing information that will lead ultimately to someone's loss\""

    me "Social engineering is not new, but the blockchain introduces vectors that can cause huge financial harm"

    me "hmm... for my [project] I should focus on protecting customers by..."

    menu:

        "Trusted third parties":

            $ protect = "umpires"

            me "Yes Trusted third parties, aka umpires will be needed"

            me "A computer can never be held accountable, so we need to have a human have the final say"

            jump chapter_5_end


        "Airdropping":

            $ protect = "airdrops"

            me "\"Show me the incentives and I will show you the outcome.\""

            me "Just need to make sure people are committed long term via airdrops"

            jump chapter_5_end


        "Auditing":

            $ protect = "auditing"

            me "Code is law!!! If the code is audited, then my customers will trust it"

            jump chapter_5_end


label chapter_5_end:

    me "Ok let's finish my [project]"

    me "DevDaoConf is next week!!"

    jump chapter_6

label chapter_6:

    scene black

    with dissolve

    narrator "Final Chapter: DevDaoStory"

    scene miami

    with dissolve

    me "Finally it's time for DevDao Conference!!!"

    me "Can't wait to tell my story!"

    me "Off to Miami we go!!"

    narrator "You bask in the sunlight of Miami"

    narrator "You enjoy the night walking down Miami beach, preparing to tell your story!"

    narrator "Morning comes, you make your way to the convention center..."

    mc "GM FRENS!"

    mc "Welcome to DevDaoConf!"

    mc "We cannot wait to hear YOUR Story!!"

    narrator "The conference goes on with an inspiring keynote embracing builders"

    narrator "Soon your slot has come up..."

    mc "Introducing DevDao holder [dev_num]"

    narrator "*claps*"

    me "GM"

    me "Today I will walk you through how i built my [project] using [blockchain]"

    me "I developed the [lang] code on my [os] using [text_editor] for 6 weeks"

    me "My [mind] mind helped me see the full picture"

    me "For data storage, I decided that..."

    me "[blockchain_data_resp]"

    me "this coupled with a [ux_resp]"

    me "provides a unique user experience"

    me "users can trust the [project] due to [protect]"

    me "These incentives ensure the users are commited."

    me "We are still early"

    me "Many great things will be coming"

    me "wagmi"

    me "Thank you for listening to my DevDaoStory"

    narrator "*cheers*"

    narrator "With that DevDaoConf has come to a close"

    narrator "I hope you enjoyed this story, and got a few ideas"

    narrator "Now it's time to go build"

    return 