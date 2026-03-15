## 1. 项目初始化

- [x] 1.1 备份原有 frontend/index.html 为 frontend/index.html.bak
- [x] 1.2 初始化 Vue3 + TypeScript + Vite 项目 (npm create vite@latest)
- [x] 1.3 配置 vite.config.ts（设置代理解决开发环境 CORS）
- [x] 1.4 配置 tsconfig.json（启用 strict 模式）
- [x] 1.5 创建项目目录结构 (components/, composables/, types/)

## 2. 类型定义

- [x] 2.1 创建 src/types/api.ts 定义 API 响应类型
  - ProgressEvent: { percent: number; message: string }
  - CompleteEvent: { download_id: string; filename: string }
  - ErrorEvent: { error: string }

## 3. 核心逻辑迁移

- [x] 3.1 创建 src/composables/useConverter.ts
  - 实现 SSE 连接和事件解析逻辑
  - 暴露响应式状态: progress, message, status, error
  - 暴露方法: startConversion(file), reset()
- [x] 3.2 实现 fetch + ReadableStream 处理 SSE
- [x] 3.3 实现错误处理和状态重置

## 4. 组件实现

- [x] 4.1 创建 src/components/FileUpload.vue
  - 文件选择 input，accept=".pdf"
  - 文件名显示
  - 禁用状态支持
- [x] 4.2 创建 src/components/ProgressBar.vue
  - 进度条显示
  - 进度文本显示
  - 显示/隐藏控制
- [x] 4.3 创建 src/components/StatusBox.vue
  - 成功/错误状态样式
  - 消息显示
  - 显示/隐藏控制

## 5. 应用集成

- [x] 5.1 创建 src/App.vue
  - 集成 FileUpload, ProgressBar, StatusBox 组件
  - 使用 useConverter 组合函数
  - 实现转换按钮点击处理
  - 实现自动下载逻辑
- [x] 5.2 创建 src/main.ts 入口文件
- [x] 5.3 创建/修改 index.html

## 6. 样式迁移

- [x] 6.1 迁移 CSS 样式到组件或全局样式文件
- [x] 6.2 确保 UI 与原版一致

## 7. 测试验证

- [x] 7.1 验证开发服务器启动正常 (npm run dev)
- [ ] 7.2 验证文件选择功能
- [ ] 7.3 验证 SSE 进度显示
- [ ] 7.4 验证转换成功下载
- [ ] 7.5 验证错误处理
- [x] 7.6 验证生产构建 (npm run build)

## 8. 清理

- [x] 8.1 确认功能正常后删除 index.html.bak
- [ ] 8.2 更新项目 README（如有）