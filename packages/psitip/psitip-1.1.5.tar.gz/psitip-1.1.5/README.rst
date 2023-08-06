PSITIP
======

Python Symbolic Information Theoretic Inequality Prover

PSITIP is a computer algebra system for information theory written in Python. Random variables, expressions and regions are objects in Python that can be manipulated easily. Moreover, it implements a versatile deduction system for automated theorem proving. PSITIP supports features such as:

- Proving linear information inequalities via the linear programming method by Yeung and Zhang. The linear programming method was first implemented in the ITIP software developed by Yeung and Yan ( http://user-www.ie.cuhk.edu.hk/~ITIP/ ).

- Automated inner and outer bounds for multiuser settings in network information theory (see the `Jupyter Notebook examples <https://nbviewer.jupyter.org/github/cheuktingli/psitip/tree/master/examples/>`_ ).

- Numerical optimization over distributions, and evaluation of rate regions involving auxiliary random variables.

- Interactive mode and Parsing LaTeX code.

- Finding examples of distributions where a set of constraints is satisfied.

- Fourier-Motzkin elimination.

- Discover inequalities via the convex hull method for polyhedron projection [Lassez-Lassez 1991].

- Non-Shannon-type inequalities.

- Integration with Jupyter Notebook and LaTeX output.

- Generation of human-readable proofs.

- Drawing information diagrams.

- User-defined information quantities. 


**Documentation:** https://github.com/cheuktingli/psitip

**Jupyter Notebook examples:** https://nbviewer.jupyter.org/github/cheuktingli/psitip/tree/master/examples/




|
|

About
~~~~~

Author: Cheuk Ting Li ( https://www.ie.cuhk.edu.hk/people/ctli.shtml ). The source code of PSITIP is released under the GNU General Public License v3.0 ( https://www.gnu.org/licenses/gpl-3.0.html ). The author would like to thank Raymond W. Yeung, Chandra Nair and Pascal O. Vontobel for their invaluable comments.

The working principle of PSITIP (existential information inequalities) is described in the following article:

- \C. T. Li, "An Automated Theorem Proving Framework for Information-Theoretic Results," arXiv preprint, available: https://arxiv.org/pdf/2101.12370.pdf , 2021.

If you find PSITIP useful in your research, please consider citing the above article.


|
|


WARNING
~~~~~~~

This program comes with ABSOLUTELY NO WARRANTY. This program is a work in progress, and bugs are likely to exist. The deduction system is incomplete, meaning that it may fail to prove true statements (as expected in most automated deduction programs). On the other hand, declaring false statements to be true should be less common. If you encounter a false accept in PSITIP, please let the author know.

|
|


Installation
~~~~~~~~~~~~

Running :code:`pip install psitip` will install PSITIP without the necessary solvers (which may not work correctly). To install PSITIP with its dependencies, use one of the following two options:

A. Installation with conda (recommended)
----------------------------------------

1. Install Python via Anaconda (https://www.anaconda.com/).

2. Open Anaconda prompt and run:

    .. code:: text

        conda install -c conda-forge glpk
        conda install -c conda-forge pulp
        conda install -c conda-forge pyomo
        conda install -c conda-forge lark-parser
        pip install pycddlib
        pip install --no-deps psitip

3. (Optional) Graphviz (https://graphviz.org/) is required for drawing Bayesian networks and communication network model. It can be installed via :code:`conda install -c conda-forge python-graphviz`

4. (Optional) If numerical optimization is needed, also install PyTorch (https://pytorch.org/).


B. Installation with pip
------------------------

1. Install Python (https://www.python.org/downloads/).

2. Run (you might need to use :code:`python3 -m pip` or :code:`py -m pip` instead of :code:`pip`):

    .. code:: text

        pip install numpy
        pip install scipy
        pip install matplotlib
        pip install pulp
        pip install pyomo
        pip install lark-parser
        pip install pycddlib
        pip install psitip

3. A linear programming solver supported by `Pyomo <https://github.com/Pyomo/pyomo>`_ or `PuLP <https://github.com/coin-or/pulp>`_ is required. We recommend GLPK, which can be installed on https://www.gnu.org/software/glpk/ or via conda.

4. (Optional) Graphviz (https://graphviz.org/) is required for drawing Bayesian networks and communication network model. A Python binding can be installed via :code:`pip install graphviz`

5. (Optional) If numerical optimization is needed, also install PyTorch (https://pytorch.org/).




References
~~~~~~~~~~

The general method of using linear programming for solving information 
theoretic inequality is based on the following work:

- \R. W. Yeung, "A new outlook on Shannon's information measures," IEEE Trans. Inform. Theory, vol. 37, pp. 466-474, May 1991.

- \R. W. Yeung, "A framework for linear information inequalities," IEEE Trans. Inform. Theory, vol. 43, pp. 1924-1934, Nov 1997.

- \Z. Zhang and R. W. Yeung, "On characterization of entropy function via information inequalities," IEEE Trans. Inform. Theory, vol. 44, pp. 1440-1452, Jul 1998.


Convex hull method for polyhedron projection:

- \C. Lassez and J.-L. Lassez, Quantifier elimination for conjunctions of linear constraints via a convex hull algorithm, IBM Research Report, T.J. Watson Research Center, RC 16779 (1991)


