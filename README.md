# nvjpeg-streamer
An attempt at live lossy encoding of raw imaging data for streaming calcium imaging data

**UPDATE: DO NOT USE. BOKEH IS NOT OPTIMAL FOR THIS PURPOSE.**

pygfx seeems promissing for this purpose! It also uses jpeg compression for improve performance so I was on the right trail

# Installation

```commandline
pip install --upgrade pip setuptools wheel
pip install cython numpy
pip install -r requirements.txt
pip install pynvjpeg
```

If CUDA is installed in a location other than `/usr/local/cuda`, install `pynvjpeg` like this:

```commandline
pip install pynvjpeg --global-option=build_ext --global-option="-I<path to cuda/include>" --global-option="-L<path to cuda/lib64>"
```

Running `scroll_memmap.ipynb`

Set `notebook_url="http://localhost:8866"` in `show()` for voila.

Remove the  `notebook_url` kwarg in `show()` for using in notebooks.
