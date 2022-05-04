# LandsBetweenCompanion
# ********README IN PROGRESS********

Application providing Elden Ring players information about damage output and combat effectiveness against the game's enemies, including bosses and enemies found in the open world. 

Uses attributes and player loadout provided by the user to determine how effective a character's build would be against enemies' damage resistances and attributes.

## Contributors

- Brandon Tran <branjtran@gmail.com>
- Connor Davis <c.a.davi2874@gmail.com>

## Concepts Used
- REST API
- 

## Implementation

Step 1:
    A: User text input
        -Input all equipment, attributes
        -Attribute points -> equipment -> medallions
    B: Data Storage of all possible equipment
        -Prefix Tree (?) , classes for storing data
    C: Overall Calculation of player stats

Step 2:
    A: Data Storage for Enemies
        -List for now, more advanced later
        -Class for storage of data
    B: Calculation of resistances

Step 3:
    A: Listing of enemies by match up
        - UI via text
    B: Storing method algorithm