#The SensorDataMerge class contains two methods, sensorData and mergeddData.
#sensorData gets the start,end time and the rate in a certain format and puts it into a tuple
#This also checks the highest rate for a given time and puts it into the dict
#mergedData loops through the data from sensorData and provides the output in sorted order
#The tuple is appended in a sorted order with start time, end time and rate


class SensorDataMerge:
    def __init__(self):
        self.data = {}
    
    #sensorData gets the start,end time and the rate in a certain format and puts it into a tuple
    #This also checks the highest rate for a given time and puts it into the dict
    def sensorData(self, sensor_data):
        for start, end, rate in sensor_data:
            for second in range(start, end): # As suggested during our discussion, I am looping through start time and end time and finding the highest rate
                if second not in self.data or rate > self.data[second]:
                    self.data[second] = rate

    #mergedData loops through the data from sensorData and provides the output in sorted order
    #The tuple is appended in a sorted order with start time, end time and rate
    def mergedData(self):
        merged_data = []
        for start_second in sorted(self.data.keys()):
            end_second = start_second + 1
            rate = self.data[start_second]
            while end_second in self.data and self.data[end_second] == rate:
                end_second += 1
            merged_data.append((start_second, end_second, rate))
        return merged_data

input_data = [(1, 2, 2),(2, 4, 6),(3, 7, 8),(7, 9, 8),(5, 10, 15),(12, 15, 12),(11, 16, 20)]
merger = SensorDataMerge()
merger.sensorData(input_data)
output_data = merger.mergedData()

print(output_data)