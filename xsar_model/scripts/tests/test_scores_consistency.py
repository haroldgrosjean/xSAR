import unittest
import pandas as pd
import sys
import os

# Allow script to find the module
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../../")))

from scripts.pipeline import analyse_score, process_dataframe_bits

class TestScoreConsistency(unittest.TestCase):

    def test_pbs_nbs_scores_match_reference(self):
        # Load the input compound dataset
        input_path = "../../data/1_OriginalRefined-957_BeforeReevaluation/Lateral_OriginalRefined-957_BeforeReevaluation.csv"
        input_df = pd.read_csv(input_path, index_col=0)

        # Load the precomputed reference PBS/NBS scores
        reference_path = "./data/Lateral_OriginalRefined-957_BeforeReevaluation_PBS_NBS_rdk_v2022.csv"
        reference_df = pd.read_csv(reference_path, index_col=0)
        reference_df.columns = ['PBS_rdk_v2022.03.3', 'NBS_rdk_v2022.03.3']

        # Compute PBS and NBS using the pipeline
        scored_df = analyse_score(input_df)
        PBS_computed = scored_df.loc['Compound'][('Predictions', 'Positive binding score')]
        NBS_computed = scored_df.loc['Compound'][('Predictions', 'Negative binding score')]

        # Combine into DataFrame matching the format of the reference
        computed_df = pd.DataFrame({
            'PBS_rdk_v2022.03.3': PBS_computed,
            'NBS_rdk_v2022.03.3': NBS_computed
        }, index=reference_df.index)

        # NOTE: Minor rounding differences observed at 15–16 decimal places
        # We therefore allow small numerical tolerance in the comparison
        try:
            pd.testing.assert_frame_equal(
                computed_df,
                reference_df,
                check_exact=False,
                rtol=1e-12,
                atol=1e-15
            )
        except AssertionError as e:
            self.fail(f"Computed PBS/NBS scores do not match the reference within tolerance:\n{e}")

    if __name__ == '__main__':
        unittest.main()
