# polars-rust-compiled-function

A short example based on the example given here: https://github.com/pola-rs/polars/tree/py-polars-v0.13.13/examples/python_rust_compiled_function
on using rust functions in the python version of polars.

Steps
* `maturin new [your_package_name]`, in this case it's called `polars-rust-compiled-function`
* Choose `pyo3`
* Make sure that that the edition in Cargo.toml is >= 2021
* Copy the contents of `ffi.rs`, and modify `lib.rs` as needed
* Create a virtual env `python -m venv .venv`
* Activate it `source .venv/bin/activate`
* Run `maturin develop`
* Run `python test.py`
