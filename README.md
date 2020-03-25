# Template-Python-Project

This notebook demonstrates code structuring for Python projects which use Jupyter notebooks.
The template Jupyter notebook demonstrates markdown functionality which can be used for documentation.
The modules in PyLib are used to save functions which you want to externalize from the notebook.
This can help to keep your Jupyter notebooks concise, even if you are using longer functions.

## BambooLib and Submodules
The BambooLib and StatLib libraries are general purpose Python libraries which can be applied across projects.
BambooLib includes general data transformation functions, and StatLib includes general statistics functions.
Please add to these libraries when you identify functions which you expect to use again on a different project.

These modules are incorporated as submodules. This means that Git tracks them separately from the project.
The modules exist as git repositories separate from this repository.

## TemplateLib and Project-specific functions
Sometimes you will need to write project-specific functions which are not generalizable.
Place these functions in the 'TemplateLib' folder. Of course rename 'TemplateLib' to something appropriate for your project.
TemplateLib is incorporated as part of this git module. Changes you make in TemplateLib will appear in this repository.
