import matplotlib.pyplot as plt

def visualize_data(data):
    # Visualize the data
    # For example, plot the stock prices
    plt.plot(data['dates'], data['prices'])
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Over Time')
    plt.show()
