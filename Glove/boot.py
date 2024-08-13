
# glove
import uasyncio as asyncio
from hall import *
import time
import machine
from ESPnow import *
from message_formating import *
from NetworkSetup import *


peer_FES = b'x!\x84\xd8\x84\xb0' # Replace with the MAC address of the receiver

hallPins = [12, 14, 27, 26, 25]

sensors = [HallSensor(pin) for pin in hallPins]


ssid = 'AnwarLaptop'
password = 'Anwar12345'
wifi = WIFI_Connection(ssid, password)

glove = espNow(peer_FES)


# Initialize the pins for the switches
timer_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
# switch_min_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
# start_stop_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Start/stop button
start_stop_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)  # Start/stop button

counter = 0

max_values = []
min_values = []

# Example threshold values for each finger
thresholds = [1, 1, 1, 1, 1]

max_set = False
min_set = False
checking_angles = False

grasping_count = 0
releasing_count = 0

def median(lst):
    n = len(lst)
    s = sorted(lst)
    medians_list = s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2
    return medians_list

def average(lst):
    return sum(lst) / len(lst) if lst else 0

def get_max_min_list_of_angles(sensors):
    values = []
    start_time = time.time()
    
    while (time.time() - start_time) < 2:  # Run for 5 seconds
        wifi.disconnect_wifi()
        angles = getAllAngles(sensors)
        wifi.connect_wifi()
        print("step(1)_angles:", angles)
        values.append(angles)
        time.sleep(0.1)
    print(len(values))
    print("\n")
    print("step(2)_all_angles_lists:", values)
    print("\n")

    # Divide the values list into 2 sublists
    num_sublists = 2
    sublist_size = len(values) // num_sublists
    sublists = [values[i * sublist_size:(i + 1) * sublist_size] for i in range(num_sublists)]
    
    print("step(3)_sublists:", sublists)
    print("\n")

    all_median_values = []
    
    for sublist in sublists:
        # Further divide each sublist into groups of 6 lists
        divided_values = [sublist[i:i + 6] for i in range(0, len(sublist), 6)]
        print("step(4)_lists(include 6 lists)_of_sublists:", divided_values)
        median_values = []
        
        for group in divided_values:
            if len(group) == 6:
                median_group = [median([v[i] for v in group]) for i in range(len(group[0]))]
                median_values.append(median_group)
        
        print("step(5)_median_of_groups_in_sublist:", median_values)
        print("\n")
        
        if median_values:
            # Calculate the average of the median values for each sublist
            average_median_values = [average([median_values[j][i] for j in range(len(median_values))]) for i in range(len(median_values[0]))]
            all_median_values.append(average_median_values)
    
        print("step(6)_average_median_values:", all_median_values)
        print("\n")

    return all_median_values

def start_timer(angles_type):
    global max_values, min_values, max_set, min_set    # Declare globals to modify them
   
    if angles_type == "max":
        max_values.clear()
        max_set = False
    elif angles_type == "min":
        min_values.clear()
        min_set = False

    while True:
        if angles_type == "max":
            max_values.append(get_max_min_list_of_angles(sensors))
            print("final_step_max", max_values)
            max_set = True
            break
        elif angles_type == "min":
            min_values.append(get_max_min_list_of_angles(sensors))
            print("final_step_min", min_values)
            min_set = True
            break

def calculate_closeness(angles, max_vals, min_vals):
    grasping_percentages = []
    releasing_percentages = []
    
    for angle, max_val, min_val in zip(angles, max_vals, min_vals):
        if max_val != min_val:  # Avoid division by zero
            grasping_percentage = abs(100 * angle / max_val)
            releasing_percentage = abs(100 * (1 - angle / max_val))
        else:
            grasping_percentage = 50
            releasing_percentage = 50
        
        grasping_percentages.append(grasping_percentage)
        releasing_percentages.append(releasing_percentage)
    
    avg_grasping = sum(grasping_percentages) / len(grasping_percentages)
    avg_releasing = sum(releasing_percentages) / len(releasing_percentages)
    
    return avg_grasping, avg_releasing

def check_angles():
    global max_values, min_values, thresholds, checking_angles, grasping_count, releasing_count  # Declare globals to use them
    
    while checking_angles:
        angles = getAllAngles(sensors)
        print("Checking angles:", angles)
        
        for max_group, min_group in zip(max_values, min_values):
            
            for max_vals, min_vals in zip(max_group, min_group):
                differences_max = [abs(angle - max_val) for angle, max_val in zip(angles, max_vals)]
                differences_min = [abs(angle - min_val) for angle, min_val in zip(angles, min_vals)]
                
                print("Differences from max values:", differences_max)
                print("Differences from min values:", differences_min)
                
                avg_grasping, avg_releasing = calculate_closeness(angles, max_vals, min_vals)
                print(f"Closeness to Grasping: {avg_grasping:.2f}%")
                print(f"Closeness to Releasing: {avg_releasing:.2f}%")
                
                precentage_msg =MessageEncoding(GLOVE_HEADER, GLOVE_ANGLES_SUBHEADER, [avg_releasing,avg_grasping])
                glove.espNow_Send(glove.peer_master, precentage_msg)
                
                if all(diff <= thresh for diff, thresh in zip(differences_max, thresholds)):
                    grasping_count += 1
                    print(f"Grasping count: {grasping_count}")
                    if grasping_count > 3:
                        print("Grasping completely done")
                        state_msg =MessageEncoding(GLOVE_HEADER, GLOVE_STATE_SUBHEADER, GLOVE_STATE_GRASP)
                        glove.espNow_Send(glove.peer_master, state_msg)
                        checking_angles = False
                        return
                elif all(diff <= thresh for diff, thresh in zip(differences_min, thresholds)):
                    releasing_count += 1
                    print(f"Releasing count: {releasing_count}")
                    if releasing_count > 3:
                        print("Releasing completely done")
                        state_msg =MessageEncoding(GLOVE_HEADER, GLOVE_STATE_SUBHEADER, GLOVE_STATE_RELEASE)
                        glove.espNow_Send(glove.peer_master, state_msg)
                        checking_angles = False
                        return
        
        time.sleep(0.1)

def calibrate_sensors():
    global counter, max_set, min_set, checking_angles, grasping_count, releasing_count  # Declare globals to modify them

    while True:
        rec_msg = glove.espNow_Receive()
        header,sub_header,values = MessageDecoding(rec_msg)
        if timer_button.value() == 0:
            if values == FES_ROM_RELEASE:         
                print("Open your hand to record max values")
                start_timer("max")
                print("Max values stored successfully")
            if values == FES_ROM_GRASP:
                print("Close your hand to record min values")
                start_timer("min")
                print("Min values stored successfully")
                
        if max_set and min_set:
            time.sleep(2)
            break

    while True:
        rec_msg = glove.espNow_Receive()
        header,sub_header,values = MessageDecoding(rec_msg)
        if header == MASTER_HEADER :
            glove.espNow_Send(glove.peer_fes, rec_msg)
            if checking_angles:
                print("Started checking angles")
                grasping_count = 0  # Reset counters when starting new check
                releasing_count = 0
            else:
                print("Stopped checking angles")
        if checking_angles:
            check_angles()
        time.sleep(0.1)

calibrate_sensors()
