import math

def variant_key(base, fog, lightmap):
    """变体键。"""
    raise NotImplementedError("TODO: variant_key")

def cache_bucket(platform, driver):
    """驱动分桶。"""
    raise NotImplementedError("TODO: cache_bucket")

def fallback_entry(stripped, base, fallback):
    """剥离回退。"""
    raise NotImplementedError("TODO: fallback_entry")

def pso_matches(shader_key, pso_key):
    """PSO 匹配。"""
    raise NotImplementedError("TODO: pso_matches")

def animated_variant(animated):
    """属性动画变体。"""
    raise NotImplementedError("TODO: animated_variant")

def invalidate_on_reload(generation, old_generation):
    """热重载失效。"""
    raise NotImplementedError("TODO: invalidate_on_reload")

def ready_to_submit(compiled):
    """编译就绪。"""
    raise NotImplementedError("TODO: ready_to_submit")

def lock_map(locked):
    """变体表加锁。"""
    raise NotImplementedError("TODO: lock_map")

def cache_version(source_hash):
    """缓存版本。"""
    raise NotImplementedError("TODO: cache_version")

def compile_budget(ms, per_item):
    """编译预算。"""
    raise NotImplementedError("TODO: compile_budget")

def unique_variants(keys):
    """唯一变体数。"""
    raise NotImplementedError("TODO: unique_variants")

def requires_placeholder(ready):
    """占位 shader。"""
    raise NotImplementedError("TODO: requires_placeholder")

def disk_cache_stale(local, remote):
    """磁盘缓存过期。"""
    raise NotImplementedError("TODO: disk_cache_stale")

def variant_id(seed, index):
    """变体 id。"""
    raise NotImplementedError("TODO: variant_id")

def placeholder_color(ready):
    """占位颜色。"""
    raise NotImplementedError("TODO: placeholder_color")
