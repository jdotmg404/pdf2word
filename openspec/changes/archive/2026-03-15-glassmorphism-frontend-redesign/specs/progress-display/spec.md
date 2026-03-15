## ADDED Requirements

### Requirement: 渐变进度条
系统 SHALL 使用渐变填充的进度条样式。

#### Scenario: 进度条填充
- **WHEN** 转换进行中
- **THEN** 进度条使用紫色渐变填充（#8b5cf6 → #a855f7）

#### Scenario: 进度条背景
- **WHEN** 进度条渲染
- **THEN** 未填充部分使用半透明灰色背景

### Requirement: 进度条动画效果
系统 SHALL 为进度条添加动画效果。

#### Scenario: 光效动画
- **WHEN** 进度条正在更新
- **THEN** 显示从左到右的光效扫过动画

#### Scenario: 平滑过渡
- **WHEN** 进度百分比更新
- **THEN** 进度条宽度平滑过渡（transition）

### Requirement: 阶段指示器
系统 SHALL 显示转换阶段指示。

#### Scenario: 阶段显示
- **WHEN** 收到 progress 事件包含 stage 字段
- **THEN** 显示当前阶段描述（如"正在解析 PDF"、"正在生成 Word"）

#### Scenario: 阶段切换
- **WHEN** 转换阶段改变
- **THEN** 阶段指示器平滑更新

### Requirement: 进度视觉层级
系统 SHALL 使用视觉层级展示进度信息。

#### Scenario: 主要信息
- **WHEN** 进度显示
- **THEN** 百分比数字使用较大字号突出显示

#### Scenario: 次要信息
- **WHEN** 进度显示
- **THEN** 消息文字使用较小字号和灰色

## MODIFIED Requirements

### Requirement: 实时进度显示
系统 SHALL 通过 SSE 接收并显示转换进度，使用现代化进度条组件。

#### Scenario: 显示转换进度
- **WHEN** 后端发送 progress 事件
- **THEN** 进度条更新到对应的百分比，显示进度消息和阶段信息

#### Scenario: 进度从 0 到 100
- **WHEN** 转换进行中
- **THEN** 进度条从 0% 平滑更新到 100%，带有渐变和动画效果

### Requirement: 转换完成提示
系统 SHALL 在转换完成时显示成功状态。

#### Scenario: 转换成功
- **WHEN** 后端发送 complete 事件
- **THEN** 进度条显示 100% 并填充完成色，显示"转换完成！"消息

### Requirement: 错误处理
系统 SHALL 显示转换失败的错误信息。

#### Scenario: 转换失败
- **WHEN** 后端发送 error 事件或网络错误
- **THEN** 进度条显示错误状态（红色），显示错误消息

### Requirement: 状态消息显示
系统 SHALL 使用状态框显示操作结果，包含图标和动效。

#### Scenario: 成功状态显示
- **WHEN** 转换成功完成
- **THEN** 状态框显示绿色背景、成功图标和成功消息

#### Scenario: 错误状态显示
- **WHEN** 转换失败
- **THEN** 状态框显示红色背景、错误图标和错误消息

#### Scenario: 状态框出现动画
- **WHEN** 状态框显示
- **THEN** 以淡入上滑动画出现