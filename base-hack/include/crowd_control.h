typedef enum cc_state {
    CC_READY, // 0
    CC_ENABLING, // 1
    CC_ENABLED, // 2
    CC_DISABLING, // 3
    CC_LOCKED, // 4
} cc_state;

typedef struct cc_effects {
	/* 0x000 */ unsigned char drunky_chunky;
    /* 0x001 */ unsigned char disable_tag_anywhere;
    /* 0x002 */ unsigned char ice_trap;
    /* 0x003 */ unsigned char rockfall;
    /* 0x004 */ unsigned char warp_to_rap;
    /* 0x005 */ unsigned char get_kaught;
    /* 0x006 */ unsigned char balloon;
} cc_effects;