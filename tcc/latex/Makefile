# make        -> gera build/main.pdf
# make watch  -> recompila a cada alteração salva
# make clean  -> apaga os arquivos auxiliares
.PHONY: pdf watch clean
pdf:
	latexmk
watch:
	latexmk -pvc -view=none
clean:
	latexmk -C
	rm -rf build
