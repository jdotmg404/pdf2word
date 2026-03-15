## Context

当前前端是一个 135 行的单文件 HTML，包含内嵌 CSS 和 JavaScript。主要功能：
- PDF 文件选择上传
- 通过 SSE (Server-Sent Events) 接收转换进度
- 转换完成后自动下载文件

后端使用 Flask，提供 `/convert-stream` (POST) 和 `/download/:id` (GET) 接口。

## Goals / Non-Goals

**Goals:**
- 建立现代化的 Vue3 + TypeScript + Vite 项目结构
- 实现组件化架构，提高代码可维护性
- 保持与现有后端 API 完全兼容
- 支持开发环境热更新和生产环境构建优化

**Non-Goals:**
- 不修改后端代码
- 不添加新功能（如批量转换、历史记录等）
- 不引入额外的状态管理库（Pinia/Vuex）
- 不引入 UI 组件库（Element Plus/Ant Design Vue）

## Decisions

### 1. 构建工具：Vite
**选择理由**: Vite 是 Vue 生态官方推荐的构建工具，启动快、热更新快，原生支持 TypeScript 和 Vue SFC。

**备选方案**: Vue CLI (基于 Webpack)
- 弃用原因: Vue CLI 已进入维护模式，Vite 是官方推荐的新选择

### 2. 语言：TypeScript
**选择理由**: 类型安全、更好的 IDE 支持、代码可维护性。

**配置**: 使用严格模式 (`strict: true`)，但允许隐式 any 以降低迁移成本。

### 3. 项目结构
```
frontend/
├── src/
│   ├── App.vue              # 根组件
│   ├── main.ts              # 入口文件
│   ├── components/          # 业务组件
│   │   ├── FileUpload.vue   # 文件上传
│   │   └── ProgressBar.vue  # 进度条
│   ├── composables/         # 组合式函数
│   │   └── useConverter.ts  # 转换逻辑
│   └── types/               # TypeScript 类型定义
│       └── api.ts           # API 响应类型
├── index.html
├── vite.config.ts
├── tsconfig.json
└── package.json
```

### 4. API 通信
使用原生 `fetch` + `ReadableStream` 处理 SSE，与现有代码保持一致，避免引入额外依赖。

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|----------|
| 学习曲线：团队不熟悉 Vue3 | 使用 Composition API，文档完善，上手快 |
| 构建配置复杂 | 使用 Vite 默认配置，最小化自定义 |
| 迁移过程中可能引入 bug | 保持功能一致，逐步迁移，充分测试 |

## Migration Plan

1. 创建 Vue3 项目骨架
2. 迁移核心转换逻辑到 composable
3. 实现组件并集成
4. 测试验证
5. 清理旧代码

**回滚策略**: 保留原 `index.html` 为 `index.html.bak`，出现问题可快速回退。