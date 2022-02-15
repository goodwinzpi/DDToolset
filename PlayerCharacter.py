__Author__ == "goodwinzpi"

"""
PlayerCharacter should be able to:
  1. select a race which will contain ability modifiers and racial features (speed, darkvision, etc.)
  2. select a class (Hit dice, skills, equipment, class features, etc.)
  3. roll/point buy/arrange ability scores
  4. select skill proficiencies
  5. create backstory
  6. describe appearance
  7. develop backstory - assisted development via keywords/AI?
PlayerCharacter will require:
  1. A database containing the following tables:
    - Race, Primary Ability, Secondary Ability, Speed, DarkVision, Features,...
    - Class, Primary Ability, Secondary Ability
      - Equipment Table
      - Features Table
    - Skills, Ability, Description
"""
