/**
 * @file text.c
 * @author Ballaam
 * @brief Changes to the way text functions
 * @version 0.1
 * @date 2023-02-28
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include "../../include/common.h"

static unsigned int base_text_color = 0x2828FF00;
static unsigned int emph_text_colors[] = {
    0x8000FF00,
    0x8000FF00,
    0x8000FF00,
    0x8000FF00,
};

typedef struct text_params {
    /* 0x000 */ short effect_bitfield;
    /* 0x002 */ char unk2;
    /* 0x003 */ unsigned char opacity;
} text_params;

/*
    - Text effect handler: 806A370C (handleTextEffects)
    - Text normal color: (806A3B1A << 16) | 806A3B1E
    - Text Bubble Color: 806a3cb2
*/

int* displayModifiedText(int* dl, int style, int x, int y, char* text, text_params* params) {
    /**
     * @brief Display function for rendering a textbox with modified text colors
     */
    int dl_old = (int)dl;
    dl_old -= 4;
    *(unsigned int*)(dl_old) = base_text_color | (*(int*)(dl_old) & 0xFF);
    for (int i = 0; i < 4; i++) {
        if (params->effect_bitfield & (0x10 << i)) {
            *(unsigned int*)(dl_old) = emph_text_colors[i] | (*(int*)(dl_old) & 0xFF);
        }
    }
    return displayText(dl, style, x, y, text, 0);
}

void initTextChanges(void) {
    /**
     * @brief Initialize changes associated with the textboxes
     */
    // Text Bubble
    if (Rando.dark_mode_textboxes) {
        *(short*)(0x806A3CB2) = 0; // Set textbox color to #000000
        base_text_color = 0xFFFFFF00;
        emph_text_colors[0] = 0xFFA01000;
        emph_text_colors[1] = 0xFF000000;
    }
    // Text
    *(int*)(0x806A3B38) = 0xAFB10014; // Pass in effect bitfield as the last arg
    *(int*)(0x806A3B4C) = 0x0C000000 | (((int)&displayModifiedText & 0xFFFFFF) >> 2); // Modify draw function to reference new code
}