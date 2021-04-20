# NewsBits

## Description

This is a python-flask application that allows a user to preview and list news articles from various news sources around the world.
by Joy Kirii.

## Features

- A landing page with a list of some of the most popular news publishers.
- A display of articles from a selected news publisher.

## Behaviour Driven Development

|                                  Behaviour                                  |                                        Input                                         |                                                                    Output                                                                     |
| :-------------------------------------------------------------------------: | :----------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: |
| Page loads the landing page which contains a list of various, news sources. | The user, can click a news source to get articles from that specific news publisher. | The user will be redirected to the articles page of the selected news source where they will be able to see all the top articles for the day. |

## Installation

### Prerequisites

In order to run the application ensure you have the following installed in your computer:

- python version 3
- Flask
- Pip
- virtualenv
- A text Editor

### Install

- Clone the repo to your computer.
- From the terminal navigate to the clone project folder
- Create a virtual environment and access the folder via you virtual machine.
- Run chmod +x start.sh followed by ./start.sh to start the server
- Alternatively, the project can be viewed by clicking this [link](https://newsbits-joy.herokuapp.com/)

#### Note

If the server prints a 429 error when trying to serve it means the api key has stopped working.Visit [News Api](https://newsapi.org/) and register for a new API key. Follow the steps above and you should be able to serve the site on your computer.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap

## Known Bugs

- Display articles does not wrap properly

## Contact

For any comments,questions and concerns feel free to contact me via my email: joykirii@gmail.com.
