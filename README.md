RNA Sequencing Pipeline
======

This repository can serve as the starting point to a project that needs to
analyze RNA-seq data starting from raw reads. This repo has wrappers for

* downloading external references (hg19, Gencode, etc.) and software (STAR,
  samtools, etc.)
* duplicate removal
* alignment
* obtaining gene-level read counts
* obtaining exon-level read counts (for DEXSeq)
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
repository. You will likely want to install `projectpy using  `python setup.py
develop` so you can make changes to the package and have them propagated
without reinstalling the package.

## Repository Layout

This repo initially contains some directories and will make more directories as
you perform analyses.  I will describe the top-level directories.

### Top-level directories

#### `data`

This is data that you will store online in a repository like Figshare. This is
likely external data that may disappear over time or is not well-versioned,
data that you have to download manually, or data that 

#### `external_data`

This directory contains data or files that are downloaded automatically using
the "External Data and Software" notebook. These data should be well-versioned
and should not be at risk of disappearing over time. The idea is that it is not
necessary to keep track of these data sources through Figshare because they are
persistent online and already versioned. If you think that the link you used to
download the data won't download the same data in a few years, you probably
want to put this data into the `data` directory. Examples include

* ENCODE data hosted at https://www.encodeproject.org/
* SRA data

#### `notebooks`

This directory contains IPython notebooks used for running the pipeline and
performing the analyses. Note that I do not track the notebooks checkpoints (located
in `notebooks/.ipynb_checkpoints` with Git.

#### `output`

This directory contains analysis output from the IPython notebooks.

#### `projectpy`

This directory holds a Python pacakge specific to this project. You can add to
this package to make functions/magic variables/paths/etc. available throughout
your project. I use this package to organize the paths of the project so you
should not move this directory or it's `__init__.py` file, although you can to
the package.

#### `private_data`

This directory contains private data that should not be shared online. Examples
include

* raw sequencing data
* read alignments
* data that is accessed through protected databases (TCGA, dbGAP, etc.)
* ID conversions
* personally identifiable information

#### `sandbox`

Just a sandbox space to dump files or do whatever. Nothing in here is tracked.
Examples include:

* external data that you just want to take a look at

#### `software`

This directory contains extenral software that are downloaded automatically
using the "External Data and Software" notebook. These software should be
well-versioned and should not be at risk of disappearing over time. The idea is
that it is not necessary to keep track of these software because they are
persistent online and already versioned. If you think that the link you used to
download the software won't download the same software in a few years, you
probably don't want to use that software. However, if you have to use the
software, you should make a directory in this repo and store the software.

Note that if you are using software hosted in a Git repository, you should add
the software as a submodule. However, while larger software projects such as
samtools may have a Git repo, you are probably better just downloading the
release versions and storing them here.

Examples of software that could be in this directory include

* samtools
* picard tools
* R

#### `submodules`

This directory holds [Git
submodules](http://git-scm.com/book/en/v2/Git-Tools-Submodules). You should
only add things to this directory using Git commands. For instance, if you
wanted to add my Git repository for `pyencodetools`, you would use

	git submodule add https://github.com/cdeboever3/pyencodetools submodules/pyencodetools

### Git tracking

Here is a summary of which directories are tracked by Git and (ideally) by
Figshare. Note that you do not want to track large files with Git.

| Directory      | Tracked by Git | Tracked by Figshare |
|----------------|----------------|---------------------|
|`data`          |no              |yes                  |
|`external_data` |no              |no                   |
|`notebooks`     |yes             |no                   |
|`output`        |no              |yes                  |
|`private_data`  |no              |no                   |
|`projectpy`     |yes             |no                   |
|`sandbox`       |no              |no                   |
|`software`      |no              |no                   |
|`submodules`    |yes             |no                   |

## TODO

* I would like to add wrappers for running DESeq2 and DEXSeq for splice
  junctions.
* Implement Figshare tracking.
* Describe more about how to use `projectpy`.
* In the aligment notebook, I need to update the function that makes the bash
  script so that it doesn't rely on the sample names.
* Remove any references to `seq_data` directory.
* Organize links for bam/bigwig files. Can these be in the Git repo?
