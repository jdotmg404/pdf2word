# PDF 转 Word 前端

基于 Vue 3 + TypeScript + Vite 构建的 PDF 转 Word 工具前端应用。

## 技术栈

- **Vue 3** - 使用 `<script setup>` 语法的组合式 API
- **TypeScript** - 类型安全
- **Vite** - 构建工具

## 开发命令

```bash
# 安装依赖
npm install

# 启动开发服务器 (端口 5173)
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

## 项目结构

```
src/
├── App.vue              # 主应用组件
├── main.ts              # 入口文件
├── components/
│   ├── FileUpload.vue   # 文件上传组件
│   ├── ProgressBar.vue  # 进度条组件
│   └── StatusBox.vue    # 状态显示组件
├── composables/
│   └── useConverter.ts  # 转换逻辑组合式函数
└── types/
    └── api.ts           # API 类型定义
```

## API 代理配置

开发环境下，Vite 会自动代理以下请求到后端服务器 (端口 5000)：

- `/convert-stream` - SSE 流式转换接口
- `/download` - 文件下载接口

详见 `vite.config.ts` 中的 `server.proxy` 配置。

## 类型定义

### SSE 事件类型

```typescript
interface ProgressEvent {
  percent: number
  message: string
}

interface CompleteEvent {
  download_id: string
  filename: string
}

interface ErrorEvent {
  error: string
}
```

### 转换状态

```typescript
type ConversionStatus = 'idle' | 'converting' | 'success' | 'error'
```