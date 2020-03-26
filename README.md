# Template-Python-Project

This notebook demonstrates code structuring for Python projects which use Jupyter notebooks.
The template Jupyter notebook demonstrates markdown functionality which can be used for documentation.
The modules in PyLib are used to save functions which you want to externalize from the notebook.
This can help to keep your Jupyter notebooks concise, even if you are using longer functions.

## Creating a New Project

1. On your local machine, create a repository structured as follows.

```bash
.
├── MyProject
│	├── README.md
│	├── Jupyter Notebooks
│	│	├── P1 - MyAnalysisPart1.ipynb
│	│	├── P2 - MyAnalysisPart2.ipynb
│	│	├── P3 - MyAnalysisPart2.ipynb
│	├── PyLib
│	│	├── PythonFile1.py
│	│	├── PythonFile2.py
│	│	├── PythonFile3.py
```

2. Launch Anaconda and navigate to MyProject.
3. Create a Github repository in PredictiveAnalytics.
4. Create a .git repository on your local machine using the Anaconda terminal.
```
git init
git add FILENAME
git commit -m "Commit message"
```
5. Connect your remote Github repository to your local .git repository. Push your changes to the remote repo.
```
git remote add origin http://github.com/PredictiveAnalytics/mygitrepo.git
git push -u
```
6. Verify that your repo has been pushed to the remote repository on Github.


## PyLib Library

Notebooks are intended to be concise. To keep notebooks concise, move longer functions to the PyLib library. Python (.py) files from the PyLib library can be imported into notebooks using the following code. Future development could streamline this import.

```
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import PyLib.PythonFile1 as MyPy
```

During development you may wish to refresh the PyLib library so that you can modify functions as you work. You can refresh the PyLib library using Python's `importlib`.

```
import importlib
importlib.reload(MyPy)
```