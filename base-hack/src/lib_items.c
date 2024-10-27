#include "../include/common.h"

/*
	This is a pre-generated file. Please don't directly modify this file as this will be overwritten upon next build.
	Visit build/item_dictionaries.py to modify this output.
	
Thanks,
		Ballaam
*/

const short acceptable_items[] = {0x74,0xde,0xe0,0xe1,0xdd,0xdf,0x48,0x28f,0x13c,0x18d,0x90,0x5b,0x1f2,0x59,0x1f3,0x1f5,0x1f6,0x257,0x258,0x259,0x25a,0x25b,0x198,0x1b4,0x25c,0xb7,0x25d,0x264,0x265,0x25f,0x260,0x261,0x262,0x27e};
const item_conversion_info item_conversions[] = {
	{.actor=45, .model_two=116, .scale=0.25f},
	{.actor=78, .model_two=222, .scale=2.00f},
	{.actor=75, .model_two=224, .scale=2.00f},
	{.actor=77, .model_two=225, .scale=2.00f},
	{.actor=79, .model_two=221, .scale=2.00f},
	{.actor=76, .model_two=223, .scale=2.00f},
	{.actor=345, .model_two=72, .scale=0.40f},
	{.actor=346, .model_two=655, .scale=0.40f},
	{.actor=72, .model_two=316, .scale=0.17f},
	{.actor=86, .model_two=397, .scale=0.25f},
	{.actor=367, .model_two=144, .scale=0.22f},
	{.actor=348, .model_two=91, .scale=0.25f},
	{.actor=349, .model_two=498, .scale=0.25f},
	{.actor=350, .model_two=89, .scale=0.25f},
	{.actor=351, .model_two=499, .scale=0.25f},
	{.actor=352, .model_two=501, .scale=0.25f},
	{.actor=353, .model_two=502, .scale=0.25f},
	{.actor=354, .model_two=599, .scale=0.25f},
	{.actor=355, .model_two=600, .scale=0.25f},
	{.actor=356, .model_two=601, .scale=0.25f},
	{.actor=357, .model_two=602, .scale=0.25f},
	{.actor=358, .model_two=603, .scale=0.25f},
	{.actor=361, .model_two=408, .scale=0.25f},
	{.actor=362, .model_two=436, .scale=0.25f},
	{.actor=363, .model_two=604, .scale=0.25f},
	{.actor=140, .model_two=183, .scale=0.25f},
	{.actor=364, .model_two=605, .scale=0.25f},
	{.actor=365, .model_two=612, .scale=0.25f},
	{.actor=366, .model_two=613, .scale=0.25f},
	{.actor=52, .model_two=86, .scale=1.00f},
	{.actor=47, .model_two=606, .scale=0.25f},
	{.actor=121, .model_two=142, .scale=1.00f},
	{.actor=51, .model_two=143, .scale=1.00f},
	{.actor=369, .model_two=607, .scale=0.25f},
	{.actor=370, .model_two=608, .scale=0.25f},
	{.actor=371, .model_two=609, .scale=0.25f},
	{.actor=372, .model_two=610, .scale=0.25f},
	{.actor=375, .model_two=638, .scale=0.25f}
};
const unsigned short bounce_objects[] = {45,345,346,72,86,367,348,349,350,351,352,353,354,355,356,357,358,361,362,363,364,365,366,369,370,371,372,375};
const unsigned short actor_drops[] = {45,78,75,77,79,76,345,346,72,86,367,348,349,350,351,352,353,347,354,355,356,357,358,361,362,363,140,364,365,366,52,47,121,51,369,370,371,372,375};
const item_scale_info item_scales[] = {
	{.type=116, .scale=0.25f},
	{.type=222, .scale=2.00f},
	{.type=224, .scale=2.00f},
	{.type=225, .scale=2.00f},
	{.type=221, .scale=2.00f},
	{.type=223, .scale=2.00f},
	{.type=72, .scale=0.40f},
	{.type=655, .scale=0.40f},
	{.type=316, .scale=0.17f},
	{.type=397, .scale=0.25f},
	{.type=144, .scale=0.22f},
	{.type=91, .scale=0.25f},
	{.type=498, .scale=0.25f},
	{.type=89, .scale=0.25f},
	{.type=499, .scale=0.25f},
	{.type=501, .scale=0.25f},
	{.type=502, .scale=0.25f},
	{.type=0, .scale=0.25f},
	{.type=599, .scale=0.25f},
	{.type=600, .scale=0.25f},
	{.type=601, .scale=0.25f},
	{.type=602, .scale=0.25f},
	{.type=603, .scale=0.25f},
	{.type=408, .scale=0.25f},
	{.type=436, .scale=0.25f},
	{.type=604, .scale=0.25f},
	{.type=183, .scale=0.25f},
	{.type=605, .scale=0.25f},
	{.type=612, .scale=0.25f},
	{.type=613, .scale=0.25f},
	{.type=86, .scale=1.00f},
	{.type=606, .scale=0.25f},
	{.type=142, .scale=1.00f},
	{.type=143, .scale=1.00f},
	{.type=607, .scale=0.25f},
	{.type=608, .scale=0.25f},
	{.type=609, .scale=0.25f},
	{.type=610, .scale=0.25f},
	{.type=638, .scale=0.25f}
};
collision_info object_collisions[] = {
	{.type=13, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=2, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=10, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=3, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=31, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=6, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=30, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=4, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=22, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=5, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=36, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=3, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=35, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=4, .actor_equivalent=53, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=39, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=6, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=28, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=5, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=29, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=2, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=43, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=2, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=520, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=3, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=518, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=6, .actor_equivalent=110, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=517, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=4, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=519, .collectable_type=0, .unk4=0.08f, .unk8=0.95f, .intended_actor=5, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=145, .collectable_type=2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=349, .collectable_type=2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=350, .collectable_type=2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=351, .collectable_type=2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=352, .collectable_type=2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=222, .collectable_type=12, .unk4=0.08f, .unk8=0.95f, .intended_actor=2, .actor_equivalent=78, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=224, .collectable_type=12, .unk4=0.08f, .unk8=0.95f, .intended_actor=3, .actor_equivalent=75, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=225, .collectable_type=12, .unk4=0.08f, .unk8=0.95f, .intended_actor=4, .actor_equivalent=77, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=221, .collectable_type=12, .unk4=0.08f, .unk8=0.95f, .intended_actor=5, .actor_equivalent=79, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=223, .collectable_type=12, .unk4=0.08f, .unk8=0.95f, .intended_actor=6, .actor_equivalent=76, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=463, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=120, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=464, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=119, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=465, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=118, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=466, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=122, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=91, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=3 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=498, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=4 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=89, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=5 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=499, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=6 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=501, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=7 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=502, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=8 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=599, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=9 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=600, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=10 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=601, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=11 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=602, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=12 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=603, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=13 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=183, .collectable_type=1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=140, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=116, .collectable_type=8, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=45, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=86, .collectable_type=4, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=52, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=143, .collectable_type=-2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=51, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=17, .collectable_type=-2, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=142, .collectable_type=5, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=121, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=87, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=47, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=606, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=152, .collectable_type=6, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=144, .collectable_type=10, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=22 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=236, .collectable_type=11, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=54, .hitbox_y_center=0, .hitbox_radius=0, .hitbox_height=0},
	{.type=316, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=72, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=397, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=86, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=648, .collectable_type=8, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=45, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=72, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=0 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=655, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=1 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=408, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=16 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=436, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=17 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=604, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=18 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=605, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=19 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=612, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=20 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=613, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=21 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=607, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=24 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=608, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=25 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=609, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=26 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=610, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=27 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13},
	{.type=638, .collectable_type=-1, .unk4=0.08f, .unk8=0.95f, .intended_actor=0, .actor_equivalent=30 + CUSTOM_ACTORS_START, .hitbox_y_center=8, .hitbox_radius=4, .hitbox_height=13}
};
drop_item drops[] = {
	{.source_object=178, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=212, .dropped_object=47, .drop_music=47, .drop_count=2},
	{.source_object=205, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=208, .dropped_object=52, .drop_music=0, .drop_count=3},
	{.source_object=209, .dropped_object=51, .drop_music=0, .drop_count=1},
	{.source_object=3, .dropped_object=53, .drop_music=0, .drop_count=3},
	{.source_object=241, .dropped_object=78, .drop_music=76, .drop_count=1},
	{.source_object=242, .dropped_object=75, .drop_music=76, .drop_count=1},
	{.source_object=243, .dropped_object=77, .drop_music=76, .drop_count=1},
	{.source_object=244, .dropped_object=79, .drop_music=76, .drop_count=1},
	{.source_object=245, .dropped_object=76, .drop_music=76, .drop_count=1},
	{.source_object=187, .dropped_object=52, .drop_music=0, .drop_count=3},
	{.source_object=238, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=235, .dropped_object=47, .drop_music=47, .drop_count=2},
	{.source_object=291, .dropped_object=47, .drop_music=47, .drop_count=2},
	{.source_object=183, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=206, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=261, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=285, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=271, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=270, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=269, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=224, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=262, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=289, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=182, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=175, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=259, .dropped_object=121, .drop_music=0, .drop_count=1},
	{.source_object=276, .dropped_object=52, .drop_music=0, .drop_count=2},
	{.source_object=273, .dropped_object=52, .drop_music=0, .drop_count=1},
	{.source_object=230, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=340, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=373, .dropped_object=47, .drop_music=47, .drop_count=2},
	{.source_object=374, .dropped_object=47, .drop_music=47, .drop_count=1},
	{.source_object=0, .dropped_object=0, .drop_music=0, .drop_count=0}, // Terminator
};