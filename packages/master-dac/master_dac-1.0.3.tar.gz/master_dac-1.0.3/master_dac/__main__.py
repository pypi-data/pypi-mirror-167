from functools import cached_property
import click
from pathlib import Path
from appdirs import user_config_dir
import sys
import json
import logging
logging.basicConfig(level=logging.INFO)


@click.group()
def main():
    pass


class Configuration:
    def __init__(self):
        logging.info(f"Reading configuration from {self.path}")
        config = {}
        if self.path.exists():
            with self.path.open("r") as fp:
                config = json.load(fp)
            
        self.courses = set(config.get("courses", []))

    def save(self):
        self.path.parent.mkdir(exist_ok=True)
        s = json.dumps({
            "courses": [c for c in self.courses]
        })
        self.path.write_text(s)

    @cached_property
    def path(self) -> Path:
        return Path(user_config_dir("master-dac", "isir")) / "config.json"

@main.group()
def amal():
    pass

@amal.command()
def download_datasets():
    try:
        from datamaestro import prepare_dataset
    except:
        logging.error("Datamaestro n'est pas installé, lancez la commande suivante : pip install -U 'master_dac[amal]'")
        sys.exit(1)

    for dataset_id in [
        "com.lecun.mnist",
        "edu.uci.boston",
        "org.universaldependencies.french.gsd",
        "edu.stanford.aclimdb",
        "edu.stanford.glove.6b.50"
    ]:
        logging.info("Preparing %s", dataset_id)
        prepare_dataset(dataset_id)