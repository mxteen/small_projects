# Loss Function for Household Appliance Demand Forecasting

The final goal is to forecast the turnover of household appliances, which involves determining the appropriate quantity of each product to bring to a specific point of sale. Deliveries are made every three months.

It's crucial to strike a balance between stocking enough inventory to satisfy demand and avoiding excess inventory that could be difficult to manage. If we don't stock enough inventory, we risk missing out on potential profits, as customers will be unable to purchase the equipment they need. Conversely, if we stock too much, we may end up with an overflowing warehouse, which could create logistical challenges and limit our ability to import newer models.

Therefore, we must determine the optimal inventory level by developing a loss function that considers the cost of missed profits and the cost of excess inventory, among other factors. This approach will help us to find the right balance between meeting demand and minimizing inventory costs.

The aim of this prioject is to come up with a loss function that would be adequate for a given business problem.
 
## Approach

We will use the Root Mean Squared Logarithmic Error (RMSLE) as the loss function to evaluate the accuracy of the future model. 

* RMSLE is a commonly used metric for evaluating the accuracy of demand forecasting models. It is particularly useful when the demand data contains a wide range of values, including both small and large values. 
* The RMSLE penalizes the model more for underestimating large values than for underestimating small values, which is important in forecasting scenarios where there may be a few extreme values that have a significant impact on the overall performance of the model. It's acceptable if the model cannot accurately predict minor demand as it will not result in significant profit loss if we underestimate or import an excess amount of goods if we overestimate. However, if the model fails to predict substantial demand, it can lead to significant profit loss or logistical issues.
* The Huber-loss and LINEX loss functions are also useful metrics for evaluating forecasting models, but they require additional information such as cost functions or risk preferences. We have only true and predicted values.

Then we can develop a regression model using historical data on household appliance sales and use it to predict future sales. We will then use the predicted sales to determine the optimal inventory level for each point of sale.


## Modules Used

The project uses the following modules:
* `numpy` for numerical computations and handling arrays
* `seaborn` for data visualization with histograms
* `matplotlib.pyplot` for creating the histogram plot

The `turnover_error()` function takes two numpy arrays `y_true` and `y_pred`, calculates the Root Mean Squared Logarithmic Error (RMSLE) between them, and returns the error value as a float. The function includes error checking to ensure that the input arrays have the same length and contain only non-negative values. 
The testing section generates two sets of 30 random arrays, one with an underestimating model and another with an overestimating model, and plots the resulting RMSLE values in two histograms to demonstrate the impact of underestimation and overestimation on the error metric.