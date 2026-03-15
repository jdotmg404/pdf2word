## ADDED Requirements

### Requirement: CSS 变量系统
系统 SHALL 提供统一的 CSS 变量用于颜色、间距、字体、阴影等设计 Token。

#### Scenario: 使用 CSS 变量
- **WHEN** 组件需要使用主色调
- **THEN** 通过 `var(--color-primary)` 引用

#### Scenario: 变量覆盖
- **WHEN** 需要调整整体风格
- **THEN** 只需修改变量定义文件

### Requirement: 色彩规范
系统 SHALL 定义完整的色彩系统，包含主色、功能色、中性色。

#### Scenario: 主色调渐变
- **WHEN** 组件使用主色调
- **THEN** 采用 #667eea → #764ba2 → #a855f7 紫色渐变

#### Scenario: 功能色使用
- **WHEN** 显示成功状态
- **THEN** 使用 --color-success: #10b981
- **WHEN** 显示错误状态
- **THEN** 使用 --color-error: #ef4444

### Requirement: 间距系统
系统 SHALL 定义 4px 基础单位的间距变量。

#### Scenario: 间距使用
- **WHEN** 组件需要内边距
- **THEN** 使用 --spacing-sm/md/lg/xl 等变量

### Requirement: 字体层级
系统 SHALL 定义清晰的字体大小和字重层级。

#### Scenario: 标题字体
- **WHEN** 显示主标题
- **THEN** 使用 --font-size-xl 和 --font-weight-bold

### Requirement: 阴影系统
系统 SHALL 定义多级阴影变量用于卡片和悬浮效果。

#### Scenario: 卡片阴影
- **WHEN** 显示毛玻璃卡片
- **THEN** 使用 --shadow-glass 变量

### Requirement: 毛玻璃效果
系统 SHALL 实现毛玻璃视觉效果。

#### Scenario: 毛玻璃卡片
- **WHEN** 渲染主卡片容器
- **THEN** 应用 backdrop-filter: blur() 和半透明背景

#### Scenario: 降级处理
- **WHEN** 浏览器不支持 backdrop-filter
- **THEN** 使用纯色背景作为降级方案

### Requirement: 动画系统
系统 SHALL 提供统一的过渡和动画效果。

#### Scenario: 过渡动画
- **WHEN** 元素状态改变（如悬浮）
- **THEN** 使用 --transition-fast/normal/slow 变量控制动画时长

#### Scenario: 无障碍动画
- **WHEN** 用户系统设置 prefers-reduced-motion
- **THEN** 禁用或减少动画效果