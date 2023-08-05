import math
import os
from copy import deepcopy
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns
from credoai.reporting import plot_utils
from credoai.reporting.credo_reporter import CredoReporter


class NLPGeneratorAnalyzerReporter(CredoReporter):
    def __init__(self, module, size=4):
        super().__init__(module)
        self.num_gen_models = len(self.module.generation_functions)
        self.num_assessment_funs = len(self.module.assessment_functions)
        self.size = size

    def _create_assets(self):
        """Creates nlp generator report assets"""
        # Generate assessment attribute distribution parameters plots
        self.figs.append(self.plot_overall_assessment())
        self.figs.append(self.plot_fairness())
        self.figs.append(self.plot_disaggregated_assessment())
        return self.figs

    def plot_overall_assessment(self, kind="box"):
        """Plots assessment values for each generator as box plots"""
        results = self.module.get_results()["assessment_results"]
        palette = plot_utils.credo_converging_palette(self.num_gen_models)
        n_cols = 2
        n_rows = math.ceil(self.num_assessment_funs / n_cols)

        with plot_utils.get_style(
            figsize=self.size * 2 / 3, n_cols=n_cols, n_rows=n_rows
        ):
            # Generate assessment attribute distribution parameters plots
            f, axes = plt.subplots(n_rows, n_cols)
            to_loop = zip(axes.flat, results.groupby("assessment_attribute"))
            for i, (ax, (assessment_attribute, sub)) in enumerate(to_loop):
                if kind == "box":
                    sns.boxplot(
                        x="value",
                        y="generation_model",
                        dodge=True,
                        data=sub,
                        palette=palette,
                        width=0.8,
                        linewidth=1,
                        fliersize=1,
                        ax=ax,
                    )
                elif kind == "bar":
                    sns.barplot(
                        x="value",
                        y="generation_model",
                        dodge=True,
                        data=sub,
                        palette=palette,
                        linewidth=1,
                        ax=ax,
                        errwidth=1,
                    )

                sns.despine()
                ax.set_xlabel(assessment_attribute)
                ax.set_ylabel("")
                if i % 2:
                    ax.tick_params(labelleft=False)
            plt.subplots_adjust(wspace=0.5, hspace=0.5)
            plt.suptitle("Overall Assessment of Text Generators", y=1)
        return f

    def plot_disaggregated_assessment(self, kind="box"):
        """Plots assessment values for each generator and group as box plots"""
        palette = plot_utils.credo_converging_palette(self.num_gen_models)
        results = self.module.get_results()["assessment_results"]
        # if only one group, can't calculate disaggregated
        if len(results["group"].unique()) == 1:
            return

        n_cols = 2
        n_rows = math.ceil(self.num_assessment_funs / n_cols)

        with plot_utils.get_style(figsize=self.size, n_cols=n_cols, n_rows=n_rows):
            # Generate assessment attribute distribution parameters plots
            f, axes = plt.subplots(n_rows, n_cols)
            to_loop = zip(axes.flat, results.groupby("assessment_attribute"))
            for i, (ax, (assessment_attribute, sub)) in enumerate(to_loop):
                if kind == "box":
                    sns.boxplot(
                        x="value",
                        y="group",
                        hue="generation_model",
                        dodge=True,
                        data=sub,
                        palette=palette,
                        width=0.8,
                        linewidth=1,
                        ax=ax,
                        fliersize=1,
                    )
                elif kind == "bar":
                    sns.barplot(
                        x="value",
                        y="group",
                        hue="generation_model",
                        data=sub,
                        palette=palette,
                        linewidth=1,
                        ax=ax,
                        errwidth=1,
                    )

                sns.despine()
                ax.set_xlabel(assessment_attribute)
                ax.set_ylabel("")
                if i % 2:
                    ax.tick_params(labelleft=False)
                if i == self.num_assessment_funs - 1:
                    ax.legend(
                        bbox_to_anchor=(1.05, 0.9),
                        title="Text Generator",
                        labelcolor="linecolor",
                    )
                else:
                    ax.legend().set_visible(False)
            plt.subplots_adjust(wspace=0.1, hspace=0.5)
            plt.suptitle("Disaggregated Assessment across Groups", y=1)
        return f

    def plot_fairness(self):
        palette = plot_utils.credo_converging_palette(self.num_gen_models)
        results = self.module.prepare_results()
        # if only one group, can't calculate fairness
        if len(results["group"].unique()) == 1:
            return
        # create parity metrics
        parity = (
            results.groupby(["generation_model", "assessment_attribute"])["mean"]
            .agg(["max", "min"])
            .diff(axis=1)["min"]
            .abs()
            .reset_index()
        )
        parity.rename(columns={"min": "value"}, inplace=True)

        # plot
        with plot_utils.get_style(figsize=self.size, figure_ratio=0.5):
            f = plt.figure()
            ax = sns.barplot(
                x="assessment_attribute",
                y="value",
                hue="generation_model",
                data=parity,
                palette=palette,
            )
            plt.xlabel("Assessment Attribute")
            plt.ylabel("Min/Max Parity")
            plt.title("Parity of Assessment Attributes across Group")
            sns.despine()
            plt.setp(
                ax.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor"
            )
            plt.legend(
                bbox_to_anchor=(1.05, 0.9),
                title="Text Generator",
                labelcolor="linecolor",
            )
        return f

    def _plot_hists(self):
        # generate assessment attribute histogram plots
        results = self.module.get_results()["assessment_results"]
        palette = plot_utils.credo_converging_palette(self.num_gen_models)
        n_plots = self.num_assessment_funs
        with plot_utils.get_style(figsize=self.size, n_rows=n_plots):
            f, axes = plt.subplots(n_plots, 1)
        to_loop = zip(axes.flat, results.groupby("assessment_attribute"))
        for i, (ax, (assessment_attribute, sub)) in enumerate(to_loop):
            ax = axes.flat[i]
            n_bins = min(sub.shape[0] // 4, 20)
            sns.histplot(
                data=sub,
                x="value",
                hue="generation_model",
                element="step",
                stat="density",
                common_norm=False,
                bins=n_bins,
                palette=palette,
                alpha=0.7,
                ax=ax,
            )
            sns.despine()
            plt.xlim([0, 1])
            plt.xlabel(assessment_attribute)
        return f

    def _get_scrubbed_reporter(self):
        """Ensures reporter can be pickled

        Pickling can fail if the assessment contains objects that are not picklable. This
        method creates a copy of the reporter where the nlpgenerator module's assessment
        and generator functions are removed
        """
        new_reporter = deepcopy(self)
        module = new_reporter.assessment.initialized_module
        for key in ["assessment_functions", "generator_functions"]:
            module.__dict__[key] = {k: None for k in module.__dict__.keys()}
        return new_reporter
