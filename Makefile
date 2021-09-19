ifeq ($(OS),Windows_NT)
    RM := del
    DEV_NULL := 2> $$null
else
    DEV_NULL := 2>/dev/null
endif

DATA := dados_covid_sp.csv

pandiso.html: pandiso.Rmd
	 Rscript -e 'rmarkdown::render("$<")'

clean:
	$(RM) *~ *.html

tidy: clean
	$(RM) $(DATA) .RData .Rhistory .Rproj.user

.PHONY: clean tidy
