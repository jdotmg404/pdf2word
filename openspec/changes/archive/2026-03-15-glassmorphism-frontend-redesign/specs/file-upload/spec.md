## ADDED Requirements

### Requirement: 拖拽上传支持
系统 SHALL 支持用户拖拽文件到上传区域。

#### Scenario: 拖拽文件进入
- **WHEN** 用户拖拽文件进入上传区域
- **THEN** 上传区域显示高亮边框和紫色渐变背景

#### Scenario: 拖拽文件离开
- **WHEN** 用户拖拽文件离开上传区域
- **THEN** 上传区域恢复默认样式

#### Scenario: 拖拽文件释放
- **WHEN** 用户在上传区域释放 PDF 文件
- **THEN** 系统选中该文件并显示文件预览

#### Scenario: 拖拽非 PDF 文件
- **WHEN** 用户拖拽非 PDF 文件到上传区域
- **THEN** 系统显示"仅支持 PDF 文件"提示

### Requirement: 文件预览卡片
系统 SHALL 显示已选文件的预览信息卡片。

#### Scenario: 显示文件信息
- **WHEN** 用户选择 PDF 文件
- **THEN** 显示文件名、文件大小（自动转换单位）和 PDF 图标

#### Scenario: 删除已选文件
- **WHEN** 用户点击文件预览卡片的删除按钮
- **THEN** 清除已选文件并恢复初始上传区域

### Requirement: 视觉反馈效果
系统 SHALL 为上传区域提供视觉反馈效果。

#### Scenario: 悬浮效果
- **WHEN** 鼠标悬浮在上传区域
- **THEN** 边框颜色变为紫色渐变并显示提升阴影

#### Scenario: 转换中禁用样式
- **WHEN** 文件正在转换
- **THEN** 上传区域显示禁用状态（降低透明度、禁用交互）

## MODIFIED Requirements

### Requirement: PDF 文件选择
系统 SHALL 允许用户选择本地 PDF 文件，支持点击和拖拽两种方式。

#### Scenario: 点击选择有效 PDF 文件
- **WHEN** 用户点击上传区域并选择有效的 PDF 文件
- **THEN** 系统显示文件预览卡片

#### Scenario: 选择非 PDF 文件
- **WHEN** 用户选择非 PDF 格式文件
- **THEN** 系统不接收该文件并显示格式限制提示

### Requirement: 文件验证
系统 SHALL 验证已选文件的有效性。

#### Scenario: 未选择文件时点击转换
- **WHEN** 用户未选择文件即点击"开始转换"按钮
- **THEN** 系统显示提示"请先选择一个 PDF 文件"

### Requirement: 上传状态管理
系统 SHALL 在转换过程中禁用文件选择和转换按钮。

#### Scenario: 转换中禁用控件
- **WHEN** 文件正在上传和转换
- **THEN** 文件选择区域和转换按钮处于禁用状态

#### Scenario: 转换完成后恢复控件
- **WHEN** 转换完成或失败
- **THEN** 文件选择区域和转换按钮恢复可用状态