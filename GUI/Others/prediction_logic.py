# Mapp from 0 to 4069 to 180 and given new sensor value find the mapped value
mapped_value = (new_sensor_value / 4069) * 180

# From Glove
    #  State > (Grasp , Release)
    #  Percentage (0 > 100)

# From EEG 
# Gasp or Release


def predict_order():
    if (EEG_prediction == "Grasp"):
        # Grasp
        if (Glove_state == "Release" and Release_Percentage >= 95 ):
            # FES_Grasp()
            # start timer for 8 seconds
            predict_order()
    elif (EEG_prediction == "Release"):
        # Grasp
        if (Glove_state == "Grasp" and Grasp_Percentage >= 95 ):
            # FES_Release()
            # start timer for 8 seconds
            predict_order()

# if prev_eeg_pred == "Release":
#     if (Glove_state == "Release" and Release_Percentage >= 95 ):
#         # timer for 2 seconds break
#         predict_order()


    

    # if(prev_EEG_prediction == "Grasp")
    # 1. Get the percentage from the Glove
    # 2. Map the percentage to the servo motor
    # 3. Send the mapped value to the servo motor
    # 4. Send the Grasp command to the glove
    # 5. Wait for the release command
    # 6. Send the release command to the glove
    # 7. Go to step 1
    pass




# EEG

# lw 3ada w2t kza (10) w2f el fes 

