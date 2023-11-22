import data_fetcher
import data_processor
import visualizer

def main():
    # Get user input for the stock symbol
    stock_symbol = input("Enter the stock symbol: ")

    # Fetch data
    data = data_fetcher.fetch_stock_data(stock_symbol)

    # Process data
    processed_data = data_processor.process_data(data)

    # Visualize data
    visualizer.visualize_data(processed_data)

if __name__ == "__main__":
    main()
