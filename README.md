# ObscuraChess & sunfishplus.py

ObscuraChess is a way to play chess with any device compatible with Amazon Alexa (such as the Echo family of products), through a simple voice interface.
sunfishplus.py is a series of modifications to the sunfish.py chess engine, including adjustable difficulty and the ability to play as black.

To set up the skill on your own developer account, you will need to following Alexa invocations not including the standard included:

StartGameIntent: {Difficulty, Color)

MoveIntent: {Movepiece, Movedto}

ResignIntent

The StartGameIntent will query the user for the difficulty they would like to play at, and the color they would like to play as.
As of now, the AWS lambda function does not support adjustable difficulty or color, but sunfishplus.py does.

The MoveIntent consists of two parts:
Movepiece (try) Movedto, where the first is the position you would like to move from, and the second where you would like to move.
These commands are said as the NATO Phonetic Alphabet, followed by a number. For example:

Move Echo 2 try Echo 4, would make the move E2E4.

The ResignIntent will resign the game, and the computer will win.

