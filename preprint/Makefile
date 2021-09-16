ifeq ($(OS),Windows_NT)
    RM := del
    DEV_NULL := 2> $$null
else
    DEV_NULL := 2>/dev/null
endif

IMGs := estimation.png fit.png logistic.png
LATEX := xelatex

all: main.tex main.bib $(IMGs)
	$(LATEX) $< && bibtex $(patsubst %.tex,%,$<) && $(LATEX) $< && $(LATEX) $<	

main.pdf: main.tex $(IMGs)
	$(LATEX) $<

clean:
	$(RM) *.aux *.bbl *.blg *.log *.out *.spl $(DEV_NULL)
	$(RM) main.pdf $(DEV_NULL)
	$(RM) *~ $(DEV_NULL)
	$(RM) $$null

.PHONY: all clean