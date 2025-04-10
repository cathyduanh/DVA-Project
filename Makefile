update_env:
	conda env export -f builds/environment.yml

build_env:
	conda env create -f builds/environment.yml
