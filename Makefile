stress: out
	pdflatex -output-directory=out stress.tex
	bibtex out/stress
	pdflatex -output-directory=out stress.tex
	pdflatex -output-directory=out stress.tex
	mv out/Stress.pdf ./
abstract: out
	pdflatex -output-directory=out Abstract.tex
	bibtex out/Abstract
	pdflatex -output-directory=out Abstract.tex
	pdflatex -output-directory=out Abstract.tex
	mv out/Abstract.pdf ./
out:
	mkdir -p out
clean-pdf:
	rm Stress.pdf Abstract.pdf FinalPaper.pdf
clean:
	rm -rf out
