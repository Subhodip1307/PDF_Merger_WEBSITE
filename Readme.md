# Project overview
Its a simple djano project of a pdf merger website and in feature there will add option for file extension changeing. If you are a learner and learing django 
then this github repo will help you to understand that how does django code works and how to make a pdf merger website .

# requirements

> python3

> django

> PyPDF2 
 
 # Usage
 Its very simple to run and use this program in your loclhost and we will also see how to host it over the internet but useing portforwading services
  <h3>Runing in Localhost </h3>
 
 ```bash
  python mange.py runserver
 ```
 Run mange.py fille from your CMD or terminal to start the server it will run on port no - 8000
 now open your browser and type 
 ```bash
  http://localhost:8000/
          or
  localhost:8000
 ```
 Then the interface of the will apper to you and now you can use it 
 
 <h3>Runing over the internet</h3>
In order to do that you should have port forwarding services like ngrok,cloudflare,telebit etc.
>First start your portforwarding service for port no 8000 and copy the forwarding link provided by the portforwarding service (like - https://example.io.)
 
 >Now open pdfmerger folder and open settings.py in your editor
 
 >and add this fleid in this code under the ALLOWED_HOSTS and add your forwaring link both of them

```bash

  ALLOWED_HOSTS=['localhost','exampel.io'] #add  without https or http
  
  CSRF_TRUSTED_ORIGINS=['https://example.io'] # add with https or http 
  
 ```
 Now its ready to use from over the internet by putiing the forwarding link in any browser
 
 
