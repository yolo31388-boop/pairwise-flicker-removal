# pairwise-flicker-removal

## 领域

游戏、图形与多媒体

## 主题

视频去闪烁

## 说明

分区检测、运动自适应与编码验证。

初始状态下 `media/flicker_removal.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
