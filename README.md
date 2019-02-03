A web scraper for text content
==============================

The executable `scrapeurl` downloads a html document from the web and
writes the content into a plain text output file or to `stdout`. It
can parse an url from the document for further parsing. It can be used
to scrape books from websites where a book is presented in separate
chapters, provided that a link to the next chapter is present and can
be identified.


Installation

Clone this repositoy, open a terminal and `cd` into the root directory
of the clone. Then run

	pip3 install -e .

Then use `scrapeurl`.
