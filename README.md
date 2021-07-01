<strong>Steps to run this Django application</strong>

1. <strong>Install python directly in OS env </strong>


   for instance on Linux
    ```
    apt-get install python
    ```
   Create a python env 
   Version 3.7 or 3.8



   or preferably install anaconda software; it comes with python
   
   https://www.anaconda.com/products/individual

   guide on installing anaconda https://docs.anaconda.com/anaconda/install/


   After installation create a python env
    ```
    conda create -n envname python=3.7 
    ```

   Activate your python env
    ```
    conda activate envname
    ```

2. <strong>Create Django env</strong>

   version 2.2

    ```
    conda install -n envname django=2.2
    ```

3. <strong>Clone or Fork Repo from github to your local device</strong>

4. <strong>Install docker on local device</strong>
   
   https://docs.docker.com/engine/install/ubuntu/

   for linux:
   
   Update the apt package index and install packages to allow apt to use a repository over HTTPS:

    ```
     sudo apt-get update
     sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    ```
   Add Docker’s official GPG key:
    ```
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```

   set up the stable repository.
    ```
     echo \
      "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
     ```
   Install Docker Engine
    ```
     sudo apt-get update
     sudo apt-get install docker-ce docker-ce-cli containerd.io
     ```
5. <strong>Pull postgres image from docker and Edit docker compose file.</strong>
   
   Pull postgres:12.7 image from docker to your device
    ```
    docker pull postgres:12.7
    ```
   
   Input your desired postgres details for the following fields
   Username, Password, DB_name and Port
   

   Save and Run the compose file (ensure yiu are in the same dir as the dovker compose file in your command line):
     ```
    docker-compose up
     ```
   Now your database is running in a docker container


6. <strong>Connect dockerize DB to django</strong>
   
   Open setting.py file and ensure DATABASES section has same  Username, Password, DB_name and Port as the one in the docker compose file.


7. <strong>Connect Your Email address</strong>
   
   Under the EMAIL section in setting.py file, input the following:
   Host, User, Password and Port

   For gmail
     ```
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = ...@gmail.com
    EMAIL_HOST_PASSWORD = ''#fill in email password
    EMAIL_PORT = '587'
     ```
   for gmail users, ensure you add django as allowed apps in gmail settings

8. <strong>Migrate</strong>
      
   cd to the dir (Estate_listing) containing the django project and run migration cmds
    ``
    python manage.py makemigrations
    ``
     ``
    python manage.py migrate
    ``
9. <strong>Create user</strong>

   To create login username and password input the cmd below
       ``
    python manage.py createsuperuser
    ``
    follow the promts and type in your desired username, password and email address
    
 
10. <strong>Runserver</strong>

   To run django server input the cmd below
   
      ```
       python manage.py runserver
      ```
      
   Now you can view the project on your preferred web browser follwing the url on ur cmd line interface, usually: 
   http://localhost:8000/ or
   127.0.0.1:8000
