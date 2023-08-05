# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hierarchicalsoftmax']

package_data = \
{'': ['*']}

install_requires = \
['anytree>=2.8.0,<3.0.0',
 'rich>=10.16.1,<11.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'torch>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'hierarchicalsoftmax',
    'version': '0.1.4',
    'description': 'A Hierarchical Softmax Framework for PyTorch.',
    'long_description': '================================================================\nhierarchicalsoftmax\n================================================================\n\n.. start-badges\n\n|testing badge| |coverage badge| |docs badge| |black badge|\n\n.. |testing badge| image:: https://github.com/rbturnbull/hierarchicalsoftmax/actions/workflows/testing.yml/badge.svg\n    :target: https://github.com/rbturnbull/hierarchicalsoftmax/actions\n\n.. |docs badge| image:: https://github.com/rbturnbull/hierarchicalsoftmax/actions/workflows/docs.yml/badge.svg\n    :target: https://rbturnbull.github.io/hierarchicalsoftmax\n    \n.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    \n.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/f99aea7ea203d16edd063a8dd5ed395f/raw/coverage-badge.json\n    :target: https://rbturnbull.github.io/hierarchicalsoftmax/coverage/\n    \n.. end-badges\n\nA Hierarchical Softmax Framework for PyTorch.\n\n\n.. start-quickstart\n\n\nInstallation\n==================================\n\nhierarchicalsoftmax can be installed using pip from the git repository:\n\n.. code-block:: bash\n\n    pip install git+https://github.com/rbturnbull/hierarchicalsoftmax.git\n\n\nUsage\n==================================\n\nBuild up a hierarchy tree for your categories using the `SoftmaxNode` instances:\n\n.. code-block:: python\n\n    from hierarchicalsoftmax import SoftmaxNode\n\n    root = SoftmaxNode("root")\n    a = SoftmaxNode("a", parent=root)\n    aa = SoftmaxNode("aa", parent=a)\n    ab = SoftmaxNode("ab", parent=a)\n    b = SoftmaxNode("b", parent=root)\n    ba = SoftmaxNode("ba", parent=b)\n    bb = SoftmaxNode("bb", parent=b)\n\nThe `SoftmaxNode` class inherits from the `anytree <https://anytree.readthedocs.io/en/latest/index.html>`_ `Node` class \nwhich means that you can use methods from that library to build and interact with your hierarchy tree.\n\nThe tree can be rendered as a string with the `render` method:\n\n.. code-block:: python\n\n    root.render(print=True)\n\nThis results in a text representation of the tree::\n\n    root\n    ├── a\n    │   ├── aa\n    │   └── ab\n    └── b\n        ├── ba\n        └── bb\n\nThe tree can also be rendered to a file using `graphviz` if it is installed:\n\n.. code-block:: python\n\n    root.render(filepath="tree.svg")\n\n.. image:: https://raw.githubusercontent.com/rbturnbull/hierarchicalsoftmax/main/docs/images/example-tree.svg\n    :alt: An example tree rendering.\n\n\nThen you can add a final layer to your network that has the right size of outputs for the softmax layers.\nYou can do that manually by setting the output number of features to `root.layer_size`. \nAlternatively you can use the `HierarchicalSoftmaxLinear` or `HierarchicalSoftmaxLazyLinear` classes:\n\n.. code-block:: python\n\n    from torch import nn\n    from hierarchicalsoftmax import HierarchicalSoftmaxLinear\n\n    model = nn.Sequential(\n        nn.Linear(in_features=20, out_features=100),\n        nn.ReLU(),\n        HierarchicalSoftmaxLinear(in_features=100, root=root)\n    )\n\nOnce you have the hierarchy tree, then you can use the `HierarchicalSoftmaxLoss` module:\n\n.. code-block:: python\n\n    from hierarchicalsoftmax import HierarchicalSoftmaxLoss\n\n    loss = HierarchicalSoftmaxLoss(root=root)\n\nMetric functions are provided to show accuracy and the F1 score:\n\n.. code-block:: python\n\n    from hierarchicalsoftmax import greedy_accuracy, greedy_f1_score\n\n    accuracy = greedy_accuracy(predictions, targets, root=root)\n    f1 = greedy_f1_score(predictions, targets, root=root)\n\nThe nodes predicted from the final layer of the model can be inferred using the `greedy_predictions` function which provides a list of the predicted nodes:\n\n.. code-block:: python\n\n    from hierarchicalsoftmax import greedy_predictions\n\n    outputs = model(inputs)\n    inferred_nodes = greedy_predictions(outputs)\n\n.. end-quickstart\n\n\nCredits\n==================================\n\n* Robert Turnbull <robert.turnbull@unimelb.edu.au>\n\n',
    'author': 'Robert Turnbull',
    'author_email': 'robert.turnbull@unimelb.edu.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rbturnbull/hierarchicalsoftmax',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
