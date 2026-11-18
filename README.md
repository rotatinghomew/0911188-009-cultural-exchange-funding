# 文化交流项目年度概览

多年度交流活动、预算与参与记录。当前总览只按项目合计参与人数。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.14 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

`python3 -m app scope --key spring` 核对本期实际活动；`evidence` 只采纳截至会议日已收且确认的证明；`tranche` 给出按本期原承诺计算的续拨建议。`minute` 保存本期纪要，加期号可原样读回。

`amendments` 是活动承诺变更记录，`payments` 是财务回单；现行建议基于本期原承诺，且不是财务付款。证明的 `supersedes` 引用被替代的证明。活动按实际举行日期落入周期。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`programme` 决定本期承诺与候选活动, `participation` 查可采纳证明, `committee` 核对续拨条件并保存会议纪要。已有总览仍使用 `data/data.json`。
