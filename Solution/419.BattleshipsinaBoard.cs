


public int CountBattleships(char[,] board)
{
    int number = 0;
    for (int i = 0; i < board.GetLength(0); i++)
    {
        for (int j = 0; j < board.GetLength(1); j++)
        {
            if (board[i, j] == 'X' &amp;&amp; (i == 0 || board[i - 1, j] != 'X') &amp;&amp; (j == 0 || board[i, j - 1] != 'X'))
            {
                number++;
            }
        }
    return number;
}
