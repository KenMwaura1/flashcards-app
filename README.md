# flashcards-api
A flashcards Django api to create flashcards to help you remember what's important

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

User story
1. A user must be authenticated to see his flashcards.
2. A user's flash card can contain a title with some notes.
3. Flashcards should be organized according to subjects/courses.
4. A user can delete or update a flash card he has created.
5. A user should see when the flash card was created and when it was last updated.

## Currently, Work in Progress

### Getting Started

### Prerequisites

- Python and pip (I am currently using 3.9.7) Any version above 3.7 should work.
* Git installed on your machine
* Code editor/ IDE
* PostgreSQL installed on your machine

### Installation and Running the App

1. Clone GitHub repository

    ```shell
    git clone https://github.com/KenMwaura1/flashcards-app
    ```

2. Change into the folder

    ```shell
   cd flashcards-app
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./bin/activate
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv flashcards-app
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate zoo_awwards
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```


5. Migrate your database
    ```shell
    python manage.py migrate
    ```

6. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

7. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```

8. Run the app

    ```shell
   ./run.sh
    ```

   OR
   run with python

    ```shell
   python manage.py runserver
    ```

9. visit the app

    ```shell
   http://localhost:8082/api
    ```


## Technologies used

* Python-3.9.7
* Django web framework
* PostgreSQL


## Author

[Ken Mwaura](https://github.com/KenMwaura1)


## LICENSE

MIT License

Copyright (c) 2021 Kennedy Ngugi Mwaura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
