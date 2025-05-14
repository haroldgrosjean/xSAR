import unittest
import pandas as pd
import sys
import os

# Allow script to find the module
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../../")))

from scripts.pipeline import process_dataframe_bits, score_unmeasured_compounds


class TestIndependentCompoundScoring(unittest.TestCase):

    def test_independent_scoring_matches_precomputed(self):
        # Load training and test data
        train_data = pd.read_csv("../../data/4_MethodsBenchmarcking/Lateral_train.csv", index_col=0)
        test_data = pd.read_csv("../../data/4_MethodsBenchmarcking/Lateral_test.csv", index_col=0)

        # Use raw test_X (no precomputed bits)
        test_X = test_data[['Name', 'Smiles']]

        # Score unmeasured test compounds using internal fingerprinting
        scored_df = score_unmeasured_compounds(train_data, test_X, precomputed=False)

        # Load precomputed PBS/NBS values
        reference_df = pd.read_csv("./data/Retrospective-97_test_PBS_NBS_rdk_v2022.csv", index_col=0)
        reference_df.columns = ['PBS_rdk_v2022.03.3', 'NBS_rdk_v2022.03.3']

        # Extract scores from result
        PBS = scored_df.loc['Compound'][('Predictions', 'Positive binding score')].values
        NBS = scored_df.loc['Compound'][('Predictions', 'Negative binding score')].values
        scored_df_formatted = pd.DataFrame({
            'PBS_rdk_v2022.03.3': PBS,
            'NBS_rdk_v2022.03.3': NBS
        }, index=reference_df.index)

        # Allow very small rounding differences
        try:
            pd.testing.assert_frame_equal(
                scored_df_formatted,
                reference_df,
                check_exact=False,
                rtol=1e-12,
                atol=1e-15
            )
        except AssertionError as e:
            self.fail(f"Independent compound scoring does not match precomputed results:\n{e}")

if __name__ == '__main__':
    unittest.main()
