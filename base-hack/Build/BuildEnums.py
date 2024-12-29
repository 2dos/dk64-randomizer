"""Enums for the build process."""

from enum import IntEnum, auto


class ChangeType(IntEnum):
    """Change Type Enum."""

    Undefined = auto()
    PointerTable = auto()
    FixedLocation = auto()


class TextureFormat(IntEnum):
    """Texture Format Enum."""

    Null = auto()
    RGBA5551 = auto()
    RGBA32 = auto()
    I8 = auto()
    I4 = auto()
    IA8 = auto()
    IA4 = auto()


class CompressionMethods(IntEnum):
    """Texture Format Enum."""

    PythonGzip = auto()
    ExternalGzip = auto()
    Zlib = auto()


class TableNames(IntEnum):
    """Pointer Table Enum."""

    MusicMIDI = 0
    MapGeometry = auto()
    MapWalls = auto()
    MapFloors = auto()
    ModelTwoGeometry = auto()
    ActorGeometry = auto()
    Unknown6 = auto()
    TexturesUncompressed = auto()
    Cutscenes = auto()
    Setups = auto()
    InstanceScripts = auto()
    Animations = auto()
    Text = auto()
    Unknown13 = auto()
    TexturesHUD = auto()
    Paths = auto()
    Spawners = auto()
    DKTVInputs = auto()
    Triggers = auto()
    Unknown19 = auto()
    Unknown20 = auto()
    Autowalks = auto()
    Critters = auto()
    Exits = auto()
    RaceCheckpoints = auto()
    TexturesGeometry = auto()
    UncompressedFileSizes = auto()
    Unknown27 = auto()
    Unknown28 = auto()
    Unknown29 = auto()
    Unknown30 = auto()
    Unknown31 = auto()


class Maps(IntEnum):
    """Maps Enum."""

    TestMap = 0x0
    Funky = 0x1
    DKArcade = 0x2
    HelmBarrel_LankyMaze = 0x3
    JapesMountain = 0x4
    Cranky = 0x5
    JapesMinecart = 0x6
    Japes = 0x7
    JapesDillo = 0x8
    Jetpac = 0x9
    Kosh_VEasy = 0xA
    Snoop_NormalNoLogo = 0xB
    JapesShell = 0xC
    JapesPainting = 0xD
    AztecBeetle = 0xE
    Snide = 0xF
    AztecTinyTemple = 0x10
    Helm = 0x11
    Turtles_VEasy = 0x12
    Aztec5DTDK = 0x13
    AztecLlamaTemple = 0x14
    Aztec5DTDiddy = 0x15
    Aztec5DTTiny = 0x16
    Aztec5DTLanky = 0x17
    Aztec5DTChunky = 0x18
    Candy = 0x19
    Factory = 0x1A
    FactoryCarRace = 0x1B
    Helm_IntrosGameOver = 0x1C
    FactoryPowerShed = 0x1D
    Galleon = 0x1E
    GalleonSeasickShip = 0x1F
    BattyBarrel_VEasy = 0x20
    JapesUnderground = 0x21
    Isles = 0x22
    HelmBarrel_Target = 0x23
    FactoryCrusher = 0x24
    JapesBBlast = 0x25
    Aztec = 0x26
    GalleonSealRace = 0x27
    NintendoLogo = 0x28
    AztecBBlast = 0x29
    TroffNScoff = 0x2A
    Galleon5DSDiddyLankyChunky = 0x2B
    GalleonTreasureChest = 0x2C
    GalleonMermaid = 0x2D
    Galleon5DSDKTiny = 0x2E
    Galleon2DS = 0x2F
    Fungi = 0x30
    GalleonLighthouse = 0x31
    HelmBarrel_MushroomBounce = 0x32
    GalleonMechFish = 0x33
    FungiAntHill = 0x34
    BattleArena_BeaverBrawl = 0x35
    GalleonBBlast = 0x36
    FungiMinecart = 0x37
    FungiDiddyBarn = 0x38
    FungiDiddyAttic = 0x39
    FungiLankyAttic = 0x3A
    FungiDKBarn = 0x3B
    FungiSpider = 0x3C
    FungiMillFront = 0x3D
    FungiMillRear = 0x3E
    FungiMushroomSlam = 0x3F
    FungiGiantMushroom = 0x40
    Snoop_Normal = 0x41
    Maul_Hard = 0x42
    Snatch_Normal = 0x43
    Maul_Easy = 0x44
    Maul_Normal = 0x45
    FungiMushroomLeap = 0x46
    FungiShootingGame = 0x47
    Caves = 0x48
    BattleArena_KritterKarnage = 0x49
    Snatch_Easy = 0x4A
    Snatch_Hard = 0x4B
    DKRap = 0x4C
    MMayhem_Easy = 0x4D
    Barrage_Easy = 0x4E
    Barrage_Normal = 0x4F
    MainMenu = 0x50
    NFRTitleScreen = 0x51
    CavesBeetleRace = 0x52
    FungiDogadon = 0x53
    Caves5DITiny = 0x54
    Caves5DILanky = 0x55
    Caves5DIDK = 0x56
    Castle = 0x57
    CastleBallroom = 0x58
    CavesRotatingRoom = 0x59
    Caves5DCChunky = 0x5A
    Caves5DCDK = 0x5B
    Caves5DCDiddyLow = 0x5C
    Caves5DCTiny = 0x5D
    Caves1DC = 0x5E
    Caves5DIChunky = 0x5F
    Salvage_Normal = 0x60
    KLumsy = 0x61
    CavesTileFlip = 0x62
    Sortie_Easy = 0x63
    Caves5DIDiddy = 0x64
    Klamour_Easy = 0x65
    Bash_VEasy = 0x66
    Searchlight_VEasy = 0x67
    BBother_Easy = 0x68
    CastleTower = 0x69
    CastleMinecart = 0x6A
    MultiplayerBattleArena = 0x6B
    CastleCryptLankyTiny = 0x6C
    MultiplayerArena1 = 0x6D
    FactoryBBlast = 0x6E
    GalleonPufftoss = 0x6F
    CastleCryptDKDiddyChunky = 0x70
    CastleMuseum = 0x71
    CastleLibrary = 0x72
    Kosh_Easy = 0x73
    Kosh_Normal = 0x74
    Kosh_Hard = 0x75
    Turtles_Easy = 0x76
    Turtles_Normal = 0x77
    Turtles_Hard = 0x78
    BattyBarrel_Easy = 0x79
    BattyBarrel_Normal = 0x7A
    BattyBarrel_Hard = 0x7B
    Maul_Insane = 0x7C
    Snatch_Insane = 0x7D
    Snoop_VEasy = 0x7E
    Snoop_Easy = 0x7F
    Snoop_Hard = 0x80
    MMayhem_Normal = 0x81
    MMayhem_Hard = 0x82
    Barrage_Hard = 0x83
    Salvage_Hard = 0x84
    Salvage_Easy = 0x85
    Sortie_Normal = 0x86
    Sortie_Hard = 0x87
    BBother_Normal = 0x88
    BBother_Hard = 0x89
    Searchlight_Easy = 0x8A
    Searchlight_Normal = 0x8B
    Searchlight_Hard = 0x8C
    Klamour_Normal = 0x8D
    Klamour_Hard = 0x8E
    Klamour_Insane = 0x8F
    PPPanic_VEasy = 0x90
    PPPanic_Easy = 0x91
    PPPanic_Normal = 0x92
    PPPanic_Hard = 0x93
    Bash_Easy = 0x94
    Bash_Normal = 0x95
    Bash_Hard = 0x96
    CastleDungeon = 0x97
    Helm_IntroStory = 0x98
    Isles_DKTheatre = 0x99
    FactoryJack = 0x9A
    BattleArena_ArenaAmbush = 0x9B
    BattleArena_MoreKritterKarnage = 0x9C
    BattleArena_ForestFracas = 0x9D
    BattleArena_BishBashBrawl = 0x9E
    BattleArena_KamikazeKremlings = 0x9F
    BattleArena_PlinthPanic = 0xA0
    BattleArena_PinnaclePalaver = 0xA1
    BattleArena_ShockwaveShowdown = 0xA2
    CastleBasement = 0xA3
    CastleTree = 0xA4
    HelmBarrel_RandomKremling = 0xA5
    CastleShed = 0xA6
    CastleTrash = 0xA7
    CastleGreenhouse = 0xA8
    JapesLobby = 0xA9
    HelmLobby = 0xAA
    Treehouse = 0xAB
    Isles_IntroStoryRock = 0xAC
    AztecLobby = 0xAD
    GalleonLobby = 0xAE
    FactoryLobby = 0xAF
    TrainingGrounds = 0xB0
    TBarrel_Dive = 0xB1
    FungiLobby = 0xB2
    GalleonSubmarine = 0xB3
    TBarrel_Orange = 0xB4
    TBarrel_Barrel = 0xB5
    TBarrel_Vine = 0xB6
    CastleCrypt = 0xB7
    EnguardeArena = 0xB8
    CastleCarRace = 0xB9
    CavesBBlast = 0xBA
    CastleBBlast = 0xBB
    FungiBBlast = 0xBC
    FairyIsland = 0xBD
    MultiplayerArena2 = 0xBE
    RambiArena = 0xBF
    MultiplayerArena3 = 0xC0
    CastleLobby = 0xC1
    CavesLobby = 0xC2
    Isles_SnideRoom = 0xC3
    CavesDillo = 0xC4
    AztecDogadon = 0xC5
    TrainingGrounds_EndSequence = 0xC6
    CastleKutOut = 0xC7
    CavesShackDiddyHigh = 0xC8
    HelmBarrel_Rocketbarrel = 0xC9
    HelmBarrel_LankyShooting = 0xCA
    KRoolDK = 0xCB
    KRoolDiddy = 0xCC
    KRoolLanky = 0xCD
    KRoolTiny = 0xCE
    KRoolChunky = 0xCF
    BloopersEnding = 0xD0
    HelmBarrel_HiddenKremling = 0xD1
    HelmBarrel_FloorIsLava = 0xD2
    HelmBarrel_ChunkyShooting = 0xD3
    HelmBarrel_Rambi = 0xD4
    KLumsyEnding = 0xD5
    KRoolShoe = 0xD6
    KRoolArena = 0xD7


class Icons(IntEnum):
    """Icons enum."""

    WaterfallTall = 0x0
    WaterfallShort = 0x1
    Water = 0x2
    Lava = 0x3
    Sparkles = 0x4
    ExplosionPop = 0x5
    ExplosionLava = 0x6
    LeafGreen = 0x7
    ExplosionSmoke = 0x8
    ExplosionSmall = 0x9
    SolarFlare = 0xA
    Splash = 0xB
    Bubble = 0xC
    SparklePurple = 0xD
    SparkleYellow = 0xE
    SparkleGreen = 0xF
    SparklePurple_0 = 0x10
    SparkleYellow_0 = 0x11
    SparkleGreen_0 = 0x12
    ExplosionLargeSmoke = 0x13
    ExplosionPink = 0x14
    PlankBrownHorizontal = 0x15
    PlankBirchHorizontal = 0x16
    PlankBrownVertical = 0x17
    RippleStar = 0x18
    RippleCircle = 0x19
    ExplosionSmallSmoke = 0x1A
    StaticStar = 0x1B
    StaticZ = 0x1C
    FlareWhite = 0x1D
    StaticRain = 0x1E
    ExplosionMediumSmoke = 0x1F
    MelonBouncing = 0x20
    MelonRolling = 0x21
    FlareRed = 0x22
    Sparks = 0x23
    Peanut = 0x24
    FlareStar = 0x25
    PeanutShell = 0x26
    ExplosionSmall_0 = 0x27
    ExplosionLargeSmoke_0 = 0x28
    LaserBlue = 0x29
    Pineapple = 0x2A
    Fireball = 0x2B
    Orange = 0x2C
    Grape = 0x2D
    GrapeSplat = 0x2E
    SparkleTNT = 0x2F
    ExplosionFire = 0x30
    FireballSmall = 0x31
    CoinDiddy = 0x32
    CoinChunky = 0x33
    CoinLanky = 0x34
    CoinDK = 0x35
    CoinTiny = 0x36
    BananaDK = 0x37
    Film = 0x38
    OrangeBouncing = 0x39
    Crystal = 0x3A
    GB = 0x3B
    Medal = 0x3C
    BananaDiddy = 0x3D
    BananaChunky = 0x3E
    BananaLanky = 0x3F
    BananaDK_0 = 0x40
    BananaTiny = 0x41
    ExplosionKrash = 0x42
    ExplosionWhite = 0x43
    Coconut = 0x44
    CoconutShell = 0x45
    MelonSpinning = 0x46
    Tooth = 0x47
    CrateAmmo = 0x48
    CoinRace = 0x49
    BlueprintLanky = 0x4A
    Cannonball = 0x4B
    Crystal_0 = 0x4C
    Feather = 0x4D
    Guitar = 0x4E
    Bongos = 0x4F
    Sax = 0x50
    Triangle = 0x51
    Trombone = 0x52
    NoteYellowDouble = 0x53
    NoteYellowSingle = 0x54
    NoteGreenSingle = 0x55
    NotePurpleDouble = 0x56
    NoteRedDouble = 0x57
    NoteRedSingle = 0x58
    NoteWhiteDouble = 0x59
    BlueprintDiddy = 0x5A
    BlueprintChunky = 0x5B
    BlueprintDK = 0x5C
    BlueprintTiny = 0x5D
    SparkleSpinning = 0x5E
    StaticRain_0 = 0x5F
    WaterTranslucent = 0x60
    unk61 = 0x61
    ScreenBlack = 0x62
    CloudWhite = 0x63
    LaserThin = 0x64
    BubbleBlue = 0x65
    CircleWhiteFaded = 0x66
    CircleWhite = 0x67
    ParticleGreen = 0x68
    SparkleBlue = 0x69
    ExplosionWhiteSmoke = 0x6A
    Joystick = 0x6B
    FireWall = 0x6C
    StaticRainBubble = 0x6D
    ButtonA = 0x6E
    ButtonB = 0x6F
    ButtonZ = 0x70
    ButtonCD = 0x71
    ButtonCU = 0x72
    ButtonCL = 0x73
    Acid = 0x74
    ExplosionAcid = 0x75
    RaceHoop = 0x76
    AcidGoop = 0x77
    unk78 = 0x78
    BrokenBridge = 0x79
    WhitePole = 0x7A
    BridgeChip = 0x7B
    BeamRivets = 0x7C
    BunchChunky = 0x7D
    BunchDiddy = 0x7E
    BunchLanky = 0x7F
    BunchDK = 0x80
    BunchTiny = 0x81
    BalloonChunky = 0x82
    BalloonDiddy = 0x83
    BalloonDK = 0x84
    BalloonLanky = 0x85
    BalloonTiny = 0x86
    ButtonR = 0x87
    ButtonL = 0x88
    Fairy = 0x89
    BossKey = 0x8A
    Crown = 0x8B
    CoinRareware = 0x8C
    CoinNintendo = 0x8D
    NoSymbol = 0x8E
    Headphones = 0x8F
    WaterOpaque = 0x90
    ButtonStart = 0x91
    QuestionMark = 0x92
    FaceCandy = 0x93
    FaceCranky = 0x94
    FaceSnide = 0x95
    FaceFunky = 0x96
    ArrowLeft = 0x97
    SparkleWhite = 0x98
    BoulderChunkBlack = 0x99
    BoulderChunkGreen = 0x9A
    WoodChip = 0x9B
    Snowflake = 0x9C
    StaticWater = 0x9D
    SpinningLeaf = 0x9E
    FlashingWater = 0x9F
    CoinRainbow = 0xA0
    ShockwaveParticle = 0xA1
    Implosion = 0xA2
    RarewareEmployeeFace = 0xA3
    Smoke = 0xA4
    StaticSmoke = 0xA5
    BarrelBottomChunk = 0xA6
    FaceScoff = 0xA7
    BunchMulti = 0xA8
    FaceDK = 0xA9
    FaceDiddy = 0xAA
    FaceLanky = 0xAB
    FaceTiny = 0xAC
    FaceChunky = 0xAD
    FairyTick = 0xAE
    Wrinkly = 0xAF


class CreditsDirection(IntEnum):
    """Credits Direction Enum."""

    top = 0
    left = 1
    bottom = 2
    right = 3


class CreditsType(IntEnum):
    """Credits Type Enum."""

    normal = auto()
    header = auto()
    longheader = auto()


class Enemies(IntEnum):
    """List of Enemies with in-game index."""

    BeaverBlue = 0
    GiantClam = 1
    Krash = 2
    Book = 3
    ZingerCharger = 5
    Klobber = 6
    Snide = 7
    ArmyDillo = 8
    Klump = 9
    Cranky = 11
    Funky = 12
    Candy = 13
    Beetle = 14
    Mermaid = 15
    Kaboom = 16
    VultureTemple = 17
    Squawks = 18
    CutsceneDK = 19
    CutsceneDiddy = 20
    CutsceneLanky = 21
    CutsceneTiny = 22
    CutsceneChunky = 23
    TandSPadlock = 24
    Llama = 25
    MadJack = 26
    KlaptrapGreen = 27
    ZingerLime = 28
    VultureRace = 29
    KlaptrapPurple = 30
    KlaptrapRed = 31
    GetOut = 32
    BeaverGold = 33
    FireColumn = 35
    TNTMinecart0 = 36
    TNTMinecart1 = 37
    Pufftoss = 38
    SeasickCannon = 39
    KRoolFoot = 40
    Fireball = 42
    MushroomMan = 44
    Troff = 46
    BadHitDetectionMan = 48
    Ruler = 51
    ToyBox = 52
    Squawks1 = 53
    Seal = 54
    Scoff = 55
    RoboKremling = 56
    Dogadon = 57
    Kremling = 59
    SpotlightFish = 60
    KasplatDK = 61
    KasplatDiddy = 62
    KasplatLanky = 63
    KasplatTiny = 64
    KasplatChunky = 65
    MechFish = 66
    Seal1 = 67
    Fairy = 68
    SquawksSpotlight = 69
    Rabbit = 72
    Owl = 73
    NintendoLogo = 74
    FireBreath = 75
    MinigameController = 76
    BattleCrownController = 77
    ToyCar = 78
    TNTMinecart2 = 79
    CutsceneObject = 80
    Guard = 81
    RarewareLogo = 82
    ZingerRobo = 83
    Krossbones = 84
    Shuri = 85
    Gimpfish = 86
    MrDice0 = 87
    SirDomino = 88
    MrDice1 = 89
    Rabbit1 = 90
    FireballGlasses = 92
    KLumsy = 93
    SpiderBoss = 94
    SpiderSmall = 95
    Squawks2 = 96
    KRoolDK = 97
    SkeletonHead = 98
    Bat = 99
    EvilTomato = 100
    Ghost = 101
    Pufftup = 102
    Kosha = 103
    EnemyCar = 105
    KRoolDiddy = 106
    KRoolLanky = 107
    KRoolTiny = 108
    KRoolChunky = 109
    Bug = 110
    FairyQueen = 111
    IceTomato = 112


class Kong(IntEnum):
    """Kong Enum."""

    DK = 0
    Diddy = auto()
    Lanky = auto()
    Tiny = auto()
    Chunky = auto()


class Song(IntEnum):
    """Song Enum."""

    Silence = 0
    JapesStart = auto()
    Cranky = auto()
    JapesCart = auto()
    JapesDillo = auto()
    JapesCaves = auto()
    Funky = auto()
    UnusedCoin = auto()
    Minigames = auto()
    Triangle = auto()
    Guitar = auto()
    Bongos = auto()
    Trombone = auto()
    Saxophone = auto()
    AztecMain = auto()
    Transformation = auto()
    MiniMonkey = auto()
    HunkyChunky = auto()
    GBGet = auto()
    AztecBeetle = auto()
    OhBanana = auto()
    AztecTemple = auto()
    CompanyCoinGet = auto()
    BananaCoinGet = auto()
    VultureRing = auto()
    AztecDogadon = auto()
    Aztec5DT = auto()
    FactoryCarRace = auto()
    FactoryMain = auto()
    Snide = auto()
    JapesTunnels = auto()
    Candy = auto()
    MinecartCoinGet = auto()
    MelonSliceGet = auto()
    PauseMenu = auto()
    CrystalCoconutGet = auto()
    Rambi = auto()
    AztecTunnels = auto()
    WaterDroplets = auto()
    FactoryJack = auto()
    Success = auto()
    StartPause = auto()
    Failure = auto()
    TransitionOpen = auto()
    TransitionClose = auto()
    JapesHighPitched = auto()
    FairyTick = auto()
    MelonSliceDrop = auto()
    AztecChunkyKlaptraps = auto()
    FactoryCrusher = auto()
    JapesBlast = auto()
    FactoryResearchAndDevelopment = auto()
    FactoryProduction = auto()
    TroffNScoff = auto()
    BossDefeat = auto()
    AztecBlast = auto()
    GalleonOutside = auto()
    BossUnlock = auto()
    AwaitingBossEntry = auto()
    TwinklySounds = auto()
    GalleonPufftoss = auto()
    GalleonSealRace = auto()
    GalleonTunnels = auto()
    GalleonLighthouse = auto()
    BattleArena = auto()
    DropCoins = auto()
    FairyNearby = auto()
    Checkpoint = auto()
    ForestDay = auto()
    BlueprintGet = auto()
    ForestNight = auto()
    StrongKong = auto()
    Rocketbarrel = auto()
    Sprint = auto()
    ForestCart = auto()
    DKRap = auto()
    BlueprintDrop = auto()
    Galleon2DS = auto()
    Galleon5DS = auto()
    GalleonChest = auto()
    GalleonMermaid = auto()
    ForestDogadon = auto()
    MadMazeMaul = auto()
    Caves = auto()
    CavesTantrum = auto()
    NintendoLogoOld = auto()
    SuccessRaces = auto()
    FailureRaces = auto()
    BonusBarrelIntroduction = auto()
    StealthySnoop = auto()
    MinecartMayhem = auto()
    GalleonMechFish = auto()
    GalleonBlast = auto()
    ForestAnthill = auto()
    ForestBarn = auto()
    ForestMill = auto()
    SeasideSounds = auto()
    ForestSpider = auto()
    ForestMushroomRooms = auto()
    ForestMushroom = auto()
    BossIntroduction = auto()
    TagBarrel = auto()
    CavesBeetleRace = auto()
    CavesIgloos = auto()
    MiniBoss = auto()
    Castle = auto()
    CastleCart = auto()
    BaboonBalloon = auto()
    GorillaGone = auto()
    Isles = auto()
    IslesKremIsle = auto()
    IslesBFI = auto()
    IslesKLumsy = auto()
    HelmBoMOn = auto()
    MoveGet = auto()
    GunGet = auto()
    HelmBoMOff = auto()
    HelmBonus = auto()
    CavesCabins = auto()
    CavesRotatingRoom = auto()
    CavesIceCastle = auto()
    CastleTunnels = auto()
    IntroStory = auto()
    TrainingGrounds = auto()
    Enguarde = auto()
    KLumsyCelebration = auto()
    CastleCrypt = auto()
    HeadphonesGet = auto()
    PearlGet = auto()
    CastleDungeon_Chains = auto()
    AztecLobby = auto()
    JapesLobby = auto()
    FactoryLobby = auto()
    GalleonLobby = auto()
    MainMenu = auto()
    CastleInnerCrypts = auto()
    CastleBallroom = auto()
    CastleGreenhouse = auto()
    KRoolTheme = auto()
    CastleShed = auto()
    CastleTower = auto()
    CastleTree = auto()
    CastleMuseum = auto()
    BBlastFinalStar = auto()
    DropRainbowCoin = auto()
    RainbowCoinGet = auto()
    NormalStar = auto()
    BeanGet = auto()
    CavesDillo = auto()
    CastleKutOut = auto()
    CastleDungeon_NoChains = auto()
    BananaMedalGet = auto()
    KRoolBattle = auto()
    ForestLobby = auto()
    CavesLobby = auto()
    CastleLobby = auto()
    HelmLobby = auto()
    CastleTrash = auto()
    EndSequence = auto()
    KLumsyEnding = auto()
    JapesMain = auto()
    JapesStorm = auto()
    KRoolTakeoff = auto()
    CavesBlast = auto()
    ForestBlast = auto()
    CastleBlast = auto()
    IslesSnideRoom = auto()
    KRoolEntrance = auto()
    MonkeySmash = auto()
    ForestRabbitRace = auto()
    GameOver = auto()
    WrinklyKong = auto()
    FinalCBGet = auto()
    KRoolDefeat = auto()
    NintendoLogo = auto()


class Overlay(IntEnum):
    """Overlay Enum."""

    Boot = 0
    Static = 1
    Menu = 2
    Multiplayer = 3
    Minecart = 4
    Race = 5
    Critter = 6
    Boss = 7
    Bonus = 8
    Arcade = 9
    Jetpac = 10


class Vendors(IntEnum):
    """Vendors Enum."""

    Cranky = 0
    Funky = 1
    Candy = 2
    Snide = 3


class ExtraTextures(IntEnum):
    """Extra Textures in Table 25 after the bonus skins."""

    FakeGBShine = 0
    RainbowCoin0 = auto()
    RainbowCoin1 = auto()
    RainbowCoin2 = auto()
    MelonSurface = auto()
    BonusShell = auto()
    OSprintLogoLeft = auto()
    OSprintLogoRight = auto()
    BLockerItemMove = auto()
    BLockerItemBlueprint = auto()
    BLockerItemFairy = auto()
    BLockerItemBean = auto()
    BLockerItemPearl = auto()
    BLockerItemRainbowCoin = auto()
    BLockerItemIceTrap = auto()
    BLockerItemPercentage = auto()
    BLockerItemBalloon = auto()
    BLockerItemCompanyCoin = auto()
    BLockerItemKong = auto()
    BeetleTex0 = auto()
    BeetleTex1 = auto()
    BeetleTex2 = auto()
    BeetleTex3 = auto()
    BeetleTex4 = auto()
    BeetleTex5 = auto()
    BeetleTex6 = auto()
    Feather0 = auto()
    Feather1 = auto()
    Feather2 = auto()
    Feather3 = auto()
    Feather4 = auto()
    Feather5 = auto()
    Feather6 = auto()
    Feather7 = auto()
    FoolOverlay = auto()
    MedalRim = auto()
    MushTop0 = auto()
    MushTop1 = auto()
    ShellWood = auto()
    ShellMetal = auto()
    ShellQMark = auto()
    RocketTop = auto()
    BlastTop = auto()
    Anniv25Sticker = auto()
    Anniv25Barrel = auto()
    BeanSpin01 = auto()
    BeanSpin02 = auto()
    BeanSpin03 = auto()
    BeanSpin04 = auto()
    BeanSpin05 = auto()
    BeanSpin06 = auto()
    BeanSpin07 = auto()
    BeanSpin08 = auto()
    BeanSpin09 = auto()
    BeanSpin10 = auto()
    BeanSpin11 = auto()
    BeanSpin12 = auto()
    KrushaFace1 = auto()
    KrushaFace2 = auto()
    KrushaFace3 = auto()
    KrushaFace4 = auto()
    KrushaFace5 = auto()
    KrushaFace321 = auto()
    KrushaFace322 = auto()
    KrushaFace323 = auto()
    KrushaFace324 = auto()
    KrushaFace325 = auto()


class MoveTypes(IntEnum):
    """Move Types Enum."""

    special = 0
    slam = auto()
    weapon = auto()
    ammo_belt = auto()
    instrument = auto()
    flag = auto()
    gb = auto()
    gun_upgrade = auto()
    instrument_upgrade = auto()
