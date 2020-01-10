17/12
================
* Installation of Python
* Input of the user
* Algorythme of a character chain "FirstName <MiddleName> LastName"
* Dictionnary (a list of key/value) defined by {} without any order
* Import of modules
* print function with f'{variable}' and "{}".function(variable)
* splint function, allowing to separate a chain character with a separator (default: space)
* type() to know which kind of object we use: int, str, bool, dic, list, def() etc.
* isInstance 
* Operators
* Regex ^[]+$

18/12
================
* Unitary tests
* Try Except
* Git and Github
* Functions with dates
* datetime
* MVC design patterns with controller
* While syntax
* Know which class is an object with isinstance
* creation of Readme.md (markdown type)

19/12
================
* Operator callable
* __call__(self)
* __add__
* adding changelog.md
* package BeautifulSoup4. Coming from pypi.org. 
    * using pipenv install. Scraping tool > get web content.
    * DOM (Document, Object, Model) analyze. Organize the html's tag.
* Debug Mode: script execution, accès denied, flake8 etc...
* PipEnv > Virtual Environement
    * Cleaning install > python you can download
    * repository where you can put your env
    * put some new files: pipfile and pipfile.lock . Security.
    * connected to pypi.org
    * Going to Lib's folder, discovering the sources.
* package request: HTTP get URL
    * adding an header to conter security with user.agent.
* Blake: helping with indentation, lisibility of the code


20/12
=================
* Django
    * 2h: initiation.
    * Creation of the super user & user.
    * CRUD: Create, Read, Update, Delete
    * Database
* Setting.py (config Django)
* View home who display the json (get from checkurl)
* urls.py
* template page home.html


7/01
=================
* Django Admin
    * ordering data by name
    * displaying fields of the table instead of generic name
    * 
* Model Database
    * Definition of ORM, relationship between tables
    * properties and attributes
    * functions herited from models.Model
* Datas
    * Allowing some of the data to be null/Blank
    * Hidding some data.
    * Construction of some column with variable. (reference is build with the author's name and the dewey's number)
* Installing Pillow for pictures
* Creation of tables of the database, with column's fields.
* Architecture
    * client's needs
    * 4 personas
    * Amelioration of the user's experience


8/01
=================
* Algo
    * Century based on the year
*Database
    *Modification of the models and catalog
    *Utilisation of makemigrations and migrate to update
*Model
    * Adding the century's algo
    * Adding the color's code for the dewey classification
*Form
    * Brainstorming on the functions which must be added/aren't important
    * feedback from the "client" leading to some correction

9/01
=================
* Algo
    * get data based on an url
        * Title
        * Metadescription
        * picture
        *url
* Django HTML: creation of a composant html to read the data from the previous algorythm
* Django settings
    * Adding Media: file upload, downloading pictures
    * static : CSS, JS, font, jpg
        * getting all the static's ressources for the application
        * public access
* Integration of filters, searching mode and autocompletion function for the administration
* Upgrade of the user's interface
* Translation of the wording (english => user's langage)
* Adding the color system to the dewey's system. Each entry got his color.