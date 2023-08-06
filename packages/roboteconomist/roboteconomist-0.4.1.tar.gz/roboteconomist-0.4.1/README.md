# RobotEconomist

### Demo 

`python -m src.main --instrument=income --outcome=education`

### Pipeline
- Preprocess corpus (e.g. `nber`) from `data/nber/` to `data/nber/spacy`
- Extract possible regressors, instruments and outcome variables to jsonl?
- Vectorize variables
- Search over vectors to make a possible dag
- Query the dag

## Adding a new corpus

- Add `txt` files in `data/corpus/txt`
- Run `./scripts/process_corpus_locally_with_spacy.sh`
- Run `src.pipeline` to create `data/corpus/extractions` and `data/corpus/graph`

## Set up

### Set up conda

There is an `config/econ.yml` file with all of the conda information in it
- To build the env for the first time: `conda env create -f config/econ.yml`
- To update the env: `make conda` 

### Set up machine 

`brew install git-lfs`

`brew install jq`