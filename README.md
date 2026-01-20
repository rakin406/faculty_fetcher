<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Faculty Fetcher</h3>

  <p align="center">
    A program to scrape the faculty list and save them in a database.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This program is used to scrape the faculty list of AIUB and save each teacher in the database. The database system used in this
project is PostgreSQL. You can either create the database locally or on cloud platforms such as [Neon](https://neon.com/).

The table columns consist of the teacher's name, gender, photo URL and votes. In this GUI program, you have to set the gender for
every teacher manually by pressing 'm' or 'f' keys, where 'm' stands for male and 'f' stands for female. The database schema is stored
in the `migrations/` folder.

This program is not made for general users. I made it for my personal use.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

I am using the `uv` package manager. If you're not using it, skip the second step below and install all the dependencies specified in 
`pyproject.toml` using `pip`.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rakin406/faculty_fetcher.git
   ```
2. Install Python libraries
   ```sh
   uv sync
   ```
3. Enter your database URL in `.env`
   ```
   DATABASE_URL=<your database URL>
   ```
4. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

Run `main.py` and wait for the GUI program to load. Press 'm' or 'f' keys to save the teacher in the database as male or female 
respectively. When you press those keys, the program will move on to the next teacher. Do not spam the 'm' or 'f' keys; wait till the 
image loads first. Logs will be printed and saved in a file called "faculty_fetcher.log". I highly suggest you to watch the printed logs 
as you use the program, so that you'll know whether the right information is being pushed to the database. There are currently at least 
395 teachers if I am not mistaken. Good luck.

Run using uv
```sh
uv run main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/rakin406/faculty_fetcher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=rakin406/faculty_fetcher" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Rakin Rahman - rakinrahman406@gmail.com

Project Link: [https://github.com/rakin406/faculty_fetcher](https://github.com/rakin406/faculty_fetcher)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/rakin406/faculty_fetcher.svg?style=for-the-badge
[contributors-url]: https://github.com/rakin406/faculty_fetcher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rakin406/faculty_fetcher.svg?style=for-the-badge
[forks-url]: https://github.com/rakin406/faculty_fetcher/network/members
[stars-shield]: https://img.shields.io/github/stars/rakin406/faculty_fetcher.svg?style=for-the-badge
[stars-url]: https://github.com/rakin406/faculty_fetcher/stargazers
[issues-shield]: https://img.shields.io/github/issues/rakin406/faculty_fetcher.svg?style=for-the-badge
[issues-url]: https://github.com/rakin406/faculty_fetcher/issues
[license-shield]: https://img.shields.io/github/license/rakin406/faculty_fetcher.svg?style=for-the-badge
[license-url]: https://github.com/rakin406/faculty_fetcher/blob/main/LICENSE
