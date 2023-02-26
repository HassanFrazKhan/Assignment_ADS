import pandas as pd
import matplotlib.pyplot as plt
import pylab

def plot_mean_daily_vaccinations(data_path, country1, country2,country3,country4):
    """
    Ploting a line graph comparing the mean daily vaccinations for four countries or we can increase the by changig paremeters  in a given year.

    Args:
    data_path (str): File path of dta
    country1 (str): The name of the first country to compare.
    country2 (str): The name of the second country to compare.
    country3 (str): The name of the third country to compare.
    country4 (str): The name of the fourth country to compare.

    Returns(displays a line plot) 
    None
    """
    # Load the dataset
    data = pd.read_csv(data_path)

    # Filter the data for the specified countries
    filtered_data = data.loc[data['country'].isin([country1, country2,country3,country4]), ['country', 'date', 'daily_vaccinations']]

    # Convert the date column to datetime format
    filtered_data['date'] = pd.to_datetime(filtered_data['date'])

    # Extract the month from the date column
    filtered_data['month'] = filtered_data['date'].dt.month

    # Group the data by month and country, and calculate the mean daily vaccination rate for each month
    grouped_data = filtered_data.groupby(['country', 'month']).mean().reset_index()

    # Pivot the data to create separate columns for each country
    pivot_data = grouped_data.pivot(index='month', columns='country', values='daily_vaccinations')

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(pivot_data[country1], label=country1)
    plt.plot(pivot_data[country2], label=country2)
    plt.plot(pivot_data[country3], label=country3)
    plt.plot(pivot_data[country4], label=country4)

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Mean Daily Vaccinations')
    plt.title(f'Mean Daily Vaccinations in {country1} , {country2} , {country3} and {country4} (2021)')
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Line Plot')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()
    
    

def create_scatterplot(data_path):
    """
    Creates a scatter plot showing the relationship between math scores and reading scores 
    for the "Students Performance" dataset on Kaggle.
    
    Parameters:
    data_path (str): The path to the CSV file containing the dataset.
    
    Returns:
    None (displays a scatter plot)
    """
    
    # Load the dataset
    data = pd.read_csv(data_path)

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data["math score"], data["reading score"], alpha=0.5)

    # Add labels and title
    plt.xlabel("Math Score")
    plt.ylabel("Reading Score")
    plt.title("Relationship between Math and Reading Scores")
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Scatter plot')

    # Show the plot
    plt.show()
    
    


def create_heatmap(data_path):
    """
    Create a heatmap for the "vgsales.csv" dataset from Kaggle using pyplot.

    Returns:
    None (display heatmap)
    """
    # Load the dataset
    df = pd.read_csv(data_path)

    # Compute the correlation matrix
    corr_matrix = df.corr()

    # Create the heat map using Pyplot
    plt.imshow(corr_matrix, cmap='coolwarm')

    # Add labels
    plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=90)
    plt.yticks(range(len(corr_matrix)), corr_matrix.columns)

    # Add colorbar
    plt.colorbar()
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('HeatMap')

    # Add title
    plt.title('Correlation Matrix for VG Sales Dataset')

    # Show the plot
    plt.show()



if __name__=='__main__':
    plot_mean_daily_vaccinations('country_vaccinations.csv', 'Pakistan', 'India','United States','United Kingdom')
    create_scatterplot('StudentsPerformance.csv')
    create_heatmap('vgsales.csv')
    
    