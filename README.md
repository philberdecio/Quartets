# Quartets

[LINK TO APP](https://quartets.herokuapp.com/)

## Description

 Quartets is a brainstorming app that allows users to create groups of four “notes.” Each note may consist of text, an image, or an embedded tweet, Instagram Post or YouTube video. Video and image notes may also contain a short comment. Quartets are grouped into groups called Folios. Quartets strikes a balance between flexibility and focus by providing you with a unique framework for organizing your thoughts and online observations. 
 
## Technologies Used

Django, PostgreSQL

## Installation Steps

Make sure you have Django installed first
1. Clone the repository
2. Create your own virtual environment
3. Install dependencies
4. Create a new PostgreSQL database
5. Make your migrations
6. Create a new superuser
7. Start the development server

## User Stories

The user should find that four items is enough to allow for a variety of associations while being few enough to encourage focus. Allowing multiple quartets in a folio expands the range of possible associations between quartets. I see it as a kind of multidimensional note taking.

## Screen Shots

![Screen Shot 2022-10-17 at 1 37 01 AM (2)](https://user-images.githubusercontent.com/109258439/196106050-bda04a8a-9a4d-4200-8183-d3be34251af5.png)

![Screen Shot 2022-10-16 at 9 52 50 PM (2)](https://user-images.githubusercontent.com/109258439/196105969-6184af96-66f0-401e-bd79-9d5e0653118a.png)

## Entity Relationship Diagram

![Quartets ERDs (2)](https://user-images.githubusercontent.com/109258439/196103807-f2f5adc3-34d2-4984-8d48-b8d89477961f.png)

## Unsolved Problems and Future Features

I'm considering more stricctly restriciting each folio to four quartets, in addition to the existing restriction of four entries to each quartet. As it stands, there's a workaround that allows users to add additional folios when navigating to the CreateView page from another folio that has fewer than four quartets. I'd also like to alow users to update entries, bringing them up to speed with the existing full CRUD functionality of folios and quartets. The current configuration of the create views for entries made this infeasible.




