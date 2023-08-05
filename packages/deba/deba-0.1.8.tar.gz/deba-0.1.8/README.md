# Deba

Smart pipeline framework that knows how to analyze your Python scripts (without running) and generate Make rules for you. If you specify script prerequisites and targets within the script itself, Deba can pick them up automatically based on pre-defined patterns and write Make rules accordingly. In addition, Deba mandates a few good rules for sane project management.

- [Deba](#deba)
  - [Getting Started](#getting-started)
    - [Code organization](#code-organization)
    - [Initialize project](#initialize-project)
    - [Targets and prerequisites detection](#targets-and-prerequisites-detection)
      - [User-defined pattern](#user-defined-pattern)
      - [deba.data](#debadata)
      - [References](#references)
      - [Testing patterns](#testing-patterns)
    - [Give it a go](#give-it-a-go)
  - [Configuration](#configuration)
  - [Module Loading](#module-loading)
  - [Using deba.data in Jupyter notebooks](#using-debadata-in-jupyter-notebooks)

## Getting Started

Deba is a framework designed specifically for data integration projects. The main characteristic of data integration projects is that they usually perform a series of steps or stages on multiple datasets. Of course, customizations and differences are possible when processing different datasets, but the main pipeline generally remains the same. Also, before you start, Deba works solely with Python.

### Code organization

Deba requires your scripts to be organized into stages. By stages, I mean works that can be grouped by purpose. An example of a staged workflow is OCR -> NER -> cleaning -> entity matching. To start using Deba, organize your scripts into folders named after the stages, for example:

```
.
├── clean/
│   ├── script_a.py
│   └── script_b.py
├── match/
│   └── script_c.py
└── fuse/
    ├── script_d.py
    └── script_e.py
```

### Initialize project

Initialize Deba with the `init` command:

```bash
pip install deba

deba init
```

This will create a bunch of files and folders:

- `deba.yaml`: The main config file.
- `deba.mk`: Contains static Make rules for Deba. This file is automatically included in your `Makefile` if you have one. Otherwise, Deba creates a `Makefile` for you. With this file created, you can run `make deba` to update all the targets defined in `deba.yaml`.
- `.deba`: This folder contains internal files that Deba needs to operate. You should never commit it. Deba includes this folder in `.gitignore` file.

### Targets and prerequisites detection

One of Deba's main jobs is to write and maintain [Make](https://www.gnu.org/software/make/) rules for you, therefore terms such as targets and prerequisites have the same meaning as they do in Make. Deba makes some assumptions about the scripts that it analyzes:

- All processings are done in the [main block](https://docs.python.org/3/library/__main__.html). Functions and classes defined outside of the main block will still be picked up, but they have to be called within the main block (doesn't have to be called directly) to be analyzed.
- To read input data, the script calls a function or a method with the location of a target as a plain string. E.g. `df = pd.read_csv('my_data.csv')`
- To output data, the script calls a function or a method with the location of a prerequisite as a plain string. E.g. `df.to_csv('my_output.csv')`

#### User-defined pattern

Deba can extract the location of targets and prerequisites using user-defined patterns. A pattern can look similar to a Python function call, but there are some additional syntax to make patterns more flexible. Some example patterns:

| Pattern                              | Description                                                                                                                                                                                                                                                                                                                                              | Matches                                                                                                      |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `pd.read_csv('my_data.csv')`         | This looks like a regular Python function call, and will match this function call exactly. However, the location is interpreted as a regular expression, therefore, it can match more cases than you think.<br><br>Another thing to note is that the pattern can still match function calls that have extra arguments that are not found in the pattern. | - `pd.read_csv('my_data.csv')`<br>- `pd.read_csv('my_data_csv')`<br>- `pd.read_csv('my_data.csv', arg1=123)` |
| `pd.read_csv(r'.+\.csv')`            | This is a more typical pattern that you would use to extract any prerequisite that ends with ".csv".                                                                                                                                                                                                                                                     | - `pd.read_csv('arbitrary_name.csv')`                                                                        |
| `pd.read_csv(deba.data(r'.+\.csv'))` | Function calls in a pattern can be nested. Needless to say, the variable name and the method name must all match for the pattern to match.                                                                                                                                                                                                               | - `pd.read_csv(deba.data('my_file.csv'))`                                                                    |
| `` `*_df`.to_csv(r'.+\.csv') ``      | To match the variable and attribute name flexibly, you can write glob patterns between back ticks. See [fnmatch](https://docs.python.org/3/library/fnmatch.html) to learn glob syntax.                                                                                                                                                                   | - `_df.to_csv('file_a.csv')`<br>- `personnel_df.to_csv('file_b.csv')`                                        |

#### deba.data

Deba expects that all data produced by a script will end up in Deba's data folder, which defaults to "data" but you can change it with `dataDir` attribute in `deba.yaml`. You also need to prefix each target with the stage name. E.g. a `clean` script has to output a target that begins with "clean/". A common practice is to always read/write to and from Deba's `dataDir`. Deba provides you with the function `data` to make fetching the actual file location easier. Here's how you would use it in a script:

```python
# clean/my_script.py
import deba
...
df = pd.read_csv(deba.data('ocr/my_prerequisite.csv'))
...
df.to_csv(deba.data('clean/my_target.csv'))
```

Then you may define patterns like this to pick up prerequisites and targets respectively: `pd.read_csv(deba.data(r'.+\.csv'))` and `df.to_csv(deba.data(r'.+\.csv'))`. It is a good idea to always use `deba.data` while accessing data in scripts.

#### References

References are non-data prerequisites i.e. something that you keep in your Git commit. They could be reference files or config files. Reference patterns can be given along side other patterns, but the main difference is that they are assumed to be rooted at the root folder rather than the `dataDir`.

#### Testing patterns

Deba has a utility command called `test` that helps you test a pattern against a function call. Example:

```bash
deba test '`*_df`.to_csv(r".+\.csv")' 'my_df.to_csv("my_data.csv")'
```

### Give it a go

If you have been following and making changes to your scripts accordingly, you should now be able to run your entire pipeline with:

```bash
make deba
```

## Configuration

Deba configuration is read from a file called `deba.yaml`. This file should be in the same folder
as `Makefile`. Here's an example:

```yaml
# A stage is a folder that houses scripts that have the same purpose.
stages:
  # stage name is also the folder name
  - name: clean
    # if you want deba to ignore some scripts in this stage, this is how it can be done
    # file names could be Unix shell-style wildcards as supported by fnmatch
    ignoredScripts:
      - "*.spot-check.py"
      - baton_rouge_pd_cprr.py
  - name: match
    # if deba somehow cannot pick up some prerequisites, you can include them manually for all
    # scripts like this. However, the preferred method is always to add a pattern in
    # patterns.prerequisites.
    commonPrerequisites:
      - reference/us_census_first_names.csv
  - name: fuse
    # targets in this list will not be validated nor included in the Make rules.
    ignoredTargets:
      - duplicates.csv

# # make sure that the stage execution order is the same as the specified order. Specifically, when this is
# # set to true, Deba will prevent a script from reading outputs from a later stage.
# enforeStageOrder: true

# targets are the final targets of your entire pipeline. They will be updated when you run `make deba`.
targets:
  - fuse/person.csv
  - fuse/event.csv
  - fuse/allegation.csv

patterns:
  # prerequisite patterns are patterns that deba uses during code analysis to detect prerequisites
  prerequisites:
    - pd.read_csv(deba.data(r'.+\.csv'))
  # references are prerequisites that are located under root dir instead of dataDir
  references:
    - json.load(r'.+\.json')
    - yaml.load(r'.+\.yaml')
  # target patterns are patterns that deba uses during code analysis to detect targets
  targets:
    - "`*`.to_csv(deba.data(r'.+\\.csv'))"

# # overrides are Make rules that you want to include manually. Each entry is equivalent to a Make rule
# # of this form:
# #     [target]: [prerequisites]
# #         [recipe]
# # Any rule introduced here will override rules that Deba picked up from analyzing scripts. The primary
# # purpose of this section is to override any Make rule produced by Deba that you don't like. If a rule
# # does not override anything that Deba produced, don't include it here. Please include them in the
# # Makefile instead.
# overrides:
#   - target:
#       - fuse/per_new_orleans_pd.csv
#     prerequisites:
#       - match/new_orleans_personnel.csv
#     recipe: $(PYTHON) fuse/new_orleans_pd.py

# # By default, the parent folder of deba.yaml is automatically included in PYTHONPATH during script
# # execution. If you want to include more paths in PYTHONPATH then please include them here
# pythonPath:
#   - src/lib

# # dataDir is the directory that houses all data produced by scripts invoked with Deba. It is "data"
# # by default. While writing scripts, you can call deba.data to prefix file paths with this directory.
# dataDir: data

# # md5Dir is the directory that contains md5 checksum files of all Python scripts. Make looks at timestamp
# # of checksum files instead of the original files to avoid reprocessing data due to mere timestamp changes
# md5Dir: .deba/md5
```

## Module Loading

During code analysis, Deba can lookup functions, variables, and classes imported from other modules. Regular Python code should work without any problem. The only requirement is that the modules you import from have to be located inside the root directory, or one of the directories defined in the `pythonPath` setting. This means Python Standard Library and packages installed with `pip` will probably be ignored during code analysis.

## Using deba.data in Jupyter notebooks

If your notebooks reside in a different folder than `deba.yaml`, `deba.data` will not work as expected because it expects to be run in the root folder (the folder that contains `deba.yaml`). You can use `deba.set_root` to set root to the correct folder. For example, if you have a folder structure like this:

```
.
├── deba.yaml
└── notebooks/
    └── my_nb.ipynb
```

Then please put this at the top of your notebook:

```python
# notebooks/my_nb.ipynb
import deba
deba.set_root('..')
```
