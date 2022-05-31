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
