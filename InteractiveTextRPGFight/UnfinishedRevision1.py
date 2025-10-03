#⚠️ Copyright Notice
#This project is not open source. All rights reserved.
#No unauthorized use, modification, distribution, or commercial use permitted.
#Copyrighted to CosmicGrace (https://github.com/CosmicGrace)

import random #Imports the ability to pick at random

#Pre-defined variables needed in determining the outcome stats
turns = 0
dodge = 0
attack = 0
attacked = 0
wait = 0
missed = 0
blocked = 0
bled = 0
itemsUsed = 0
itemsSnatched = 0

#Useful funtions
inventory = [] #Inventory list of the item names (only user) [Weapon, Armor, etc...]
inventoryOccupied = 0 #counts the number of items in the inventory (only user)
def roller(x, y): #roller for chance based moves
  c = random.randint(x, y) #the randomizer
  return c #returns the output of the above randomizer #basic # roller

#actions to be used that are being predefined
class actions:
  healHealth = 0
  def damage (self):
  def heal (self, target, targetHealth, healType):
    if healType == "weak":
      healHealth
      targetHealth = 
    elif healType == "moderate":
    elif healType == "strong":
  def attack (self, attacker, target, targetDefense, attackerAttack, weapon, wpEffects):
    #target.health = target.health - (attackerAttack - targetDefense)
  def defend (self, attacker, target, targetDefense, attackerAttack, weapon): #defending, uses opponents defense into account
  def checkInv (self, inventory): #Checking inv
  def interactInv (self, inventory, itemSelected, whatDo, numOfInteractedItems): #Interacting with inv
    if whatDo == ("remove" or "drop" or "murder" or "destroy" or "yeet"): #removing an item from inv
    elif whatDo == ("use" or "grab" or "equip"): #using an item (weapon,potion,food)
  def gainEffect (self, effect, target, effectGiver, effectGiverName): #To gain an affect of any sorts, input effect characteristics

    
    
#Creator class functions
class charStuff:
  def __init__(self, name, baseHealth, health, baseDamage, damage, baseDefense, defense, inventory, userStatus, dodgeChance):
    self.name = name #name of the character
    self.baseHealth = baseHealth #starting health
    self.health = baseHealth #changeable health by other factors
    self.baseDamage = baseDamage #starting damage
    self.damage = baseDamage #changeable damage by other factors
    self.baseDefense = baseDefense #starting defense
    self.defense = baseDefense #changeable defense by other factors
    self.inventory = inventory #inventory of the character
    self.userStatus = userStatus #null to start but changes over time
    self.dodgeChance = dodgeChance #Calls the chance of dodging anything, may be affected by the thing being dodged
  def getInfo(self):
    info = f"""{self.name} health
    Health: {self.health}/{self.baseHealth}"""
    return info #Creates the basis of any character

class wpStuff: 
  def __int__ (self, name, type, damage, effect):
    self.name = name #Name of the weapon
    self.type = type #Either Sword, Spear, or Bow
    self.damage = damage #Damage of the weapon
    self.effect = effect #Any side effects? If none then "null"
    
class armorStuff: 
  def __int__ (self, name, material, reason, effect, weakTo, strongTo):
    self.name = name #name of the armor
    self.material =  material #The material does change factors
    self.reason = reason #what does this armor protect?
    self.effect = effect #How much does it resist?
    self.weakTo = weakTo #What weapon is it weak to? If none then "null"
    self.strongTo = strongTo #What weapon is it strong to? If none then "null"

class effects:
  def __int__ (self, effectName, tickDamage, length, ): #last 3 inputs can be 0 since the if statements will define that stuff
    self.effectName = effectName #calls the effect
    if effectName == "fire":
    elif effectName == "poison":
    elif effectName == "bleed":
