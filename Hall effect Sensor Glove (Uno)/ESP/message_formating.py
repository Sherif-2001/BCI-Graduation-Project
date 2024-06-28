GLOVE_HEADER = "GLOVE"
#====================================================================================================
GLOVE_STATE_SUBHEADER = "STATE"
GLOVE_STATE_GRASP = 1
GLOVE_STATE_RELEASE = 0
#---------------------------------------------------------------------------------------------------
GLOVE_ANGLES_SUBHEADER = "ANGLES"
#---------------------------------------------------------------------------------------------------
GLOVE_CHANNEL_SUBHEADER = "CHANNEL_STATE"
GLOVE_CHANNEL_GRASP = 1
GLOVE_CHANNEL_RELEASE = 0
#**********************************************************************************************************************************

MASTER_HEADER = "MASTER"
#====================================================================================================
MASTER_DECISION_SUBHEADER = "DECISION"
MASTER_DECISION_GRASP = 1
MASTER_DECISION_RELEASE = 0
#---------------------------------------------------------------------------------------------------
MASTER_INITIAL_FES_SUBHEADER = "INITIAL_FES"
#**********************************************************************************************************************************

FES_HEADER = "FES"
#====================================================================================================
FES_PARAM_SUBHEADER = "FES_PARAMS"
#---------------------------------------------------------------------------------------------------
FES_ROM_SUBHEADER = "RANGE_OF_MOTION"
FES_ROM_GRASP = 1
FES_ROM_RELEASE = 0
#**********************************************************************************************************************************


def MessageEncoding(header, sub_header, values_list):
    
    if values_list is not list:
        values_list = [values_list]
    
    header_deli = ": "
    sub_header_deli = "; "
    # Convert the list of values to a string
    values_str = ', '.join(map(str, values_list))
    
    # Concatenate the header with the values string
    result = header + header_deli + sub_header + sub_header_deli + values_str
    
    print(result)
    
    return result

def MessageDecoding(message):
    # Split the string at the colon
    header, rest_message = message.split(":")

    # Strip any leading or trailing whitespace from the label
    header = header.strip()
    
    sub_header, values_str = rest_message.split(";")
    
    sub_header = sub_header.strip()
    
    values = []


    if sub_header == GLOVE_ANGLES_SUBHEADER:
        # Remove brackets if present and convert the string of numbers into a list of integers
        for num in values_str:
            if num == '[' or num == ',' or num == ' ':
                continue
            elif num == ']':
                break
            else:
                values.append(int(num))
    
    else:
        # Convert the string of numbers into a list of integers
        values = [int(values_str.strip())]
        
    print(f"{header}: {sub_header}; {values}")
    
    return header, sub_header, values

# angles =  [0, 1, 2, 3, 4]
# state = GLOVE_STATE_GRASP
# channel = GLOVE_CHANNEL_GRASP

# decision = MASTER_DECISION_GRASP
# init_fes = 50

# fes_param = 30
# rom = FES_ROM_GRASP

# print("-------------------Encoding----------------------")
# message1 = MessageEncoding (GLOVE_HEADER, GLOVE_ANGLES_SUBHEADER, angles)
# message2 = MessageEncoding (GLOVE_HEADER, GLOVE_STATE_SUBHEADER, state)
# message3 = MessageEncoding (GLOVE_HEADER, GLOVE_CHANNEL_SUBHEADER, channel)

# message4 = MessageEncoding(MASTER_HEADER, MASTER_DECISION_SUBHEADER, decision)
# message5 = MessageEncoding(MASTER_HEADER, MASTER_INITIAL_FES_SUBHEADER, init_fes)

# message6 = MessageEncoding(FES_HEADER, FES_PARAM_SUBHEADER, fes_param)
# message7 = MessageEncoding(FES_HEADER, FES_ROM_SUBHEADER, rom)



# print("-------------------Decoding----------------------")
# MessageDecoding(message1)
# MessageDecoding(message2)
# MessageDecoding(message3)
# MessageDecoding(message4)
# MessageDecoding(message5)
# MessageDecoding(message6)
# MessageDecoding(message7)


