# Laptop Price Analysis

## Author
- Daniele Panizzolo - Department of Statistical Sciences, University of Padua, Italy.

## Abstract
This project focuses on analyzing the laptop market to gain a general understanding of trends and consumer choices regarding components. Utilizing principal libraries such as Pandas, Numpy, and Matplotlib, I implemented graphs and tables to examine the data. The workbook contains two CSV files, one for training and one for testing, aiming to develop a model that performs well on both datasets.

## Requirements Analysis
- The analysis ensures the import of the two datasets into our folder as soon as we start our program; it will ask which dataset we want to operate on.
- The program provides functionalities to access data exploration and to see the related information of the chosen dataset.
- The system supports statistical data analysis, including calculations of median, mode, variance, standard deviation, correlation, and covariance, and allows graphical display of many important pieces of information related to our dataset with bar charts and pie charts.
- The program's execution time can be viewed by importing the "time" module.

## Project Implementation
The main steps of the program's implementation with frequent comments in the code for better understanding include:
- Necessary library imports: `os` for interacting with the operating system, `pandas` for data manipulation and analysis, `numpy` for mathematical operations on arrays, `matplotlib.pyplot` for creating charts, `sklearn` for training linear regression models and calculating evaluation metrics, `pyfiglet` for creating artistic text (at the end of the program session), `seaborn` for creating advanced statistical charts (such as Boxplot).
- Definition of the main menu and "statistical menu", where the main menu contains the program's main options, and the statistical menu shows options for specific analyses.
- Implementation of functions for managing user choices, loading data, and information display, and handling specific analysis choices. Functions for displaying charts such as pie charts and diagrams were also included.
- `main()`: The main function that manages the program flow.

## Conclusions and Results Evaluation
The analysis provided a general overview of the dataset and relevant information about the manufacturers, prices, categories, and RAM capacity of the considered laptops. This analysis allowed me to acquire deep knowledge of the laptop market and consumer preferences in terms of component choices, representing an important contribution to better understanding the context and formulating possible future recommendations or strategies based on the analyzed data.

## Future Developments and Improvements
There are definitely wide margins for improvement in this project. Further implementations could include more precise and significant charts, such as scatter plots or heat maps, and efforts to make the code more concise and efficient. I maximized the resources provided by Professor Zennaro, which have been of great help in using the Pandas, Numpy, and Matplotlib libraries. I have also delved into computational complexity and included my program's execution time. Another fundamental aspect of my code was error and exception management, crucial for ensuring accurate data analysis.

## Acknowledgments
I extend my deepest thanks to the Professor for his kind attention and hope that my work meets his expectations.

## Bibliography and Sources Used
To finalize my project, I researched various instructions and functionalities of different libraries through many web resources like:
- [Exploratory Data Analysis with Python and Pandas](https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/)
- [Explore and Analyze Data with Python - Microsoft](https://learn.microsoft.com/it-it/training/modules/explore-analyze-data-with-python/)
- [Laptop Price Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/arnabchaki/laptop-price-prediction)
- [Python Data Science Handbook by Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/)

## License
This project is distributed under the [MIT License](LICENSE).
