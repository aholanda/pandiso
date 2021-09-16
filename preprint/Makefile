ifeq ($(OS),Windows_NT)
    RM := del
    DEV_NULL := 2> $$null
else
    DEV_NULL := 2>/dev/null
endif

LATEX := xelatex

main.pdf: main.tex main.bib
	$(LATEX) $< && bibtex $(patsubst %.tex,%,$<) && $(LATEX) $< && $(LATEX) $<	

clean:
	$(RM) *.aux *.bbl *.blg *.log *.out *.spl $(DEV_NULL)
	$(RM) main.pdf $(DEV_NULL)
	$(RM) *~ $(DEV_NULL)
	$(RM) $$null

.PHONY: clean