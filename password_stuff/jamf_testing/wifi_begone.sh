#!/bin/bash

remove_ssid () {
    SSID=$1
    current_ssid_template_success="Removed $SSID from the preferred networks list"
    printf 'Deleting %s from saved SSIDs... ' "$SSID";
    # Remove the SSID from the preferred networks list
    PW_RM=$(networksetup -removepreferredwirelessnetwork "en0" "$SSID")
    # If the template success message does not match the actual output message, then there was an error.
    if [ "$current_ssid_template_success" != "$PW_RM" ]; then
      printf 'Error: %s, moving on.\\n' "$PW_RM"
    else
        printf "Done.\\nOutput: %s", "$PW_RM"
    fi
}

delete_local_keychain () {
    printf 'Deleting local keychain... '
    UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
    USER=$(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')
    printf 'User: %s\\n', "$USER"
    localkeychain="/Users/$USER/Library/Keychains/$UUID/keychain-2.db"
    DELETE_LOCAL="$(rm -r "$localkeychain")"
    printf 'Done. \\nOutput: %s', "$DELETE_LOCAL"
    
}

delete_wifi_password () {
    SSID=$1
    printf 'Deleting %s password from keychain... ' "$SSID";
    keychain_delete="$(security delete-generic-password -l "$SSID" '/Library/Keychains/System.keychain')"
    if [[ "$keychain_delete" == "security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain." ]]; then
        printf "Error: %s password was not found in the keychain. This is okay if the SSID was not saved to the keychain or if the password was already deleted.\\nDone.", "$SSID"
    else
        printf 'Done.\\nOutput: %s', "$keychain_delete"
    fi
}


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
        # If the password still exists in the local keychain, the best way to remove it is to either run the rm command yourself, or reconnect to the network, flush the logs for this specific computer, and then restart the mac. The reason for this is that the keychain is deleted only if either "apple" or "ACDSParentWifi" is found in the saved networks list, otherwise the keychain is not touched.
    fi
done <<< "$SSIDS"

if [ "$CURRENTSSID" == "ACDSParentWiFi" ] || [ "$CURRENTSSID" == "apple" ]; then
    # Reconnect to ensure that the computer is disconnected, should reconnect to AlmadenCountryDaySchool instead.
    printf "Disconnecting from %s... ", "$CURRENTSSID"
    networksetup -setairportpower en0 off
    networksetup -setairportpower en0 on
    printf "All Done!"
fi
