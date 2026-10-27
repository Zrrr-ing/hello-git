# hello-git

我的第一个 Git 仓库，用来验证本机的 Git → GitHub 链路已经打通。

## 本机环境

| 组件 | 版本 |
|---|---|
| Git | 2.56.0.windows.4 |
| Node.js | v24.22.1 (LTS Krypton) |
| npm | 11.19.1 |
| Python | 3.15.0 |
| 认证方式 | SSH（ed25519，免密） |

## 内容

- `hello.py` —— Python 版 hello world
- `hello.js` —— Node.js 版 hello world
- `.gitignore` —— 常见忽略规则

## 常用命令备忘

```bash
git status              # 看当前改动
git add .               # 把改动加入暂存区
git commit -m "说明"    # 提交
git push                # 推送到 GitHub
git pull                # 拉取远端更新
git log --oneline       # 看提交历史
```
