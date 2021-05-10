# About this repository
<p> This repository is a <b>Flask App</b> that has a machine learning model merged with it and deployed on heroku.<br> This predicts famous iris species among <i>Versicolor, Setosa and Virginica</i>
<br> 
</p>
<h5>Here is picture of thosed species</h5> <br>

<img src="./assets/speciesEx.png">

# ML model used

<p>In this repository I have used <b>Linear Support Vector Classsification</b> model pre-built in sklearn for predicting classes.
LinearSVC works well for datasets having less data and less atrributes to train the model. Dataset used has only 150 data samples overall so
LinearSVC performed well with accuracy of 93% and predicted only 3 test data wrong.
<img src="./assets/report.png">
</p> 

# Predicted classes visualization
<h3>Scatter plot between attributes and categorized using color based on predictions</h3>
<img src="./assets/pwVSpl.png">
<img src="./assets/pwVSsw.png">
<p>More visualization can be found in jupyter notebook in this repository itself named: <b>Flowers Identification using svm.ipynb</b> </p>

# Libraries used
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Seaborn</li>
<li>Matplotlib</li>
<li>Sklearn</li>
</ul>
