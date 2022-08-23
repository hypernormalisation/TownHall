"""mappings.py

Module to contain mappings and allowed values for data to be stored in the postgres db.
"""
import discord

# Class color hexes
color_druid = 0xFF7C0A
color_dk = 0xC41E3A
color_hunter = 0xAAD372
color_mage = 0x3FC7EB
color_paladin = 0xF48CBA
color_priest = 0xFFFFFF
color_rogue = 0xFFF468
color_shaman = 0x0070DD
color_warlock = 0x8788EE
color_warrior = 0xC69B6D

# The vacancy sql labels vs the options presented to the player
vacancy_mapping = {

    # general;
    "dps": "DPS",
    "melee_dps": "Melee DPS",
    "ranged_dps": "Ranged DPS",
    "tank": "Tank",
    "healer": "Healer",
    "pvp": "PvP",

    # classes
    "dk": "Death Knight",
    "druid": "Druid",
    "hunter": "Hunter",
    "mage": "Mage",
    "paladin": "Paladin",
    "priest": "Priest",
    "rogue": "Rogue",
    "shaman": "Shaman",
    "warlock": "Warlock",
    "warrior": "Warrior",

    # specs
    "blood_dk": "Blood Death Knight",
    "frost_dk": "Frost Death Knight",
    "unholy_dk": "Unholy Death Knight",

    "balance_druid": "Balance Druid",
    "feral_druid": "Feral Druid",
    "feral_dps_druid": "Feral Druid DPS",
    "feral_tank_druid": "Feral Druid Tank",
    "resto_druid": "Resto Druid",

    "bm_hunter": "Beast Mastery Hunter",
    "mm_hunter": "Marksman Hunter",
    "surv_hunter": "Survival Hunter",

    "arcane_mage": "Arcane Mage",
    "fire_mage": "Fire Mage",
    "frost_mage": "Frost Mage",

    "holy_paladin": "Holy Paladin",
    "prot_paladin": "Prot Paladin",
    "ret_paladin": "Retribution Paladins",

    "disc_priest": "Disc Priest",
    "holy_priest": "Holy Priest",
    "shadow_priest": "Shadow Priest",

    "assassin_rogue": "Assassination Rogue",
    "combat_rogue": "Combat Rogue",
    "sub_rogue": "Subtlety Rogue",

    "ele_shaman": "Elemental Shaman",
    "enhance_shaman": "Enhancement Shaman",
    "resto_shaman": "Resto Shaman",

    "affli_warlock": "Affliction Warlock",
    "demo_warlock": "Demonology Warlock",
    "destro_warlock": "Destruction Warlock",

    "dps_warrior": "DPS Warrior",
    "arm_warrior": "Arms Warrior",
    "fury_warrior": "Fury Warrior",
    "prot_warrior": "Prot Warrior",

}


vacancy_mapping_reversed = {v: k for k, v in vacancy_mapping.items()}


def get_color_from_label(label):
    """Function to get the relevant class color from a class/spec label."""

    label = label.lower()
    if 'knight' in label:
        return color_dk
    elif 'druid' in label:
        return color_druid
    elif 'hunter' in label:
        return color_hunter
    elif 'mage' in label:
        return color_mage
    elif 'paladin' in label:
        return color_paladin
    elif 'priest' in label:
        return color_priest
    elif 'rogue' in label:
        return color_rogue
    elif 'shaman' in label:
        return color_shaman
    elif 'warlock' in label:
        return color_warlock
    elif 'warrior' in label:
        return color_warrior

    # Finally return a default if no special match.
    return discord.Color.blurple()


"arcane_mage"
"fire_mage"
"frost_mage"

"holy_paladin"
"prot_paladin"
"ret_paladin"

"disc_priest"
"holy_priest"
"shadow_priest"

"assassin_rogue"
"combat_rogue"
"sub_rogue"

"ele_shaman"
"enhance_shaman"
"resto_shaman"

"affli_warlock"
"demo_warlock"
"destro_warlock"

"dps_warrior"
"arm_warrior"
"fury_warrior"
"prot_warrior"
