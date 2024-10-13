"""Update wrinkly hints compressed file."""

import random

import js
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.WrinklyHints import HintLocation, hints
from randomizer.Patching.Lib import grabText, writeText
from randomizer.Patching.Patcher import LocalROM


def writeWrinklyHints(file_index, text):
    """Write the text to ROM."""
    temp_text = []
    for item in text:
        temp_text.append([{"text": item}])
    writeText(file_index, temp_text)

def UpdateHint(WrinklyHint: HintLocation, message: str):
    """Update the wrinkly hint with the new string.

    Args:
        WrinklyHint (Hint): Wrinkly hint object.
        message (str): Hint message to write.
    """
    # Seek to the wrinkly data
    if len(message) <= 914:
        # We're safely below the character limit
        WrinklyHint.hint = message
        return True
    else:
        raise Exception("Hint message is longer than allowed.")
    return False


def updateRandomHint(message: str, kongs_req=[], keywords=[], levels=[]):
    """Update a random hint with the string specifed.

    Args:
        message (str): Hint message to write.
    """
    hint_pool = []
    for x in range(len(hints)):
        if hints[x].hint == "" and hints[x].kong in kongs_req and hints[x].level in levels:
            is_banned = False
            for banned in hints[x].banned_keywords:
                if banned in keywords:
                    is_banned = True
            if not is_banned:
                hint_pool.append(x)
    if len(hint_pool) > 0:
        selected = random.choice(hint_pool)
        return UpdateHint(hints[selected], message)
    return False


def PushHints(spoiler):
    """Update the ROM with all hints."""
    hint_arr = []
    short_hint_arr = []
    for replacement_hint in spoiler.hint_list.values():
        if replacement_hint == "":
            replacement_hint = "error: missing hint - report this error to the discord"
        hint_arr.append([replacement_hint.upper()])
    for short_hint in spoiler.short_hint_list.values():
        if short_hint == "":
            short_hint = "error: missing hint - report this error to the discord"
        short_hint_arr.append([short_hint.upper()])
    writeWrinklyHints(41, hint_arr)
    writeWrinklyHints(45, short_hint_arr)
    spoiler.hint_list.pop("First Time Talk")  # The FTT needs to be written to the ROM but should not be found in the spoiler log


def wipeHints():
    """Wipe the hint block."""
    for x in range(len(hints)):
        if hints[x].kong != Kongs.any:
            hints[x].hint = ""


def PushItemLocations(spoiler):
    """Push item hints to ROM."""
    text_arr = []
    for loc in spoiler.location_references:
        text_arr.append([loc.item_name.upper()])
        for subloc in loc.locations:
            text_arr.append([subloc.upper()])
    writeWrinklyHints(44, text_arr)


def replaceIngameText(spoiler):
    """Replace text in-game with defined modifications."""
    for file_index in spoiler.text_changes:
        old_text = grabText(file_index)
        modification_data = spoiler.text_changes[file_index]
        for mod in modification_data:
            if mod["mode"] == "replace":
                old_textbox = old_text[mod["textbox_index"]]
                new_textbox = []
                for seg in old_textbox:
                    text = []
                    for line in seg["text"]:
                        new_line = line.replace(mod["search"], mod["target"])
                        text.append(new_line)
                    new_textbox.append({"text": text.copy()})
                old_text[mod["textbox_index"]] = new_textbox.copy()
            elif mod["mode"] == "replace_whole":
                # print(mod["target"])
                old_text[mod["textbox_index"]] = ({"text": [mod["target"]]},)
        writeText(file_index, old_text)


def PushHelpfulHints(spoiler, ROM_COPY: LocalROM):
    """Push the flags to ROM which control the dim_solved_hints setting."""
    for index, flag in enumerate(spoiler.tied_hint_flags.values()):
        ROM_COPY.seek(0x1FFE000 + (2 * index))
        ROM_COPY.writeMultipleBytes(flag, 2)


def PushHintTiedRegions(spoiler, ROM_COPY: LocalROM):
    """Push the flags to ROM which control the dim_solved_hints setting."""
    for index, flag in enumerate(spoiler.tied_hint_regions):
        ROM_COPY.seek(0x1FFE080 + (2 * index))
        ROM_COPY.writeMultipleBytes(flag, 2)
