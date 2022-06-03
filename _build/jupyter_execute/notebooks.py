#!/usr/bin/env python
# coding: utf-8

# # Content with notebooks
# 
# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.
# 
# ## Markdown + notebooks
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# ```{figure} images/logo-wide.jpeg
# ---
# height: 300px
# name: directive-fig
# ---
# My cat is so awesome. The cat (Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat; the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries.[6]
# ```
# ![](images/logo-wide.jpeg)
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# ## MyST markdown
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


get_ipython().run_line_magic('matplotlib', 'widget')

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np

plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams["axes.prop_cycle"] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D

custom_lines = [
    Line2D([0], [0], color=cmap(0.0), lw=4),
    Line2D([0], [0], color=cmap(0.5), lw=4),
    Line2D([0], [0], color=cmap(1.0), lw=4),
]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ["Cold", "Medium", "Hot"]);


# 

# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
