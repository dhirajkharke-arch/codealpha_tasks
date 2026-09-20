# ============================================
# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker
# ============================================

# Predefined stock prices
stocks = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "MSFT": 420.0,
    "AMZN": 180.0
}

# User's portfolio
portfolio = {}


# --------------------------------------------
# Display available stocks
# --------------------------------------------
def show_stocks():
    print("\n" + "=" * 40)
    print("        AVAILABLE STOCKS")
    print("=" * 40)

    for symbol, price in stocks.items():
        print(f"{symbol:<8} - ${price:.2f}")

    print("=" * 40)


# --------------------------------------------
# Add stock to portfolio
# --------------------------------------------
def add_stock():
    show_stocks()

    symbol = input("\nEnter stock symbol: ").strip().upper()

    if symbol not in stocks:
        print("Invalid stock symbol!")
        return

    while True:
        quantity_input = input("Enter quantity of shares: ").strip()

        try:
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

    value = stocks[symbol] * portfolio[symbol]

    print("\nStock added successfully!")
    print(f"Stock: {symbol}")
    print(f"Total Shares: {portfolio[symbol]}")
    print(f"Investment Value: ${value:.2f}")


# --------------------------------------------
# Display portfolio
# --------------------------------------------
def show_portfolio():
    print("\n" + "=" * 55)
    print("                 MY PORTFOLIO")
    print("=" * 55)

    if not portfolio:
        print("Your portfolio is empty.")
        print("=" * 55)
        return

    print(f"{'Stock':<10}{'Shares':<10}{'Price':<15}{'Value':<15}")
    print("-" * 55)

    total = 0

    for symbol, quantity in portfolio.items():
        price = stocks[symbol]
        value = price * quantity
        total += value

        print(
            f"{symbol:<10}"
            f"{quantity:<10}"
            f"${price:<14.2f}"
            f"${value:<14.2f}"
        )

    print("-" * 55)
    print(f"{'TOTAL PORTFOLIO VALUE':<35}${total:.2f}")
    print("=" * 55)


# --------------------------------------------
# Calculate total portfolio value
# --------------------------------------------
def calculate_total():
    total = 0

    for symbol, quantity in portfolio.items():
        total += stocks[symbol] * quantity

    return total


# --------------------------------------------
# Remove stock from portfolio
# --------------------------------------------
def remove_stock():
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    show_portfolio()

    symbol = input("\nEnter stock symbol to remove: ").strip().upper()

    if symbol not in portfolio:
        print("This stock is not in your portfolio.")
        return

    del portfolio[symbol]

    print(f"{symbol} removed from your portfolio.")


# --------------------------------------------
# Main program
# --------------------------------------------
def main():

    print("\n" + "=" * 50)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    print("CodeAlpha Python Developer Internship")
    print("Task 2")
    print("=" * 50)

    while True:

        print("\nMENU")
        print("-" * 30)
        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Calculate Total Value")
        print("5. Remove Stock")
        print("6. Exit")
        print("-" * 30)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_stocks()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            show_portfolio()

        elif choice == "4":
            total = calculate_total()
            print(f"\nTotal Portfolio Value: ${total:.2f}")

        elif choice == "5":
            remove_stock()

        elif choice == "6":
            print("\n" + "=" * 40)
            print("Thank you for using Stock Portfolio Tracker!")
            print("Goodbye!")
            print("=" * 40)
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


# --------------------------------------------
# Start the program
# --------------------------------------------
if __name__ == "__main__":
    main()
