import math

def variant_key(base, fog, lightmap):
    """变体键：渲染状态（雾、lightmap）进 key，同材质不同房间不再串变体。"""
    return f"{base}|fog={int(bool(fog))}|lightmap={int(bool(lightmap))}"

def cache_bucket(platform, driver):
    """驱动分桶：缓存键带平台与驱动版本，换机器不加载不兼容二进制。"""
    return f"{platform}:{driver}"

def fallback_entry(stripped, base, fallback):
    """剥离回退：变体被剥离时校验并指向 fallback 入口，否则用本体。"""
    return fallback if stripped else base

def pso_matches(shader_key, pso_key):
    """PSO 匹配：PSO 与 shader 状态同源，key 一致才算匹配。"""
    return shader_key == pso_key

def animated_variant(animated):
    """属性动画变体：属性动画走 uniform/常量缓冲，不新建变体。"""
    return False if animated else True

def invalidate_on_reload(generation, old_generation):
    """热重载失效：代际号前进则旧 PSO 全部失效。"""
    return generation != old_generation

def ready_to_submit(compiled):
    """编译就绪：只有编译完成才提交，未就绪不提交 draw。"""
    return bool(compiled)

def lock_map(locked):
    """变体表加锁：多线程编译访问 variant map 必须持锁（或分片）。"""
    return bool(locked)

def cache_version(source_hash):
    """缓存版本：版本号取自源码哈希前缀，源码变则旧缓存不命中。"""
    return str(source_hash)[:12]

def compile_budget(ms, per_item):
    """编译预算：每帧限流，ms 毫秒的帧预算内最多编 per_item 毫秒/个的变体数。"""
    if per_item <= 0:
        return 0
    return int(ms // per_item)

def unique_variants(keys):
    """唯一变体数。"""
    return len(set(keys))

def requires_placeholder(ready):
    """占位 shader：未就绪走占位且不提交真实 PSO。"""
    return not ready

def disk_cache_stale(local, remote):
    """磁盘缓存过期：本地版本与源码版本不一致即过期。"""
    return local != remote

def variant_id(seed, index):
    """变体 id。"""
    return f"{seed}:{index}"

def placeholder_color(ready):
    """占位颜色：未就绪返回占位色（品红提示），就绪返回 None 表示用真实 shader。"""
    return None if ready else (1.0, 0.0, 1.0, 1.0)
