# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kmerpapa', 'kmerpapa.algorithms']

package_data = \
{'': ['*']}

install_requires = \
['numba>=0.56.2,<0.57.0',
 'numpy>=1.23.3,<2.0.0',
 'scikit-optimize>=0.9.0,<0.10.0',
 'scipy>=1.9.1,<2.0.0']

entry_points = \
{'console_scripts': ['kmerpapa = kmerpapa.cli:main']}

setup_kwargs = {
    'name': 'kmerpapa',
    'version': '0.2.3',
    'description': 'Tool to calculate a k-mer pattern partition from position specific k-mer counts.',
    'long_description': '# kmerPaPa\nTool to calculate a "k-mer pattern partition" from position specific k-mer counts. This can for instance be used to train a mutation rate model.\n\n## Requirements\nkmerPaPa requires Python 3.7 or above.\n\n## Installation\nkmerPaPa can be installed using pip:\n```\npip install kmerpapa\n```\nor using [pipx](https://pypa.github.io/pipx/):\n```\npipx install kmerpapa\n```\n\n## Test data\nThe test data files used in the usage examples below can be downloaded from the test_data directory in the project\'s github repository:\n```\nwget https://github.com/BesenbacherLab/kmerPaPa/raw/main/test_data/mutated_5mers.txt\nwget https://github.com/BesenbacherLab/kmerPaPa/raw/main/test_data/background_5mers.txt\n```\n\n## Usage\nIf we want to train a mutation rate model then the input data should specifiy the number of times each k-mer is observed mutated and unmutated. One option is to have one file with the mutated k-mer counts (positive) and one file with the count of k-mers in the whole genome (background).  We can then run kmerpapa like this:\n```\nkmerpapa --positive mutated_5mers.txt \\\n         --background background_5mers.txt \\\n         --penalty_values 3 5 7\n```\nThe above command will first use cross validation to find the best penalty value between the values 3,5 and 7. Then it will find the optimal k-mer patter partiton using that penalty value.\nIf both a list of penalty values and a list of pseudo-counts are specified then all combinations of values will be tested during cross validation:\n```\nkmerpapa --positive mutated_5mers.txt \\\n         --background background_5mers.txt \\\n         --penalty_values 3 5 6 \\\n         --pseudo_counts 0.5 1 10\n```\nIf only a single combination of penalty_value and pseudo_count is provided then the default is not to run cross validation unless "--n_folds" option or the "CV_only" is used. The "CV_only" option can be used together with "--CVfile" option to parallelize grid search.\nFx. using bash:\n```\nfor c in 3 5 6; do\n    for a in 0.5 1 10; do\n        kmerpapa --positive mutated_5mers.txt \\\n         --background background_5mers.txt \\\n         --penalty_values $c \\\n         --pseudo_counts $a \\\n         --CV_only --CVfile CV_results_c${c}_a${a}.txt &\n    done\ndone\n```\n\n## Creating input data\nInput files with k-mer counts can be created using [kmer_counter](https://github.com/BesenbacherLab/kmer_counter).\nGiven a file of point mutations in a file that contain the CHROM, POS, REF and ALT columns from a vcf file:\n```\nchr1 1000000 G A\nchr1 1000100 G A\nchr1 1000200 C T\nchr1 1000300 C T\nchr1 1000400 C T\n```\nWe can count the 5-mers around each mutation using this command:\n```\nkmer_counter snv --radius 2 {genome}.2bit {point_mutations_file} > mutated_5mers.txt\n```\nGiven a bed file with regions that are sufficiently covered by sequencing we can count the background 5-mers using this command:\n```\nkmer_counter background --bed {regions}.bed -radius 2 {genome}.2bit > background_5mers.txt\n```\n\nThe file `{genome}.2bit` should be a 2bit file of the same reference genome that were used for calling the mutations. 2bit files can be downloaded from: `https://hgdownload.cse.ucsc.edu/goldenpath/{genome}/bigZips/{genome}.2bit` where `{genome}` is a valid UCSC genome assembly name (fx. "hg38").\n\n\n\n',
    'author': 'Søren Besenbacher',
    'author_email': 'besenbacher@clin.au.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/besenbacherLab/kmerpapa',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
