import metrics
# Test data is based off the Indy500, $1 Million Challenge, and Acura Grand Prix of Long Beach with 
# the exception of tyreLaps. That data is from news articles relating to races.
def testTotalFuel():
    assert metrics.totalFuel(raceLengthMiles=500) == 125, "Should be 125.00 gallons of gas"
    assert metrics.totalFuel(raceLengthMiles=61.34) == 15.34, "Should be 15.34 gallons of gas"
    assert metrics.totalFuel(raceLengthMiles=167.28) == 41.82, "Should be 41.82 gallons of gas"

def testFuelPitStops():
    assert metrics.fuelPitStops(raceLengthMiles=500)==6, "Should be 6 fuel based pit stops"
    assert metrics.fuelPitStops(raceLengthMiles=61.34)==0, "Should be 0 fuel based pit stops"
    assert metrics.fuelPitStops(raceLengthMiles=167.28)==2, "Should be 2 fuel based pit stops"

def testTyreRate():
    assert metrics.tyreWearRate(tyreLaps=30)==3.33, "Should be tyres degrade at 3.33% per lap"
    assert metrics.tyreWearRate(tyreLaps=39)==2.56, "Should be tyres degrade at 2.56% per lap"
    assert metrics.tyreWearRate(tyreLaps=45)==2.22, "Should be tyres degrade at 2.22% per lap"

def testLapsPerTank():
    assert metrics.lapsPerTank(raceLengthMiles=500, raceLengthLaps=200)==29, "Should be 29 laps"
    assert metrics.lapsPerTank(raceLengthMiles=61.34, raceLengthLaps=20)==24, "Should be 24 laps"
    assert metrics.lapsPerTank(raceLengthMiles=167.28, raceLengthLaps=85)==37, "Should be 37 laps"

def testNecessaryPitStops():
    assert metrics.necessaryPitStops(raceLengthMiles=500, raceLengthLaps=200, tyreLaps=50)==6, "Should be 6 pit stops"
    assert metrics.necessaryPitStops(raceLengthMiles=61.34, raceLengthLaps=20, tyreLaps=25)==0, "Should be 0 pit stops"
    assert metrics.necessaryPitStops(raceLengthMiles=167.28, raceLengthLaps=85, tyreLaps=27.5)==3, "Should be 3 pit stops"

def testPitStopLaps():
    assert metrics.pitStopLaps(raceLengthMiles=500, raceLengthLaps=200, tyreLaps=50)==[29, 58, 87, 116, 145, 174], "Pitstops should be at laps 29, 58, 87, 116, 145, and 174"
    assert metrics.pitStopLaps(raceLengthMiles=61.34, raceLengthLaps=20, tyreLaps=25)==[], "Should be no pitstops"
    assert metrics.pitStopLaps(raceLengthMiles=167.28, raceLengthLaps=85, tyreLaps=27.5)==[27, 54, 81], "Pitstops should be at laps 27, 54, and 81"

if __name__ == "__main__":
    testTotalFuel()
    testFuelPitStops()
    testTyreRate()
    testLapsPerTank()
    testNecessaryPitStops()
    testPitStopLaps()
    print("Everything passed")