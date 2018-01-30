all: impressive.py man demo

man: impressive.1

impressive.1: site/impressive.html html2man.py
	python html2man.py -O $@ site/impressive.html

test-man: impressive.1
	man -l $<

demo: demo.pdf

test: impressive.py demo.pdf
	xvfb-run -s "-screen 0 640x480x24 -ac +extension GLX +render -noreset" ./impressive.py -I alltrans.info -a 1 -Q demo.pdf

test-demo: demo
	mupdf -r150 demo.pdf &

release:
	sh makerelease.sh

%.pdf:	%.tex
	pdflatex -halt-on-error $<
	pdflatex -halt-on-error $<

impressive.py: compile.py impressive_dev.py src/*.py
	python $<
	chmod +x $@

install: impressive.py
	install -m 755 $< /usr/local/bin/impressive

clean:
	rm -f *.nav *.out *.snm *.toc *.vrb *.aux *.log *.pyc *.pyo
	rm -f *.tmp.py
	rm -rf win32/mplayer

distclean: clean
	rm -f demo.pdf impressive.1 impressive.py
	rm -rf dist

.PHONY: all man test-man demo test-demo test release clean distclean install
