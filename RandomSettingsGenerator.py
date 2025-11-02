import os
import sys
import datetime
import json
import random
import conditionals
import inspect

funcs = dict(inspect.getmembers(conditionals, inspect.isfunction))

# open weights file
with open("weights.json", "r") as w:
    ganCasWeights = json.load(w)["ganonCastle"]

with open("weights.json", "r") as w:
    randWeights = json.load(w)["randomizer"]

with open("weights.json", "r") as w:
    enhaWeights = json.load(w)["enhancements"]

with open("weights.json", "r") as w:
    randEnhancementRando = json.load(w)["otherRando"]

with open("weights.json", "r") as w:
    hintWeights = json.load(w)["hints"]
    
with open("weights.json", "r") as w:
    condWeights = json.load(w)["conditionals"]

with open("weights.json", "r") as w:
    startWeights = json.load(w)["startingItems"]

#Gsnons Castle Settings here - BK and Bridge, currently Greg only for Rainbow as an option

chosenSettings = {}
if isinstance (ganCasWeights["ShuffleGanonBossKey"], dict):
    if len(ganCasWeights["ShuffleGanonBossKey"]) == 1:
        value = next(iter(ganCasWeights["ShuffleGanonBossKey"].keys()))
        chosenSettings["ShuffleGanonBossKey"] = int(value)
    else:
        chosenSettings["ShuffleGanonBossKey"] = int(
            random.choices(list(ganCasWeights["ShuffleGanonBossKey"].keys()), weights=list(ganCasWeights["ShuffleGanonBossKey"].values()))[0]
            )
else:
    chosenSettings["ShuffleGanonBossKey"] = int(ganCasWeights["ShuffleGanonBossKey"])

chosenSettings["LacsRewardOptions"] = 0

rewardsToUse = ""
if chosenSettings["ShuffleGanonBossKey"] == 7:
    rewardsToUse = "LacsStoneCount"
elif chosenSettings["ShuffleGanonBossKey"] == 8:
    rewardsToUse = "LacsMedallionCount"
elif chosenSettings["ShuffleGanonBossKey"] == 9:
    rewardsToUse = "LacsRewardCount"
elif chosenSettings["ShuffleGanonBossKey"] == 10:
    rewardsToUse = "LacsDungeonCount"
elif chosenSettings["ShuffleGanonBossKey"] == 11:
    rewardsToUse = "LacsTokenCount"

if rewardsToUse != "":
    if isinstance (ganCasWeights[rewardsToUse], dict):
        if len(ganCasWeights[rewardsToUse]) == 1:
            value = next(iter(ganCasWeights[rewardsToUse].keys()))
            chosenSettings[rewardsToUse] = int(value)
        else:
            chosenSettings[rewardsToUse] = int(
                random.choices(list(ganCasWeights[rewardsToUse].keys()), weights=list(ganCasWeights[rewardsToUse].values()))[0]
                )
    else:
        chosenSettings[rewardsToUse] = int(ganCasWeights[rewardsToUse])

if isinstance (ganCasWeights["RainbowBridge"], dict):
    if len(ganCasWeights["RainbowBridge"]) == 1:
        value = next(iter(ganCasWeights["RainbowBridge"].keys()))
        chosenSettings["RainbowBridge"] = int(value)
    else:
        chosenSettings["RainbowBridge"] = int(
            random.choices(list(ganCasWeights["RainbowBridge"].keys()), weights=list(ganCasWeights["RainbowBridge"].values()))[0]
            )
else:
    chosenSettings["RainbowBridge"] = int(ganCasWeights["RainbowBridge"])

chosenSettings["BridgeRewardOptions"] = 0

rainbowRewards = ""
if chosenSettings["RainbowBridge"] == 2:
    rainbowRewards = "StoneCount"
elif chosenSettings["RainbowBridge"] == 3:
    rainbowRewards = "MedallionCount"
elif chosenSettings["RainbowBridge"] == 4:
    rainbowRewards = "RewardCount"
elif chosenSettings["RainbowBridge"] == 5:
    rainbowRewards = "DungeonCount"
elif chosenSettings["RainbowBridge"] == 6:
    rainbowRewards = "TokenCount"

if rainbowRewards != "":
    if isinstance (ganCasWeights[rainbowRewards], dict):
        if len(ganCasWeights[rainbowRewards]) == 1:
            value = next(iter(ganCasWeights[rainbowRewards].keys()))
            chosenSettings[rainbowRewards] = int(value)
        else:
            chosenSettings[rainbowRewards] = int(
                random.choices(list(ganCasWeights[rainbowRewards].keys()), weights=list(ganCasWeights[rainbowRewards].values()))[0]
                )
    else:
        chosenSettings[rainbowRewards] = int(ganCasWeights[rainbowRewards])

#Triforce Hunt Settings
if isinstance (ganCasWeights["TriforceHunt"], dict):
    if len(ganCasWeights["TriforceHunt"]) == 1:
        value = next(iter(ganCasWeights["TriforceHunt"].keys()))
        chosenSettings["TriforceHunt"] = int(value)
    else:
        chosenSettings["TriforceHunt"] = int(
            random.choices(list(ganCasWeights["TriforceHunt"].keys()), weights=list(ganCasWeights["TriforceHunt"].values()))[0]
            )
else:
    chosenSettings["TriforceHunt"] = int(ganCasWeights["TriforceHunt"])

if chosenSettings["TriforceHunt"] == 1:
    if isinstance (ganCasWeights["TriforceHuntTotalPieces"], dict):
        if len(ganCasWeights["TriforceHuntTotalPieces"]) == 1:
            value = intnext(iter(ganCasWeights["TriforceHuntTotalPieces"].keys()))
            chosenSettings["TriforceHuntTotalPieces"] = int(value)
        else:
            chosenSettings["TriforceHuntTotalPieces"] = int(
                random.choices(list(ganCasWeights["TriforceHuntTotalPieces"].keys()), weights=list(ganCasWeights["TriforceHuntTotalPieces"].values()))[0]
                )
    else:
        chosenSettings["TriforceHuntTotalPieces"] = int(ganCasWeights["TriforceHuntTotalPieces"])
    if isinstance (ganCasWeights["TriforceHuntRequiredPieces"], dict):
        if len(ganCasWeights["TriforceHuntRequiredPieces"]) == 1:
            value = int(next(iter(ganCasWeights["TriforceHuntRequiredPieces"].keys())))
        else:
            value = int(
                random.choices(list(ganCasWeights["TriforceHuntRequiredPieces"].keys()), weights=list(ganCasWeights["TriforceHuntRequiredPieces"].values()))[0]
                )
    else:
        value = int(ganCasWeights["TriforceHuntRequiredPieces"])
    chosenSettings["TriforceHuntRequiredPieces"] = int(int(value * chosenSettings["TriforceHuntTotalPieces"])/100)
    
#Shuffles Randomiser Settings
for setting, options in randWeights.items():
    #If dictionary
    if isinstance(options, dict):
        #If only one option
        if len(options) == 1:
            # Uses only that option and skips randomly choosing
            single_value = next(iter(options.keys()))
            chosenSettings[setting] = int(single_value)
        else:
            # Chooses randomly if more than 1 option
            chosenSettings[setting] = int(
                random.choices(list(options.keys()), weights=list(options.values()))[0]
            )

    # If defined as a single option without a weight, choose that option only
    else:
        chosenSettings[setting] = int(options)

#RandoEnhancementSettings
chosenRandoEnhancement = {}
for setting, options in randEnhancementRando.items():
    #If dictionary
    if isinstance(options, dict):
        #If only one option
        if len(options) == 1:
            # Uses only that option and skips randomly choosing
            single_value = next(iter(options.keys()))
            chosenRandoEnhancement[setting] = int(single_value)
        else:
            # Chooses randomly if more than 1 option
            chosenRandoEnhancement[setting] = int(
                random.choices(list(options.keys()), weights=list(options.values()))[0]
            )

    # If defined as a single option without a weight, choose that option only
    else:
        chosenRandoEnhancement[setting] = int(options)

#Enhancements may need something special doing, maybe check if it's in enhancements or rando or other areas: use array for this
inRandoSettings = {"FullWallets", "BlueFireArrows", "SunlightArrows", "CompleteMaskQuest", "BigPoeTargetCount", "EnableBombchuDrops", "InfinityUpgrades", "GsExpectSunsSong", "CompleteMaskQuest", "SkipEponaRace", "SkipScarecrowsSong"}
chosenEnhancements = {}

for enhancement, options in enhaWeights.items():
    #If dictionary
    if isinstance(options, dict):
        #If only one option
        if len(options) == 1:
            # Uses only that option and skips randomly choosing
            single_value = next(iter(options.keys()))
            chosenEnhancements[enhancement] = int(single_value)
        else:
            # Chooses randomly if more than 1 option
            chosenEnhancements[enhancement] = int(
                random.choices(list(options.keys()), weights=list(options.values()))[0]
            )

    # If defined as a single option without a weight, choose that option only
    else:
        chosenEnhancements[enhancement] = int(options)

for starting, options in startWeights.items():
    #If dictionary
    if isinstance(options, dict):
        #If only one option
        if len(options) == 1:
            # Uses only that option and skips randomly choosing
            single_value = next(iter(options.keys()))
            chosenSettings[starting] = int(single_value)
        else:
            # Chooses randomly if more than 1 option
            chosenSettings[starting] = int(
                random.choices(list(options.keys()), weights=list(options.values()))[0]
            )

    # If defined as a single option without a weight, choose that option only
    else:
        chosenSettings[starting] = int(options)

chosenHints = {}

for hint, options in hintWeights.items():
    #If dictionary
    if isinstance(options, dict):
        #If only one option
        if len(options) == 1:
            # Uses only that option and skips randomly choosing
            single_value = next(iter(options.keys()))
            chosenHints[hint] = int(single_value)
        else:
            # Chooses randomly if more than 1 option
            chosenHints[hint] = int(
                random.choices(list(options.keys()), weights=list(options.values()))[0]
            )

    # If defined as a single option without a weight, choose that option only
    else:
        chosenHints[hint] = int(options)

#Conditional Settings Here
if 'condWeights' in globals() and condWeights:
    for name, cparams in condWeights.items():
        func = funcs.get(name)
        if func:
            result = func(chosenSettings, cparams=cparams)
            if isinstance(result, dict):
                chosenSettings.update(result)


#Writes to the shipofharkinian.json
data = json.load(open("shipofharkinian.json"))
data["CVars"]["gRandoSettings"].update(chosenSettings)
data["CVars"]["gRandoSettings"].update(chosenHints)
data["CVars"]["gRandoEnhancements"].update(chosenRandoEnhancement)
for setting in chosenEnhancements:
    if (setting in inRandoSettings):
        data["CVars"]["gRandoSettings"][setting] = chosenEnhancements[setting]
    else:
        data["CVars"]["gEnhancements"][setting] = chosenEnhancements[setting]
with open("shipofharkinian.json", "w") as f:
    json.dump(data, f, indent=4)
