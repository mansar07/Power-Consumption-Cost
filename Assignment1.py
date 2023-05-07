# CS 1026 Assignment 1 Re-Do

# Assigning each varibale with its designated value
off_peak_cost = 0.085
on_peak_cost = 0.176
mid_peak_cost = 0.119
total_usage_discount = 0.04
on_peak_discount = 0.05
senior_discount = 0.11
tax_rate = 0.13
electricity_cost = float
user_input_offpeak = float
user_input_onpeak = float
user_input_midpeak = float
total_electricity_cost = float

while user_input_offpeak != 0:  # A while loop that keeps looping until a 0 is entered for the offpeak period
        user_input_offpeak = (float(input("Enter kwh during Off Peak period: ")))  # Asking user for input for the offpeak period

        if user_input_offpeak == 0:  # An if statement being used to break the loop when the user inputs 0
                break

        user_input_onpeak = (float(input("Enter kwh during On Peak period: ")))  # Asking user for input for the onpeak period
        user_input_midpeak = (float(input("Enter kwh during Mid Peak period: ")))  # Asking user for input for the midpeak period
        user_input_senior_discount = (input("Is owner senior (Type Y or N): "))  # Asking user for input for senior information

        def discount_cost():  # Creating a seperate function that stores the values involved with the discount process
                electricity_cost = (user_input_offpeak * off_peak_cost) + (user_input_onpeak * on_peak_cost) + (user_input_midpeak * mid_peak_cost)  # All the user inputs for the peak periods are multiplied by their prices and added together, which are stored in the electricity cost variable

                # Here i am creating multiple scenarios for the inputs for instance if the sums is less than 400 and is senior than only the senior and sums discount will be applied because if the sums discount is applied the onpeak discount is not

                if (user_input_offpeak + user_input_onpeak + user_input_midpeak) < 400:  # If the sums of the user inputs for the peak periods is less than 400 then a discount is applied and subtracted from the electricity cost variable
                        electricity_cost -= electricity_cost * total_usage_discount

                elif user_input_onpeak < 150:
                        electricity_cost -= electricity_cost * on_peak_discount  # If the user input for onpeak is less than 150 then a discount is applied and subtracted from the electricity cost variable

                if user_input_senior_discount == 'Y' or user_input_senior_discount == 'y': # If the user input for senior is Y or y then a senior discount is applied which is subtracted from the electricity cost variable
                        electricity_cost -= electricity_cost * senior_discount

                return electricity_cost  # Return the value stored in this variable when the function is called

        def total_cost():  # Create a separate function that returns the final cost with the tax added
                total_electricity_cost = discount_cost()  # Assign the discounted price from the discount function into a new variable
                total_electricity_cost += discount_cost() * tax_rate  # Add on the tax value into the new variable that will store the final cost
                return total_electricity_cost  # Return the value stored in this variable when the function is called

        print("$"'{:.2f}'.format(total_cost()))  # print the final value to 2 decimal places
