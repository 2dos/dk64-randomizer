typedef enum console {
    NONE,
    N64,
    WIIU,
    EMULATOR,
} console;

typedef enum data_indexes {
	Music_MIDI,
	Map_Geometry,
	Map_Walls,
	Map_Floors,
	ModelTwo_Geometry,
	Actor_Geometry,
	Unk06,
	Textures_Uncompressed,
	Cutscenes,
	Map_Setups,
	Map_Object_Scripts,
	Animations,
	Text,
	Unk0D,
	Textures,
	Map_Paths,
	Map_Character_Spawners,
	Unk11,
	Map_Loading_Zones,
	Unk13,
	Unk14,
	Map_Autowalks,
	Unk16,
	Map_Exits,
	Map_Race_Checkpoints,
	Textures_2,
	Uncompressed_File_Sizes,
	Unk1B,
	Unk1C,
	Unk1D,
	Unk1E,
	Unk1F,
	Unk20,
} data_indexes;

typedef enum load_modes {
	SAVESTATE,
	MAPWARP,
} load_modes;

typedef enum codecs {
    IA4,
    IA8,
    RGBA16,
    RGBA32,
} codecs;

typedef enum collision_types {
	/* 0x000 */ COLLISION_BBLAST,
	/* 0x001 */ COLLISION_UNKNOWN_1,
	/* 0x002 */ COLLISION_SIMIAN_SPRING,
	/* 0x003 */ COLLISION_MONKEYPORT_WARP,
	/* 0x004 */ COLLISION_GORILLA_GONE,
	/* 0x005 */ COLLISION_BANANAPORT,
	/* 0x006 */ COLLISION_BABOON_BALLOON,
	/* 0x007 */ COLLISION_BATTLE_CROWN,
	/* 0x008 */ COLLISION_UNKNOWN_8,
	/* 0x009 */ COLLISION_MULTI_BANANAPORT,
	/* 0x00A */ COLLISION_MAPWARP,
} collision_types;

typedef enum location_list {
	/* 0x000 */ LOCATION_DIVE,
	/* 0x001 */ LOCATION_ORANGE,
	/* 0x002 */ LOCATION_BARREL,
	/* 0x003 */ LOCATION_VINE,
	/* 0x004 */ LOCATION_BFI
} location_list;

typedef enum helm_hurry_items {
	/* 0x000 */ HHITEM_NOTHING,
	/* 0x001 */ HHITEM_GB,
	/* 0x002 */ HHITEM_BLUEPRINT,
	/* 0x003 */ HHITEM_COMPANYCOIN,
	/* 0x004 */ HHITEM_MOVE,
	/* 0x005 */ HHITEM_MEDAL,
	/* 0x006 */ HHITEM_RAINBOWCOIN,
	/* 0x007 */ HHITEM_KEY,
	/* 0x008 */ HHITEM_CROWN,
	/* 0x009 */ HHITEM_BEAN,
	/* 0x00A */ HHITEM_PEARL,
	/* 0x00B */ HHITEM_KONG,
	/* 0x00C */ HHITEM_FAIRY,
	/* 0x00D */ HHITEM_CB,
	/* 0x00E */ HHITEM_FAKEITEM,
} helm_hurry_items;

typedef enum purchase_classification {
	/* 0x000 */ PCLASS_NOTHING,
	/* 0x001 */ PCLASS_MOVE,
	/* 0x002 */ PCLASS_INSTRUMENT,
	/* 0x003 */ PCLASS_GUN,
	/* 0x004 */ PCLASS_CAMERA,
	/* 0x005 */ PCLASS_SHOCKWAVE,
	/* 0x006 */ PCLASS_CAMSHOCK,
	/* 0x007 */ PCLASS_GB,
	/* 0x008 */ PCLASS_BLUEPRINT,
	/* 0x009 */ PCLASS_COMPANYCOIN,
	/* 0x00A */ PCLASS_MEDAL,
	/* 0x00B */ PCLASS_RAINBOWCOIN,
	/* 0x00C */ PCLASS_KEY,
	/* 0x00D */ PCLASS_CROWN,
	/* 0x00E */ PCLASS_BEAN,
	/* 0x00F */ PCLASS_PEARL,
	/* 0x010 */ PCLASS_KONG,
	/* 0x011 */ PCLASS_FAIRY,
	/* 0x012 */ PCLASS_FAKEITEM,
} purchase_classification;

typedef enum pad_refresh_signals {
    /* 0x000 */ ITEMREFRESH_BLAST,
    /* 0x001 */ ITEMREFRESH_SPRING,
    /* 0x002 */ ITEMREFRESH_BALLOON,
    /* 0x003 */ ITEMREFRESH_MONKEYPORT,
    /* 0x004 */ ITEMREFRESH_GONE,
	/* 0x005 */ ITEMREFRESH_VINE,
} pad_refresh_signals;

typedef enum moverando_hinttext {
	/* 0x000 */ MRT_CANBUY_BBLAST,
	/* 0x001 */ MRT_CANBUY_SKONG,
	/* 0x002 */ MRT_CANBUY_GGRAB,
	/* 0x003 */ MRT_CANBUY_CCHARGE,
	/* 0x004 */ MRT_CANBUY_RBARREL,
	/* 0x005 */ MRT_CANBUY_SSPRING,
	/* 0x006 */ MRT_CANBUY_OSTAND,
	/* 0x007 */ MRT_CANBUY_BBALLOON,
	/* 0x008 */ MRT_CANBUY_OSPRINT,
	/* 0x009 */ MRT_CANBUY_MMONKEY,
	/* 0x00A */ MRT_CANBUY_PTT,
	/* 0x00B */ MRT_CANBUY_MPORT,
	/* 0x00C */ MRT_CANBUY_HCHUNKY,
	/* 0x00D */ MRT_CANBUY_PPUNCH,
	/* 0x00E */ MRT_CANBUY_GGONE,
	/* 0x00F */ MRT_CANBUY_SLAM,
	/* 0x010 */ MRT_CANBUY_COCONUT,
	/* 0x011 */ MRT_CANBUY_PEANUT,
	/* 0x012 */ MRT_CANBUY_GRAPE,
	/* 0x013 */ MRT_CANBUY_FEATHER,
	/* 0x014 */ MRT_CANBUY_PINEAPPLE,
	/* 0x015 */ MRT_CANBUY_HOMING,
	/* 0x016 */ MRT_CANBUY_SNIPER,
	/* 0x017 */ MRT_CANBUY_AMMOBELT,
	/* 0x018 */ MRT_CANBUY_BONGOS,
	/* 0x019 */ MRT_CANBUY_GUITAR,
	/* 0x01A */ MRT_CANBUY_TROMBONE,
	/* 0x01B */ MRT_CANBUY_SAX,
	/* 0x01C */ MRT_CANBUY_TRIANGLE,
	/* 0x01D */ MRT_CANBUY_INSTRUMENTUPGRADE,
	/* 0x01E */ MRT_CANBUY_DIVE,
	/* 0x01F */ MRT_CANBUY_ORANGE,
	/* 0x020 */ MRT_CANBUY_BARREL,
	/* 0x021 */ MRT_CANBUY_VINE,
	/* 0x022 */ MRT_CANBUY_CAMERA,
	/* 0x023 */ MRT_CANBUY_SHOCKWAVE,
	/* 0x024 */ MRT_CANBUY_CAMERACOMBO,
	/* 0x025 */ MRT_CANBUY_BANANA,
	/* 0x026 */ MRT_CANBUY_CROWN,
	/* 0x027 */ MRT_CANBUY_MEDAL,
	/* 0x028 */ MRT_CANBUY_KEY,
	/* 0x029 */ MRT_CANBUY_BLUEPRINT,
	/* 0x02A */ MRT_CANBUY_NINTENDO,
	/* 0x02B */ MRT_CANBUY_RAREWARE,
	/* 0x02C */ MRT_CANBUY_BEAN,
	/* 0x02D */ MRT_CANBUY_PEARL,
	/* 0x02E */ MRT_CANBUY_KONG,
	/* 0x02F */ MRT_CANBUY_FAIRY,
	/* 0x030 */ MRT_CANBUY_FAKEITEM,
	/* 0x031 */ MRT_NOBUY_SPECIALMOVE,
	/* 0x032 */ MRT_NOBUY_SLAM,
	/* 0x033 */ MRT_NOBUY_GUN,
	/* 0x034 */ MRT_NOBUY_AMMOBELT,
	/* 0x035 */ MRT_NOBUY_INSTRUMENT,
	/* 0x036 */ MRT_NOBUY_TRAINING,
	/* 0x037 */ MRT_NOBUY_FAIRYMOVE,
	/* 0x038 */ MRT_NOBUY_ITEM,
	/* 0x039 */ MRT_NOBUY_BANANA,
	/* 0x03A */ MRT_NOBUY_BLUEPRINT,
	/* 0x03B */ MRT_NOBUY_MEDAL,
	/* 0x03C */ MRT_NOBUY_KONG,
} moverando_hinttext;

typedef enum item_purchase_text {
	/* 0x000 */ ITEMTEXT_SLAM1,
	/* 0x001 */ ITEMTEXT_SLAM1_LATIN,
	/* 0x002 */ ITEMTEXT_SLAM2,
	/* 0x003 */ ITEMTEXT_SLAM2_LATIN,
	/* 0x004 */ ITEMTEXT_SLAM3,
	/* 0x005 */ ITEMTEXT_SLAM3_LATIN,
	/* 0x006 */ ITEMTEXT_BBLAST,
	/* 0x007 */ ITEMTEXT_BBLAST_LATIN,
	/* 0x008 */ ITEMTEXT_SKONG,
	/* 0x009 */ ITEMTEXT_SKONG_LATIN,
	/* 0x00A */ ITEMTEXT_GGRAB,
	/* 0x00B */ ITEMTEXT_GGRAB_LATIN,
	/* 0x00C */ ITEMTEXT_CCHARGE,
	/* 0x00D */ ITEMTEXT_CCHARGE_LATIN,
	/* 0x00E */ ITEMTEXT_RBARREL,
	/* 0x00F */ ITEMTEXT_RBARREL_LATIN,
	/* 0x010 */ ITEMTEXT_SSPRING,
	/* 0x011 */ ITEMTEXT_SSPRING_LATIN,
	/* 0x012 */ ITEMTEXT_OSTAND,
	/* 0x013 */ ITEMTEXT_OSTAND_LATIN,
	/* 0x014 */ ITEMTEXT_BBALLOON,
	/* 0x015 */ ITEMTEXT_BBALLOON_LATIN,
	/* 0x016 */ ITEMTEXT_OSPRINT,
	/* 0x017 */ ITEMTEXT_OSPRINT_LATIN,
	/* 0x018 */ ITEMTEXT_MMONKEY,
	/* 0x019 */ ITEMTEXT_MMONKEY_LATIN,
	/* 0x01A */ ITEMTEXT_PTT,
	/* 0x01B */ ITEMTEXT_PTT_LATIN,
	/* 0x01C */ ITEMTEXT_MPORT,
	/* 0x01D */ ITEMTEXT_MPORT_LATIN,
	/* 0x01E */ ITEMTEXT_HCHUNKY,
	/* 0x01F */ ITEMTEXT_HCHUNKY_LATIN,
	/* 0x020 */ ITEMTEXT_PPUNCH,
	/* 0x021 */ ITEMTEXT_PPUNCH_LATIN,
	/* 0x022 */ ITEMTEXT_GGONE,
	/* 0x023 */ ITEMTEXT_GGONE_LATIN,
	/* 0x024 */ ITEMTEXT_COCONUT,
	/* 0x025 */ ITEMTEXT_PEANUT,
	/* 0x026 */ ITEMTEXT_GRAPE,
	/* 0x027 */ ITEMTEXT_FEATHER,
	/* 0x028 */ ITEMTEXT_PINEAPPLE,
	/* 0x029 */ ITEMTEXT_BONGOS,
	/* 0x02A */ ITEMTEXT_GUITAR,
	/* 0x02B */ ITEMTEXT_TROMBONE,
	/* 0x02C */ ITEMTEXT_SAX,
	/* 0x02D */ ITEMTEXT_TRIANGLE,
	/* 0x02E */ ITEMTEXT_HOMING,
	/* 0x02F */ ITEMTEXT_SNIPER,
	/* 0x030 */ ITEMTEXT_BELT1,
	/* 0x031 */ ITEMTEXT_BELT2,
	/* 0x032 */ ITEMTEXT_THIRDMELON,
	/* 0x033 */ ITEMTEXT_INSUPGRADE1,
	/* 0x034 */ ITEMTEXT_INSUPGRADE2,
	/* 0x035 */ ITEMTEXT_DIVE,
	/* 0x036 */ ITEMTEXT_ORANGE,
	/* 0x037 */ ITEMTEXT_BARREL,
	/* 0x038 */ ITEMTEXT_VINE,
	/* 0x039 */ ITEMTEXT_CAMERA,
	/* 0x03A */ ITEMTEXT_SHOCKWAVE,
	/* 0x03B */ ITEMTEXT_CAMERACOMBO,
	/* 0x03C */ ITEMTEXT_BANANA,
	/* 0x03D */ ITEMTEXT_MEDAL,
	/* 0x03E */ ITEMTEXT_BLUEPRINT_DK,
	/* 0x03F */ ITEMTEXT_BLUEPRINT_DIDDY,
	/* 0x040 */ ITEMTEXT_BLUEPRINT_LANKY,
	/* 0x041 */ ITEMTEXT_BLUEPRINT_TINY,
	/* 0x042 */ ITEMTEXT_BLUEPRINT_CHUNKY,
	/* 0x043 */ ITEMTEXT_NINTENDO,
	/* 0x044 */ ITEMTEXT_RAREWARE,
	/* 0x045 */ ITEMTEXT_KEYGENERIC,
	/* 0x046 */ ITEMTEXT_CROWN,
	/* 0x047 */ ITEMTEXT_BEAN,
	/* 0x048 */ ITEMTEXT_KEY1,
	/* 0x049 */ ITEMTEXT_KEY2,
	/* 0x04A */ ITEMTEXT_KEY3,
	/* 0x04B */ ITEMTEXT_KEY4,
	/* 0x04C */ ITEMTEXT_KEY5,
	/* 0x04D */ ITEMTEXT_KEY6,
	/* 0x04E */ ITEMTEXT_KEY7,
	/* 0x04F */ ITEMTEXT_KEY8,
	/* 0x050 */ ITEMTEXT_PEARL,
	/* 0x051 */ ITEMTEXT_KONG_DK,
	/* 0x052 */ ITEMTEXT_KONG_DIDDY,
	/* 0x053 */ ITEMTEXT_KONG_LANKY,
	/* 0x054 */ ITEMTEXT_KONG_TINY,
	/* 0x055 */ ITEMTEXT_KONG_CHUNKY,
	/* 0x056 */ ITEMTEXT_FAIRY,
	/* 0x057 */ ITEMTEXT_RAINBOWCOIN,
	/* 0x058 */ ITEMTEXT_FAKEITEM,
} item_purchase_text;