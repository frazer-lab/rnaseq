RNA Sequencing Pipeline
======

This repository can serve as the starting point to a project that needs to
analyze RNA-seq data starting from raw reads. This repo has wrappers for

* downloading external references (hg19, Gencode, etc.) and software (STAR,
  samtools, etc.)
* duplicate removal
* alignment
* obtaining gene read counts
* obtaining exon read counts (for DEXSeq)
* processing splice junction counts from STAR's `SJ.out.tab` files
* running DEXSeq for exon coverage

## Dependencies

### Submodules

After cloning this repository from Github, change into the repo and run:

	git submodule init
	git submodule update

You will need to install the Python package `cdpybio` by changing into the
`cdpybio` directory and running `python setup.py install`.

### Python

The following Python packages are required:

* `cdpybio`
* `HTSeq`
* `projectpy`

`cdpybio` is provided as a submodule. `HTSeq` can be installed using `pip
install HTSeq`. `projecpy` is a project-specific python package in this
repository. You can change into the `projecpy` directory and install using
`python setup.py install` or `python setup.py develop` if you want to make
changes to the package and have them propagated without reinstalling the
package.

## Future work

I would like to add wrappers for running DESeq2 and DEXSeq for splice junctions.
