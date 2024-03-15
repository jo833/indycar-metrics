import math

# All this math is done in the perfect scenario without account for extenuating factors 
# of driving style, weather, and strategy based stops. 

def totalFuel( raceLengthMiles ) :
    # indycars use about 4 miles per gallon on average
    return round(raceLengthMiles / 4, 2)

def fuelPitStops( raceLengthMiles ) : 
    # indycars on can go 74 miles on a full tank of gas; granted that is using all of the gas
    fullTankMiles = 74

    return math.ceil( (raceLengthMiles - fullTankMiles)/ fullTankMiles)

def tyreWearRate( tyreLaps ) :
    return round(100 / tyreLaps, 2)

def lapsPerTank( raceLengthMiles, raceLengthLaps ):
    fuelTankMiles = 74
    milesPerLap = round(raceLengthMiles/raceLengthLaps, 2)
    return math.floor(fuelTankMiles/milesPerLap)

def necessaryPitStops( raceLengthMiles, raceLengthLaps, tyreLaps ):
    fuelLap = lapsPerTank(raceLengthMiles, raceLengthLaps)
    if (fuelLap < tyreLaps):
        return fuelPitStops(raceLengthMiles)
    else:
        return math.ceil( (raceLengthLaps - tyreLaps)/ tyreLaps)

def pitStopLaps( raceLengthMiles, raceLengthLaps, tyreLaps ):
    fuelLap = lapsPerTank(raceLengthMiles, raceLengthLaps)
    pitStopLoc = []
    if (fuelLap < tyreLaps):
        lapMax = fuelLap
        while (lapMax < raceLengthLaps):
            pitStopLoc.append(lapMax)
            lapMax += fuelLap
    else:
       lapMax = math.floor(tyreLaps)
       while (lapMax <raceLengthLaps):
           pitStopLoc.append(lapMax)
           lapMax += math.floor(tyreLaps)

    return pitStopLoc
