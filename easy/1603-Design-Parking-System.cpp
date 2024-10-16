class ParkingSystem {
public:
    // Store number of spaces of a certain size
    // and the number of those spaces filled
    int numBig = 0;
    int bigFilled = 0;
    int numMedium = 0;
    int mediumFilled = 0;
    int numSmall = 0;
    int smallFilled = 0;
    
    ParkingSystem(int big, int medium, int small) {
        numBig = big;
        numMedium = medium;
        numSmall = small;
    }
    
    bool addCar(int carType) {
        if(carType == 1) 
        {
            if(bigFilled < numBig)
            {
                bigFilled++;
                return true;
            }
            else
                return false;
        }
        if(carType == 2)
        {
            if(mediumFilled < numMedium)
            {
                mediumFilled++;
                return true;
            }
            else
                return false;
        }
        if(carType == 3)
        {
            if(smallFilled < numSmall)
            {
                smallFilled++;
                return true;
            }
            else
                return false;
        }
        
        // No spaces for other sizes
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
