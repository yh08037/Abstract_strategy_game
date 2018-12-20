#include <stdio.h>

void show_board(char chess_board[8][8])
{
	int i, j;
	for (i = 7; i > -1; i--)  // for (i = 8 - 1; i > 0 - 1; i--)
	{
		for (j = 0; j < 8; j++)
			printf("%c", chess_board[i][j]);
		printf("\n");
	}
	
}

int main(void)
{
	char chess_board[8][8] = { 
	{'R','N','B','K','Q','B','N','R'},   //A열  대문자는 하얀색 기물
	{'P','P','P','P','P','P','P','P'},   //B열
	{' ',},
	{' ' ,},
	{' ',},
	{' ',},
	{'p','p','p','p','p','p','p','p'},   //G열  소문자는 검은색 기물
	{'r','n','b','k','q','b','n','r'} }; //H열

	show_board(chess_board);

	int Is_game_end = 1; // 0은 게임 끝남, 1은 게임이 끝나지 않음
	while (Is_game_end)
	{
		//하얀색 차례 또는 검은색
			//행마 코드 입력받기
			//행마가 재대로 되는지 검사 (1. 움직이려는 자리에 아군이 있는지, 2. 해당 칸을 벗어나지 않았는지, 3. 해당 기물에 맞게 움직였는지, 4. 해당 기물을 움직였을 때 왕이 위협을 받게 되는지)
			//검은색 왕이 체크 또는 체크메이트인지 검사

		//체크메이트(승리), 스테일메이트, 50수 규칙, 3수 동일반복 규칙(이하 무승부)에 해당하면 게임을 끝냄

	}

	return 0;


}
