import pickle

# Main function
def main():
    # Dictionary of planet surface gravity factors
    dictPlanetGravity = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }

    # File name for pickling
    sFileName = "bcPlanetaryWeights.db"

    # Attempt to load previous history
    try:
        with open(sFileName, 'rb') as file:
            dictPlanetHistory = pickle.load(file)
    except FileNotFoundError:
        dictPlanetHistory = {}

    # Ask user if they want to see history
    sShowHistory = input("Do you want to see the history? (Y/N): ").strip().lower()
    if sShowHistory == 'y':
        if dictPlanetHistory:
            print("\nPrevious Entries:")
            for name, weights in dictPlanetHistory.items():
                print(f"{name}: {weights}")
        else:
            print("\nNo history found.")

    while True:
        # Prompt for a unique name
        sName = input("\nEnter a unique name (or press Enter to exit): ").strip()
        if not sName:  # Exit loop on blank input
            break
        if sName in dictPlanetHistory:
            print("Name already exists in history. Please enter a different name.")
            continue

        # Prompt for Earth weight with validation
        while True:
            try:
                nEarthWeight = float(input("Enter your Earth weight: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Calculate planetary weights
        dictPersonWeights = {}
        for sPlanet, fGravity in dictPlanetGravity.items():
            nPlanetWeight = nEarthWeight * fGravity
            dictPersonWeights[sPlanet] = f"{nPlanetWeight:10.2f}"

        # Add to history and display results
        dictPlanetHistory[sName] = dictPersonWeights
        print(f"\n{sName}'s Solar System's Weights:")
        for sPlanet, sWeight in dictPersonWeights.items():
            print(f"{sPlanet:<10}: {sWeight}")

    # Save updated history to file using pickling
    with open(sFileName, 'wb') as file:
        pickle.dump(dictPlanetHistory, file)

# Run the program
if __name__ == "__main__":
    main()
