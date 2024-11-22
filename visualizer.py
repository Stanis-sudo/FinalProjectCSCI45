from bridges.bridges import *
from bridges.array import *
from bridges.array1d import *

# Initialize Bridges
    # create the Bridges object, set credentials
bridges = Bridges(5, "Stan", "1558142281567")
        # set title, description
bridges.set_title("Phonebook Storage Visualization")
bridges.set_description("The Phonebook app uses a custom Hash table to store contacts.")

def visualize(obj):
    # Create a Bridges array to represent the hash table
    arr = Array1D(len(obj.table))
    for i, bucket in enumerate(obj.table):
        if bucket:
            #bucket_str = ", ".join(str(contact) for contact in bucket)
            arr[i].label = len(bucket)
            if len(bucket) == 1:
                color = "green"
            elif len(bucket) == 2:
                color = "yellow"
            else: color = "red"
            arr[i].visualizer.color = color
        else:
            arr[i].label = "Empty"
            arr[i].visualizer.color = "cyan"
    bridges.set_data_structure(arr)
    bridges.visualize()