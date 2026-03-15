## ADDED Requirements

### Requirement: PDF 文件选择
系统 SHALL 允许用户选择本地 PDF 文件。

#### Scenario: 选择有效 PDF 文件
- **WHEN** 用户点击文件选择按钮并选择有效的 PDF 文件
- **THEN** 系统显示已选文件名

#### Scenario: 选择非 PDF 文件
- **WHEN** 用户选择非 PDF 格式文件
- **THEN** 系统不接收该文件（HTML accept 属性限制）

### Requirement: 文件验证
系统 SHALL 验证已选文件的有效性。

#### Scenario: 未选择文件时点击转换
- **WHEN** 用户未选择文件即点击"开始转换"按钮
- **THEN** 系统显示提示"请先选择一个 PDF 文件"

### Requirement: 上传状态管理
系统 SHALL 在转换过程中禁用文件选择和转换按钮。

#### Scenario: 转换中禁用控件
- **WHEN** 文件正在上传和转换
- **THEN** 文件选择框和转换按钮处于禁用状态

#### Scenario: 转换完成后恢复控件
- **WHEN** 转换完成或失败
- **THEN** 文件选择框和转换按钮恢复可用状态