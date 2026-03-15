## Why

当前前端界面功能完整但视觉朴素，缺乏品牌感和情感连接。用户使用文件转换工具时期望信任感、效率感和愉悦感，现有设计无法满足这些期望。采用毛玻璃现代风格 + 紫色渐变主题可以同时满足普通用户的友好体验和企业用户的专业感需求。

## What Changes

- **视觉系统重构**: 引入紫色渐变背景、毛玻璃卡片效果、光效边框
- **上传组件增强**: 支持拖拽上传、悬浮效果、文件信息预览、删除按钮
- **进度条升级**: 渐变填充、光效动画、阶段指示器
- **状态反馈优化**: 成功/错误状态的图标 + 颜色 + 微动效
- **整体布局重构**: 品牌区、主操作区、状态区清晰分层
- **响应式适配**: 支持移动端和桌面端的自适应布局
- **动效系统**: 过渡动画、悬浮反馈、加载动画

## Capabilities

### New Capabilities

- `visual-design-system`: 视觉设计系统，包含色彩规范、间距系统、字体层级、阴影系统、动效规范

### Modified Capabilities

- `vue3-app`: 添加 CSS 变量、全局样式、响应式断点配置
- `file-upload`: 添加拖拽上传、悬浮效果、文件预览卡片、删除功能
- `progress-display`: 添加渐变进度条、阶段指示、动画效果、时间预估

## Impact

- **前端文件**:
  - `frontend/src/App.vue` - 主布局重构
  - `frontend/src/components/FileUpload.vue` - 拖拽上传 + 视觉升级
  - `frontend/src/components/ProgressBar.vue` - 动画进度条
  - `frontend/src/components/StatusBox.vue` - 图标 + 动效
  - `frontend/src/main.ts` - 引入全局样式
  - `frontend/src/style.css` - 新建全局样式文件

- **新增文件**:
  - `frontend/src/styles/variables.css` - CSS 变量定义
  - `frontend/src/styles/animations.css` - 动画关键帧
  - `frontend/src/components/BrandLogo.vue` - 品牌 Logo 组件（可选）

- **依赖**: 无新增外部依赖，使用原生 CSS 实现