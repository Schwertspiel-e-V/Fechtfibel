import subprocess

subprocess.run([
    "latexmk",
    "-pdf",
    "-interaction=nonstopmode",
    "-quiet",
    "-output-directory=../Output",
    "Fechtfibel.tex"
], cwd="Source")
