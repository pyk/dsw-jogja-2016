default: build

build: clean notes.bbl
	pdflatex -halt-on-error notes
	
notes.aux:
	pdflatex -halt-on-error notes

notes.bbl: notes.aux notes.bib
	bibtex notes

clean:
	rm -f notes.aux notes.bbl

slide:
	make -c slide
