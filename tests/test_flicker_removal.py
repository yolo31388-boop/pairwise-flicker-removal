import pytest
import media.flicker_removal as mod

CASES = [
    ("region_detect", (0.5, 0.2)),
    ("motion_adapt", (1.0, 2.0)),
    ("chroma_process", (1, 2)),
    ("frequency_id", (50, 60)),
    ("exposure_split", (1, 2)),
    ("stripe_separate", (1, 2)),
    ("order_late", (1, 2)),
    ("param_consistent", (1, 2)),
    ("luminance_adapt", (0.3, 0.6)),
    ("encode_verify", (1, 2)),
    ("band_filter", (0.1, 0.2)),
    ("threshold_map", (0.4, 0.2)),
    ("proxy_check", (1, 2)),
    ("temporal_window", (5, 3)),
    ("output_gate", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
