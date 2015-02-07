# Makefile for vim
#

.PHONY: docs clean pack

README.txt: README.markdown
	pandoc -o $@ $^

pack.zip: README.txt
	zip $@ $< *.py

clean:
	rm *.pyc README.txt *.man *.html pack.zip
