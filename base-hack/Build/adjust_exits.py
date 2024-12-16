"""Adjust exits to prevent logical problems with LZR."""

import os
import zlib
from typing import BinaryIO

from BuildEnums import TableNames, Maps
from BuildLib import intf_to_float, main_pointer_table_offset

new_caves_portal_coords = [120.997, 50, 1182.974]


exit_adjustments = [
    {
        "containing_map": Maps.Fungi,  # Fungi Main
        "exits": [
            {
                # Dark Attic
                "exit_index": 3,
                "x": 3429,
                "y": 462,
                "z": 4494,
            },
            {
                # Mill (W1 Exit)
                "exit_index": 6,
                "x": 4153,
                "y": 163,
                "z": 3721,
            },
            {
                # DK Barn
                "exit_index": 4,
                "x": 3982,
                "y": 115,
                "z": 2026,
            },
            {
                # Mill Rear PPunch Door
                "exit_index": 5,
                "x": 4550,
                "y": 162,
                "z": 3646,
            },
        ],
    },
    {
        "containing_map": Maps.Galleon,  # Galleon
        "exits": [
            {
                # Lighthouse
                "exit_index": 10,
                "x": 1524,
                "y": 1754,
                "z": 3964,
            },
            {
                # Seal Race
                "exit_index": 19,
                "x": 3380,
                "y": 1640,
                "z": 120,
            },
        ],
    },
    {
        "containing_map": Maps.CastleCryptDKDiddyChunky,  # DDC Crypt
        "exits": [
            {
                # Minecart
                "exit_index": 1,
                "x": 1515,
                "y": 80,
                "z": 2506,
            }
        ],
    },
    {
        "containing_map": Maps.Isles,  # Isles
        "exits": [
            {
                # Aztec Lobby
                "exit_index": 3,
                "x": 3464,
                "y": 1040,
                "z": 1716,
            },
            {
                # Galleon Lobby
                "exit_index": 5,
                "x": 1947,
                "y": 406,
                "z": 3229,
            },
        ],
    },
    {
        "containing_map": Maps.Factory,  # Factory
        "exits": [
            {
                # Crusher
                "exit_index": 8,
                "x": 814,
                "y": 8,
                "z": 1334,
            }
        ],
    },
    {
        "containing_map": Maps.Castle,  # Castle
        "exits": [
            {
                # Tree
                "exit_index": 15,
                "x": 1293,
                "y": 472,
                "z": 238,
            },
            {
                # Ballroom
                "exit_index": 11,
                "x": 1808,
                "y": 1406,
                "z": 1270,
            },
        ],
    },
    {
        "containing_map": Maps.Caves,  # Caves
        "exits": [
            {
                # Unused 5DI Portal Exit
                "exit_index": 11,
                "x": int(new_caves_portal_coords[0] - 25),
                "y": int(new_caves_portal_coords[1]),
                "z": int(new_caves_portal_coords[2] - 12),
            }
        ],
    },
]

exit_additions = []

temp_file = "temp.bin"


def shortToUshort(short):
    """Convert Short to Unsigned Short."""
    if short < 0:
        return short + 65536
    return short


def adjustExits(fh):
    """Write new exits."""
    print("Adjusting Exits")
    # Get Setups
    fh.seek(main_pointer_table_offset + (4 * TableNames.Setups))
    setup_table = main_pointer_table_offset + int.from_bytes(fh.read(4), "big")
    for map_index in range(216):
        exit_coords = []
        if map_index not in (0x61, 0xAA, 0x11):  # Prevent K. Lumsy exit being generated with fake warp
            fh.seek(setup_table + (4 * map_index))
            setup_start = main_pointer_table_offset + int.from_bytes(fh.read(4), "big")
            setup_end = main_pointer_table_offset + int.from_bytes(fh.read(4), "big")
            setup_size = setup_end - setup_start
            fh.seek(setup_start)
            indicator = int.from_bytes(fh.read(2), "big")
            is_compressed = False
            if indicator == 0x1F8B:
                is_compressed = True
            fh.seek(setup_start)
            data = fh.read(setup_size)
            if is_compressed:
                data = zlib.decompress(data, (15 + 32))
            with open(temp_file, "wb") as fg:
                fg.write(data)
            with open(temp_file, "rb") as fg:
                model2_count = int.from_bytes(fg.read(4), "big")
                for model2_item in range(model2_count):
                    item_start = 4 + (model2_item * 0x30)
                    fg.seek(item_start + 0x28)
                    item_type = int.from_bytes(fg.read(2), "big")
                    item_id = int.from_bytes(fg.read(2), "big")
                    if item_type >= 0x210 and item_type <= 0x214:
                        if item_id == 0x57 and map_index == 0x48:
                            fg.seek(item_start + 4)
                            coords = [int(176.505), int(intf_to_float(int.from_bytes(fg.read(4), "big"))) + 5, int(1089.408)]
                        else:
                            fg.seek(item_start)
                            coords = []
                            for coord_index in range(3):
                                coords.append(int(intf_to_float(int.from_bytes(fg.read(4), "big"))))
                            coords[1] += 5
                        exit_coords.append(coords.copy())
            if os.path.exists(temp_file):
                os.remove(temp_file)
        if map_index == Maps.Isles:
            # Isles
            exit_coords.append([2524, 1724, 3841])  # Top of Krem Isles
        elif map_index == Maps.Galleon:
            # Galleon
            exit_coords.append([2886, 1249, 1121])  # Mech Fish Exit
        elif map_index == Maps.CavesBeetleRace:
            # Caves Beetle
            exit_coords.append([1315, 5130, 485])
        exit_additions.append(exit_coords.copy())
    # Exits
    fh.seek(main_pointer_table_offset + (4 * TableNames.Exits))
    ptr_table = main_pointer_table_offset + int.from_bytes(fh.read(4), "big")
    for map_index in range(216):
        fh.seek(ptr_table + (4 * map_index))
        exit_start = main_pointer_table_offset + (int.from_bytes(fh.read(4), "big") & 0x7FFFFFFF)
        exit_end = main_pointer_table_offset + (int.from_bytes(fh.read(4), "big") & 0x7FFFFFFF)
        exit_size = exit_end - exit_start
        fh.seek(exit_start)
        data = fh.read(exit_size)
        file_name = f"exit{map_index}.bin"
        with open(file_name, "wb") as fg:
            fg.write(data)
            for exit_set in exit_additions[map_index]:
                for coord in exit_set:
                    fg.write(shortToUshort(coord).to_bytes(2, "big"))
                fg.write((0).to_bytes(4, "big"))
        with open(file_name, "r+b") as fg:
            for x in exit_adjustments:
                if map_index == x["containing_map"]:
                    for exit in x["exits"]:
                        exit_start = exit["exit_index"] * 0xA
                        fg.seek(exit_start)
                        fg.write(shortToUshort(exit["x"]).to_bytes(2, "big"))
                        fg.write(shortToUshort(exit["y"]).to_bytes(2, "big"))
                        fg.write(shortToUshort(exit["z"]).to_bytes(2, "big"))
        exit_count = 0
        data = None
        with open(file_name, "rb") as fg:
            data = fg.read()
            exit_count = int(len(data) / 10)
        if exit_count == 0:
            print(f"NO EXITS FOUND FOR {Maps(map_index).name}")
            data = bytes(bytearray([0] * 10))
        default_exit = 0
        if map_index == Maps.Japes:
            default_exit = 15
        elif map_index == Maps.Fungi:
            default_exit = 27
        default_start = default_exit * 10
        print(f"Rewriting exit file with {exit_count} exits:", map_index, data)
        with open(file_name, "wb") as fg:
            fg.write(data[default_start : default_start + 10])
            fg.write(exit_count.to_bytes(2, "big"))
            fg.write(data)
        if os.path.exists(file_name):
            if os.path.getsize(file_name) == 0:
                os.remove(file_name)


class LoadingZone:
    """Class to store information regarding a loading zone."""

    def __init__(self, x: int, y: int, z: int, radius: int, height: int, map_id: Maps, exit: int):
        """Initialize with given parameters."""
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
        if height is None:
            self.height = 0xFFFF
        self.map_id = map_id
        self.exit = exit

    def writeZone(self, fh: BinaryIO):
        """Write data to file."""
        for value in (self.x, self.y, self.z):
            v = value
            if value < 0:
                v += 0x10000
            fh.write(v.to_bytes(2, "big"))
        fh.write(self.radius.to_bytes(2, "big"))  # 0x6
        fh.write(self.height.to_bytes(2, "big"))  # 0x8
        fh.write((1).to_bytes(2, "big"))  # 0xA
        fh.write((1).to_bytes(2, "big"))  # 0xC
        fh.write((1).to_bytes(1, "big"))  # 0xE
        fh.write((0).to_bytes(1, "big"))  # 0XF
        LZ_TYPE = 9
        fh.write(LZ_TYPE.to_bytes(2, "big"))
        fh.write(self.map_id.to_bytes(2, "big"))
        fh.write(self.exit.to_bytes(2, "big"))
        TRANSITION_TYPE = 0
        fh.write(TRANSITION_TYPE.to_bytes(2, "big"))
        for _ in range(0x38 - 0x18):
            fh.write((0).to_bytes(1, "big"))


mech_fish_triggers = [
    LoadingZone(360, 70, 92, 50, None, Maps.Galleon, 34),
]


def addMechFishLZ():
    """Add mech fish loading zone to the trigger file."""
    with open("mech_fish_triggers.bin", "wb") as fh:
        fh.write(len(mech_fish_triggers).to_bytes(2, "big"))
        for trigger in mech_fish_triggers:
            trigger.writeZone(fh)
