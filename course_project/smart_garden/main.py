from garden import Garden
from pot import Pot
from plant import Plant
from sensor import Sensor

if __name__ == '__main__':
    herbs = Plant("Herbs", 40,50, 22, 6, "")
    cherry_tomato = Plant("Cherry Tomatoes", 50, 70, 21, 8, "")

    herbs_pot = Pot(1001,"Herbs Pot", herbs, [Sensor(11, "Soil Moisture"), Sensor(12, "Light intensity")])
    cherry_tomato_pot = Pot(1002,"Cherry tomatoes", cherry_tomato,[Sensor(21, "Soil Moisture"), Sensor(22, "Light intensity")])

    my_garden = Garden("Home garden", "New", [herbs_pot, cherry_tomato_pot], (0.2, 0.2), "home" )

    print(my_garden)
