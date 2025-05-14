import unittest
import pandas as pd
import sys
import os

# Allow script to find the module
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../../")))

from scripts.pipeline import analyse_score, process_dataframe_bits

class TestPrecomputedScoringConsistency(unittest.TestCase):

    def test_precomputed_vs_non_precomputed_scores(self):
        # Load the input compound dataset
        input_path = "../../data/1_OriginalRefined-957_BeforeReevaluation/Lateral_OriginalRefined-957_BeforeReevaluation.csv"
        df = pd.read_csv(input_path)

        # Prepare precomputed input
        df_preprocessed = process_dataframe_bits(df)

        # Run scoring pipeline with precomputed bits
        df_scored_precomputed = analyse_score(df_preprocessed, precomputed=True)

        # Run scoring pipeline without precomputing
        df_scored_direct = analyse_score(df, precomputed=False)

        # Extract PBS and NBS values from each
        PBS_pre = df_scored_precomputed.loc['Compound'][('Predictions', 'Positive binding score')].values
        NBS_pre = df_scored_precomputed.loc['Compound'][('Predictions', 'Negative binding score')].values

        PBS_dir = df_scored_direct.loc['Compound'][('Predictions', 'Positive binding score')].values
        NBS_dir = df_scored_direct.loc['Compound'][('Predictions', 'Negative binding score')].values

        # Combine into DataFrames for exact match assertion
        df_pre = pd.DataFrame({'PBS': PBS_pre, 'NBS': NBS_pre})
        df_dir = pd.DataFrame({'PBS': PBS_dir, 'NBS': NBS_dir})

        # Assert exact match
        try:
            pd.testing.assert_frame_equal(
                df_pre,
                df_dir,
                check_exact=True
            )
        except AssertionError as e:
            self.fail(f"Precomputed and non-precomputed score results differ:\n{e}")

if __name__ == '__main__':
    unittest.main()
