# BA_Model
# Barabási-Albert Network Generation and Analysis

This project focuses on generating a Barabási-Albert network with N = 10^4 nodes using the Barabási-Albert model with m = 4. The following tasks will be performed:

## Network Generation
1. Generate a network with N = 10^4 nodes using the Barabási-Albert model with m = 4.
2. Use a fully connected network with m = 4 nodes as the initial condition.

## Degree Distribution Analysis
1. Measure the degree distribution at intermediate steps when the network has 10^2, 10^3, and 10^4 nodes.
2. Compare the degree distributions at these intermediate steps by plotting them together.
3. Fit each degree distribution to a power-law distribution with degree exponent γ.
4. Determine if the distributions "converge" by analyzing the changes in the degree distribution shape.
![1 a](https://github.com/MiladAlipour98/BA_Model/assets/105122009/e86c8864-259b-4740-8d9b-bd25306d288f)

## Cumulative Degree Distribution
1. Plot the cumulative degree distributions at intermediate steps.
2. Analyze the changes in the cumulative degree distributions and observe any patterns.
![1 b](https://github.com/MiladAlipour98/BA_Model/assets/105122009/81b0e842-b27f-4b61-b97c-3c3c99101e7c)
![1 c](https://github.com/MiladAlipour98/BA_Model/assets/105122009/c2df9684-f2ac-43cc-b7f8-0407e20d37e2)

## Average Clustering Coefficient
1. Measure the average clustering coefficient as a function of the network size N.
2. Plot the average clustering coefficient curve to observe its behavior with increasing network size.
![1 d](https://github.com/MiladAlipour98/BA_Model/assets/105122009/756810e5-3904-4fb2-83f7-977084653e1a)

## Degree Dynamics
1. Measure the degree dynamics of one of the initial nodes and the nodes added to the network at time t = 100, t = 1,000, and t = 5,000.
2. Follow Figure 5.6a in the book to capture the degree dynamics.
3. Plot the degree dynamics curves for the selected nodes at different time steps.
![1](https://github.com/MiladAlipour98/BA_Model/assets/105122009/dd7b36c8-954b-407b-a950-0626cc706ff6)

## Dependencies
- Python
- Relevant Python packages for network generation, analysis, and visualization (e.g., NetworkX, Matplotlib)

## Usage
1. Clone the project repository.
2. Install the required dependencies, including Python and the necessary packages for network generation and analysis.
3. Run the provided Python scripts for Barabási-Albert network generation and analysis.
4. Examine the generated plots, degree distributions, cumulative degree distributions, average clustering coefficient, and degree dynamics.

This project aims to generate Barabási-Albert networks and analyze their properties, including degree distributions, cumulative degree distributions, average clustering coefficient, and degree dynamics. By studying the network's growth process and analyzing various network metrics, insights into the underlying structure and behavior of Barabási-Albert networks can be gained.
