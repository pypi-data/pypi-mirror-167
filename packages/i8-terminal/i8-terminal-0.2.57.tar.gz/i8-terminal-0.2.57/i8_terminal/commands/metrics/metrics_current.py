from typing import Any, Dict, Optional

import click
from rich.console import Console

from i8_terminal.commands.metrics import metrics
from i8_terminal.common.cli import pass_command
from i8_terminal.common.layout import df2Table
from i8_terminal.common.metrics import (
    get_current_metrics_df,
    prepare_current_metrics_formatted_df,
)
from i8_terminal.common.stock_info import validate_tickers
from i8_terminal.common.utils import export_data
from i8_terminal.config import APP_SETTINGS
from i8_terminal.types.metric_identifier_param_type import MetricIdentifierParamType
from i8_terminal.types.ticker_param_type import TickerParamType


@metrics.command()
@click.option(
    "--tickers",
    "-k",
    type=TickerParamType(),
    required=True,
    callback=validate_tickers,
    help="Comma-separated list of tickers.",
)
@click.option(
    "--metrics",
    "-m",
    type=MetricIdentifierParamType(),
    default="pe_ratio_ttm",
    help="Comma-separated list of daily metrics.",
)
@click.option("--export", "export_path", "-e", help="Filename to export the output to.")
@pass_command
def current(tickers: str, metrics: str, export_path: Optional[str]) -> None:
    """
    Lists the given metrics and indicators for a given list of companies. TICKERS is a comma-separated list of tickers.

    Examples:

    `i8 metrics current --metrics total_revenue,net_income,price_to_earnings --tickers AMD,INTC,QCOM`
    """
    console = Console()
    with console.status("Fetching data...", spinner="material"):
        df = get_current_metrics_df(tickers, metrics)
    if df is None:
        console.print("No data found for metrics with selected tickers", style="yellow")
        return
    for m in [*set(metric.split(".")[0] for metric in set(metrics.split(","))) - set(df["metric_name"])]:
        console.print(f"\nNo data found for metric {m} with selected tickers", style="yellow")
    if export_path:
        export_data(
            prepare_current_metrics_formatted_df(df, "store", include_period=True),
            export_path,
            column_width=18,
            column_format=APP_SETTINGS["styles"]["xlsx"]["financials"]["column"],
        )
    else:
        columns_justify: Dict[str, Any] = {}
        for metric_display_name, metric_df in df.groupby("display_name"):
            columns_justify[metric_display_name] = "left" if metric_df["display_format"].values[0] == "str" else "right"
        table = df2Table(
            prepare_current_metrics_formatted_df(df, "console", include_period=True), columns_justify=columns_justify
        )
        console.print(table)
