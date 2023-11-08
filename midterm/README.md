House Price Prediction

Ridge, Lasso and Random Forest models are used. The saved model is the Random Forest model.



To run the web server from outside of the virtual environment, enter: 
pipenv run gunicorn --bind 0.0.0.0:9696 predict_app:app and then it'll be connected as shown below.  

<img width="419" alt="image" src="https://github.com/dencan06/mlzoomcamp/assets/43348217/fc8dbaf5-045c-408a-9307-4adcbadc3272">  

From another terminal, you can run
pipenv run python predict_test.py  
<img width="483" alt="image" src="https://github.com/dencan06/mlzoomcamp/assets/43348217/c720565b-4ddc-4125-8371-1481745d1565">  
