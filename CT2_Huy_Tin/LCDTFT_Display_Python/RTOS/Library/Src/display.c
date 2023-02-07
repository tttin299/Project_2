#include <display.h>
#include "ILI9341_Driver.h"
#include "icons_included.h"
#include "PicTest.c"
#include "PicTest1.c"



void Display_Round_Icon_40x40(const unsigned int icon[], unsigned int x0, unsigned int y0, unsigned int r)
{
	uint64_t k = 0;

    ILI9341_Draw_Circle(x0, y0, r, BLUE, 1);

	for(uint32_t j = y0 - 19; j < y0 + 21; j++)
	{
		for(uint32_t i = x0 -19; i < x0 + 21; i++)
		{
				ILI9341_Draw_Pixel(i, j, icon[k]);
				k++;
		}
	}
}

void Display_Round_Icon_20x20(const unsigned int icon[], unsigned int x0, unsigned int y0, unsigned int r)
{
	uint64_t k = 0;

    ILI9341_Draw_Circle(x0, y0, r, BLUE, 1);

	for(uint32_t j = y0 - 9; j < y0 + 11; j++)
	{
		for(uint32_t i = x0 -9; i < x0 + 11; i++)
		{
				ILI9341_Draw_Pixel(i, j, icon[k]);
				k++;
		}
	}
}


void Display_Square_Icon_40x40(const unsigned int icon[], unsigned int x0, unsigned int y0)
{
	uint64_t k = 0;

	for(uint32_t j = y0; j < y0 + 40; j++)
	{
		for(uint32_t i = x0; i < x0 + 40; i++)
		{
				ILI9341_Draw_Pixel(i, j, icon[k]);
				k++;
		}
	}
}

void Display_Menu()
{

	ILI9341_Set_Rotation(3);

	/* Refresh the screen to black background */
	//ILI9341_Fill_Screen(BLACK);
	//HAL_Delay(500);

	/* Counting through all the bytes of those icons */
	uint64_t k = 0;
	/* Draw border for the menu */
    ILI9341_Draw_Empty_Rectangle(YELLOW, 10, 30, 310, 230);

    /* Write something */
	ILI9341_Draw_String(10,10,WHITE,BLACK,"Nha xe tu dong!",2);

	/* Battery Icon in the top right corner */
    for(uint32_t j = 10; j < 20; j++) {
    	for(uint32_t i = 280; i < 300; i++) {
				ILI9341_Draw_Pixel(i, j, battery_icon[k]);
				k++;
			}
	}

    /* =================================List of Icons================================= */

    /* ===========================Icon No.1=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 35, 55, 20);

    /* ===========================Icon No.2=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 85, 55, 20);

    /* ===========================Icon No.3=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 135, 55, 20);

    /* ===========================Icon No.4=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 185, 55, 20);

    /* ===========================Icon No.5=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 235, 55, 20);

    /* ===========================Icon No.6=========================== */
    Display_Round_Icon_20x20(a_icon_20x20, 285, 55, 20);
	
		/*#####################################################################*/
		
		/* ===========================Icon No.1=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 35, 105, 20);

    /* ===========================Icon No.2=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 85, 105, 20);

    /* ===========================Icon No.3=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 135, 105, 20);

    /* ===========================Icon No.4=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 185, 105, 20);

    /* ===========================Icon No.5=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 235, 105, 20);

    /* ===========================Icon No.6=========================== */
    Display_Round_Icon_20x20(b_icon_20x20, 285, 105, 20);
		
		/*#####################################################################*/
		
		/* ===========================Icon No.1=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 35, 155, 20);

    /* ===========================Icon No.2=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 85, 155, 20);

    /* ===========================Icon No.3=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 135, 155, 20);

    /* ===========================Icon No.4=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 185, 155, 20);

    /* ===========================Icon No.5=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 235, 155, 20);

    /* ===========================Icon No.6=========================== */
    Display_Round_Icon_20x20(c_icon_20x20, 285, 155, 20);
		
		/*#####################################################################*/
		
		/* ===========================Icon No.1=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 35, 205, 20);

    /* ===========================Icon No.2=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 85, 205, 20);

    /* ===========================Icon No.3=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 135, 205, 20);

    /* ===========================Icon No.4=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 185, 205, 20);

    /* ===========================Icon No.5=========================== */
    Display_Round_Icon_20x20(unpark_icon_20x20, 235, 205, 20);

    /* ===========================Icon No.6=========================== */
    Display_Round_Icon_20x20(d_icon_20x20, 285, 205, 20);
	
		

	CS_OFF;
}


void Display_Picture()
{
	/* Set the rotation that fit the image */
	ILI9341_Set_Rotation(1);

	/* Drawing Image to the LCD */
	uint64_t k = 0;
	for(uint32_t i = 0; i < 240; i++)
	{
		for(uint32_t j = 320; j > 0; j--)
		{
			ILI9341_Draw_Pixel(i, j, gImage_PicTest[k]);
			k++;
		}
	}
}

void Display_Text()
{
	/* Refresh the screen to black background */
	ILI9341_Fill_Screen(BLACK);
	HAL_Delay(500);

	/* Draw border for the menu */
    ILI9341_Draw_Empty_Rectangle(YELLOW, 10, 30, 310, 230);

    /* Write something */
	ILI9341_Draw_String(20, 40, WHITE, BLACK, "Hello User!", 2);

	ILI9341_Draw_String(20, 60, WHITE, BLACK, "This is the test for TFT LCD!", 2);

	ILI9341_Draw_String(20, 80, WHITE, BLACK, "For more information, please visit:", 2);

	ILI9341_Draw_String(20, 100, WHITE, BLACK, "    aweirdolife.wordpress.com    ", 2);

	Display_Square_Icon_40x40(back_icon_40x40, 0, 200);
}



void Display_Color_Picture()
{
	for (uint16_t i = 0; i < 86; i++)
	{
		for (uint16_t j = 0; j < 86; j++)
		{
			ILI9341_Draw_Double_Pixel(j+117, i+77, gImage_PicTest[(172 * i) + j * 2], gImage_PicTest[(172 * i) + j * 2 + 1]);
		}
	}

	//Display_Square_Icon_40x40(back_icon_40x40, 0, 200);
}




void Display_Color_Picture1()
{
	for (uint16_t i = 0; i < 180; i++)
	{
		for (uint16_t j = 0; j < 160; j++)
		{
			ILI9341_Draw_Double_Pixel(j+80, i+40, gImage_PicTest1[(320 * i) + j * 2], gImage_PicTest1[(320 * i) + j * 2 + 1]);
		}
	}

	//Display_Square_Icon_40x40(back_icon_40x40, 0, 200);
}
