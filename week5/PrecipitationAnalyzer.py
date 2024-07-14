class PrecipitationAnalyzer:
    # Initialize class attributes for total_rainfall and total_months
    total_rainfall = 0
    total_months = 0

    # Prompt the user for number of years
    num_years = int(input("Enter the number of years: "))

    # Loop through each year and month to calculate total rainfall and total months
    for year in range(1, num_years + 1):
        print(f"Year {year}:")
        
        # Loop through each month to calculate total rainfall and total months
        for month in range(1, 13):
            # Prompt the user for the inches of rainfall for each month
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_rainfall += rainfall
            total_months += 1
    # Print the total months, total inches of rainfall, and average rainfall per month
    print(f"\nTotal months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {total_rainfall / total_months:.2f}")

# Create the instance of the PrecipitationAnalyzer class
PrecipitationAnalyzer()
