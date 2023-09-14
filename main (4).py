#Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")
#Define the derived class Batsman
  class Batsman( player):
    def play(self):
      print ("The batsman isbatting.")
 #Define the derived class Bawer
class Bower(play):
  def play(self):
    print("The bower is bowhing.")
 # create object of Batsman and Bowler classes
  batsman= Batsman()
  bowler=Bowler()
 # class the player() method for each object
  batsman.play()
  bowler.play()
      