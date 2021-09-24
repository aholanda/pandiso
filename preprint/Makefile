ifeq ($(OS),Windows_NT)
    RM := del
    DEV_NULL := 2> $$null
else
    DEV_NULL := 2>/dev/null
endif

IMGs := estimation.png fit.png logistic.png
LATEX := xelatex

all: main.tex main.bib macros.tex $(IMGs) clean
	$(LATEX) $< && bibtex $(patsubst %.tex,%,$<) && $(LATEX) $< && $(LATEX) $<	

main.pdf: main.tex macros.tex $(IMGs)
	$(LATEX) $<

main.aux: main.pdf

main.bbl: main.aux
	bibtex $<

pandiso.zip: macros.tex main.bbl main.bib main.tex $(IMGs)
	@zip -r $@ $^

clean:
	$(RM) *.aux *.bbl *.blg *.log *.out *.spl $(DEV_NULL)
	$(RM) main.pdf $(DEV_NULL)
	$(RM) pandiso.zip
	$(RM) *~ $(DEV_NULL)
	$(RM) $$null

.PHONY: all clean