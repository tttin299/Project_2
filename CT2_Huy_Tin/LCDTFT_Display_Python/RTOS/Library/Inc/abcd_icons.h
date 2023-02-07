#include "stm32f1xx_hal.h"
#include "icons_config.h"
const unsigned int a_icon_20x20[20*20] = {
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,Y,Y,Y,Y,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,Y,Y,Y,Y,Y,Y,B,B,B,B,B,B,B,
		B,B,B,B,B,B,Y,Y,B,B,B,B,Y,Y,B,B,B,B,B,B,
		B,B,B,B,B,Y,Y,B,B,B,B,B,B,Y,Y,B,B,B,B,B,
		B,B,B,B,Y,Y,B,B,B,B,B,B,B,B,Y,Y,B,B,B,B,
		B,B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B
};

const unsigned int b_icon_20x20[20*20] = {
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,Y,Y,Y,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B
};

const unsigned int c_icon_20x20[20*20] = {
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,B,B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B
};

const unsigned int d_icon_20x20[20*20] = {
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,
		B,B,Y,Y,B,B,B,B,B,B,B,B,B,B,B,Y,Y,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,
		B,B,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
		B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B
};




