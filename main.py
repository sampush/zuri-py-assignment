from random import random, randrange


computerResult = ["rock", "paper", "scissors"]
condition = True
playerinput = ""
computerrandomchoice = ""
playerinput = ""


def playerinputcheck():
        if (playerinput != "rock" and playerinput != "paper" and playerinput != "scissors"):
           print('error invalid format')
           rungame()
        else:
             rungame()


def rungame():
         pRockWin = False
         cRockWin = False
         pPaperWin = False
         cPaperWin = False
         pScissorsWin = False
         cScissorsWin = False
         condition = True

         while (condition):
             print('Welcome to the rock, paper, scisscors game ')
             playerinput = input('Choose either rock, paper or scissors ')
             computerrandomchoice = randrange(0, 2)
             computerrandomchoice = computerResult[computerrandomchoice]
             playerinputcheck()


rungame()


def gamebrain():
    if (playerinput == "rock" and computerrandomchoice == "scissors"):
             pRockWin = True

    if (playerinput == "scissors" and computerrandomchoice == "rock"):
             cRockWin = True

    if (playerinput == "paper" and computerrandomchoice == "rock"):
             pPaperWin = True

    if (playerinput == "rock" and computerrandomchoice == "paper"):
             cPaperWin = True

    if (playerinput == "scissors" and computerrandomchoice == "paper"):
             pScissorsWin = True

    if (playerinput == "paper" and computerrandomchoice == "scissors"):
             cScissorsWin = True

    if (pRockWin == True):
            print("Player(" + playerinput  +  ") CPU(" + computerrandomchoice)
            print("player wins")

            condition = False

    if (cRockWin == True):
             print("Player(" + playerinput +  ") CPU(" + computerrandomchoice)
             print('computer wins')
             condition = False

    if (pPaperWin == True):
              print("Player(" + playerinput + ") CPU(" + computerrandomchoice)
              print('player wins')
              condition = False

    if (cPaperWin == True):
              print("Player(" + playerinput + ") CPU(" + computerrandomchoice)
              print('computer wins')
              condition = False

    if (cPaperWin == True ):
              print("Player(" + playerinput + ") CPU(" + computerrandomchoice )
              print('computer wins')
              condition = False

    if (pScissorsWin == True ):
              print("Player(" + playerinput + ") CPU(" + computerrandomchoice )
              print('player wins')
              condition = False

    if (cScissorsWin == True ):
             print("Player(" + playerinput + ") CPU(" + computerrandomchoice )
             print('computer wins')
             condition = False
