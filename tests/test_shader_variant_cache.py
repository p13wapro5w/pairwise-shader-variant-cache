import pytest
from render import shader_variant_cache as mod

CASES = [
    ("key", 'm.variant_key("lit", True, False) == "lit|fog=1|lightmap=0"'),
    ("bucket", 'm.cache_bucket("win", "nv") == "win:nv"'),
    ("fallback", 'm.fallback_entry(True, "lit", "basic") == "basic"'),
    ("fallback2", 'm.fallback_entry(False, "lit", "basic") == "lit"'),
    ("pso", 'm.pso_matches("a", "a") is True'),
    ("anim", 'm.animated_variant(True) is False'),
    ("reload", 'm.invalidate_on_reload(2, 1) is True'),
    ("ready", 'm.ready_to_submit(True) is True'),
    ("lock", 'm.lock_map(True) is True'),
    ("version", 'm.cache_version("abcdef123456789") == "abcdef123456"'),
    ("budget", 'm.compile_budget(16, 4) == 4'),
    ("unique", 'm.unique_variants(["a", "a", "b"]) == 2'),
    ("placeholder", 'm.requires_placeholder(False) is True'),
    ("stale", 'm.disk_cache_stale("v1", "v2") is True'),
    ("id", 'm.variant_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
