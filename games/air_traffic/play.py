from retro.game import Game
from agents.plane_agent import Plane
from agents.airport_agent import Airport
from agents.plane_spawner import AirplaneSpawner

def main():
    plane_spawner = AirplaneSpawner()
    cyan_airport1 = Airport("_", "cyan", (59, 28))
    cyan_airport2 = Airport("_", "cyan", (60, 28))
    cyan_airport3 = Airport("_", "cyan", (61, 28))
    cyan_airport4 = Airport("_", "cyan", (62, 28))
    cyan_airport5 = Airport("_", "cyan", (63,28))
    cyan_airport6 = Airport("_", "cyan", (58,28))
    cyan_airport7 = Airport("|", "cyan", (57, 29))
    cyan_airport8 = Airport("|", "cyan", (57, 30))
    cyan_airport9 = Airport("|", "cyan", (57, 31))
    
    green_airport1 = Airport("_", "green", (0, 3))
    green_airport2 = Airport("_", "green", (1, 3))
    green_airport3 = Airport("_", "green", (2, 3))
    green_airport4 = Airport("_", "green", (3, 3))
    green_airport5 = Airport("_", "green", (4,3))
    green_airport6 = Airport("|", "green", (5,3))
    green_airport7 = Airport("|", "green", (5, 0))
    green_airport8 = Airport("|", "green", (5, 1))
    green_airport9 = Airport("|", "green", (5, 2))
    
    magenta_airport1 = Airport("_", "magenta", (5, 28))
    magenta_airport2 = Airport("_", "magenta", (0, 28))
    magenta_airport3 = Airport("_", "magenta", (1, 28))
    magenta_airport4 = Airport("_", "magenta", (2, 28))
    magenta_airport5 = Airport("_", "magenta", (3,28))
    magenta_airport6 = Airport("_", "magenta", (4,28))
    magenta_airport7 = Airport("|", "magenta", (6, 29))
    magenta_airport8 = Airport("|", "magenta", (6, 30))
    magenta_airport9 = Airport("|", "magenta", (6, 31))
    
    game = Game(
        [plane_spawner,
        cyan_airport1, cyan_airport2, 
        cyan_airport3, cyan_airport4, 
        cyan_airport5, cyan_airport6, 
        cyan_airport7, cyan_airport8, cyan_airport9, 
        magenta_airport1, magenta_airport2, 
        magenta_airport3, magenta_airport4, 
        magenta_airport5, magenta_airport6, 
        magenta_airport7, magenta_airport8, magenta_airport9,
        green_airport1, green_airport2, 
        green_airport3, green_airport4, 
        green_airport5, green_airport6, 
        green_airport7, green_airport8, green_airport9],
        {"Planes Landed": 0}
    )
    game.play()
