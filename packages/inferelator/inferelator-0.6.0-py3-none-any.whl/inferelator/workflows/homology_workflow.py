import functools
import pandas as pd
import numpy as np

from inferelator.regression.amusr_regression import filter_genes_on_tasks
from inferelator.utils import Debug
from .amusr_workflow import MultitaskLearningWorkflow

class MultitaskHomologyWorkflow(MultitaskLearningWorkflow):

    _regulator_expression_filter = "union"

    _homology_group_key = None

    _tf_homology = None
    _tf_homology_group_key = None
    _tf_homology_gene_key = None

    def set_homology(self,
        homology_group_key=None,
        tf_homology_map=None,
        tf_homology_map_group_key=None,
        tf_homology_map_gene_key=None
    ):
        """
        Set the gene metadata key that identifies genes to group by homology

        :param homology_group_key: _description_, defaults to None
        :type homology_group_key: _type_, optional
        """

        self._set_with_warning('_homology_group_key', homology_group_key)
        self._set_with_warning('_tf_homology', tf_homology_map)
        self._set_with_warning('_tf_homology_group_key', tf_homology_map_group_key)
        self._set_with_warning('_tf_homology_gene_key', tf_homology_map_gene_key)

    def startup_finish(self):

        self._create_homology_map()
        super().startup_finish()
        self.homology_groupings()

    def homology_groupings(self):

        # Get all the homology groups and put them in a list
        _all_groups = functools.reduce(
            lambda x, y: x.union(y),
            [pd.Index(t._adata.var[self._homology_group_key]) for t in self._task_response]
        )

        # Build a dict, keyed by homology group ID
        # Values are a list of (task, gene_id) tuples for that homology group
        _group_dict = {g: [] for g in _all_groups}

        for i, t in enumerate(self._task_response):
            for k, gene in zip(t._adata.var[self._homology_group_key], t._adata.var_names):
                _group_dict[k].append((i, gene))

        # Unpack them into a list of lists
        self._task_genes = [v for _, v in _group_dict.items()]

    def _create_homology_map(self):

        self._tf_homology_map = dict([
            (g, i) for t in self._task_objects
            for g, i in zip(
                t.data._adata.var_names,
                t.data._adata.var[self._homology_group_key]
            )
            if t is not None
        ])

    def _align_design_response(self):
        """
        Align the design matrix
        TFs which are not in a task will be set to all zero
        """

        # Get the homology IDs for the design data
        current_task_groups = [
            pd.Index([self._tf_homology_map[x] for x in y.gene_names])
            for y in self._task_design
        ]

        # Get all the homology IDs
        all_task_groups = filter_genes_on_tasks(
            current_task_groups,
            'union'
        )

        n_features = len(all_task_groups)

        Debug.vprint(
            f"Rebuilding design matrices for {n_features} combined TFs",
            level=0
        )

        for i in range(len(self._task_design)):
            design_data = self._task_design[i]

            _has_mapping = [
                k in self._tf_homology_map.keys()
                for k in design_data.gene_names
            ]

            Debug.vprint(
                f"Task {design_data.name} design matrix has "
                f"{design_data.shape[1] - np.sum(_has_mapping)} TFs not in homology map. "
                f"Changing from {design_data.shape[1]} features to {n_features} features.",
                level=1
            )

            _homology_map = [
                self._tf_homology_map[x]
                for x in design_data.gene_names[_has_mapping]
            ]

            _integer_map_new = [
                all_task_groups.get_loc(x)
                for x in _homology_map
            ]

            _integer_map_old = np.arange(design_data.shape[1])[_has_mapping]

            _new_data = np.zeros((design_data.shape[0], n_features),
                                 dtype=design_data.values.dtype)
            _new_names = list(map(lambda x: f"TF_ZERO_{x}", range(n_features)))

            for i, loc in zip(_integer_map_old, _integer_map_new):
                _new_data[:, loc] = design_data.values[:, i]
                _new_names[loc] = design_data.gene_names[i]

            design_data.replace_data(
                _new_data,
                new_gene_metadata=design_data.gene_data.reindex(_new_names).fillna(0)
            )

        self.design_homology_features = all_task_groups
