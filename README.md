# pairwise-shader-variant-cache

第一次走进新场景时整帧卡住两秒，着色器变体在渲染线程同步编译，主循环被拖死；变体 key 漏了雾、lightmap、阴影接收三种组合，同材质在不同房间反复编译；缓存键没带平台与驱动版本，换机器后加载到不兼容二进制；变体剥离后 fallback 指向错误入口，物体渲染成粉色；PSO 与 shader 的混合状态不匹配，深度测试被静默关掉；材质属性动画每帧切一次变体，变体表无限增长；热重载后旧 PSO 没失效，改完代码画面不变；异步编译完成前用占位 shader，物体黑一帧；多线程编译共用一张 variant map，偶发键覆盖；磁盘缓存版本号不随源码变，旧缓存一直命中。render/shader_variant_cache.py 是核心，tests/test_shader_variant_cache.py 15个红。要修的是：变体 key 补全渲染状态；按驱动分桶缓存；剥离后 fallback 校验入口；PSO 与 shader 状态同源；属性动画不新建变体；热重载使旧 PSO 失效；未就绪走占位且不提交；variant map 加锁或分片；缓存版本随源码哈希；编译队列限流并分帧。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
