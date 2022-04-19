<div id="top"></div>


<!-- TITLE -->
<p align="center">
  <img width="275" src="https://github.com/RodneyMcCoy/store-website-database/blob/main/icon1.png">
</p>

<h2 align="center" id="heading">A Store Website + Database </h2>

<p align="center">This Repo holds the implmentation for the Perfect Purchase <em>(Best Buy)</em> website. The django-based website and associated relational database built here is meant to connect customers and vendors together so various products and services can be bought and sold. <br> <br> <a href="http://example.com/">Website Not Currently Hosted Here</a></p>

</div>



<!-- TABLE OF CONTENTS -->
## Tables of Contents

<ol>
  <li><a href="#setting-up">Setting Up</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#built-with">Built With</a></li>
  <li><a href="#contributors">Contributors</a></li>
  <li><a href="#license">License</a></li>
</ol>




<!-- Setting Up -->
## Setting Up


### Prerequisites

* Install Django with `python -m pip install Django` along with the following packages
  * SQLite 3
  * Pillow
  * crispy forms 

### Running the Website on Windows

* Clone the repository using `git clone git@github.com:RodneyMcCoy/store-website-database.git` or using *Github Desktop*
  * You must have an SSH key setup if cloning with SSH
* Ensure you have the prerequisites installed
* Located manage.py and run `python manage.py runserver`
* Navigate to `localhost:8000` to see the server running


### Running the Website on Linux

* Clone the repository using `git clone git@github.com:RodneyMcCoy/store-website-database.git`
  * You must have an SSH key setup
* Activate the python virtual environment by using `python -m venv env`
  * This is extremly important since we dont have `apt-get` or access to `sudo` outside of the virtual environment
  * You can exit the virtual environment using `ctrl-c` or re-enter using `source env/bin/activate`
* Install the prerequisites as decribed above
* Pin your dependencies	python -m pip freeze > requirements.txt
* Locate manage.py and run `python manage.py runserver`
* Navigate to `localhost:8000` to see the server running. 
  * **Warning. We can't access local host through PUTTY**




<!--
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
-->

<p align="right">(<a href="#top">to the top</a>)</p>





<!-- FEATURES -->
## Features


- [ ] Vendor and Customer Accounts
  - [ ] Create registration page to log in / log out and view account information
  - [ ] Store in the database
- [ ] Vendor Products / Services / Bundles  
  - [ ] Vendors can create and view products
  - [ ] Customers can view all of the products and search by keyword
  - [ ] Store in the database
- [ ] Customer Wishlists
  - [ ] Allow customers to define their wishlists
  - [ ] Show if there wishlists can be fulfilled


<p align="right">(<a href="#top">to the top</a>)</p>





<!-- BUILT WITH -->
## Built With

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [SQLite](https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15)
* [Mockaroo](https://www.mockaroo.com/)


<p align="right">(<a href="#top">to the top</a>)</p>













<!-- CONTRIBUTORS -->
## Contributors


David Waters
- Champion Features
  - Implimenting the Django Back End
- Contact Information
  - elde1366@vandals.uidaho.edu
  - [GitHub Profile](https://github.com/iTzLegend23)



Hunter Leppek
- Champion Features
  - Implimenting the Database Scheme using SQLite
  - Populating it with fake data using Mockaroo
- Contact Information
  - lepp8728@vandals.uidaho.edu
  - [GitHub Profile](https://github.com/Hunter-SE)


Rodney McCoy
- Champion Features
  - Setup and populated the GitHub Repository 
  - Writing the Documentation and Project Reports
  - Implimenting the Bootstrap Front End
- Contact Information
  - 208-860-4186
  - rbmj2001@outlook.com
  - [GitHub Profile](https://github.com/RodneyMcCoy)


<p align="right">(<a href="#top">to the top</a>)</p>



<!-- LICENSE -->
# License

Distributed under the MIT License. See [`LICENSE`](https://github.com/RodneyMcCoy/store-website-database/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">to the top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
