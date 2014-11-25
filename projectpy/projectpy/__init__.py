import os
from os.path import join

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
def _get_project_dir():
    return os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[0:-3])

root = _get_project_dir()

## data
subdir = join(root, 'data')
sjout = join(subdir, 'SJ.out.tab')
star_logs = join(subdir, 'Log.final.out')

## dexseq
subdir = join(root, 'output', 'dexseq')
exon_counts_combined = join(subdir, 'exon_counts_combined.tsv')

## external_data
subdir = join(root, 'external_data')
hg19 = join(subdir, 'hg19', 'hg19.fa')
gencode_gtf = join(subdir, 'gencode', 'gencode.v19.annotation.gtf')
star_index = join(subdir, 'star_index')

## output

### gencode_alignment_processing
subdir = join(root, 'output', 'gencode_alignment_processing')
gencode_dexseq = join(subdir, 'gencode.v19.dexseq.gff')
gencode_gene_info = join(subdir, 'gene_info.tsv')
gencode_sj_info = join(subdir, 'sj_info.tsv')
gencode_transcripts_genes = join(subdir, 'transcripts_genes.tsv')
star_stats = join(subdir, 'star_combined_final_logs.tsv')
sj_counts = join(subdir, 'sj_counts.tsv')
sj_annot = join(subdir, 'sj_annot.tsv')

## software
subdir = join(root, 'software')
bedGraphToBigWig = join(subdir, 'bedGraphToBigWig')
bedtools = join(subdir, 'bedtools2-2.20.1/bin/bedtools')
samtools = join(subdir, 'samtools-bcftools-htslib-1.0_x64-linux', 'bin',
                'samtools')
picard = join(subdir, 'picard-tools-1.118')
R = join(subdir, 'R-3.1.1', 'bin', 'R')
star = join(subdir, 'STAR_2.3.1z15/STARstatic')

# STAR Align
star_threads = 30
picard_memory = 58
# Soft links will be made to the bam and bigwig files in these directories.
local_ucsc_bigwig_path = '/raid/projects/TODO/web/bigwig'
local_ucsc_bam_path = '/raid/projects/TODO/web/bam'
web_ucsc_bigwig_path = 'http://flc.ucsd.edu/TODO/bigwig'
web_ucsc_bam_path = 'http://flc.ucsd.edu/TODO/bam'

## submodules
subdir = join(root, 'submodules')
pileup2base = join(subdir, 'pileup2base', 'pileup2baseindel_no_strand.pl')

# Miscellaneous

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass

# TODO: It's useful to implement a function like this that can figure out the
# sample ID from file paths etc.
def sample_name(p):
    """Get the sample name of one of the samples from a path"""
    names = []
    for name in ['1bpdel', 'P95H', 'WT', 'P95H_4bpdel']:
        if name in p:
            names.append(name)
    # Since P95H is a substring of P95H_4bpdel, we'll have to assume that if
    # they are both in a path, we should return P95H_4bpdel.
    if 'P95H' in names and 'P95H_4bpdel' in names:
        names.remove('P95H')
    if len(names) == 0:
        return None
    elif len(names) == 1:
        return names[0]
