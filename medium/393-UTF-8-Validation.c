// Return whether the provided bytes are a valid UTF-8 encoding
bool validUtf8(int* data, int dataSize){
    int dataIndex = 0; // Current byte being looked at
    while(dataIndex < dataSize) // While there are bytes left
    {
        int dataCurrent = data[dataIndex]; // Store the current byte

        if(dataCurrent < 128) // If it's a 1-byte character (starts with a 0)
        {
            dataIndex++; // Move the index to the next byte
            continue;
        }
        // If the byte is < 11000000 or > 11101111 (out of valid range)
        else if(dataCurrent < 192 || dataCurrent > 247)
        {
            return false;
        }
        else // If it's an n-byte character where n > 1
        {
            int length; // Number of bytes that compose the character
            if(dataCurrent >= 240) // If the byte is >= 11110000
                length = 4;
            else if(dataCurrent >= 224) // If the byte is >= 11100000
                length = 3;
            else // If the byte is >= 11000000
                length = 2;

            // If the bytes that compose the character are more than the bytes
            // left
            if(length > dataSize - dataIndex)
            {
                return false;
            }

            int counter = 1; // Tracks the current byte of the current character
            while(counter < length) // Loop over the rest of the bytes
            {
                int dataCounter = data[dataIndex+counter]; // Get the next byte
                // If the byte doesn't start with 10
                if(dataCounter < 128 || dataCounter > 191)
                {
                    return false;
                }

                counter++; // Move to the next byte
            }

            dataIndex += length; // Move the index to the next character
        }
    }

    return true;
}
