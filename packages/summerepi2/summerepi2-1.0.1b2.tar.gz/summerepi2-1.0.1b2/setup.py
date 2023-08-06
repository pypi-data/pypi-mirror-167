# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['summer2',
 'summer2.compute',
 'summer2.experimental',
 'summer2.parameters',
 'summer2.runner',
 'summer2.runner.jax']

package_data = \
{'': ['*']}

install_requires = \
['computegraph>=0.3.5',
 'networkx>=2.6.2',
 'numpy>=1.20.3',
 'pandas>=1.3.2',
 'plotly>=5.5.0']

extras_require = \
{':sys_platform == "darwin"': ['jax[cpu]>=0.3.14,<0.4.0'],
 ':sys_platform == "linux"': ['jax[cpu]>=0.3.14,<0.4.0']}

setup_kwargs = {
    'name': 'summerepi2',
    'version': '1.0.1b2',
    'description': 'Summer is a compartmental disease modelling framework, written in Python. It provides a high-level API to build and run models.',
    'long_description': '# Summer: compartmental disease modelling in Python\n\n[![Automated Tests](https://github.com/monash-emu/summer/actions/workflows/tests.yml/badge.svg)](https://github.com/monash-emu/summer/actions/workflows/tests.yml)\n\nSummer is a Python-based framework for the creation and execution of [compartmental](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) (or "state-based") epidemiological models of infectious disease transmission.\n\nIt provides a range of structures for easily implementing compartmental models, including structure for some of the most common features added to basic compartmental frameworks, including:\n\n- A variety of inter-compartmental flows (infections, transitions, births, deaths, imports)\n- Force of infection multipliers (frequency, density)\n- Post-processing of compartment sizes into derived outputs\n- Stratification of compartments, including:\n  - Adjustments to flow rates based on strata\n  - Adjustments to infectiousness based on strata\n  - Heterogeneous mixing between strata\n  - Multiple disease strains\n\nSome helpful links to learn more:\n\n- [Rationale](http://summerepi.com/rationale.html) for why we are building Summer\n- **[Documentation](http://summerepi.com/)** with [code examples](http://summerepi.com/examples)\n- [Available on PyPi](https://pypi.org/project/summerepi2/) as `summerepi2`.\n- [Performance benchmarks](https://monash-emu.github.io/summer/)\n\n## Installation and Quickstart\n\nThis project requires at least Python 3.7\n\nSet up and activate an appropriate virtual environment, then install the `summerepi2` package from PyPI\n\n```bash\npip install summerepi2\n```\n\nImportant note for Windows users:\nsummerepi2 relies on the Jax framework for fast retargetable computing.  This is automatically\ninstalled under Linux, OSX, and WSL environments.  If you are using Windows, you can either install\nvia WSL, or run the following command after installing\n\n```bash\npip install jax[cpu]==0.3.14 -f https://whls.blob.core.windows.net/unstable/index.html\n```\n\nThen you can now use the library to build and run models. See [here](http://summerepi.com/examples) for some code examples.\n\n## Optional (recommended) extras\n\nSummer has advanced interactive plotting tools built in - but they are greatly improved with the\naddition of the pygraphviz library.\n\nIf you are using conda, the simplest method of installation is as follows:\n\n```bash\nconda install --channel conda-forge pygraphviz\n```\n\nFor other install methods, see\nhttps://pygraphviz.github.io/documentation/stable/install.html\n\n## Development\n\n[Poetry](https://python-poetry.org/) is used for packaging and dependency management.\n\nInitial project setup is documented [here](./docs/dev-setup.md) and should work for Windows or Ubuntu, maybe for MacOS.\n\nSome common things to do as a developer working on this codebase:\n\n```bash\n# Activate summer conda environment prior to doing other stuff (see setup docs)\nconda activate summer\n\n# Install latest requirements\npoetry install\n\n# Publish to PyPI - use your PyPI credentials\npoetry publish --build\n\n# Add a new package\npoetry add\n\n# Run tests\npytest -vv\n\n# Format Python code\nblack .\nisort . --profile black\n```\n\n## Releases\n\nReleases are numbered using [Semantic Versioning](https://semver.org/)\n\n- 1.0.0/1:\n  - Initial release\n- 1.1.0:\n  - Add stochastic integrator\n- 2.0.2:\n  - Rename fractional flow to transition flow\n  - Remove sojourn flow\n  - Add vectorized backend and other performance improvements\n- 2.0.3:\n  - Set default IVP solver to use a maximum step size of 1 timestep\n- 2.0.4:\n  - Add runtime derived values\n- 2.0.5:\n  - Remove legacy Summer implementation\n- 2.1.0:\n  - Add AdjustmentSystems\n  - Improve vectorization of flows\n  - Add computed_values inputs to flow and adjustment parameters\n- 2.1.1:\n  - Fix for invalid/unused package imports (cachetools)\n- 2.2.0\n  - Add validation and compartment caching optimizations\n- 2.2.1\n  - Derived output index caching\n  - Optimized fast-tracks for infectious multipliers\n- 2.2.2\n  - JIT infectiousness calculations\n  - Various micro-optimizations\n- 2.2.3\n  - Bugfix release (clamp outputs to 0.0)\n- 2.2.4\n  - Datetime awareness, DataFrame outputs\n- 2.2.5\n  - Performance improvements (frozenset), no API changes\n- 2.2.6\n  - Verify strata in flow adjustments (prevent unexpected behaviour)\n- 2.2.7\n  - Rename add_flow_adjustments -> set_flow_adjustments\n- 2.2.8\n  - Split imports functionality (add_importation_flow now requires split_imports arg)\n- 2.2.9\n  - Post-stratification population restribution\n- 2.3.0\n  - First official version to support only Python 3.7\n- 2.5.0\n  - Support Python 3.9\n- 2.6.0\n  - Merge 3.9/master branches\n- 2.7.0\n  - Include Python 3.10 support and update requirements\n- 2.7.1\n  - Bugfix (source flows not counted correctly in _add_transition_flow)\n- 3.1.0\n  - Parameter aware summer using computegraph\n- 3.1.1\n  - Update computegraph and add additional param awareness\n- 3.1.2\n  - Initial population/stratification now param aware\n- 3.1.3\n  - More jax implementation (strain stratification)\n- 3.1.4\n  - Bugfix release (jax imported even though optional)\n- 3.1.5\n  - Bugfix and minor improvements search for parameters\n- 3.1.6\n  - Support lists of adjustments and flow params\n- 4.0.0a\n  - Full jax support with ModelBuilder wrapper\n- 4.1.0a\n  - Abstract and lazy parameters\n- 4.2.0a\n  - Refactor parameters, combine runners\n\n## Release process\n\nTo do a release:\n\n- Commit any code changes and push them to GitHub\n- Choose a new release number accoridng to [Semantic Versioning](https://semver.org/)\n- Add a release note above\n- Edit the `version` key in `pyproject.toml` to reflect the release number\n- Publish the package to [PyPI](https://pypi.org/project/summerepi/) using Poetry, you will need a PyPI login and access to the project\n- Commit the release changes and push them to GitHub (Use a commit message like "Release 1.1.0")\n- Update `requirements.txt` in Autumn to use the new version of Summer\n\n```bash\npoetry build\npoetry publish\n```\n\n## Documentation\n\nSphinx is used to automatically build reference documentation for this library.\nThe documentation is automatically built and deployed to [summerepi.com](http://summerepi.com/) whenever code is pushed to `master`.\n\nTo run or edit the code examples in the documentation, start a jupyter notebook server as follows:\n\n```bash\njupyter notebook --config docs/jupyter_notebook_config.py\n# Go to http://localhost:8888/tree/docs/examples in your web browser.\n```\n\nYou can clean outputs from all the example notbooks with\n\n```bash\n./docs/scripts/clean.sh\n```\n\nTo build and deploy\n\n```bash\n./docs/scripts/build.sh\n./docs/scripts/deploy.sh\n```\n\nTo work on docs locally\n\n```bash\n./docs/scripts/watch.sh\n```\n',
    'author': 'James Trauer',
    'author_email': 'james.trauer@monash.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://summerepi.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
