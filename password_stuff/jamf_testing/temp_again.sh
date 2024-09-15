#!/bin/bash

remove_ssid () {
    SSID=$1
    current_ssid_template_success="Removed $SSID from the preferred networks list"
    
    printf 'Deleting %s from saved SSIDs... ' $SSID;
    # Remove the SSID from the preferred networks list
    PW_RM=$(networksetup -removepreferredwirelessnetwork "en0" $SSID)
    echo $PW_RM
    # If the template success message does not match the actual output message, then there was an error.
    if [ "$current_ssid_template_success" != "$PW_RM" ]; then
      printf 'Error: %s, moving on.\\n' $PW_RM
    else
        printf Done.\\n
    fi
}

delete_local_keychain () {
    UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
    localkeychain="/Users/$(id -un)/Library/Keychains/$UUID/keychain-2.db"
    echo $(id -un)
    echo $(whoami)
    echo $(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')
    DELETE_LOCAL="$(rm -r $localkeychain)"
    echo "$DELETE_LOCAL"
}

delete_wifi_password () {
    SSID=$1
    keychain_delete="$(security delete-generic-password -l $SSID '/Library/Keychains/System.keychain')"
    echo $keychain_delete
}

# --- NEW CODE ---
# Get all the Wifi SSIDs saved to the computer
SSIDS=$(networksetup -listpreferredwirelessnetworks "en0" | sed '1d')
# Get the network that the computer is currently connected to
CURRENTSSID=$(networksetup -getairportnetwork "en0" | sed 's/^Current Wi-Fi Network: //')

# loop through all preferred networks (varname = SSID)
while read -r SSID; do
    if [ "$SSID" == "ACDSParentWiFi" ]; then
        remove_ssid $SSID
        delete_local_keychain
        delete_wifi_password $SSID
    elif [ "$SSID" == "apple" ]; then
        remove_ssid $SSID
        delete_local_keychain
        delete_wifi_password $SSID
    fi
done <<< "$SSIDS"

if [ "$CURRENTSSID" == "ACDSParentWiFi" ] || [ "$CURRENTSSID" == "apple" ]; then
    # Reconnect to ensure that the computer is disconnected, should reconnect to AlmadenCountryDaySchool instead.
    echo "Disconnecting from $CURRENTSSID"
    networksetup -setairportpower en0 off
    networksetup -setairportpower en0 on
    echo All Done!
fi







# --- OLD CODE ---

# Get all the Wifi SSIDs saved to the computer
SSIDS=$(networksetup -listpreferredwirelessnetworks "en0" | sed '1d')
# Get the network that the computer is currently connected to
CURRENTSSID=$(networksetup -getairportnetwork "en0" | sed 's/^Current Wi-Fi Network: //')
# printf 'Current SSID: %s', $CURRENTSSID

# loop through all preferred networks (varname = SSID)
while read -r SSID; do
    # If the current SSID is ACDSParentWiFi
  if [ "$SSID" == "ACDSParentWiFi" ]; then
    # Make a template error message to compare with the actual output error message (since success and errors both have exit code 0)
    current_ssid_template_error="Network $SSID was not found in the preferred networks list"
    current_ssid_template_success="Removed $SSID from the preferred networks list"
    
    
    # echo $current_ssid_template_error

    printf 'Deleting %s from saved SSIDs... ' $SSID;
    # Remove the SSID from the preferred networks list
    ACDSPW_RM=$(networksetup -removepreferredwirelessnetwork "en0" $SSID)
    echo $ACDSPW_RM
    # If the template success message does not match the actual output message, then there was an error.
    if [ "$current_ssid_template_success" != "$ACDSPW_RM" ]; then
      printf 'Error: %s, moving on.\\n' $ACDSPW_RM
    else
        printf Done.\\n
    fi

    # Remove the password from the keychain
    printf 'Deleting %s password from keychain... ' $SSID;
    
    UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
    localkeychain="/Users/$(id -un)/Library/Keychains/$UUID/keychain-2.db"
    DELETE_LOCAL="$(rm -r $localkeychain)"
    echo $DELETE_LOCAL
    
    keychain_delete="$(security delete-generic-password -l $SSID '/Library/Keychains/System.keychain')"
    echo $keychain_delete
    # COMMENTED BECAUSE THE KEYCHAIN COMMAND DUMPS ALL THE KEYCHAIN DATA AND CAUSES IT TO BUG OUT. THIS ISN'T NEEDED ANYWAY, JUST A NICE ERROR HANDLER.

    # Check if the keychain item was deleted by checking if the exit co
    #if [[ $keychain_delete == *"password has been deleted."* ]]; then
      printf Done.\\n
    #else
    #  printf 'Error: %s, moving on.\\n' $keychain_delete
    #fi


    # If the current SSID is apple
  elif [ "$SSID" == "apple" ]; then
    # Make a template error message to compare with the actual output error message (since success and errors both have exit code 0)
    current_ssid_template_error="Network $SSID was not found in the preferred networks list"
    # echo $current_ssid_template_error
    printf 'Deleting %s from saved SSIDs... ' $SSID;

    # Remove the SSID from the preferred networks list
    APPLE_RM=$(networksetup -removepreferredwirelessnetwork "en0" $SSID)
    # If the template error message matches the actual output error message, then there was an error.
    if [ "$current_ssid_template_error" == "$APPLE_RM" ]; then
      printf 'Error: %s, moving on.\\n' $APPLE_RM
    else
        printf Done.\\n
    fi
    
    # Remove the password from the keychain
    printf 'Deleting %s password from keychain... ' $SSID;
    printf 'id -un: %s', $(id -un)
    UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
    localkeychain="/Users/$(id -un)/Library/Keychains/$UUID/keychain-2.db"
    DELETE_LOCAL="$(rm -r $localkeychain)"
    echo $DELETE_LOCAL
    
    keychain_delete="$(security delete-generic-password -l $SSID '/Library/Keychains/System.keychain')"
    echo $keychain_delete
    # COMMENTED BECAUSE THE KEYCHAIN COMMAND DUMPS ALL THE KEYCHAIN DATA AND CAUSES IT TO BUG OUT. THIS ISN'T NEEDED ANYWAY, JUST A NICE ERROR HANDLER.

    # Check if the keychain item was deleted by checking if the exit co
    #if [[ $keychain_delete == *"password has been deleted."* ]]; then
      printf Done.\\n
    #else
    #  printf 'Error: %s, moving on.\\n' $keychain_delete
    #fi

    
    
  #else
    # echo Deleting $SSID
    # networksetup -removepreferredwirelessnetwork "en0" "$SSID"
  fi
done <<< "$SSIDS"

if [ "$CURRENTSSID" == "ACDSParentWiFi" ]; then
# Reconnect to ensure that the computer is disconnected, should reconnect to AlmadenCountryDaySchool instead.
  echo "Disconnecting from $CURRENTSSID"
  networksetup -setairportpower en0 off
  networksetup -setairportpower en0 on
  echo All Done!
fi
