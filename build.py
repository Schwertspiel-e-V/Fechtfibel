import os
import subprocess

os.makedirs("Output", exist_ok=True)

subprocess.run([
    "latexmk",
    "-pdf",
    "-interaction=nonstopmode",
    "-output-directory=../Output",
    "Fechtfibel.tex"
], cwd="Source")
