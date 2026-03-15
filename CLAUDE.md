# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此仓库中工作时提供指导。

## 项目概述

PDF 转 Word 在线转换工具，通过 SSE (Server-Sent Events) 实现实时进度显示。

**技术栈：**
- 后端：Python Flask + pdf2docx (PDF 转换库)
- 前端：Vue 3 + TypeScript + Vite

## 开发命令

### 后端
```bash
# 安装依赖
uv sync  # 或 pip install -e .

# 启动后端服务 (端口 5000)
conda run -n pdf2word python backend/app.py
```

### 前端
```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器 (端口 5173，支持热重载)
npm run dev

# 生产环境构建
npm run build

# 预览生产构建
npm run preview
```

## 架构说明

### 后端 (`backend/app.py`)
- Flask 服务器，启用 CORS
- 使用 SSE 实时推送转换进度
- 主要接口：
  - `POST /convert-stream` - SSE 流式转换，实时推送进度事件
  - `GET /download/<download_id>` - 下载转换后的文件
  - `POST /convert` - 同步转换（旧接口，保留兼容）

### 前端 (`frontend/src/`)
- `App.vue` - 主应用组件
- `composables/useConverter.ts` - 核心转换逻辑，处理 SSE 事件
- `components/` - FileUpload、ProgressBar、StatusBox 组件
- `styles/` - 全局样式（variables.css 设计变量、animations.css 动画、style.css 基础样式）
- `types/api.ts` - API 事件的 TypeScript 类型定义

### API 通信
- Vite 开发服务器将 `/convert-stream` 和 `/download` 代理到后端（配置在 `vite.config.ts`）
- SSE 事件类型：`progress`、`complete`、`error`
- 进度事件字段：`stage`、`message`、`current`、`total`、`percent`

### 文件存储
- 转换后的文件以 UUID 为键存储在内存中（后端 `converted_files` 字典）
- 临时文件在转换完成后自动清理
- 下载为一次性操作（下载后从内存中删除）