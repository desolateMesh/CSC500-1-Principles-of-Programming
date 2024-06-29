def calculate_meal_total():
        food_charge = float(input("What was the toal for the meal: $"))
    
        tip = food_charge * 0.18
        sales_tax = food_charge * 0.07
        total_price = food_charge + tip + sales_tax

        print(f"\nBill Total: ${food_charge:.2f}")
        print(f"Tip (18%): ${tip:.2f}")
        print(f"Sales Tax (7%): ${sales_tax:.2f}")
        print(f"Total Price: ${total_price:.2f}")
    
calculate_meal_total()
