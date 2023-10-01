"""Region enum."""
from enum import Enum, auto


class Regions(Enum):
    """Region enum."""

    # Special regions
    GameStart = auto()  # This holds your training barrels for fast start and sends you off to your starting region
    Credits = auto()  # This holds the Banana Hoard

    # DK Isles Regions
    Treehouse = auto()
    TrainingGrounds = auto()
    IslesMain = auto()
    OuterIsles = auto()
    IslesMainUpper = auto()
    IslesEar = auto()
    Prison = auto()
    BananaFairyRoom = auto()
    RarewareGBRoom = auto()
    JungleJapesLobby = auto()
    AngryAztecLobby = auto()
    KremIsle = auto()
    KremIsleBeyondLift = auto()
    KremIsleTopLevel = auto()
    IslesSnideRoom = auto()
    FranticFactoryLobby = auto()
    GloomyGalleonLobby = auto()
    GloomyGalleonLobbyEntrance = auto()
    CabinIsle = auto()
    IslesAboveWaterfall = auto()
    IslesAirspace = auto()
    AztecLobbyRoof = auto()
    FungiForestLobby = auto()
    CrystalCavesLobby = auto()
    CreepyCastleLobby = auto()
    HideoutHelmLobby = auto()
    KRool = auto()

    # Jungle Japes Regions
    JungleJapesMedals = auto()
    JungleJapesStart = auto()
    JungleJapesMain = auto()
    JapesBeyondPeanutGate = auto()
    JapesBeyondCoconutGate1 = auto()
    JapesBeyondFeatherGate = auto()
    TinyHive = auto()
    JapesBeyondCoconutGate2 = auto()
    BeyondRambiGate = auto()
    JapesLankyCave = auto()
    Mine = auto()
    JapesTopOfMountain = auto()
    JapesMinecarts = auto()
    JapesCatacomb = auto()
    JapesBossLobby = auto()
    JapesBoss = auto()
    JapesBaboonBlast = auto()

    # Angry Aztec Regions
    AngryAztecMedals = auto()
    AngryAztecStart = auto()
    BetweenVinesByPortal = auto()
    AztecTunnelBeforeOasis = auto()
    AngryAztecOasis = auto()
    TempleStart = auto()
    TempleUnderwater = auto()
    AngryAztecConnectorTunnel = auto()
    AngryAztecMain = auto()
    AztecDonkeyQuicksandCave = auto()
    DonkeyTemple = auto()
    DiddyTemple = auto()
    LankyTemple = auto()
    TinyTemple = auto()
    ChunkyTemple = auto()
    AztecTinyRace = auto()
    LlamaTemple = auto()
    LlamaTempleBack = auto()
    AztecBossLobby = auto()
    AztecBoss = auto()
    AztecBaboonBlast = auto()

    # Frantic Factory Regions
    FranticFactoryMedals = auto()
    FranticFactoryStart = auto()
    Testing = auto()
    RandD = auto()
    FactoryTinyRaceLobby = auto()
    FactoryTinyRace = auto()
    ChunkyRoomPlatform = auto()
    PowerHut = auto()
    BeyondHatch = auto()
    LowerCore = auto()
    InsideCore = auto()
    MiddleCore = auto()
    UpperCore = auto()
    FactoryBossLobby = auto()
    FactoryBoss = auto()
    FactoryBaboonBlast = auto()

    # Gloomy Galleon Regions
    GloomyGalleonMedals = auto()
    GloomyGalleonStart = auto()
    GalleonPastVines = auto()
    GalleonBeyondPineappleGate = auto()
    LighthouseSurface = auto()
    LighthousePlatform = auto()
    LighthouseUnderwater = auto()
    LighthouseSnideAlcove = auto()
    Lighthouse = auto()
    MermaidRoom = auto()
    SickBay = auto()
    Shipyard = auto()
    ShipyardUnderwater = auto()
    SealRace = auto()
    TreasureRoom = auto()
    TreasureRoomDiddyGoldTower = auto()
    TinyChest = auto()
    Submarine = auto()
    Mechafish = auto()
    LankyShip = auto()
    TinyShip = auto()
    BongosShip = auto()
    GuitarShip = auto()
    TromboneShip = auto()
    SaxophoneShip = auto()
    TriangleShip = auto()
    GalleonBossLobby = auto()
    GalleonBoss = auto()
    GalleonBaboonBlast = auto()

    # Fungi Forest Regions
    FungiForestMedals = auto()
    FungiForestStart = auto()
    ForestMinecarts = auto()
    GiantMushroomArea = auto()
    MushroomLower = auto()
    MushroomLowerExterior = auto()
    MushroomUpper = auto()
    MushroomNightDoor = auto()
    MushroomNightExterior = auto()
    MushroomUpperExterior = auto()
    MushroomChunkyRoom = auto()
    MushroomLankyZingersRoom = auto()
    MushroomLankyMushroomsRoom = auto()
    HollowTreeArea = auto()
    Anthill = auto()
    MillArea = auto()
    MillChunkyTinyArea = auto()
    SpiderRoom = auto()
    GrinderRoom = auto()
    MillRafters = auto()
    WinchRoom = auto()
    MillAttic = auto()
    ThornvineArea = auto()
    ThornvineBarn = auto()
    WormArea = auto()
    ForestBossLobby = auto()
    ForestBoss = auto()
    ForestBaboonBlast = auto()

    # Crystal Caves Regions
    CrystalCavesMedals = auto()
    CrystalCavesMain = auto()
    CavesSnideArea = auto()
    CavesBlueprintCave = auto()
    CavesBonusCave = auto()
    CavesBlueprintPillar = auto()
    CavesBananaportSpire = auto()
    BoulderCave = auto()
    CavesLankyRace = auto()
    FrozenCastle = auto()
    IglooArea = auto()
    GiantKosha = auto()
    DonkeyIgloo = auto()
    DiddyIgloo = auto()
    LankyIgloo = auto()
    TinyIgloo = auto()
    ChunkyIgloo = auto()
    CabinArea = auto()
    RotatingCabin = auto()
    DonkeyCabin = auto()
    DiddyLowerCabin = auto()
    DiddyUpperCabin = auto()
    LankyCabin = auto()
    TinyCabin = auto()
    ChunkyCabin = auto()
    CavesBossLobby = auto()
    CavesBoss = auto()
    CavesBaboonBlast = auto()

    # Creepy Castle Regions
    CreepyCastleMedals = auto()
    CreepyCastleMain = auto()
    CastleWaterfall = auto()
    CastleTree = auto()
    Library = auto()
    Ballroom = auto()
    MuseumBehindGlass = auto()
    CastleTinyRace = auto()
    Tower = auto()
    Greenhouse = auto()
    TrashCan = auto()
    Shed = auto()
    Museum = auto()
    LowerCave = auto()
    Crypt = auto()
    CastleMinecarts = auto()
    Mausoleum = auto()
    UpperCave = auto()
    Dungeon = auto()
    CastleBossLobby = auto()
    CastleBoss = auto()
    CastleBaboonBlast = auto()

    # Hideout Helm Regions
    HideoutHelmStart = auto()
    HideoutHelmMain = auto()
    HideoutHelmDonkeyRoom = auto()
    HideoutHelmDiddyRoom = auto()
    HideoutHelmLankyRoom = auto()
    HideoutHelmTinyRoom = auto()
    HideoutHelmChunkyRoom = auto()
    HideoutHelmAfterBoM = auto()

    # Shop Regions
    FunkyGeneric = auto()
    FunkyJapes = auto()
    FunkyAztec = auto()
    FunkyFactory = auto()
    FunkyGalleon = auto()
    FunkyForest = auto()
    FunkyCaves = auto()
    FunkyCastle = auto()
    CandyGeneric = auto()
    CandyAztec = auto()
    CandyFactory = auto()
    CandyGalleon = auto()
    CandyCaves = auto()
    CandyCastle = auto()
    CrankyGeneric = auto()
    CrankyJapes = auto()
    CrankyAztec = auto()
    CrankyFactory = auto()
    CrankyGalleon = auto()
    CrankyForest = auto()
    CrankyCaves = auto()
    CrankyCastle = auto()
    CrankyIsles = auto()
    Snide = auto()
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __mod__(self, other):
        if isinstance(other, int):
            return self.value % other
        raise TypeError("Unsupported operand types for % ({} and {})".format(type(self).__name__, type(other).__name__))

    def __to_bytes(self, length, byteorder, signed):
        return self.value.to_bytes(length, byteorder, signed=signed)

    def to_bytes(self, length, byteorder='big', signed=False):
        return self.__to_bytes(length, byteorder, signed)

    def __sub__(self, other):
        if isinstance(other, int):
            return self.value - other
        raise TypeError("Unsupported operand types for - ({} and {})".format(type(self).__name__, type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, type(self)):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, type(self)):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        return NotImplemented