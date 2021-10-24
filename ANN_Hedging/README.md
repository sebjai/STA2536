# ANN Hedge

This folder contains an example of using an ANN to learn the hedge strategy in a Black-Scholes model wihtout explicitly targeting the hedge, but rather simply minimising the mean squared profit and loss at terminal time.

Here is an example of the learned distribution with different ANNs 


50 nodes per layer and 1 layer
<img src="images/net_50_1_dist24.png" alt="ANN_50_1" width="400"/>

25 nodes per layer and 2 layers
<img src="images/net_25_2_dist24.png" alt="ANN_25_2" width="400"/>

10 nodes per layer and 5 layers
<img src="images/net_10_5_dist24.png" alt="ANN_10_5" width="400"/>

