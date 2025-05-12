import csv

# Step 1: Read Data
def getDataInput(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [row for row in reader]

# Step 2: Calculate Median
def getMedian(prices):
    n = len(prices)
    prices.sort()
    if n % 2 == 1:
        return float(prices[n // 2])
    else:
        mid1, mid2 = prices[n // 2 - 1], prices[n // 2]
        return (mid1 + mid2) / 2

# Step 3: Main Function
def main():
   
    records = getDataInput("RealEstateData.csv")
   
   
    prices = []
    city_summary = {}
    zip_summary = {}
    type_summary = {}

    # Process records
    for record in records:
        city = record[1]
        zip_code = record[2]
        property_type = record[7]
        price = float(record[8])

        # Add price to list
        prices.append(price)

        # Summarize by City
        city_summary[city] = city_summary.get(city, 0) + price

        # Summarize by Zip
        zip_summary[zip_code] = zip_summary.get(zip_code, 0) + price

        # Summarize by Property Type
        type_summary[property_type] = type_summary.get(property_type, 0) + price

    # Sort prices for analytics
    prices.sort()

    # Calculate analytics
    min_price = min(prices)
    max_price = max(prices)
    total_price = sum(prices)
    avg_price = total_price / len(prices)
    median_price = getMedian(prices)

    # Output results
    print(f"Minimum Price: ${min_price:,.2f}")
    print(f"Maximum Price: ${max_price:,.2f}")
    print(f"Total Price: ${total_price:,.2f}")
    print(f"Average Price: ${avg_price:,.2f}")
    print(f"Median Price: ${median_price:,.2f}")

    print("\nSummary by City:")
    for city, total in city_summary.items():
        print(f"{city}: ${total:,.2f}")

    print("\nSummary by Zip:")
    for zip_code, total in zip_summary.items():
        print(f"{zip_code}: ${total:,.2f}")

    print("\nSummary by Property Type:")
    for property_type, total in type_summary.items():
        print(f"{property_type}: ${total:,.2f}")

# Run the program
if __name__ == "__main__":
    main()
