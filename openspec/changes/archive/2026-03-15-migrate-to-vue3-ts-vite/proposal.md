## Why

当前前端项目是单文件 HTML，存在以下问题：
- 缺乏组件化架构，代码难以维护和扩展
- 无类型检查，容易引入运行时错误
- 无构建优化，生产环境性能不佳
- 无模块化支持，代码复用困难

迁移到 Vue3 + TypeScript + Vite 将带来现代前端开发体验，提升代码质量、可维护性和开发效率。

## What Changes

- **BREAKING**: 重构前端架构，从单文件 HTML 迁移到 Vue3 项目结构
- 引入 Vite 构建工具，支持热更新和快速构建
- 引入 TypeScript，提供类型安全和更好的 IDE 支持
- 采用 Vue3 Composition API，实现更好的代码组织
- 将现有功能组件化：文件上传组件、进度显示组件、状态提示组件
- 配置 ESLint + Prettier 代码规范

## Capabilities

### New Capabilities
- `vue3-app`: Vue3 项目基础架构，包含 Vite 配置、TypeScript 支持、目录结构
- `file-upload`: 文件上传组件，支持 PDF 文件选择和验证
- `progress-display`: 转换进度显示组件，支持 SSE 实时进度更新
- `download-handler`: 文件下载处理模块

### Modified Capabilities
<!-- 无现有 specs -->

## Impact

- **前端代码**: `frontend/` 目录完全重构，从单文件改为标准 Vue 项目结构
- **后端 API**: 无需修改，保持现有 `/convert-stream` 和 `/download/:id` 接口兼容
- **构建流程**: 新增 `npm install` 和 `npm run build` 步骤
- **开发流程**: 新增 `npm run dev` 本地开发服务器