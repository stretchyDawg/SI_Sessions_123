import math

# theoretical, neutrailzed
data = [(.4921, .448), (.2612, .448), (.1732, .128), (.2811, .448), (.2962, .512), (.1718, .192), (.3138, .512), (.2084, .320)]

def percent_reacted(data_point):
    percent_reached = (data_point[1]/data_point[0]) * 100.0
    return percent_reached

def percent_error(data_point):
    percent_error = ((abs(data_point[0]-data_point[1]))/data_point[0])*100.0
    return percent_error

def main():
    count = 1
    avg_reached = 0
    avg_error = 0
    for point in data:
        print("Trial ", count, ": \n\tPercent Reacted: ", percent_reacted(point), "\n\tPercent Error: ", percent_error(point), "\n", sep = "")
        avg_reached += percent_reacted(point)
        avg_error += percent_error(point)
        count += 1
    print("Average Reached:", (avg_reached/8))
    print("Average Error:", (avg_error/8))

    
    
main()