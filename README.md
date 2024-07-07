# Tech Directory
**Tech Directory** is a Django application that generates a CSV file listing IT companies in a specified location. Each entry includes the company name, website, and phone number, providing an organized directory for users seeking IT services or business contacts.

## Features
* Lists IT companies in a specified location
* CSV format for easy data handling
* Includes company name, website, and phone number

## Installation
1. Clone the repository:

    ``git clone https://github.com/yourusername/tech-directory.git``

2. Navigate to the project directory:

   ``cd tech-directory``

4. Create a virtual environment:

    ``python -m venv env``

 4. Activate the virtual environment:
* On Windows:

    ``.\env\Scripts\activate``

* On macOS and Linux:
 
    ``source env/bin/activate``

5. Install the required dependencies:

    ``pip install -r requirements.txt``

6. Apply migrations:

    ``python manage.py migrate ``




## Usage
1. Run the Django development server:

   ``python manage.py runserver``

2. Open your web browser and go to http://127.0.0.1:8000/.
3. Use the web interface to specify the location and generate the CSV file.

## Add More Locations
1. Update **mainapp/views.py** :
   
   ![city.png](https://github.com/Varinder-KM/Tech-Directory/blob/master/city.png)


2. Update **Index.html**:
   
   ![city.png](https://github.com/Varinder-KM/Tech-Directory/blob/master/area.png)



