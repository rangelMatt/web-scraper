# Lab 17: Web Scraping

## Author: Matt Rangel

## 5/10/2022

## Links and Resources

- Morning Lecture
- Roger Wells
- Bishal Khanal
- [Beautiful Soup 4 Cheatsheet](https://whatacold.io/blog/2021-12-05-beautifulsoup4-cheatsheet/)

## Set up

- BS4 from Beautiful Soup imported

## Take Away

Quickly scraping the web for instances of specific strings, in this case "citations needed' on Wikipedia pages. [Beautiful Soup 4 Cheatsheet](https://whatacold.io/blog/2021-12-05-beautifulsoup4-cheatsheet/) was a big help in helping solve this lab.

I went into the wikipedia site to find "citations needed", and inspected an instance to find a key to get the value of what I was looking for. Then returned the length of each instance for the first method.

For the second method, I used the same code, and found that I needed to get the `parent.text` of what I found, and that will return the paragraph of what the citation was needs. I used a for loop to get all the instances on the site.
