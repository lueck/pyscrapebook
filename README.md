A web scraper for text content
==============================

The commandline programm `scrapebook` can be used to scrape books from
websites where a book is presented in separate chapters. Scraping the
whole book is done automatically provided that a link to the next
chapter is present and can be identified. It downloads a html document
from the web and writes the content into a plain text output file or
to `stdout`. It can parse an url from the document for further
parsing.

## Requirements ##

`scrapebook` is written in the Python programming language. So
[Python](https://www.python.org/downloads/), version 3, is required to
use it.


## Installation ##

Clone this repositoy, open a terminal and `cd` into the root directory
of the clone. Then run

	pip3 install -e .

Then use `scrapebook`.


## Usage ##

After installation run `scrapebook -h` on a terminal.

	$ scrapebook -h
	usage: scrapebook [-h] [-o OUTFILE] [-t TAG] [-i ID] [-x] [-l NEXTLABEL] url

	Scrape a book from a website, joining it's chapters.

	positional arguments:
	  url                   URL to scrape content from.

	optional arguments:
	  -h, --help            show this help message and exit
	  -o OUTFILE, --outfile OUTFILE
							The path to the output file. Writing to stdout if not
							specified.
	  -t TAG, --tag TAG     Tag name of the content container. Defaults to "div".
	  -i ID, --id ID        Id of the content container. Defaults to "content".
	  -x, --next            Parse for a subsequent url. By default, no further
							parsing is done.
	  -l NEXTLABEL, --nextlabel NEXTLABEL
							Significant part of the label of the link to the next
							document's url. Defaults to ">>".


For scraping a book from, e.g., `Projekt Gutenberg-DE` do:

	$ scrapebook -x -i gutenb -o KdU.txt http://gutenberg.spiegel.de/buch/kritik-der-urteilskraft-3507/1
