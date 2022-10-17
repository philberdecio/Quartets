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

## Wireframes

![Screen Shot 2022-10-16 at 9 44 36 PM (2)](https://user-images.githubusercontent.com/109258439/196101252-4bc392d4-ca85-41d3-ac82-5dea68bc9e1c.png)
![Screen Shot 2022-10-16 at 9 52 50 PM (2)](https://user-images.githubusercontent.com/109258439/196101298-33bc0642-9bb6-42a0-9838-99ebe50ee30e.png)

## Entity Relationship Diagram

![Quartets ERDs (2)](https://user-images.githubusercontent.com/109258439/196103807-f2f5adc3-34d2-4984-8d48-b8d89477961f.png)

## Unsolved Problems and Future Features

I'm considering more stricctly restriciting each folio to four quartets, in addition to the existing restriction of four entries to each quartet. As it stands, there's a workaround that allows users to add additional folios when navigating to the CreateView page from another folio that has fewer than four quartets. I'd also like to alow users to update entries, bringing them up to speed with the existing full CRUD functionality of folios and quartets. The current configuration of the create views for entries made this infeasible.




