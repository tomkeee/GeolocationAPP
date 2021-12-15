Geolocation APP Deployed on Heroku : https://sofomogeolocation.herokuapp.com
<br/>
It is also available on Docker : docker run -p 4000:3003 66122001/sofomoapp
<br/>
<br/>
<br/>
Deployment proccess:

-> Deployed using Docker
<img width="1440" alt="container" src="https://user-images.githubusercontent.com/80860556/146183584-0509920f-fc8b-4f8a-a4f4-2af7dbb2b0eb.png">


-> Added Postgresql
<img width="1440" alt="Screen Shot 2021-12-15 at 13 02 06" src="https://user-images.githubusercontent.com/80860556/146183125-d2f2863c-c947-413c-9441-62ee03b2be04.png">

<br/>
<br/>
<br/>
1) Adding a new user:
POST request on https://sofomogeolocation.herokuapp.com/register/
<img width="1440" alt="Screen Shot 2021-12-15 at 13 48 03" src="https://user-images.githubusercontent.com/80860556/146189306-96bd54b7-54f5-42f7-806a-c2f6bbc13b21.png">

Output: new user + access token (read-only)

<br/>
<br/>
<br/>


2) retrieving access and refresh token 
POST request on https://sofomogeolocation.herokuapp.com/api/token/
<img width="1440" alt="Screen Shot 2021-12-15 at 13 49 31" src="https://user-images.githubusercontent.com/80860556/146189512-59a4332c-b1fa-410c-b20c-7731c31fdf93.png">


<br/>
<br/>
<br/>

3) retrieving access token, using refresh token
POST request on https://sofomogeolocation.herokuapp.com/api/token/refresh/
<img width="1440" alt="Screen Shot 2021-12-15 at 13 59 00" src="https://user-images.githubusercontent.com/80860556/146190799-199b6d4b-b41e-47fa-b776-c1d78224a2d3.png">


<br/>
<br/>
<br/>

4) List or add data about specific geolocation

a) List 
GET request on https://sofomogeolocation.herokuapp.com/api/
<img width="1440" alt="Screen Shot 2021-12-15 at 14 24 06" src="https://user-images.githubusercontent.com/80860556/146194380-99e38cbe-013c-4a5b-a6df-6074e3288dfd.png">


b) Add
POST request on https://sofomogeolocation.herokuapp.com/api/
<img width="1440" alt="Screen Shot 2021-12-15 at 14 22 33" src="https://user-images.githubusercontent.com/80860556/146194284-a7bc09c9-677e-4123-87b2-82a00c5bf1be.png">



<br/>
<br/>
<br/>

5) Adding data, using current client data
GET request on https://sofomogeolocation.herokuapp.com/api/add
<img width="1440" alt="Screen Shot 2021-12-15 at 14 29 16" src="https://user-images.githubusercontent.com/80860556/146196038-82a6258a-864b-46f7-926b-fc72ce0223b3.png">



