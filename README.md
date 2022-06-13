# endless

This repo will become a roguelike fantasy card game that features a solo adventurer.  The player must guide this adventurer toward a randomly selected goal and then find safety.  Success is rewarded by treasure, new abilities, and further quests; failure means that all progress is lost.  

The Python package `cmd` should provide a natural framework for the interface; see https://pymotw.com/3/cmd/index.html.  

Card types
* Ability
* Item: Consumable or permanent objects that may help your adventurer.  May be used to bribe intelligent creatures so that they don't attack.  A few items are cursed; these take up space in your hand and can't be discarded.
* Event: May either help or harm.  Harmful events include traps or environmental hazards.  
* Location
* Creature
* Cache
* Quest
* Exit

Overall flow
* Choose an Ability.  
* Draw a Quest.  
* Draw cards until you find a Location.  
* Within a Location, you may find Events, Creatures, or Caches.  Events simply happen and change the game state as described.  Creatures must be fought or bribed.  Caches contain items.  
* When the next Location card is drawn, you move to that Location.  
* Move from Location to Location until the goal given on the Quest card is reached.  
* Once the goal has been achieved, keep moving until you find the Exit.  
* Play ends when the solo adventurer runs out of health or the exit is found after the goal has been achieved.  

Further thoughts that may not mesh with those above:
Three decks: locations, encounters, items
Locations have a number of exits, a number of encounters, and a number of items
Upon visiting a location, draw the encounters and items
Some monsters can be bribed with an item instead of fighting them
Note the total monster score of unbribed enemies; this is the number to beat
Roll dice and add bonuses from abilities and items
If you win, the monsters are discarded, you get the items, and you can draw location cards equal to the number of exits; select among these location cards
If you lose, your health decreases by 1, and you draw only one location and immediately move to it

Abilities include
carry an extra item (normally only some number can be carried)
have a bonus in combat
be able to identify potions
be able to read spell scrolls (take multiple times to use higher-level spells)
be able to avoid traps
draw an extra location card when moving

Gebbeth -- a shadow enemy appears in multiple quests and becomes progressively harder, overshadowing other boss monsters related to quests; can't be bribed

More thoughts
Taking further inspiration from Le Guin, let's say that there is an item called phrenite ore that gives you a big advantage in combat; the effect increases with the number of pieces of phrenite that you carry.  However, every time you use it, a shadow enemy is created.  The game will force you to use phrenite at least once in fighting a dragon (Yevaud -- the name should provide an indication for where some of these ideas are coming from).  These shadows persist in the game across quests until they are destroyed or the adventurer dies.  Speaking of player death, it is permanent in the roguelike sense, but all completed quests remain completed, and the first quest that the new PC undertakes is to recover the equipment of the last one.  


