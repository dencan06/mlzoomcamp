## House Price Prediction

In this project, prices of houses are determined from their given features. 
Ridge, Lasso and Random Forest models are used. The saved model (house_price_model.bin) is the Random Forest model.

predict.py - is just to run the example prediction use case on the terminal without any deployment or docker.  
predict_app - should be used to deploy on web using flask and/or docker.

** I used virtual environment from visual studio on mac. For that the .vscode folder should be in the same directory.  

- To run the web server from outside of the virtual environment, enter: 
pipenv run gunicorn --bind 0.0.0.0:9696 predict_app:app and then it'll be connected as shown below.  

<img width="419" alt="image" src="https://github.com/dencan06/mlzoomcamp/assets/43348217/fc8dbaf5-045c-408a-9307-4adcbadc3272">  

From another terminal, you can run
pipenv run python predict_test.py  
<img width="483" alt="image" src="https://github.com/dencan06/mlzoomcamp/assets/43348217/c720565b-4ddc-4125-8371-1481745d1565">  

- For docker, first start the Docker desktop and then from terminal run:  
docker build -t predictapp .  
![docker building](https://github.com/dencan06/mlzoomcamp/assets/43348217/68bedae1-508c-4654-993d-48a3805d0dc3)


docker run -it --rm -p 9696:9696 predictapp:latest

![docker running](https://github.com/dencan06/mlzoomcamp/assets/43348217/7582fcc8-8277-491a-b152-26c1d1c9ce93)

For the cloud I used render as suggested by some other participants on slack:

![render](https://github.com/dencan06/mlzoomcamp/assets/43348217/0cd960e4-972b-4383-a2f1-9a0c5e7427b0)

