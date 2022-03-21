import polars as pl
from polars_rust_compiled_function.polars_rust_compiled_function import hamming_distance

if __name__ == "__main__":
    df = pl.DataFrame({"a": ["asdf", "qwertz"], "b": ["wasd", "qwerty"]})
    transformed = df.select([
        pl.all(),
        hamming_distance(df["a"], df["b"])
    ])

    print(df)
    print(transformed)
