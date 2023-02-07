/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "cmsis_os.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "ILI9341_Driver.h"
#include "Touch.h"
#include "display.h"
#include "string.h"
#include "park_icons.h"
#include "rc522.h"


/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
int lan = 0;
int state = 0 ;
uint16_t xtemp, ytemp;
char *select = {0};
int sel;
int sel_tmp;
int sel_chuyen;
int sel15,sel14,sel13,sel12,sel11=0;
int sel25,sel24,sel23,sel22,sel21=0;
int sel35,sel34,sel33,sel32,sel31=0;
int sel45,sel44,sel43,sel42,sel41=0;

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

uint16_t xtemp, ytemp;

uint8_t 	k;
uint8_t 	i;
uint8_t 	j;
uint8_t 	b;
uint8_t 	q;
uint8_t 	en;
uint8_t		lastID[4];
uint8_t	 txBuffer[16] = "";
uint8_t	str[MFRC522_MAX_LEN];
uint8_t 	retstr[10];
//uint8_t 	rxBuffer[14792];
uint8_t 	rxBuffer[14792]; // max 14894
//uint8_t 	rxBuffer1[30000];
//unsigned char 	rxBuffer1[12800];

//int tt=0;
//int m =0;
//int n =0;
//int a;
//uint8_t Rx_data;
char *str2 = {0};
//unsigned char gImage_PicTest[57600];
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
SPI_HandleTypeDef hspi1;
SPI_HandleTypeDef hspi2;

TIM_HandleTypeDef htim2;

UART_HandleTypeDef huart1;

osThreadId defaultTaskHandle;
osThreadId myTask02Handle;
osThreadId myTask03Handle;
/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_SPI1_Init(void);
static void MX_SPI2_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_TIM2_Init(void);
void StartDefaultTask(void const * argument);
void StartTask02(void const * argument);
void StartTask03(void const * argument);

/* USER CODE BEGIN PFP */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	HAL_UART_Receive_IT(&huart1,(uint8_t*)rxBuffer, 14792);
//	a = (char)rxBuffer[14791];
//	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_SET);
	if (rxBuffer[0] == 2 && rxBuffer[1] == 2 && rxBuffer[2] == 2 && rxBuffer[3] == 2 && rxBuffer[4] == 2)
	{
		// cho phep cam ung
		state=2;
	}else if (rxBuffer[0] == 0 && rxBuffer[1] == 0 && rxBuffer[2] == 0 && rxBuffer[3] == 0 && rxBuffer[4] == 0){
		// tat cam ung
		state=0;
	}else if (rxBuffer[0] == 3 && rxBuffer[1] == 3 && rxBuffer[2] == 3 && rxBuffer[3] == 3 && rxBuffer[4] == 3){
	
		// kiem tra va hien cho da co xe	
		sel11 = rxBuffer[5];
		sel12 = rxBuffer[6];
		sel13 = rxBuffer[7];
		sel14 = rxBuffer[8];
		sel15 = rxBuffer[9];

		sel21 = rxBuffer[10];
		sel22 = rxBuffer[11];
		sel23 = rxBuffer[12];
		sel24 = rxBuffer[13];
		sel25 = rxBuffer[14];

		sel31 = rxBuffer[15];
		sel32 = rxBuffer[16];
		sel33 = rxBuffer[17];
		sel34 = rxBuffer[18];
		sel35 = rxBuffer[19];
	
		sel41 = rxBuffer[20];
		sel42 = rxBuffer[21];
		sel43 = rxBuffer[22];
		sel44 = rxBuffer[23];
		sel45 = rxBuffer[24];
		
		state=3;
	
	}else{
		// cho hien hinh mat
		state=1;
	}
}
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void HienThiCho(){	
		//lan = lan + 1;
		if(sel15==15){
			Display_Round_Icon_20x20(park_icon_20x20, 235, 55, 20);
		} else	Display_Round_Icon_20x20(unpark1_icon_20x20, 235, 55, 20);
		
		if(sel14==14){
			Display_Round_Icon_20x20(park_icon_20x20, 185, 55, 20);
		} else	Display_Round_Icon_20x20(unpark1_icon_20x20, 185, 55, 20);
		
		if(sel13==13){
			Display_Round_Icon_20x20(park_icon_20x20, 135, 55, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 135, 55, 20);
		
		if(sel12==12){
			Display_Round_Icon_20x20(park_icon_20x20, 85, 55, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 85, 55, 20);
		
		if(sel11==11){
			Display_Round_Icon_20x20(park_icon_20x20, 35, 55, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 35, 55, 20);
		
	/*#######################################################################*/
		if(sel25==25){
			Display_Round_Icon_20x20(park_icon_20x20, 235, 105, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 235, 105, 20);
		
		if(sel24==24){
			Display_Round_Icon_20x20(park_icon_20x20, 185, 105, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 185, 105, 20);	
		
		if(sel23==23){
			Display_Round_Icon_20x20(park_icon_20x20, 135, 105, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 135, 105, 20);
		
		if(sel22==22){
			Display_Round_Icon_20x20(park_icon_20x20, 85, 105, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 85, 105, 20);
		
		if(sel21==21){
			Display_Round_Icon_20x20(park_icon_20x20, 35, 105, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 35, 105, 20);
		
	/*################################################################*/
		if(sel35==35){
			Display_Round_Icon_20x20(park_icon_20x20, 235, 155, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 235, 155, 20);
		
		if(sel34==34){
			Display_Round_Icon_20x20(park_icon_20x20, 185, 155, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 185, 155, 20);
		
		if(sel33==33){
			Display_Round_Icon_20x20(park_icon_20x20, 135, 155, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 135, 155, 20);
		
		if(sel32==32){
			Display_Round_Icon_20x20(park_icon_20x20, 85, 155, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 85, 155, 20);
		
		if(sel31==31){
			Display_Round_Icon_20x20(park_icon_20x20, 35, 155, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 35, 155, 20);
		
	/*################################################################*/
		if(sel45==45){
			Display_Round_Icon_20x20(park_icon_20x20, 235, 205, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 235, 205, 20);
		
		if(sel44==44){
			Display_Round_Icon_20x20(park_icon_20x20, 185, 205, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 185, 205, 20);
		
		if(sel43==43){
			Display_Round_Icon_20x20(park_icon_20x20, 135, 205, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 135, 205, 20);
		
		if(sel42==42){
			Display_Round_Icon_20x20(park_icon_20x20, 85, 205, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 85, 205, 20);
		
		if(sel41==41){
			Display_Round_Icon_20x20(park_icon_20x20, 35, 205, 20);
		} else Display_Round_Icon_20x20(unpark1_icon_20x20, 35, 205, 20);

			
}

void ChonCho(int sel){
	
	switch(sel){
		case 15: str2 = "A5";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 14: str2 = "A4";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 13: str2 = "A3";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 12: str2 = "A2";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 11: str2 = "A1";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		
		case 25: str2 = "B5";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 24: str2 = "B4";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 23: str2 = "B3";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 22: str2 = "B2";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 21: str2 = "B1";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		
		case 35: str2 = "C5";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 34: str2 = "C4";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 33: str2 = "C3";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 32: str2 = "C2";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 31: str2 = "C1";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		
		case 45: str2 = "D5";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 44: str2 = "D4";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 43: str2 = "D3";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 42: str2 = "D2";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
		case 41: str2 = "D1";HAL_UART_Transmit(&huart1, (uint8_t*)str2, 2, 100);;break;
	}
	
	//__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 80);
	__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 80);
	//osDelay(80);
}


void char_to_hex(uint8_t data) {
	uint8_t digits[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};

	if (data < 16) {
		retstr[0] = '0';
		retstr[1] = digits[data];
	} else {
		retstr[0] = digits[(data & 0xF0)>>4];
		retstr[1] = digits[(data & 0x0F)];
	}
}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_SPI1_Init();
  MX_SPI2_Init();
  MX_USART1_UART_Init();
  MX_TIM2_Init();
  /* USER CODE BEGIN 2 */

	ILI9341_Init();
  ILI9341_Set_Rotation(1);
	ILI9341_Fill_Screen(BLACK);
	MFRC522_Init();
  HAL_TIM_Base_Start(&htim2);
	// Start PWM at Port-B pin#6
	HAL_TIM_PWM_Start(&htim2,TIM_CHANNEL_1);
	
	//HAL_TIM_Base_Start(&htim1);
	// Start PWM at Port-B pin#6
	//HAL_TIM_PWM_Start(&htim1,TIM_CHANNEL_4);
//	Display_Color_Picture();
//	ILI9341_Draw_String(50, 205, BLACK, WHITE, "Xe vao!", 2);
//	Display_Color_Picture1();
//	ILI9341_Draw_String(220, 205, BLACK, WHITE, "Xe ra!", 2);
	
	//ILI9341_Fill_Screen(BLACK);
  //Display_Menu();
	//ILI9341_Set_Rotation(3);
	//Display_Color_Picture();
	//Display_Color_Picture1();
	//ILI9341_Set_Rotation(3);
	ILI9341_Fill_Screen1(BLACK);
	Display_Menu();

  TP_Init();
  /* USER CODE END 2 */

  /* USER CODE BEGIN RTOS_MUTEX */
  /* add mutexes, ... */
  /* USER CODE END RTOS_MUTEX */

  /* USER CODE BEGIN RTOS_SEMAPHORES */
  /* add semaphores, ... */
  /* USER CODE END RTOS_SEMAPHORES */

  /* USER CODE BEGIN RTOS_TIMERS */
  /* start timers, add new ones, ... */
  /* USER CODE END RTOS_TIMERS */

  /* USER CODE BEGIN RTOS_QUEUES */
  /* add queues, ... */
  /* USER CODE END RTOS_QUEUES */

  /* Create the thread(s) */
  /* definition and creation of defaultTask */
  osThreadDef(defaultTask, StartDefaultTask, osPriorityNormal, 0, 128);
  defaultTaskHandle = osThreadCreate(osThread(defaultTask), NULL);

  /* definition and creation of myTask02 */
  osThreadDef(myTask02, StartTask02, osPriorityIdle, 0, 128);
  myTask02Handle = osThreadCreate(osThread(myTask02), NULL);

  /* definition and creation of myTask03 */
  osThreadDef(myTask03, StartTask03, osPriorityIdle, 0, 128);
  myTask03Handle = osThreadCreate(osThread(myTask03), NULL);

  /* USER CODE BEGIN RTOS_THREADS */
  /* add threads, ... */
  /* USER CODE END RTOS_THREADS */

  /* Start scheduler */
  osKernelStart();

  /* We should never get here as control is now taken by the scheduler */
  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
//		if(state==1){
//			ILI9341_Fill_Screen1(BLACK);
//			Display_Color_Picture();
//			HAL_Delay(500);
//			ILI9341_Fill_Screen1(BLACK);
//			state=0;
//		}
			
		
		
		


  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief SPI1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_SPI1_Init(void)
{

  /* USER CODE BEGIN SPI1_Init 0 */

  /* USER CODE END SPI1_Init 0 */

  /* USER CODE BEGIN SPI1_Init 1 */

  /* USER CODE END SPI1_Init 1 */
  /* SPI1 parameter configuration*/
  hspi1.Instance = SPI1;
  hspi1.Init.Mode = SPI_MODE_MASTER;
  hspi1.Init.Direction = SPI_DIRECTION_2LINES;
  hspi1.Init.DataSize = SPI_DATASIZE_8BIT;
  hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi1.Init.NSS = SPI_NSS_SOFT;
  hspi1.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_4;
  hspi1.Init.FirstBit = SPI_FIRSTBIT_MSB;
  hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi1.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN SPI1_Init 2 */

  /* USER CODE END SPI1_Init 2 */

}

/**
  * @brief SPI2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_SPI2_Init(void)
{

  /* USER CODE BEGIN SPI2_Init 0 */

  /* USER CODE END SPI2_Init 0 */

  /* USER CODE BEGIN SPI2_Init 1 */

  /* USER CODE END SPI2_Init 1 */
  /* SPI2 parameter configuration*/
  hspi2.Instance = SPI2;
  hspi2.Init.Mode = SPI_MODE_MASTER;
  hspi2.Init.Direction = SPI_DIRECTION_2LINES;
  hspi2.Init.DataSize = SPI_DATASIZE_8BIT;
  hspi2.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi2.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi2.Init.NSS = SPI_NSS_SOFT;
  hspi2.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_4;
  hspi2.Init.FirstBit = SPI_FIRSTBIT_MSB;
  hspi2.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi2.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi2.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN SPI2_Init 2 */

  /* USER CODE END SPI2_Init 2 */

}

/**
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 1440;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 65535;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 500;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */
  HAL_TIM_MspPostInit(&htim2);

}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 115200;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, RESET_Pin|DC_Pin|CS_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_12|T_CLK_Pin|T_CS_Pin|T_DIN_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pins : RESET_Pin DC_Pin CS_Pin */
  GPIO_InitStruct.Pin = RESET_Pin|DC_Pin|CS_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : PB12 */
  GPIO_InitStruct.Pin = GPIO_PIN_12;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : T_CLK_Pin T_CS_Pin T_DIN_Pin */
  GPIO_InitStruct.Pin = T_CLK_Pin|T_CS_Pin|T_DIN_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : T_DO_Pin T_IRQ_Pin */
  GPIO_InitStruct.Pin = T_DO_Pin|T_IRQ_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/* USER CODE BEGIN Header_StartDefaultTask */
/**
  * @brief  Function implementing the defaultTask thread.
  * @param  argument: Not used
  * @retval None
  */
/* USER CODE END Header_StartDefaultTask */
void StartDefaultTask(void const * argument)
{
  /* USER CODE BEGIN 5 */
  /* Infinite loop */
	//HAL_UART_Receive_IT(&huart1,(uint8_t*)rxBuffer, 1);
  for(;;)
  {
		if(state == 2){
			
			tp_dev.scan(0);
			if(tp_dev.sta & TP_PRES_DOWN)
			{
				xtemp = TP_Read_XOY(0xD0);
				ytemp = TP_Read_XOY(0x90);
									 
				//Sau khi chon dung' thi se~ gui uart den python de chup, tu python se gui anh ve`
				if(xtemp > 700 && xtemp < 1400 && ytemp > 2600 && ytemp < 3100) {
					Display_Round_Icon_20x20(park_icon_20x20, 235, 55, 20);
					sel=15;
					ChonCho(sel);				
				}
				if(xtemp > 700 && xtemp < 1400 && ytemp > 2000 && ytemp < 2500) {
					Display_Round_Icon_20x20(park_icon_20x20, 185, 55, 20);
					sel=14;
					ChonCho(sel);
				}
				if(xtemp > 700 && xtemp < 1400 && ytemp > 1400 && ytemp < 1900) {
					Display_Round_Icon_20x20(park_icon_20x20, 135, 55, 20);
					sel=13;
					ChonCho(sel);
				}
				if(xtemp > 700 && xtemp < 1400 && ytemp > 800 && ytemp < 1300) {
					Display_Round_Icon_20x20(park_icon_20x20, 85, 55, 20);
					sel=12;
					ChonCho(sel);
				}
				if(xtemp > 700 && xtemp < 1400 && ytemp > 200 && ytemp < 700) {
					Display_Round_Icon_20x20(park_icon_20x20, 35, 55, 20);
					sel=11;
					ChonCho(sel);
				}
	/*################################################################################*/
				
				if(xtemp > 1500 && xtemp < 2200 && ytemp > 2600 && ytemp < 3100) {
					Display_Round_Icon_20x20(park_icon_20x20, 235, 105, 20);
					sel=25;
					ChonCho(sel);
				}
				if(xtemp > 1500 && xtemp < 2200 && ytemp > 2000 && ytemp < 2500) {
					Display_Round_Icon_20x20(park_icon_20x20, 185, 105, 20);
					sel=24;
					ChonCho(sel);
				}
				if(xtemp > 1500 && xtemp < 2200 && ytemp > 1400 && ytemp < 1900) {
					Display_Round_Icon_20x20(park_icon_20x20, 135, 105, 20);
					sel=23;
					ChonCho(sel);
				}
				if(xtemp > 1500 && xtemp < 2200 && ytemp > 800 && ytemp < 1300) {
					Display_Round_Icon_20x20(park_icon_20x20, 85, 105, 20);
					sel=22;
					ChonCho(sel);
				}
				if(xtemp > 1500 && xtemp < 2200 && ytemp > 200 && ytemp < 700) {
					Display_Round_Icon_20x20(park_icon_20x20, 35, 105, 20);
					sel=21;
					ChonCho(sel);
				}
	/*################################################################################*/
				
				if(xtemp > 2300 && xtemp < 3000 && ytemp > 2600 && ytemp < 3100) {
					Display_Round_Icon_20x20(park_icon_20x20, 235, 155, 20);
					sel=35;
					ChonCho(sel);
				}
				if(xtemp > 2300 && xtemp < 3000 && ytemp > 2000 && ytemp < 2500) {
					Display_Round_Icon_20x20(park_icon_20x20, 185, 155, 20);
					sel=34;
					ChonCho(sel);
				}
				if(xtemp > 2300 && xtemp < 3000 && ytemp > 1400 && ytemp < 1900) {
					Display_Round_Icon_20x20(park_icon_20x20, 135, 155, 20);
					sel=33;
					ChonCho(sel);
				}
				if(xtemp > 2300 && xtemp < 3000 && ytemp > 800 && ytemp < 1300) {
					Display_Round_Icon_20x20(park_icon_20x20, 85, 155, 20);
					sel=32;
					ChonCho(sel);
				}
				if(xtemp > 2300 && xtemp < 3000 && ytemp > 200 && ytemp < 700) {
					Display_Round_Icon_20x20(park_icon_20x20, 35, 155, 20);
					sel=31;
					ChonCho(sel);
				}
	/*################################################################################*/
				
				if(xtemp > 3100 && xtemp < 3800 && ytemp > 2600 && ytemp < 3100) {
					Display_Round_Icon_20x20(park_icon_20x20, 235, 205, 20);
					sel=45;
					ChonCho(sel);
				}
				if(xtemp > 3100 && xtemp < 3800 && ytemp > 2000 && ytemp < 2500) {
					Display_Round_Icon_20x20(park_icon_20x20, 185, 205, 20);
					sel=44;
					ChonCho(sel);
				}
				if(xtemp > 3100 && xtemp < 3800 && ytemp > 1400 && ytemp < 1900) {
					Display_Round_Icon_20x20(park_icon_20x20, 135, 205, 20);
					sel=43;
					ChonCho(sel);
					
				}
				if(xtemp > 3100 && xtemp < 3800 && ytemp > 800 && ytemp < 1300) {
					Display_Round_Icon_20x20(park_icon_20x20, 85, 205, 20);
					sel=42;
					ChonCho(sel);
				}
				if(xtemp > 3100 && xtemp < 3800 && ytemp > 200 && ytemp < 700) {
					Display_Round_Icon_20x20(park_icon_20x20, 35, 205, 20);
					sel=41;
					ChonCho(sel);
				}
			}
		}
		
		
		if(state==1){
			ILI9341_Fill_Screen1(BLACK);
			//Display_Color_Picture();
			for (uint16_t i = 0; i < 86; i++)
			{
				for (uint16_t j = 0; j < 86; j++)
				{
					ILI9341_Draw_Double_Pixel(j+117, i+77, rxBuffer[(172 * i) + j * 2], rxBuffer[(172 * i) + j * 2 + 1]);
				}
			}
			
			osDelay(1000);
			ILI9341_Fill_Screen1(BLACK);
			Display_Menu();
		
			HienThiCho();
		}
		
		
		if(state==3){
			
//			ILI9341_Fill_Screen1(BLACK);
//			Display_Menu();
			HienThiCho();
		/*################################################################*/
			//osDelay(100);
			state = 0;
			__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 40);
		}
		
		//if(state==0){
//			ILI9341_Fill_Screen1(BLACK);
//			Display_Menu();
			
		/*################################################################*/
			
			
//		}
		
    osDelay(1);
  }
  /* USER CODE END 5 */
}

/* USER CODE BEGIN Header_StartTask02 */
/**
* @brief Function implementing the myTask02 thread.
* @param argument: Not used
* @retval None
*/
/* USER CODE END Header_StartTask02 */
void StartTask02(void const * argument)
{
  /* USER CODE BEGIN StartTask02 */
	//int iii;
	HAL_UART_Receive_IT(&huart1,(uint8_t*)rxBuffer, 14792);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_SET);
  /* Infinite loop */
  for(;;)
  {
//		i++;
//		if(tt==1){
//			__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 250);
//			HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_RESET);
//			osDelay(5000);
//			tt=0;
//		}
//		else{
//			HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_SET);
//			__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 650	);
//		}
		if (!MFRC522_Request(PICC_REQIDL, str)) 
		{	
			if (!MFRC522_Anticoll(str)) 
			{			
			//HAL_ResumeTick();
				j = 0;
				q = 0;			
				b = 8;
				en = 1;
 
				for (i=0; i<4; i++) if (lastID[i] != str[i]) j = 1;
 
				if (j && en) {
					q = 0;
					en = 0;
					for (i=0; i<4; i++) lastID[i] = str[i];
					
					for (i=0; i<4; i++) {
						char_to_hex(str[i]);
						
						txBuffer[b] = retstr[0];
						b++;
						txBuffer[b] = retstr[1];
						b++;
					}
					
					//while(!MFRC522_Anticoll(str));
					HAL_UART_Transmit(&huart1, txBuffer, 16, 100);
					HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13);
					
				
				}	
			}
		}	
		q = q + 200;
		if (!q) {
			en = 1;																															// Delay against scan kode
			for (i=0; i<4; i++) lastID[i] = 0;	
		}
		//HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13);
		osDelay(100);
//    osDelay(100);
  }
  /* USER CODE END StartTask02 */
}

/* USER CODE BEGIN Header_StartTask03 */
/**0
* @brief Function implementing the myTask03 thread.
* @param argument: Not used
* @retval None
*/
/* USER CODE END Header_StartTask03 */
void StartTask03(void const * argument)
{
  /* USER CODE BEGIN StartTask03 */
  /* Infinite loop */
	__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1,40);
  for(;;)
  {
//		__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 30);
//		osDelay(80);
		//__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 75);
//		__HAL_TIM_SetCompare(&htim2, TIM_CHANNEL_1, 80);
//    osDelay(10);
		
  }
  /* USER CODE END StartTask03 */
}

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
