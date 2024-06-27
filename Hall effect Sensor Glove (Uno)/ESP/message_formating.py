
def MessageEncoding(header, values_list):
    header_deli = ": "
    # Convert the list of values to a string
    values_str = ', '.join(map(str, values_list))
    
    # Concatenate the header with the values string
    result = header + header_deli + values_str
    
    print(result)
    
    return result

def MessageDecoding(message):
    # Split the string at the colon
    label, angles_str = message.split(":")

    # Strip any leading or trailing whitespace from the label
    label = label.strip()

    # Convert the string of numbers into a list of integers
    angles = [int(num.strip()) for num in angles_str.split(",")]
    
    return label, angles