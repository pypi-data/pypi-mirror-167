from pathlib import Path
from typing import Optional, List

import typer

from bigeye_cli.functions import cli_client_factory
from bigeye_sdk.controller.metric_suite_controller import MetricSuiteController
from bigeye_sdk.log import get_logger

log = get_logger(__file__)

app = typer.Typer(no_args_is_help=True, help='Bigconfig Commands for Bigeye CLI')

"""
File should contain commands relating to deploying Bigconfig files.
"""


@app.command()
def plan(
        bigeye_conf: str = typer.Option(
            None
            , "--bigeye_conf"
            , "-b"
            , help="Bigeye Basic Auth Configuration File"),
        input_path: str = typer.Option(
            Path.cwd()
            , "--input_path"
            , "-ip"
            , help="(Optional) Input path containing Bigconfig files.  If no input path is defined then current"
                   "working directory will be used."),
        output_path: str = typer.Option(
            Path.cwd()
            , "--output_path"
            , "-op"
            , help="(Optional) Output path where reports and fixme files will be saved.  If no output path is defined "
                   "then current working directory will be used."),
        purge_source_names: Optional[List[str]] = typer.Option(
            None
            , "--purge_source_name"
            , "-psn"
            , help="List of source names to purge  E.g. -psn source_1 -psn source_2."
        ),
        purge_all_sources: bool = typer.Option(
            False
            , "--purge_all_sources"
            , "-purge_all"
            , help="Purge all sources: True or False."
        ),

):
    """Executes a plan for purging sources or processing bigconfig files in the input path/current
    working directory."""

    client = cli_client_factory(bigeye_conf)
    mc = MetricSuiteController(client=client)

    if purge_source_names or purge_all_sources:
        mc.execute_purge(purge_source_names=purge_source_names, purge_all_sources=purge_all_sources,
                         output_path=output_path, apply=False)
    else:
        mc.execute_bigconfig(input_path=input_path, output_path=output_path, apply=False)


@app.command()
def apply(
        bigeye_conf: str = typer.Option(
            None
            , "--bigeye_conf"
            , "-b"
            , help="Bigeye Basic Auth Configuration File"),
        input_path: str = typer.Option(
            Path.cwd()
            , "--input_path"
            , "-ip"
            , help="(Optional) Input path containing Bigconfig files.  If no input path is defined then current"
                   "working directory will be used."),
        output_path: str = typer.Option(
            Path.cwd()
            , "--output_path"
            , "-op"
            ,
            help="(Optional) Output path where reports and fixme files will be saved.  If no output path is defined "
                 "then current working directory will be used."),
        purge_source_names: Optional[List[str]] = typer.Option(
            None
            , "--purge_source_name"
            , "-psn"
            , help="List of source names to purge  E.g. -psn source_1 -psn source_2."
        ),
        purge_all_sources: bool = typer.Option(
            False
            , "--purge_all_sources"
            , "-purge_all"
            , help="Purge all sources: True or False."
        ),

):
    """Applies a purge of deployed metrics or applies Bigconfig files from the input path/current working directory to
    the Bigeye workspace."""

    client = cli_client_factory(bigeye_conf)
    mc = MetricSuiteController(client=client)

    if purge_source_names or purge_all_sources:
        mc.execute_purge(purge_source_names=purge_source_names, purge_all_sources=purge_all_sources,
                         output_path=output_path, apply=True)
    else:
        mc.execute_bigconfig(input_path=input_path, output_path=output_path, apply=True)

