# Omar_Barakat_IA_7

#population data
popData = {
    'CA': 39.5, 'TX': 30.0, 'FL': 22.2, 'NY': 19.8, 'PA': 13.0,
    'IL': 12.8, 'OH': 11.8, 'GA': 10.9, 'NC': 10.7, 'MI': 10.1
}

#retrieve_pop
def retrieve_pop(region_code, data_dict):
    if region_code in data_dict:
        return data_dict[region_code]
    else:
        return None

# Function: main
def main():
    # Store all valid country/state codes in a list
    valid_codes = list(popData.keys())

    # Start a loop for user input
    while True:
        # Ask user for a code
        user_code = input("Please enter a country/state code: ")

        # Remove spaces and convert to uppercase
        user_code = user_code.strip().upper()

        # Call function to get population
        population = retrieve_pop(user_code, popData)

        # If code exists
        if population is not None:
            print(f"{user_code} population = {population}")
            break
        else:
            # Show error and codes
            print(f"Error: '{user_code}' not recognized.")
            print(f"Valid codes: {', '.join(valid_codes)}")

            # Ask if user wants to try again
            again = input("Would you like to try again? (yes/no): ")
            again = again.strip().lower()

            # If user says no, end it
            if again == "no" or again == "n":
                print("Program terminated.")
                break
            # If yes or y, loop
            elif again == "yes" or again == "y":
                continue
            # Any other input to exit
            else:
                print("Program terminated.")
                break
main()
