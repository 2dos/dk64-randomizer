"""CLI script for running seed generation."""
import argparse
import codecs
import json
import pickle
import pprint
import random
import os
import sys
import traceback

from randomizer.Enums.Settings import SettingsMap, SettingsStringEnum, SettingsStringListTypeMap, SettingsStringTypeMap
from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.SettingStrings import decrypt_setting_string
from randomizer.Spoiler import Spoiler


def generate(generate_settings, file_name):
    """Gen a seed and write the file to an output file."""
    settings = Settings(generate_settings)
    spoiler = Spoiler(settings)
    Generate_Spoiler(spoiler)
    encoded = codecs.encode(pickle.dumps(spoiler), "base64").decode()
    with open(file_name, "w") as outfile:
        outfile.write(encoded)


def main():
    """CLI Entrypoint for generating seeds."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--settings_string", help="The settings string to use to generate a seed", required=False)
    parser.add_argument("--preset", help="Preset to use", required=False)
    parser.add_argument("--output", help="File to name patch file", required=True)
    parser.add_argument("--seed", help="Seed ID to use", required=False)
    args = parser.parse_args()
    if not os.environ.get("POST_BODY"):
        if args.settings_string is not None:
            decrypt_setting_string(args.settings_string)
            try:
                setting_data = decrypt_setting_string(args.settings_string)
            except Exception:
                print("Invalid settings String")
                sys.exit(2)
        elif args.preset is not None:
            presets = json.load(open("static/presets/preset_files.json"))
            default = json.load(open("static/presets/default.json"))
            found = False
            for file in presets.get("progression"):
                with open("static/presets/" + file, "r") as preset_file:
                    data = json.load(preset_file)
                    if args.preset == data.get("name"):
                        setting_data = default
                        for key in data:
                            setting_data[key] = data[key]
                        setting_data.pop("name")
                        setting_data.pop("description")
                        found = True
            if found is False:
                sys.exit(2)
        if args.seed is not None:
            setting_data["seed"] = args.seed
        else:
            setting_data["seed"] = random.randint(0, 100000000)
    else:
        setting_data = json.loads(os.environ.get("POST_BODY"))
        if not setting_data.get("seed"):
            setting_data["seed"] = random.randint(0, 100000000)
    # Convert string data to enums where possible.
    for k, v in setting_data.items():
        if k in SettingsMap:
            if type(v) is list:
                values = []
                for val in v:
                    if type(val) is int:
                        values.append(SettingsMap[k](val))
                    else:
                        values.append(SettingsMap[k][val])
                setting_data[k] = values
            elif type(v) is int:
                setting_data[k] = SettingsMap[k](v)
            else:
                setting_data[k] = SettingsMap[k][v]
    # For every value in the settings if its a string and the string is a number convert it to an int.
    for k, v in setting_data.items():
        if type(v) is str:
            if v.isnumeric():
                setting_data[k] = int(v)
    del setting_data["seed"]
    # Load the default preset and then create a new settings object using the SettingsMap to convert the strings to enums.
    default = json.load(open("static/presets/default.json"))
    # sort the default settings so that the order is the same as the settings map.
    default = {k: default[k] for k in sorted(default)}
    for k, v in default.items():
        if k in SettingsMap:
            if type(v) is list:
                values = []
                for val in v:
                    if type(val) is int:
                        values.append(SettingsMap[k](val))
                    else:
                        values.append(SettingsMap[k][val])
                default[k] = values
            elif type(v) is int:
                default[k] = SettingsMap[k](v)
            else:
                default[k] = SettingsMap[k][v]
    # Add all the missing settings to the setting data.
    for k, v in default.items():
        if k not in setting_data:
            setting_data[k] = v
    print(default)
    # Sort the setting data so that the order is the same as the settings map.
    settings_data = {k: setting_data[k] for k in sorted(setting_data)}
    pprint.pprint(settings_data)
    encoded = encode_enum_dict(setting_data)
    print(encoded)
    pprint.pprint(decode_enum_dict(encoded, default))
    try:
        #generate(setting_data, args.output)
        print("")
    except Exception as e:
        with open("error.log", "w") as file_object:
            file_object.write(repr(e))
        with open("traceback.log", "w") as file_object:
            file_object.write(str(traceback.format_exc()))
        print(traceback.format_exc())
        if os.environ.get("DISCORD_WEBHOOK"):
            from discord_webhook import DiscordWebhook, DiscordEmbed

            webhook = DiscordWebhook(url=os.environ.get("DISCORD_WEBHOOK"))
            embed = DiscordEmbed(title="Error Generating Seed", description=str(traceback.format_exc()), color="800020")
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
        sys.exit(1)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

index_to_letter = {i: letters[i] for i in range(64)}
letter_to_index = {letters[i]: i for i in range(len(letters))}

def encode_enum_dict(enum_dict):
    """Encode a dictionary of enums, bools, ints and lists to a string of letters."""
    bitstring = ""
    for key in enum_dict:
        value = enum_dict[key]
        keyEnum = SettingsStringEnum[key]
        if isinstance(value, bool):
            bitstring += bin(keyEnum)[2:].zfill(8)
            bitstring += "1" if value else "0"
        elif isinstance(value, int):
            bitstring += bin(keyEnum)[2:].zfill(8)
            bitstring += bin(value)[2:].zfill(16)
        elif isinstance(value, list):
            for item in value:
                bitstring += bin(keyEnum)[2:].zfill(8)
                if isinstance(item, bool):
                    bitstring += "1" if item else "0"
                elif isinstance(item, int):
                    bitstring += bin(item)[2:].zfill(16)
                else:
                    enum_class = type(item)
                    enum_values = [member.value for member in enum_class]
                    index = enum_values.index(item.value)
                    bitstring += format(index, f"0{len(enum_values).bit_length()}b")
        else:
            bitstring += bin(keyEnum)[2:].zfill(8)
            enum_class = type(value)
            enum_values = [member.value for member in enum_class]
            index = enum_values.index(value.value)
            bitstring += format(index, f"0{len(enum_values).bit_length()}b")
    
    # Pad the bitstring with zeroes until the length is divisible by 6.
    mod6 = len(bitstring) % 6
    if mod6 > 0:
        remaining_zeroes = 6 - mod6
        for _ in range(0, remaining_zeroes):
            bitstring += "0"
    
    # Split the bitstring into 6-bit chunks and look up the corresponding letters
    letter_string = ""
    for i in range(0, len(bitstring), 6):
        chunk = int(bitstring[i:i+6], 2)
        letter_string += letters[chunk]
    return letter_string

def decode_enum_dict(settings_string, default_dict):
    # take each letter of the settings_string and convert it to a 6-bit binary number, then using each number use it as the index of the default dict (sorted order) and then use the key from the default dict to get the value from the settings string.
    bitstring = ""
    for letter in settings_string:
        index = letter_to_index[letter]
        bitstring += f"{index:06b}"
    bitstring_length = len(bitstring)
    enum_dict = {}
    bit_index = 0
    # If there are fewer than nine characters left in our bitstring, we have
    # hit the padding.
    while bit_index < (bitstring_length-9):
        # Consume the next key.
        key = int(bitstring[bit_index:bit_index+8], 2)
        bit_index += 8
        keyEnum = SettingsStringEnum(key)
        keyName = keyEnum.name
        settingType = SettingsStringTypeMap[keyEnum]
        if settingType == bool:
            enum_dict[keyName] = True if bitstring[bit_index] == "1" else False
            bit_index += 1
        elif settingType == int:
            enum_dict[keyName] = int(bitstring[bit_index:bit_index+16], 2)
            bit_index += 16
        elif settingType == list:
            listType = SettingsStringListTypeMap[keyEnum]
            value = None
            if listType == bool:
                value = True if bitstring[bit_index] == "1" else False
                bit_index += 1
            elif listType == int:
                value = int(bitstring[bit_index:bit_index+16], 2)
                bit_index += 16
            else:
                enum_values = [member.value for member in listType]
                index = int(bitstring[bit_index:bit_index+len(enum_values).bit_length()], 2)
                value = listType(index)
                bit_index += len(enum_values).bit_length()
            if keyName not in enum_dict:
                enum_dict[keyName] = [value]
            else:
                enum_dict[keyName].append(value)
        else:
            enum_values = [member.value for member in settingType]
            index = int(bitstring[bit_index:bit_index+len(enum_values).bit_length()], 2)
            enum_dict[key] = settingType(index)
            bit_index += len(enum_values).bit_length()
    return enum_dict


if __name__ == "__main__":
    main()
