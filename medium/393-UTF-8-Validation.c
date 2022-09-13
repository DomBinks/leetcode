bool validUtf8(int* data, int dataSize){
    int current = 0;
    while(current < dataSize)
    {
        if(data[current] < 128) 
        {
            current++;
            continue;
        }
        else if(data[current] > 128 && data[current] < 192 || data[current] == 255)
        {
            return false;
        }
        else
        {
            int length = 0;
            int col = 128;
            while(data[current] - col >= 0)
            {
               data[0] -= col;
               length++;
               col /= 2;
            }

            if(length > dataSize)
            {
                return false;
            }

            int counter = 1;
            while(counter < length)
            {
                if(data[current+counter] < 128 || data[current+counter] > 191)
                {
                    return false;
                }

                counter++;
            }

            current += length;
        }
    }

    return true;
}
