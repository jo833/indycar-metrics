import metrics

if __name__ == "__main__":
    while (1):
        print("Welcome to indycar-metrics!\nPlease select which metric you wish to see:")
        print("1. Total Fuel Needed")
        print("2. Number of Fuel Pit Stops Needed")
        print("3. Tyre Wear Rate")
        print("4. Laps per Full Tank of Gas")
        print("5. Necessary Pit Stops Needed Based on Gas and Tyres")
        print("6. Laps that Pit Stops Need to Occur at")
        print("7. All Metrics")
        print("8. Exit")
        
        while (1):
            try:
                choice = int(input())
                break
            except:
                print("Please select a valid choice")
                
        if (choice == 1):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Total Fuel Needed:", metrics.totalFuel(raceLengthMiles))
        
        elif (choice == 2):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Fuel Pit Stop Needed:", metrics.fuelPitStops(raceLengthMiles))
        
        elif (choice == 3):
            print("Insert the Laps Per Tyres")
            while (1):
                try:
                    tyreLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Tyre Wear Rate:", metrics.tyreWearRate(tyreLaps))
        
        elif (choice == 4):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Race Length in Laps")
            while (1):
                try:
                    raceLengthLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Laps Per Tank:", metrics.lapsPerTank(raceLengthMiles, raceLengthLaps))

        elif (choice == 5):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Race Length in Laps")
            while (1):
                try:
                    raceLengthLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Laps Per Tyres")
            while (1):
                try:
                    tyreLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Necessary Pit Stops Needed Based on Gas and Tyres:", metrics.necessaryPitStops(raceLengthMiles, raceLengthLaps, tyreLaps))
        
        elif (choice == 6):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Race Length in Laps")
            while (1):
                try:
                    raceLengthLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Laps Per Tyres")
            while (1):
                try:
                    tyreLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Laps that Pit Stops Need to Occur at:", metrics.pitStopLaps(raceLengthMiles, raceLengthLaps, tyreLaps))
        
        elif (choice == 7):
            print("Insert the Race Length in Miles")
            while (1):
                try:
                    raceLengthMiles = float(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Race Length in Laps")
            while (1):
                try:
                    raceLengthLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            print("Insert the Laps Per Tyres")
            while (1):
                try:
                    tyreLaps = int(input())
                    break
                except:
                    print("Invalid Length. Try again.")
            
            print("Total Fuel Needed:", metrics.totalFuel(raceLengthMiles))
            print("Fuel Pit Stop Needed:", metrics.fuelPitStops(raceLengthMiles))
            print("Tyre Wear Rate:", metrics.tyreWearRate(tyreLaps))
            print("Laps Per Tank:", metrics.lapsPerTank(raceLengthMiles, raceLengthLaps))
            print("Necessary Pit Stops Needed Based on Gas and Tyres:", metrics.necessaryPitStops(raceLengthMiles, raceLengthLaps, tyreLaps))
            print("Laps that Pit Stops Need to Occur at:", metrics.pitStopLaps(raceLengthMiles, raceLengthLaps, tyreLaps))

        elif (choice == 8):
            print("Goodbye")
            break
        
        else:
            print("Invalid Choice")
