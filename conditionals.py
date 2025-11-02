import os
import sys
import datetime
import json
import random

gregBridgeSettings = {2, 3, 4, 5}
gregGBKSettings = {7, 8, 9, 10}

def select_one_pots_crates_freestanding(random_settings, **kwargs):
    chance_one_is_on = int(kwargs['cparams'][0])
    setting_weights = [int(x) for x in kwargs['cparams'][1].split('/')]
    weights = [int(x) for x in kwargs['cparams'][2].split('/')]

    # If setting is randomized off, return
    if not (random.randint(0, 100) < chance_one_is_on):
       return

    # Choose which of the settings to turn on
    allSettings = ["ShufflePots", "ShuffleCrates", "ShuffleFreestanding"]
    chosenSetting = random.choices(allSettings, weights=setting_weights)[0]
    chosenValue = random.choices([1, 2, 3], weights=weights)[0]

    for s in allSettings:
        random_settings[s] = chosenValue if s == chosenSetting else 0
        
    return {s: random_settings[s] for s in allSettings}
	
def fishing_pond_shuffles_rod(random_settings, **kwargs):
    if (kwargs['cparams'][0] == False):
    	return
    if (random_settings["Fishsanity"] == 2 or random_settings["Fishsanity"] == 4):
    	random_settings["ShuffleFishingPole"] = 1
    else:
    	random_settings["ShuffleFishingPole"] = 0
    return {random_settings["ShuffleFishingPole"]}

def shuffle_fish_age_split(random_settings, **kwargs):
    random_settings["FishsanityAgeSplit"] = 0
    if (kwargs['cparams'][0] == False):
        return {random_settings["FishsanityAgeSplit"]}
    if (random_settings["Fishsanity"] == 2 or random_settings["Fishsanity"] == 4):
        chance_enabled = kwargs['cparams'][1]
        if (random.randint(0, 100) >= chance_enabled):
            random_settings["FishsanityAgeSplit"] = 1
    return {random_settings["FishsanityAgeSplit"]}

def master_quest_dungeons(random_settings, **kwargs):
    random_settings["MQDungeons"] = 0
    if (kwargs['cparams'][0] == False):
        return (random_settings["MQDungeons"])
    if not (isinstance(kwargs['cparams'][0], bool)):
        random_enable = random.randint(0, 100)
        if (random_enable >= kwargs['cparams'][0]):
            return (random_settings["MQDungeons"])
    mqSettings = ["MQDungeons", "MQDungeonCount"]
    if (kwargs['cparams'][2] == "set"):
        random_settings["MQDungeons"] = 2
        random_settings["MQDungeonCount"] = kwargs['cparams'][1]
        return {s: random_settings[s] for s in mqSettings}
    number_chosen = random.randint(0, 2**kwargs['cparams'][1])
    chosen_amount = 0
    for i in range(1, kwargs['cparams'][1] + 1):
        if (number_chosen < 2**(kwargs['cparams'][1] - i)):
            chosen_amount = i
            continue
        break
    random_settings["MQDungeonCount"] = chosen_amount
    if (random_settings["MQDungeonCount"] == 0):
        return (random_settings["MQDungeons"])
    random_settings["MQDungeons"] = 2
    return {s: random_settings[s] for s in mqSettings}
            
def key_ring_settings(random_settings, **kwargs):
    random_settings["ShuffleKeyRings"] = 0
    if (kwargs['cparams'][0] == False):
        return (random_settings["ShuffleKeyRings"])
    if not (isinstance(kwargs['cparams'][0], bool)):
        random_enable = random.randint(0, 100)
        if (random_enable >= int(kwargs['cparams'][0])):
            return (random_settings["ShuffleKeyRings"])
    keyRingSettings = ["ShuffleKeyRings", "ShuffleKeyRingsRandomCount"]
    if (kwargs['cparams'][2] == "set"):
        random_settings["ShuffleKeyRings"] = 2
        random_settings["ShuffleKeyRingsRandomCount"] = kwargs['cparams'][1]
        return {s: random_settings[s] for s in keyRingSettings}
    number_chosen = random.randint(0, 2**kwargs['cparams'][1])
    chosen_amount = 0
    for i in range(1, kwargs['cparams'][1] + 1):
        if (number_chosen < 2**(kwargs['cparams'][1] - i)):
            chosen_amount = i
            continue
        break
    random_settings["ShuffleKeyRingsRandomCount"] = chosen_amount
    if (random_settings["ShuffleKeyRingsRandomCount"] == 0):
        return (random_settings["ShuffleKeyRings"])
    random_settings["ShuffleKeyRings"] = 2
    return {s: random_settings[s] for s in keyRingSettings}

def fortress_keys_match_dungeons(random_settings, **kwargs):
    if (kwargs['cparams'][0] == False) or (random_settings["FortressCarpenters"] == 2):
        return
    random_settings["GerudoKeys"] = max(0, random_settings["Keysanity"] - 2)
    return {random_settings["GerudoKeys"]}

def ganon_trial_settings(random_settings, **kwargs):
    random_settings["GanonTrial"] = 2
    trialSettings = ["GanonTrial", "GanonTrialCount"]
    if (kwargs['cparams'][1] == "set"):
        random_settings["GanonTrialCount"] = kwargs['cparams'][0]
        return {s: random_settings[s] for s in trialSettings}
    random_settings["GanonTrialCount"] = random.randint(0, kwargs['cparams'][0] + 1)
    return {s: random_settings[s] for s in trialSettings}

def shopsanity_settings(random_settings, **kwargs):
    if (random_settings["Shopsanity"] == 0):
        return
    shopSettings = ["ShopsanityCount", "ShopsanityPrices", "ShopsanityFixedPrice"]
    if (kwargs['cparams'][1] == "set"):
        random_settings["ShopsanityCount"] = kwargs['cparams'][0]
    else:
        random_settings["ShopsanityCount"] = random.randint(0, kwargs['cparams'][0] + 1)
    price_weights = [int(x) for x in kwargs['cparams'][2].split('/')]
    price_settings = [0, 1, 2, 3]
    random_settings["ShopsanityPrices"] = random.choices(price_settings, weights=price_weights)[0]
    random_settings["ShopsanityFixedPrice"] = kwargs['cparams'][3]
    return {s: random_settings[s] for s in shopSettings}

def allow_greg_gbk(random_settings, **kwargs):
    if random_settings["ShuffleGanonBossKey"] not in gregGBKSettings or kwargs['cparams'][0] == False:
        return
    typ = ""
    if random_settings["ShuffleGanonBossKey"] == 7:
        typ = "LacsStoneCount"
    elif random_settings["ShuffleGanonBossKey"] == 8:
        typ = "LacsMedallionCount"
    elif random_settings["ShuffleGanonBossKey"] == 9:
        typ = "LacsRewardCount"
    elif random_settings["ShuffleGanonBossKey"] == 10:
        typ = "LacsDungeonCount"
    countSettings = ["LacsRewardOptions",typ]
    allow_weights = [int(x) for x in kwargs['cparams'][1].split('/')]
    additional_weights = [int(x) for x in kwargs['cparams'][2].split('/')]
    random_settings["LacsRewardOptions"] = random.choices(["0", "1", "2"], weights=allow_weights)
    if random_settings["LacsRewardOptions"] == 2:
        if (random.choices([True, False], weights=additional_weights) == True):
            random_settings[typ] += 1
    return {s: random_settings[s] for s in countSettings}
        
def allow_greg_bridge(random_settings, **kwargs):
    if random_settings["RainbowBridge"] not in gregBridgeSettings or kwargs['cparams'][0] == False:
        return
    typ = ""
    if random_settings["RainbowBridge"] == 7:
        typ = "StoneCount"
    elif random_settings["RainbowBridge"] == 8:
        typ = "MedallionCount"
    elif random_settings["RainbowBridge"] == 9:
        typ = "RewardCount"
    elif random_settings["RainbowBridge"] == 10:
        typ = "DungeonCount"
    countSettings = ["BridgeRewardOptions",typ]
    allow_weights = [int(x) for x in kwargs['cparams'][1].split('/')]
    additional_weights = [int(x) for x in kwargs['cparams'][2].split('/')]
    random_settings["BridgeRewardOptions"] = random.choices(["0", "1", "2"], weights=allow_weights)
    if random_settings["BridgeRewardOptions"] == 2:
        if (random.choices([True, False], weights=additional_weights) == True):
            random_settings[typ] += 1
    return {s: random_settings[s] for s in countSettings}

def shuffle_only_ow_or_int(random_settings, **kwargs):
    if kwargs['cparams'][0] == 0:
        return
    
    chance_one_is_on = int(kwargs['cparams'][0])
    setting_weights = [int(x) for x in kwargs['cparams'][1].split('/')]

    # If setting is randomized off, return
    if not (random.randint(0, 100) < chance_one_is_on):
       return

    # Choose which of the settings to turn on
    allSettings = ["ShuffleOverworldEntrances", "ShuffleInteriorsEntrances"]
    chosenValue = random.choices([0, 1, 2], weights=setting_weights)[0]

    if chosenValue == 0:
        random_settings["ShuffleOverworldEntrances"] = 1
    else:
        random_settings["ShuffleOverworldEntrances"] = 0
    random_settings["ShuffleInteriorsEntrances"] = chosenValue
        
    return {s: random_settings[s] for s in allSettings}

def starting_consumables(random_settings, **kwargs):
    chance_enabled = int(kwargs['cparams'][0])
    if not (random.randint(0, 100) < chance_enabled):
       return
    random_settings["StartingSticks"] = 1
    random_settings["StartingNuts"] = 1
    return {random_settings["StartingSticks"], random_settings["StartingNuts"]}

def starting_hearts(random_settings, **kwargs):
    if (kwargs['cparams'][1] == "set"):
        random_settings["StartingHearts"] = kwargs['cparams'][0] - 1
        return {random_settings["StartingHearts"]}
    number_chosen = random.randint(0, 2**(kwargs['cparams'][0] - kwargs['cparams'][2]))
    chosen_amount = 0
    for i in range(1, kwargs['cparams'][0] + 1):
        if (number_chosen < 2**(kwargs['cparams'][0] - kwargs['cparams'][2] - i)):
            chosen_amount = i
            continue
        break
    random_settings["StartingHearts"] = kwargs['cparams'][2] + chosen_amount
    return {random_settings["StartingHearts"]}
