class BookwormBounty:
    # Initialize class attributes for points and books_purchased
    points = 0
    books_purchased = int(input("Enter the number of books purchased this month: "))
    
    # Calculate the points awarded based on the number of books purchased
    if books_purchased == 0:
        points = 0
    elif books_purchased >= 1 and books_purchased < 2:
        points = 0
    elif books_purchased >= 2 and books_purchased < 4:
        points = 5
    elif books_purchased >= 4 and books_purchased < 6:
        points = 15
    elif books_purchased >= 6 and books_purchased < 8:
        points = 30
    elif books_purchased >= 8:
        points = 60
    
    # Print the points awarded
    print(f"Points awarded: {points}")
    
# Create the instance of the BookwormBounty class
BookwormBounty()