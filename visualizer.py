from bridges.bridges import *
from bridges.array import *
from bridges.array1d import *
import datetime
import sys

# Initialize Bridges
    # create the Bridges object, set credentials
bridges = Bridges(5, "Stan", "1558142281567")
    # set title, description
bridges.set_title("Phonebook Storage Visualization")
bridges.set_description("The Phonebook app uses a custom Hash table to store contacts.")
#bridges.post_visualization_link(False)


def visualize(obj, operation):
    # Create a Bridges array to represent the hash table
    arr = Array1D(len(obj.table))
    for i, bucket in enumerate(obj.table):
        if bucket:
            arr[i].label = len(bucket)
            if len(bucket) == 1:
                color = "deepskyblue"
            elif len(bucket) == 2:
                color = "lawngreen"
            elif len(bucket) == 3:
                color = "gold"
            elif len(bucket) == 4:
                color = "lightpink"
            else: color = "salmon"
            arr[i].visualizer.color = color
            arr[i].opacity = 0.50
        else:
            arr[i].label = "Empty"
            arr[i].visualizer.color = "cyan"

    with open("visualizer.log", "a") as file:
        # Redirect stdout to log file
        sys.stdout = file
        bridges.set_data_structure(arr)
        print(f"[{datetime.datetime.now()}] - \'{operation}\'       element={obj.contactCount}       hashSize={obj.size}")  # Log the current timestamp
        bridges.visualize()
        # Reset stdout back to default
        sys.stdout = sys.__stdout__
        
        