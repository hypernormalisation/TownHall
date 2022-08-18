"""mappings.py

Module to contain mappings and allowed values for data to be stored in the postgres db.
"""
import discord

color_druid = 0xFF7C0A
color_rogue = 0xFFF468


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


}


vacancy_mapping_reversed = {v: k for k, v in vacancy_mapping.items()}


def get_color_from_label(label):
    """Function to get the relevant class color from a class/spec label."""

    label = label.lower()
    if 'druid' in label:
        return color_druid
    elif 'rogue' in label:
        return color_rogue

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
