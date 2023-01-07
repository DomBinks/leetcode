class Solution:
    def recursiveFunc(self, arrays: List[List[int]]) -> List[int]:
        groups = []
        for array in arrays:
            found = False
            for i in range(len(groups)):
                if array[0] == groups[i][0]:
                    groups[i] = array[1::1] + groups[i]
                    found = True
                    break
                elif array[0] == groups[i][-1]:
                    groups[i].append(array[1::1])
                    found = True
                    break
                elif array[-1] == groups[i][0]:
                    groups[i] = array[0:-1] + groups[i]
                    found = True
                    break
                elif array[-1] == groups[i][-1]:
                    groups[i].append(array[0:-1])
                    found = True
                    break

            if found == False:
                groups.append(array)
        
        return groups

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        output = adjacentPairs
        while(len(output) > 1):
            output = self.recursiveFunc(output)
        
        return output[0]