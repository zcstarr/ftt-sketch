from datetime import datetime
import click
from model.execution import execute_experiment, save_execution


@click.command()
def main() -> None:
    df = execute_experiment()
    import pdb
    pdb.set_trace()
    save_execution(df)


if __name__ == "__main__":
    main()