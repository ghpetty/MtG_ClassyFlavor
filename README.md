## MtG_ClassyFlavor

A work-in-progress demo of using the flavor text of **Magic: The Gathering** cards to classify them by color, card type, and more. 

### Preamble

**Magic: The Gathering** is a fantasy card game created by _Wizards of the Coast_ where players cast powerful spells and summon creatures to do battle. There are currently over 25,000 unique cards in the game, with new ones printed each year. Cards in **Magic** are played by spending _mana_. There are five colors of mana in the game: White, Blue, Black, Red, and Green. The different colors correspond to different types of game mechanics and different "flavors" of magic. For example, Red mana grants powers over fire and lightning, allows the player to do direct damage to their opponent and summon fast, aggressive creatures. Black mana grants the powers of necromancy, allowing the player to kill their opponent's creatures and bring their own back from the dead. [Learn more about the game here!](https://magic.wizards.com/en/intro)

<img src="https://cards.scryfall.io/large/front/e/f/ef614cf8-8f97-4677-b32c-7556f40c75af.jpg?1687904849" alt="Lightning Elemental, a Red card. Image provided by Scryfall, copyright Wizards of the Coast." width="150"/> <img src="https://cards.scryfall.io/large/front/4/9/4950c3c2-80c1-4447-ac38-cf40f76b9545.jpg?1562198355" alt="Raise Dead, a Black card. Image provided by Scryfall, copyright Wizards of the Coast." width="150"/>

Each card has rules text describing how it works in the game. Many cards also possess _flavor text_ written in italics at the bottom of the card. Flavor text has no bearing on the rules, but provides a description relating to the characters or lore within the world of the game. In this project, I am investigating to what degree the flavor text of a card is related to its game mechanic properties: Based on flavor text alone, can we predict what color a card is? Whether it is a creature or spell? What abilities it has? 

This is a toy project to practice machine learning techniques with ScikitLearn and plotting with Seaborn and MatPlotLib. Hopefully we will uncover some interesting things about the **Magic** along the way!

All card images and data are trademarked and copyright by Wizards of the Coast, 2023. Card images and data are retrieved from [Scryfall](https://scryfall.com/), a powerfull database and search engine for the game.


